from manim import  *
import numpy as np


point_name_size = 25

o = np.array([2, 0, 0])
O = Dot(o, color=ORANGE)
O_ = Text('O', font_size=point_name_size, color=ORANGE).next_to(o, DOWN)
r = 2.5
R_ = Text('r', font_size=point_name_size)
crc = Circle(radius=r, color=GREEN).move_to(o)

p = np.array([-3 * np.sqrt(3) + o[0], 3 + o[1], 0])
P = Dot(p, color=ORANGE)
P_ = Text('P', font_size=point_name_size, color=ORANGE).next_to(p, LEFT)

PO = Line(start=p, end=o, color=ORANGE)


class TwoTangents(Scene):
    def construct(self):

        alpha = ValueTracker(-PI / 6)
        f = np.array([r * np.cos(alpha.get_value()) + o[0], r * np.sin(alpha.get_value() + o[1]), 0])
        F = always_redraw(lambda: Dot([r * np.cos(alpha.get_value()) + o[0], r * np.sin(alpha.get_value() + o[1]), 0]))

        PF = always_redraw(lambda: Line(start=p, end=[r * np.cos(alpha.get_value()) + o[0], r * np.sin(alpha.get_value() + o[1]), 0], 
        color=ORANGE).scale_about_point(
            10 / np.sqrt(sum((p - np.array([r * np.cos(alpha.get_value()) + o[0], r * np.sin(alpha.get_value() + o[1]), 0]))**2)), p))

        

        # tang = TangentLine(crc, alpha / (2 * PI), length=5, color=ORANGE)

        # self.wait(0.5)

        self.add(O, O_, crc, P, P_, PO, F, PF)

        self.play(alpha.animate.set_value(2 * PI), run_time=5, rete_func=linear)

        # self.wait(1)


class test(Scene):
    def construct(self):

        self.add(o, O_, crc, P, P_)

