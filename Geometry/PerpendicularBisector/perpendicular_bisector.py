from manim import *
from manim.utils import tex_templates
import numpy as np
from Functions.GeometryFunctions.GeometryFunctions import *


class PerpBisect(MovingCameraScene):
    def construct(self):

        # self.camera.frame.save_state()
#   INIT Points, Lines, equality_signs     
    # Points A and B, segment AB and midpoint M
        a = np.array([-1.5, -1, 0])
        b = np.array([1.5, -1, 0])
        A = Dot(a)
        B = Dot(b)
        label_A = LabelPoint(A, 'A')
        label_B = LabelPoint(B, 'B', DR*0.5)
        AB = Line(A, B)
        M = Dot(AB.get_midpoint())
        label_M = LabelPoint(M, 'M', DOWN*0.75)

    # Point C with coordinates as ValueTrackers
        c_x = ValueTracker(-3)
        c_y = ValueTracker(1)
        C = always_redraw(lambda: Dot([c_x.get_value(), c_y.get_value(), 0]))
        label_C = always_redraw(lambda: LabelPoint(C, 'C', UP*0.75))

    # Lines CA CB CM with color using ValueTracker
        color_frac = ValueTracker(0)
        CA = always_redraw(lambda: Line(C.get_center(), A,
            color=rgb_to_hex(hex_to_rgb(RED)*(1-color_frac.get_value()) + hex_to_rgb(ORANGE)*color_frac.get_value())))
        CB = always_redraw(lambda: Line(C.get_center(), B,
            color=rgb_to_hex(hex_to_rgb(GREEN)*(1-color_frac.get_value()) + hex_to_rgb(ORANGE)*color_frac.get_value())))

    # Equality signs for CA and CB with 2 small lines
        equality_sign_AM = SegmentsEqualitySign_2(Line(A, M))
        equality_sign_BM = SegmentsEqualitySign_2(Line(B, M))


  
# ANIMATION BLOCK FUNCTIONS

        def move_C_to_PB_and_change_colors(run_time):
            # Function for animationg moving C to the Perpendicular bisector and changing colos of CA and CB
            self.play(c_x.animate(rate_func=linear).set_value((a[0] + b[0]) / 2), c_y.animate().set_value(2.5), 
                color_frac.animate(rate_func=linear).set_value(1), run_time=run_time)

        def move_C_down_and_up(run_time=2.5):
            # Function for moving C down then up
            self.play(c_y.animate(rate_func=linear).set_value(1), run_time=run_time)
            self.wait(1)
            self.play(c_y.animate(rate_func=linear).set_value(3), run_time=run_time)

        def Create_ABC_MoveC_To_PB(moving_run_time=5):
            # ANIMATION: Create A, B, C, CA, CB and move C to the perpendicular bisector of AB
            self.play(Create(A), Create(label_A))
            self.play(Create(B), Create(label_B))
            self.wait(0.3)
            self.play(Create(C), Create(label_C))
            self.play(Create(CA), Create(CB))
            move_C_to_PB_and_change_colors(run_time=moving_run_time)
            self.add(A, B, C) # To put the points on top of the lines

        def Add_M_MC():
            # ANIMATION: Put equality signs, Create AB, M, CM
            self.play(Create(equality_sign_CA))
            self.play(Create(equality_sign_CB))
            self.play(Create(AB))
            self.play(Create(M), Create(label_M))
            self.play(Create(equality_sign_AM))
            self.play(Create(equality_sign_BM))
            self.play(Create(CM))
            self.add(C, M) # To put the points on top of the lines
            self.play(FadeIn(ACM),FadeIn(BCM))
            self.wait(0.5)
            self.play(self.camera.frame.animate.shift(3*RIGHT))


# ANIMATIONS FOR DRAWING
    # Create_ABC_MoveC_To_PB
        self.wait(0.5)
        Create_ABC_MoveC_To_PB(moving_run_time=5)

    # NOT ANIMATION: init new mobjects dependent on ValueTracker value
        # Equality signs for CA and CB with 1 small line and segment CM
        equality_sign_CA = always_redraw(lambda: SegmentsEqualitySign_1(CA))
        equality_sign_CB = always_redraw(lambda: SegmentsEqualitySign_1(CB))
        CM = always_redraw(lambda: Line(C.get_center(), M.get_center(), color=GREEN))
        # Color ACM and BCM triangles
        ACM = Polygon(A.get_center(), C.get_center(), M.get_center(), fill_opacity=0.3).set_fill(ORANGE).set_stroke(width=0)
        BCM = Polygon(B.get_center(), C.get_center(), M.get_center(), fill_opacity=0.3).set_fill(GREEN).set_stroke(width=0)

    # Add_M_MC
        Add_M_MC()
        self.wait(1)

# SOLUTION

    # INIT
        fc = self.camera.frame_center

        solution = Tex('$\\begin{cases} AC=BC \\\ AM=BM \\\ CM-ն ընդհանուր է \\end{cases}$', tex_template=tex_armenian).move_to(fc)



        

class test(Scene):
    def construct(self):
        
        solution = Tex('Քանի որ', '$\\begin{cases} AC=BC \\\ AM=BM \\\ CM \\textrm{-ն ընդհանուր է} \\end{cases}$', tex_template=tex_armenian)

        self.add(solution)

