# Manim

In each folder there must be a Readme file, in which must be written what are the animations in that folder's .py files.
You can find template Readme file in template Folder (and just copy paste and edit it as needed)

To use funtions from Functions/Directory/file.py, write
```py
import sys
sys.path.append("../../") # relative path of master
from Functions.Directory.file import *
```

To render the animation of file.py just type 'manim -pql file_name.py scene_name' in the terminal in the file's directory

To make it work the computer must have manimCE miktex etc installed.
