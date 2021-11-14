from manim import *
import numpy as np
from GeometryFunctions import *


class PerpBisect(Scene):
    def construct(self):
        
        # Points A and B, segment AB and midpoint M
        a = np.array([-1.5, -1, 0])
        b = np.array([1.5, -1, 0])
        A = Dot(a)
        B = Dot(b)
        label_A = LabelPoint(A, 'A')
        label_B = LabelPoint(B, 'B', DR*0.5)
        AB = Line(a, b)
        M = Dot(AB.get_midpoint())
        label_M = LabelPoint(M, 'M', DOWN*0.75)

        # Point C with coordinates as ValueTrackers
        c_x = ValueTracker(-3)
        c_y = ValueTracker(1)
        C = always_redraw(lambda: Dot([c_x.get_value(), c_y.get_value(), 0]))
        label_C = always_redraw(lambda: LabelPoint(C, 'C', UP*0.75))

        # Lines CA and CB with color using ValueTracker
        color_frac = ValueTracker(0)
        CA = always_redraw(lambda: Line(C.get_center(), a,
            color=rgb_to_hex(hex_to_rgb(RED)*(1-color_frac.get_value()) + hex_to_rgb(ORANGE)*color_frac.get_value())))
        CB = always_redraw(lambda: Line(C.get_center(), b,
            color=rgb_to_hex(hex_to_rgb(GREEN)*(1-color_frac.get_value()) + hex_to_rgb(ORANGE)*color_frac.get_value())))

        def move_C_to_perp_bisect_and_change_colors():
            self.play(c_x.animate(rate_func=linear).set_value((a[0] + b[0]) / 2), c_y.animate().set_value(2), 
                color_frac.animate(rate_func=linear).set_value(1), run_time=5)
        
        # Equality signs for CA and CB with 1 small line
        equality_sign_CA = always_redraw(lambda: SegmentsEqualitySign_1(CA))
        equality_sign_CB = always_redraw(lambda: SegmentsEqualitySign_1(CB))
        # Equality signs for CA and CB with 2 small lines
        equality_sign_AM = SegmentsEqualitySign_2(Line(A, M))
        equality_sign_BM = SegmentsEqualitySign_2(Line(B, M))

        # test animations
        self.wait(0.5)
        self.add(A, B, C, CA, CB, AB, M, label_C, label_A, label_B, equality_sign_AM, equality_sign_BM, label_M)
        move_C_to_perp_bisect_and_change_colors()
        self.add(equality_sign_CB, equality_sign_CA)
        # self.play(c_y.animate().set_value(a[1]))
        self.wait()



        # # FINAL ANIMATIONS
        # self.wait(0.5)

        # self.play(Create(A), Create(label_A))
        # self.play(Create(B), Create(label_B))
        # self.wait(0.3)
        # self.play(Create(C), Create(label_C))
        # self.play(Create(CA), Create(CB))
        # move_C_to_perp_bisect_and_change_colors()

        # self.wait(0.5)
        

class test(Scene):
    def construct(self):
        a = np.array([-1.5, -1, 0])
        b = np.array([1.5, -1, 0])
        c = np.array([-3, 1, 0])
        A = Dot(a)
        B = Dot(b)
        C = Dot(c)
        AB = Line(a, b)
        CA = Line(c, a)
        CB = Line(c, b)

        M = Dot((a+b) / 2)

        equality_CA = SegmentsEqualitySign_2(CA)

        self.add(CA, equality_CA)

