bl_info = {
    "name": "Object Sequence",
    "description": "Automatically sequentialize objects along the timeline and render individual frames.",
    "author": "Zakrich",
    "version": (1, 3),
    "blender": (2, 80, 0),
    "location": "View3D",
    "wiki_url": "https://github.com/sacrish/Object-Sequence",
    "tracker_url": "https://github.com/sacrish/Object-Sequence/issues",
    "category": "Scene" }


import bpy

from .op_sequentialize import *
from .op_render import *
from .ui_panel import *

classes = (
    Sequentialize,
    Show_All,
    Render_Marked_Frames,
    ObSeq_Panel,
)

def register():
    bpy.types.Scene.target_collection = bpy.props.StringProperty (
        name = "Target collection",
        default = "",
        description = "The target collection of objects to be sequentialized"
    )

    bpy.types.Scene.only_parent = bpy.props.BoolProperty(
        name = "Parents only",
        default = True,
        description = "Count grouped objects as one"
    )

    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.target_collection
    del bpy.types.Scene.only_parent

if __name__ == "__main__":
    register()
    