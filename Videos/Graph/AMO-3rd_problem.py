from manim import *
import sys

sys.path.append('../../')
from Functions.QarakusiFunctions import *

class Third(Scene):
    def construct(self):
        vertices = range(1,21)
        edges = []
        G = Graph(vertices, edges)
        n = 10
        whites = VGroup(*[Line(UP, DOWN) for i in range(n)]).arrange(RIGHT)
        quantity = VGroup(Brace(whites), Tex(f"{n}")).arrange(DOWN)
        self.add(whites)
        quantity.next_to(whites, DOWN)
        self.add(quantity)
        self.add(G)
    