import bpy

class Sequentialize(bpy.types.Operator):
    bl_idname = "object.sequentialize_collection"
    bl_label = "Sequentialize collection"
    bl_description = "Sequentialize objects in collection.\nWARNING: will clear animation data!"
    bl_options = {'REGISTER','UNDO'}

    def execute (self, context):

        scene = context.scene
        collection = bpy.data.collections[scene.target_collection]
        sequentialize(collection)

        return {"FINISHED"}

class Show_All(bpy.types.Operator):
    bl_idname = "object.show_all"
    bl_label = "Clear sequence"
    bl_description = "Clear object sequence and show all objects"
    bl_options = {'REGISTER' , 'UNDO'}

    def execute (self, context):

        scene = context.scene
        collection = bpy.data.collections[scene.target_collection]
        show_all(collection)

        return{"FINISHED"}

def sequentialize(collection):
    scene = bpy.context.scene

    if scene.only_parent:
        objs = [obj for obj in collection.all_objects if obj.parent is None]
    else:
        objs = [obj for obj in collection.all_objects if is_model(obj)]

    l = len(objs)
    if l == 0:
        return
    # debug
    # print ('object count: ',l)
    scene.frame_end = scene.frame_start + l - 1
    # delete all markers
    scene.timeline_markers.clear()

    for f in range(scene.frame_start, scene.frame_end + 1):
        i = f - scene.frame_start
        obj = objs[i]
        # debug
        # print (obj.name)    
        if scene.only_parent:
            children = (obj,) + get_all_children(obj)
        else:
            children = [obj]

        for chd in children:
            # clear keyframes
            chd.animation_data_clear()
            chd.hide_viewport = True
            chd.hide_render = True
            # key as hidden on the previous frame
            chd.keyframe_insert('hide_viewport',frame=f-1)
            chd.keyframe_insert('hide_render',frame=f-1)
            # key as hidden on the next frame
            chd.keyframe_insert('hide_viewport',frame=f+1)
            chd.keyframe_insert('hide_render',frame=f+1)
            # key as visible on the current frame
            chd.hide_viewport = False
            chd.hide_render = False
            chd.keyframe_insert('hide_viewport',frame=f)
            chd.keyframe_insert('hide_render',frame=f)
        # add marker with object name
        scene.timeline_markers.new(obj.name,frame=f)

# get all children and subchildren of object
def get_all_children(obj):
    children = ()
    if len(obj.children) == 0:
        return obj.children
    for c in obj.children:
        children = children + (c,)
        if len(c.children) != 0:
            children = children + get_all_children(c)
    return children

# check if object is actual model
def is_model(obj):
    valid_types = ('MESH', 'CURVE', 'SURFACE', 'META')
    vtypes = set(t.lower() for t in valid_types)
    if obj.type.lower() in vtypes:
        return True
    else:
        return False

# clear object sequence
def show_all(collection):
    scene = bpy.context.scene
    if not collection.all_objects:
        return
    for obj in collection.all_objects:
        obj.animation_data_clear()
        obj.hide_render = False
        obj.hide_viewport = False
    scene.timeline_markers.clear()
    
