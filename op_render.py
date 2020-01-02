import bpy
import os

class Render_Marked_Frames(bpy.types.Operator):
    bl_idname = "render.render_marked_frames"
    bl_label = "Render marked frames"
    bl_description = "Render and save object sequence frames"
    bl_options = {'REGISTER','UNDO'}

    def execute (self, context):
        scn = context.scene
        output_folder = scn.render.filepath
        render_marked_frames(output_folder)
        return {"FINISHED"}

def render_marked_frames(folder):
    scn = bpy.context.scene

    # check if there are markers
    if not scn.timeline_markers.items():
        return
    # iterate through markers and render
    for k, m in scn.timeline_markers.items():  
        frame = m.frame
        markerName = m.name
        scn.frame_set(frame)
        scn.render.filepath = os.path.join(folder, markerName + ".png")
        bpy.ops.render.render( write_still=True )
    # restore filepath
    scn.render.filepath = folder
