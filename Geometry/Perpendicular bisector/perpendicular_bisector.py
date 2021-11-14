from manim import *
import numpy as np

point_name_size = 25

class PerpBisect(Scene):
    def construct(self):
        
        # Init points A and B and segment AB
        a = np.array([-1.5, -1, 0])
        b = np.array([1.5, -1, 0])
        A = Dot(a)
        B = Dot(b)
        A_name = Text('A', font_size=point_name_size).next_to(A, DL)
        B_name = Text('B', font_size=point_name_size).next_to(B, DR)
        AB = Line(A, B)

        # Init point C with coordinates as ValueTracker
        c_x = ValueTracker(-3)
        c_y = ValueTracker(1.5)
        C = always_redraw(lambda: Dot([c_x.get_value(), c_y.get_value(), 0]))
        C_name = always_redraw(lambda: Text('C', font_size=point_name_size).next_to(C, UL))

        # Init lines CA and CB
        CA = always_redraw(lambda: Line(C, A))
        CB = always_redraw(lambda: Line(C, B))

        def move_c_up_right():
            self.play(c_x.animate(rate_func=linear).set_value(-1), c_y.animate().set_value(2.5), run_time=4)
        
        # # test animations
        # self.wait(0.5)
        # self.add(A, B, C, CA, CB)
        # move_c_up_right()
        # self.wait()

        # FINAL ANIMATIONS
        self.wait(0.5)

        self.play(Create(A), Create(A_name))
        self.play(Create(B), Create(B_name))
        self.wait(0.3)
        self.play(Create(C), Create(C_name))
        self.play(Create(CA), Create(CB))

        self.wait(0.5)
        