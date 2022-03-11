from manim import *
import sys

sys.path.append('../../../')
from Functions.QarakusiFunctions import *

class ApplyFuncExample(Scene):
    def construct(self):
        circ = Circle().scale(1.5)
        circ_ref = circ.copy()
        circ.apply_complex_function(
            lambda x: np.exp(x*1j)
        )
        # t = ValueTracker(0)
        # circ.add_updater(
        #     lambda x: x.become(circ_ref.copy().apply_complex_function(
        #         lambda x: np.exp(x+t.get_value()*1j)
        #     )).set_color(BLUE)
        # )
        #self.add(circ_ref)
        self.play(TransformFromCopy(circ_ref, circ))
        #self.play(t.animate.set_value(TAU), run_time=3)