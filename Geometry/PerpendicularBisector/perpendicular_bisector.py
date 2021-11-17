from manim import *
from manim.utils import tex_templates
import numpy as np
import sys
sys.path.append("../../")
sys.path.append("../../Functions/GeometryFunctions/GeometryFunctions.py")
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
        label_a = 'A'
        label_b = 'B'
        label_A = LabelPoint(A, label_a)
        label_B = LabelPoint(B, label_b, DR*0.5)
        AB = Line(A.get_center(), B.get_center())
        M = Dot(AB.get_midpoint())
        label_m = 'M'
        label_M = LabelPoint(M, label_m, DOWN*0.75)

    # Point C with coordinates as ValueTrackers
        c_x = ValueTracker(-3)
        c_y = ValueTracker(1)
        C = always_redraw(lambda: Dot([c_x.get_value(), c_y.get_value(), 0]))
        label_c = 'C'
        label_C = always_redraw(lambda: LabelPoint(C, label_c, UP*0.75))

    # Lines CA CB CM with color using ValueTracker
        color_frac = ValueTracker(0)
        CA = always_redraw(lambda: Line(C.get_center(), A.get_center(),
            color=rgb_to_hex(hex_to_rgb(RED)*(1-color_frac.get_value()) + hex_to_rgb(ORANGE)*color_frac.get_value())))
        CB = always_redraw(lambda: Line(C.get_center(), B.get_center(),
            color=rgb_to_hex(hex_to_rgb(GREEN)*(1-color_frac.get_value()) + hex_to_rgb(ORANGE)*color_frac.get_value())))

    # Equality signs for AM and BM with 2 small lines
        AM = Line(A.get_center(), M.get_center())
        BM = Line(B.get_center(), M.get_center())
        equality_sign_AM = SegmentsEqualitySign_2(AM)
        equality_sign_BM = SegmentsEqualitySign_2(BM)


# FUNCTIONS FOR ANIMATIONS BLOCKS

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


# # ANIMATIONS FOR DRAWING
    # # Create_ABC_MoveC_To_PB
    #     self.wait(0.5)
    #     Create_ABC_MoveC_To_PB(moving_run_time=5)

    # # NOT ANIMATION: init new mobjects dependent on ValueTracker value
    #     # Equality signs for CA and CB with 1 small line and segment CM
    #     equality_sign_CA = always_redraw(lambda: SegmentsEqualitySign_1(CA))
    #     equality_sign_CB = always_redraw(lambda: SegmentsEqualitySign_1(CB))
    #     CM = always_redraw(lambda: Line(C.get_center(), M.get_center(), color=GREEN))
    #     # Color ACM and BCM triangles
    #     ACM = Polygon(A.get_center(), C.get_center(), M.get_center(), 
    #         fill_opacity=0.3).set_fill(ORANGE).set_stroke(width=0)
    #     BCM = Polygon(B.get_center(), C.get_center(), M.get_center(), 
    #         fill_opacity=0.3).set_fill(GREEN).set_stroke(width=0)

    # # Add_M_MC
    #     Add_M_MC()
    #     self.wait(1)


# TEMPORARY ADDING
        self.add(A, B, C, AB, CA, CB, label_A, label_B, label_C)
        move_C_to_PB_and_change_colors(1)
        self.play(self.camera.frame.animate.shift(3*RIGHT))
        # NOT ANIMATION: init new mobjects dependent on ValueTracker value
        # Equality signs for CA and CB with 1 small line and segment CM
        equality_sign_CA = always_redraw(lambda: SegmentsEqualitySign_1(CA))
        equality_sign_CB = always_redraw(lambda: SegmentsEqualitySign_1(CB))
        CM = always_redraw(lambda: Line(C.get_center(), M.get_center(), color=GREEN))
        # Color ACM and BCM triangles
        ACM = Polygon(A.get_center(), C.get_center(), M.get_center(), 
            fill_opacity=0.3).set_fill(ORANGE).set_stroke(width=0)
        BCM = Polygon(B.get_center(), C.get_center(), M.get_center(), 
            fill_opacity=0.3).set_fill(GREEN).set_stroke(width=0)
        self.add(M, CM, ACM, BCM, equality_sign_CA, equality_sign_CB, equality_sign_AM, equality_sign_BM, label_M)
        self.wait(1)


# SOLUTION

    # INIT
        fc = self.camera.frame_center

        vertices_ACM = (A, C, M)
        sides_ACM = (CA, CM, AM)
        mob_labels_ACM = (label_A, label_C, label_M)
        labels_acm = (label_a, label_c, label_m)
        triangle_ACM = (vertices_ACM, sides_ACM, mob_labels_ACM, labels_acm)

        vertices_BCM = (B, C, M)
        sides_BCM = (CB, CM, BM)
        mob_labels_BCM = (label_B, label_C, label_M)
        labels_bcm = (label_b, label_c, label_m)
        triangle_BCM = (vertices_BCM, sides_BCM, mob_labels_BCM, labels_bcm)

        triangles_equality = TriangleFnctions.TriangleEquality3Sides(
                            self, *triangle_ACM, *triangle_BCM, common=CM, colors=[0, 0, RED], 
                            brace_tip=fc+np.array([0, 2, 0]), wiggle_simultaneously=[False, True, True], 
                            run_times=[6, 4, 1], wait_time=[0, 0, 0])
        
        


        self.wait(1)
         



        

class test(Scene):
    def construct(self):
    
    # init points, segments, labels
        a = [-5, 0.5, 0]
        b = [-4, 2.5, 0]
        c = [-1, 0.5, 0]
        x = [-5, -2.5, 0]
        y = [-4, -0.5, 0]
        z = [-1, -2.5, 0]

        A = Dot(a)
        B = Dot(b)
        C = Dot(c)
        vertices_1 = [A, B, C]
        X = Dot(x)
        Y = Dot(y)
        Z = Dot(z)
        vertices_2 = [X, Y, Z]

        AB = Line(a, b)
        BC = Line(b, c)
        CA = Line(c, a)
        sides_1 = [AB, BC, CA]
        XY = Line(x, y)
        YZ = Line(y, z)
        ZX = Line(z, x)
        sides_2 = [XY, YZ, ZX]

        label_a = 'A'
        label_b = 'B'
        label_c = 'C'
        label_A = LabelPoint(A, label_a)
        label_B = LabelPoint(B, label_b, UP*0.75)
        label_C = LabelPoint(C, label_c, DR*0.5)
        labels_1 = [label_a, label_b, label_c]
        mob_labels_1  = Group(label_A, label_B, label_C)


        label_x = 'X_1'
        label_y = 'Y_1'
        label_z = 'Z_1'
        label_X = LabelPoint(X, label_x)
        label_Y = LabelPoint(Y, label_y, UP*0.75)
        label_Z = LabelPoint(Z, label_z, DR*0.5)
        labels_2 = [label_x, label_y, label_z]
        mob_labels_2 = Group(label_X, label_Y, label_Z)

        abc = label_a + label_b + label_c
        xyz = label_x + label_y + label_z

        triangle_ABC = [vertices_1, sides_1, mob_labels_1, labels_1]
        triangle_XYZ = [vertices_2, sides_2, mob_labels_2, labels_2]
    # end init
        

        bt = np.array([0, 0, 0])    # Brace Tip
        fs = 30
        triangle_equality = Group(
            Tex('A', font_size=fs).move_to(bt + np.array([0.25, 0.5, 0])),
            Tex('B', font_size=fs).move_to(bt + np.array([0.50, 0.5, 0])),
            Tex('=', font_size=fs).move_to(bt + np.array([0.85, 0.5, 0])),
            Tex('X', font_size=fs).move_to(bt + np.array([1.20, 0.5, 0])),
            Tex('Y', font_size=fs).move_to(bt + np.array([1.45, 0.5, 0])),

            Tex('B', font_size=fs).move_to(bt + np.array([0.25, 0, 0])),
            Tex('C', font_size=fs).move_to(bt + np.array([0.50, 0, 0])),
            Tex('=', font_size=fs).move_to(bt + np.array([0.85, 0, 0])),
            Tex('Y', font_size=fs).move_to(bt + np.array([1.20, 0, 0])),
            Tex('Z', font_size=fs).move_to(bt + np.array([1.45, 0, 0])),

            Tex('C', font_size=fs).move_to(bt + np.array([0.25, -0.5, 0])),
            Tex('A', font_size=fs).move_to(bt + np.array([0.50, -0.5, 0])),
            Tex('=', font_size=fs).move_to(bt + np.array([0.85, -0.5, 0])),
            Tex('Z', font_size=fs).move_to(bt + np.array([1.20, -0.5, 0])),
            Tex('X', font_size=fs).move_to(bt + np.array([1.45, -0.5, 0])),

            BraceBetweenPoints(bt + np.array([0.25, 0.75, 0]), bt + np.array([0.25, -0.75, 0]))
            )
        
        self.add(*vertices_1, *vertices_2, *sides_1, *sides_2, mob_labels_1, mob_labels_2)

        TriangleFnctions.TriangleEquality3Sides(self, *triangle_ABC, *triangle_XYZ, brace_tip=[1, 1, 0], 
            colors=[RED, GREEN, 0], wiggle_simultaneously=[True, True, False], 
                transform_simultaneously=[False, True, True], font_size=100)



class shtest(Scene):
    def construct(self):
        
        # x_1 = MathTex(r'' + 'X_1', font_size=80, tex_template=armenian_tex_template)
        # x_2 = MathTex(r'' + 'X_2').next_to(x_1, RIGHT, buff=0.1)
        # s = x_1.get_top() - x_1.get_bottom()
        # print(x_1.font_size)
        armen = MathTex(r'\textrm{- ընդհանուր է}', tex_template=armenian_tex_template)
        self.add(armen)





        

