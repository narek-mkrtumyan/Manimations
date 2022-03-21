from manim import *
import numpy as np
import sys
sys.path.append('../')
from Objects.Objects import *
from Configs import *

from Functions.GeometryFunctions import *
from Functions.Board import *
from Functions.MaserovKhndirnerFunctions import *
from Functions.PeriodicProblemsFunctions import *
from Functions.Board import *


# Կամյական խնդրի ձևակերպում
class Task(VGroup):
    def __init__(
        self,
        number: MathTex,
        text: VGroup,
        **kwargs
    ):
        VGroup.__init__(self)

        self.number = number.set_color(YELLOW)
        self.text = text.arrange(DOWN, aligned_edge=LEFT)
        #self = VGroup(Task.number, Task.text).arrange(RIGHT, aligned_edge=UP)

        self.add(self.number, self.text.align_to(self.number, UP))
        self.arrange(RIGHT, aligned_edge=UP)

    def up(
        self,
        scene: Scene
    ):
        [x_number_0, y_number_0, z_number_0] = self.number.get_center()
        [x_text_0, y_text_0, z_text_0] = self.text.get_center()
        y_up_number_0 = self.number.get_edge_center(UP)[1]
        y_up_text_0 = self.text.get_edge_center(UP)[1]
        [x_number_1, y_number_1, z_number_1] = [-6, 24/7, 0]
        [x_text_1, y_text_1, z_text_1] = [x_text_0, 24/7 + (y_up_number_0 - y_number_0) - (y_up_text_0 - y_text_0), z_text_0]
        def go_up(self, t):
            pos_number = [x_number_0 * (1-t) + x_number_1 * t,
                          y_number_0 * (1-t) + y_number_1 * t,
                          z_number_0 * (1-t) + z_number_1 * t]
            self.number.move_to(pos_number).set_opacity(1-t/2)
            pos_text = [x_text_0 * (1-t) + x_text_1 * t,
                        y_text_0 * (1-t) + y_text_1 * t,
                        z_text_0 * (1-t) + z_text_1 * t]
            self.text.move_to(pos_text).set_opacity(1-t/3)

        scene.play(UpdateFromAlphaFunc(self, go_up))

