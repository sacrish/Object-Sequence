# Object Sequence

## What is this

This is a blender addon I made for myself to quickly render individual images of multiple 3D objects. For example: I have 100 building models made for an RTS game, and need a thumbnail of each one of them to display in the game menu. This is when Object Sequence does the job.

This is the very first time I write something in Python, so expect bugs and always backup your files.

## How to install

Simply download this repository as .zip and install it in Blender preferences. Once installed and enabled, the addon panel should appear in the Misc tab of the N-bar.

This addon is made for Blender 2.80+. I do not guarantee that it works for 2.79 and below.

## How to use

1. Set up your scene with camera and lighting. Make sure all objects are within the render area. Don't worry if they overlap each other - this addon will fix it for you.
2. Move all the objects which you want to render into a collection. DON'T put your camera and lamps in that collection.
3. In the Object Sequence panel, choose that collection as the target. Enable "**Parents only**" if you have models which consist of multiple objects and want to render them as a whole. Otherwise all objects will be rendered individually.
4. Click "**Sequentialize Collection**". This will distribute the objects along the timeline, by keyframing their visibility. Each frame is marked with the object name. **This step will clear all existing animations and timeline markers of selected objects, so keep a backup if you still need them**.
5. Click "**Render Sequence**", and the addon will automatically save each frame with corresponding object's name. The output size and path is set in Blender's output panel.

I highly recommend using this addon with EEVEE to have it render at light speed.
