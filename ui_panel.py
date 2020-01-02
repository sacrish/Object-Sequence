import bpy
from bpy.types import Panel

class ObSeq_Panel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Misc"
    bl_idname = "panel.obseq_panel"
    bl_label = "Object Sequentializer"

    def draw(self, context):

        layout = self.layout
        scene = context.scene

        layout.use_property_split = True

        row = layout.row()
        row.prop_search(scene, "target_collection", bpy.data, "collections", icon="GROUP", text="Target collection")
        row = layout.row()
        row.prop(scene, "only_parent")
        row = layout.row()
        row.operator("object.sequentialize_collection", icon='SEQUENCE', text="Sequentialize")
        row.operator("object.show_all", icon='HIDE_OFF', text="Clear Sequence")
        row = layout.row()
        row.operator("render.render_marked_frames",icon='SCENE',text="Render Sequence")
        