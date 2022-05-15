# Video Lessons

Each folder must contain a `README.md` file describing the animations implemented in that folder's all `.py` files. After completing that animations drag and drop final video in the README.

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

## Linux Setup

First, install the following packages
```bash
sudo apt-get install sox ffmpeg libcairo2 libcairo2-dev texlive-full python3.8 python3-pip python3.8-venv
```

Afterwards, you can create a virtual environment by
```bash
python3.8 -mvenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Each time you open a terminal, activate your virtual environment by
```bash
source .venv/bin/activate
```

Run a script by
```bash
PYTHONPATH=. manim -pql Videos/path/to/file.py SceneClassName
```

With PYTHONPATH set to the root of the repository, the sys.path.append part is not needed.
