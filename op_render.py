import bpy
import os

class Render_Marked_Frames(bpy.types.Operator):
    """Render and save frames with marker names."""
    bl_idname = "render.render_marked_frames"
    bl_label = "Render and save frames with markers."
    bl_options = {'REGISTER','UNDO'}

    def execute (self, context):
        scn = context.scene
        output_folder = scn.render.filepath
        render_marked_frames(output_folder)
        return {"FINISHED"}

def render_marked_frames(folder):
    scn = bpy.context.scene
    # iterate through markers and render
    for k, m in scn.timeline_markers.items():  
        frame = m.frame
        markerName = m.name
        scn.frame_set(frame)
        scn.render.filepath = os.path.join(folder, markerName + ".png")
        bpy.ops.render.render( write_still=True )
    # restore filepath
    scn.render.filepath = folder
