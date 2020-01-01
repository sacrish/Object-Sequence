import bpy
from bpy.types import Panel

class ObSeq_Panel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Misc"
    bl_idname = "panel.obseq_panel"
    bl_label = "Object Sequentializer"
    # bl_category = "ObSeq"

    def draw(self, context):

        layout = self.layout
        scene = context.scene

        layout.prop_search(scene, "target_collection", bpy.data, "collections", icon="GROUP")
        layout.prop(scene, "only_parent")
        layout.operator("object.sequentialize_collection", icon='SEQUENCE', text="Sequentialize Collection")
        layout.operator("render.render_marked_frames",icon='SCENE',text="Render Sequence")