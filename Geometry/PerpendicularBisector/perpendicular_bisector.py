from manim import *
from manim.utils import tex_templates
import numpy as np
import sys
sys.path.append("../../")
# sys.path.append("../../Functions/GeometryFunctions/GeometryFunctions.py")
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
        equality_sign_AM = SegmentEqualitySign_2(AM)
        equality_sign_BM = SegmentEqualitySign_2(BM)
        


# FUNCTIONS FOR ANIMATIONS BLOCKS

        def Create_A_B_C():
            # ANIMATION: Create A, B, C, CA, CB and move C to the perpendicular bisector of AB
            self.play(Create(A), Create(label_A))
            self.play(Create(B), Create(label_B))
            self.wait(0.3)
            self.play(Create(C), Create(label_C))
            self.play(Create(CA), Create(CB))

        def move_C_to_PB_and_change_colors(run_time):
            # Function for animationg moving C to the Perpendicular bisector and changing colos of CA and CB
            self.play(c_x.animate(rate_func=linear).set_value((a[0] + b[0]) / 2), c_y.animate().set_value(2.5), 
                color_frac.animate(rate_func=linear).set_value(1), run_time=run_time)
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
            

        def move_C_down_and_up(run_time=2.5):
            # Function for moving C down then up
            self.play(c_y.animate(rate_func=linear).set_value(1), run_time=run_time)
            self.wait(1)
            self.play(c_y.animate(rate_func=linear).set_value(3), run_time=run_time)


# ANIMATIONS FOR DRAWING

    # Create A, B, C, CA, CB. Move C to Perpendicular bisector while changing colors
        self.wait(0.5)
        Create_A_B_C()
        move_C_to_PB_and_change_colors(run_time=2)

    # NOT ANIMATION: init new mobjects dependent on ValueTracker value
        # Equality signs for CA and CB with 1 small line and segment CM
        equality_sign_CA = always_redraw(lambda: SegmentEqualitySign_1(CA))
        equality_sign_CB = always_redraw(lambda: SegmentEqualitySign_1(CB))
        CM = always_redraw(lambda: Line(C.get_center(), M.get_center(), color=GREEN))
        # Color ACM and BCM triangles
        ACM = Polygon(A.get_center(), C.get_center(), M.get_center(), 
            fill_opacity=0.3).set_fill(ORANGE).set_stroke(width=0)
        BCM = Polygon(B.get_center(), C.get_center(), M.get_center(), 
            fill_opacity=0.3).set_fill(GREEN).set_stroke(width=0)

    # Add_M_MC, shift camera
        Add_M_MC()
        self.wait(0.5)
        self.play(self.camera.frame.animate.shift(3*RIGHT))
        self.wait(0.5)


# TEMPORARY ADDING
        # self.add(A, B, C, AB, CA, CB, label_A, label_B, label_C)
        # move_C_to_PB_and_change_colors(1)
        # self.play(self.camera.frame.animate.shift(3*RIGHT))
        # # NOT ANIMATION: init new mobjects dependent on ValueTracker value
        # # Equality signs for CA and CB with 1 small line and segment CM
        # equality_sign_CA = always_redraw(lambda: SegmentEqualitySign_1(CA))
        # equality_sign_CB = always_redraw(lambda: SegmentEqualitySign_1(CB))
        # CM = always_redraw(lambda: Line(C.get_center(), M.get_center(), color=GREEN))
        # # Color ACM and BCM triangles
        # ACM = Polygon(A.get_center(), C.get_center(), M.get_center(), 
        #     fill_opacity=0.3).set_fill(ORANGE).set_stroke(width=0)
        # BCM = Polygon(B.get_center(), C.get_center(), M.get_center(), 
        #     fill_opacity=0.3).set_fill(GREEN).set_stroke(width=0)
        # self.add(M, CM, ACM, BCM, equality_sign_CA, equality_sign_CB, equality_sign_AM, equality_sign_BM, label_M)
        # self.wait(1)


# SOLUTION

    # INIT Triangles
        fc = self.camera.frame_center     # Camera frame center after shifting camera

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

    #

        triangles_equality = TrianglesCongruence.SSS(
            self, *triangle_ACM, *triangle_BCM, common=CM, colors=[0, 0, RED], 
                brace_tip=fc + np.array([0, 2, 0]), wiggle_simultaneously=[False, True, True], 
                    run_times=[2.5, 2.5, 2.5], wait_time=[0, 0, 0])
        
        
        
        self.wait(1)
         



        

class test(Scene):
    def construct(self):
    
    # init points, segments, labels, MathTex equalities
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

        equality_AB_XY = MathtexSegmentsEquality((label_a, label_b, label_x, label_y))
        equality_BC_YZ = MathtexSegmentsEquality((label_b, label_c, label_y, label_z))
        equality_CA_ZX = MathtexSegmentsEquality((label_c, label_a, label_z, label_x))

        segment_AB = (AB, A, B, label_A, label_B)
        segment_BC = (BC, B, C, label_B, label_C)
        segment_CA = (CA, C, A, label_C, label_A)

        segment_XY = (XY, X, Y, label_X, label_Y)
        segment_YZ = (YZ, Y, Z, label_Y, label_Z)
        segment_ZX = (ZX, Z, X, label_Z, label_X)

    # end init

        self.add(AB, BC, CA)
        self.add(A, B, C)
        self.add(label_A, label_B, label_C)

        
        angle_BCA = Angle(BC, CA, quadrant=(-1, 1), color=ORANGE, elbow=True)
        filled_angle_BCA = FilledAngle(BC, CA, quadrant=(-1, 1), fill_color=ORANGE)

        angle_2 = Angle2(BC, CA, quadrant=(-1, 1), color=ORANGE)

        self.add(angle_BCA)



        



class shtest(Scene):
    def construct(self):
        
        C = Dot([-1, 1, 0])
        A = Dot([1, -1, 0])

        label_A = LabelPoint(A, 'A', DOWN)
        label_C = LabelPoint(C, 'C', UP)
        equality = MathTex('A')
            


        CA = always_redraw(lambda: Line(C.get_center(), A.get_center()))
        self.add(C, A, CA)
        animation = (C.animate().move_to([3, 1, 0]), A.animate().move_to([-3, -1, 0]))
        self.wait(0.5)
        self.play(*animation)
        self.wait(0.5)
        self.remove(A)
        self.wait(0.5)
