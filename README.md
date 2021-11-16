# Manim

In each folder must be a Readme file, in which must be written what are the animations in that folder's .py files.

You can find template Readme file in template Folder (and just copy paste and edit it as needed)

DO NOT add any directory named images, texts etc (see more in .gitignore)
Directories named test also will be ignored, so feel free to make test/ in your computer if you need


To use funtions from Directory/file.py, add the following in your code
```py
import sys
sys.path.append("../../")       # relative path of master
from Directory.file import *    # or import specific function
```

To render the animation of file.py just type 'manim -pql file_name.py scene_name' in the terminal in the file's directory

To make it work the computer must have manimCE miktex etc installed.
