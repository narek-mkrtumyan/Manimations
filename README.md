# Video Lessons

In each folder must contain a `README.md` file describing the animations implemented in that folder's `.py` files.

You can find a template for the Readme files [here](./template/README.md) (just copy and edit it as needed).

DO **NOT** add any directory named `images`, `texts`, etc. (see more in [.gitignore](./.gitignore)).
Directories named `test` also will be ignored, so feel free to make `test/` in your computer if you need.


To use functions from Directory/file.py, add the following in your code
```py
import sys
sys.path.append("../../")       # relative path to the root of the repository
from Directory.file import *    # or import specific function
# from Functions.GeometryFunctions.GeometryFunctions import *
```

To render the animation implemented in `file.py` just type `'manim -pql file_name.py scene_name'` in the terminal in
the directory containing the file.

To make it work the computer must have `manimCE`, `miktex`, etc. installed.
