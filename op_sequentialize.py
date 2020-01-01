import bpy

class Sequentialize(bpy.types.Operator):
    """Sequentialize objects in active collection along timeline"""
    bl_idname = "object.sequentialize_collection"
    bl_label = "Sequentialize objects in collection.\nWARNING: will clear animation data!"
    bl_options = {'REGISTER','UNDO'}

    def execute (self, context):

        scene = context.scene
        collection = bpy.data.collections[scene.target_collection]
        sequentialize(collection)
        # colname = context.scene.target_collection
        # for collection in bpy.data.collections:
        #     if collection.name == colname:
        #         sequentialize(collection)
        return {"FINISHED"}

def sequentialize(col):
    scene = bpy.context.scene

    # for collection in bpy.data.collections:
    #     objs = [obj for obj in collection.all_objects if collection.name == colname]
    if scene.only_parent:
        objs = [obj for obj in col.all_objects if obj.parent is None]
    else:
        objs = [obj for obj in col.all_objects]
    # for i, obj in enumerate(objs):
    #     # clear keyframes
    #     obj.animation_data_clear()
    #     # hide all objects in collection
    #     obj.hide_viewport = True
    #     obj.hide_render = True
    l = len(objs)
    # debug
    # print ('object count: ',l)
    scene.frame_end = scene.frame_start + l - 1
    # delete all markers
    scene.timeline_markers.clear()

    for f in range(scene.frame_start, scene.frame_end + 1):
        i = f - scene.frame_start
        #if i >= len(objs):
        #    break
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

def get_all_children(obj):
    children = ()
    if len(obj.children) == 0:
        return obj.children
    for c in obj.children:
        children = children + (c,)
        if len(c.children) != 0:
            children = children + get_all_children(c)
    return children
