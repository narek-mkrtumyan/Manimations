# Video Lessons

In each folder must contain a `README.md` file describing the animations implemented in that folder's `.py` files. After completing that animations drag and drop final video in the README.

DO **NOT** add any directories named `images`, `media` etc. (see more in [.gitignore](./.gitignore)).
Directories named `test` also will be ignored, so feel free to make `test/` in your computer if you need.

See [`Configs.py`](./Configs.py)

To use functions from Directory/file.py, add the following in your code
QarakusiFunctions contains every other function file that we write, so importing only QarakusiFunctions will be enough.
```py
import sys
sys.path.append("../../../../")       # relative path to the root of the repository
from Directory.file import *    # or import specific function
# example below
from Functions.QarakusiFunctions import *
```

To render the animation implemented in `file.py` just type `'manim -pql file_name.py scene_name'` in the terminal in
the directory containing the file.

To make it work the computer must have `manimCE`, `miktex`, etc. installed.
