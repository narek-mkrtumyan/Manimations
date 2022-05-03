import sys
sys.path.append('../../../')
from Functions.qarakusi import *

path_to_SVG = os.path.join(helpers.root(), 'Objects', 'SVG_files')
path_to_Objects = os.path.join(helpers.root(), 'Objects')





class test(Scene):
    def construct(self):
        
        p_12 = WhitePaper(12)
        p_18 = WhitePaper(18).shift(4*LEFT)

        self.add(p_12, p_18)