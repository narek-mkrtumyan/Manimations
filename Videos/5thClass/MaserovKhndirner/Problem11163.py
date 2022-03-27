import sys
sys.path.append('../../../')
from Functions.qarakusi import *

class paper(VMobject):
    def __init__(self):
        VMobject.__init__(self)

        self.paper_1 = SVGMobject(os.path.join(path_to_SVG, 'papers', 'paper_1')).set_color(WHITE)
        self.paper_2 = SVGMobject(os.path.join(path_to_SVG, 'papers', 'paper_2')).set_color(WHITE).scale(0.87)
        self.paper_3 = SVGMobject(os.path.join(path_to_SVG, 'papers', 'paper_3')).set_color(WHITE).scale(0.78)
        





class Problem11163(Scene):
    def construct(self):
        p1 = paper().paper_1.shift(3*LEFT)
        p2 = paper().paper_2
        p3 = paper().paper_3.shift(3*RIGHT)
        self.add(p1, p2, p3)

        

        




