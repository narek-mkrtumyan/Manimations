from manim import *
from manim.utils import tex_templates
import numpy as np
import sys
sys.path.append("../../")
# sys.path.append("../../Functions/GeometryFunctions/GeometryFunctions.py")
from Functions.GeometryFunctions.GeometryFunctions import *

fs = 30 # font_size for MathTex

class Scene1(MovingCameraScene):
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

    # Equality signs for MA and MB with 2 small lines
        MA = Line(M.get_center(), A.get_center())
        MB = Line(M.get_center(), B.get_center())
        equality_sign_MA = SegmentEqualitySign2(MA)
        equality_sign_MB = SegmentEqualitySign2(MB)
        


# FUNCTIONS FOR ANIMATIONS BLOCKS

        def Create_A_B_C():
            # ANIMATION: Create A, B, C, CA, CB and move C to the perpendicular bisector of AB
            self.play(Create(A), Create(label_A))
            self.play(Create(B), Create(label_B))
            self.wait(0.3)
            self.play(Create(C), Create(label_C))
            self.play(Create(CA), Create(CB))

        def move_C_to_PB_and_change_colors(run_time):
            # Function for animation moving C to the Perpendicular bisector and changing colors of CA and CB
            self.play(
                c_x.animate(rate_func=linear).set_value((a[0] + b[0]) / 2), 
                c_y.animate().set_value(2.5), 
                color_frac.animate(rate_func=linear).set_value(1), run_time=run_time)
            self.add(A, B, C) # To put the points on top of the lines

        def Add_M_MC():
            # ANIMATION: Put equality signs, Create AB, M, CM
            self.play(Create(equality_sign_CA), Create(equality_sign_CB))
            self.play(Create(AB))
            self.play(Create(M), Create(label_M))
            self.play(Create(equality_sign_MA), Create(equality_sign_MB))
            self.play(Create(CM))
            self.add(C, M) # To put the points on top of the lines
            self.play(FadeIn(fill_ACM),FadeIn(fill_BCM))
            


# ANIMATIONS FOR DRAWING

    # Create A, B, C, CA, CB. Move C to Perpendicular bisector while changing colors
        self.wait(0.5)
        Create_A_B_C()
        move_C_to_PB_and_change_colors(run_time=4.5)

    # NOT ANIMATION: init new mobjects dependent on ValueTracker value
        # Equality signs for CA and CB with 1 small line and segment CM
        equality_sign_CA = always_redraw(lambda: SegmentEqualitySign1(CA))
        equality_sign_CB = always_redraw(lambda: SegmentEqualitySign1(CB))
        CM = always_redraw(lambda: Line(C.get_center(), M.get_center(), color=GREEN))
        # fill_ACM and fill_BCM triangles
        fill_ACM = always_redraw(lambda: 
            Polygon(A.get_center(), C.get_center(), M.get_center(), 
                fill_opacity=0.3).set_fill(YELLOW).set_stroke(width=0))

        fill_BCM = always_redraw(lambda: 
            Polygon(B.get_center(), C.get_center(), M.get_center(), 
                fill_opacity=0.3).set_fill(GREEN).set_stroke(width=0))

    # Add_M_MC, shift camera
        self.wait(0.5)
        Add_M_MC()
        self.wait(0.5)
        self.play(self.camera.frame.animate.shift(3*RIGHT))
        self.wait(0.5)



# SOLUTION

        fc = self.camera.frame_center     # Camera frame center after shifting ([3, 0, 0])

    # INIT Triangles

        vertices_ACM = (A, C, M)
        sides_ACM = (CA, CM, MA)
        mob_labels_ACM = (label_A, label_C, label_M)
        labels_acm = (label_a, label_c, label_m)
        triangle_ACM = (vertices_ACM, sides_ACM, mob_labels_ACM, labels_acm)

        vertices_BCM = (B, C, M)
        sides_BCM = (CB, CM, MB)
        mob_labels_BCM = (label_B, label_C, label_M)
        labels_bcm = (label_b, label_c, label_m)
        triangle_BCM = (vertices_BCM, sides_BCM, mob_labels_BCM, labels_bcm)

    # Show triangle equality CMA and CMB
        triangles_equality = TrianglesCongruence.SSSWiggling(
            self, *triangle_ACM, *triangle_BCM, common=CM, colors=[0, 0, RED], 
            brace_tip=fc + np.array([-1, 2, 0]), wiggle_simultaneously=[False, True, True], 
            run_times=[2.5, 2.5, 2.5], wait_time=[0, 0, 0], transform_simultaneously=[True, False, True])
    
    # INIT angles, and CMA=CMB=90
        rightarrow_1 = MathTex(r'' + '\Rightarrow', font_size=fs).next_to(triangles_equality, RIGHT)

        angle_CMA = always_redraw(lambda: 
            Angle(CM, MA, quadrant=(-1, 1), radius=0.3, color=fill_ACM.get_color()))

        angle_CMB = always_redraw(lambda: 
        Angle(CM, MB, quadrant=(-1, 1), other_angle=True, radius=0.4, color=fill_BCM.get_color()))

        right_angle_CMA = always_redraw(lambda: 
            RightAngle(CM, MA, quadrant=(-1, 1), length=0.3, color=fill_ACM.get_color()))

        right_angle_CMB = always_redraw(lambda: 
            RightAngle(CM, MB, quadrant=(-1, 1), length=0.4, color=fill_BCM.get_color()))

        CMA_CMB_equal_90 = MathTex(r'\angle CMA', r'=', r'\angle CMB', r'= 90^{\circ}', font_size=fs)
        CMA_CMB_equal_90.next_to(fc, RIGHT, buff=0)

    # FUNCTIONS FOR ANIMATIONS BLOCKS

        def show_CMA_CMB_equality():
            # Function for adding angles CMA and CMB and write their equality
            self.play(Create(angle_CMA), Create(angle_CMB))
            self.play(Write(rightarrow_1))

            self.play(
                ReplacementTransform(angle_CMA.copy(), CMA_CMB_equal_90[0]), 
                Write(CMA_CMB_equal_90[1]), 
                ReplacementTransform(angle_CMB.copy(), CMA_CMB_equal_90[2]))

            self.wait(0.5)
            self.play(
                ReplacementTransform(angle_CMA, right_angle_CMA),
                ReplacementTransform(angle_CMB, right_angle_CMB))

            self.play(Write(CMA_CMB_equal_90[3]))
        

        def move_C_up_down(run_time=1.5):
            # Function for moving C up then down
            self.play(c_y.animate(rate_func=linear).set_value(3.5), run_time=run_time)
            self.wait(1)
            self.play(c_y.animate(rate_func=linear).set_value(1.5), run_time=run_time)

    # ANIMATIONS FOR DRAWING

        self.wait(1)
        show_CMA_CMB_equality()

        self.wait(1)
        move_C_up_down()

        self.wait(1)

        system = VGroup(*[triangles_equality[i] for i in range(len(triangles_equality) - 1)])

        self.play(
            self.camera.frame.animate.shift(2*RIGHT, 1.75*DOWN),
            system.animate(rate_func=linear).next_to([0, -2, 0], DOWN, buff=0),
            triangles_equality[-1].animate(rate_func=linear).next_to([-0.25, -3.75, 0], DOWN, buff=0),
            rightarrow_1.animate(rate_func=linear).next_to([1.25, -3.9, 0], RIGHT),
            CMA_CMB_equal_90.animate(rate_func=linear).next_to([0, -4.5, 0], DOWN, buff=0), 
            run_time=2
        )
        self.wait(1)

        under_first_triangle = VGroup(*triangles_equality, rightarrow_1, CMA_CMB_equal_90)

    # Divide screen into 2 parts by vertical line
        fc = self.camera.frame_center    # [5, -1.75, 0]
        height = self.camera.frame_height
        
        divide_line = DashedLine(fc + np.array([0, height/2, 0]), fc + np.array([0, -height/2, 0]))
        divide_line.shift(LEFT*2.75)

        self.play(Create(divide_line))
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

        AB = always_redraw(lambda: Line(A.get_center(), B.get_center()))
        BC = always_redraw(lambda: Line(B.get_center(), C.get_center()))
        CA = always_redraw(lambda: Line(C.get_center(), A.get_center()))
        sides_1 = [AB, BC, CA]
        XY = always_redraw(lambda: Line(X.get_center(), Y.get_center()))
        YZ = always_redraw(lambda: Line(Y.get_center(), Z.get_center()))
        ZX = always_redraw(lambda: Line(Z.get_center(), X.get_center()))
        sides_2 = [XY, YZ, ZX]

        label_a = 'A'
        label_b = 'B'
        label_c = 'C'
        label_A = always_redraw(lambda: LabelPoint(A, label_a))
        label_B = always_redraw(lambda: LabelPoint(B, label_b, UP*0.75))
        label_C = always_redraw(lambda: LabelPoint(C, label_c, DR*0.5))
        labels_1 = [label_a, label_b, label_c]
        mob_labels_1  = Group(label_A, label_B, label_C)


        label_x = 'X_1'
        label_y = 'Y_1'
        label_z = 'Z_1'
        label_X = always_redraw(lambda: LabelPoint(X, label_x))
        label_Y = always_redraw(lambda: LabelPoint(Y, label_y, UP*0.75))
        label_Z = always_redraw(lambda: LabelPoint(Z, label_z, DR*0.5))
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

        # self.add(AB.set_color(ORANGE), BC.set_color(BLUE), CA.set_color(GREEN))
        # self.add(A.set_color(BLUE), B.set_color(GREEN), C.set_color(ORANGE))
        # self.add(label_A.set_color(BLUE), label_B.set_color(GREEN), label_C.set_color(ORANGE))
        self.add(AB, BC, CA)
        self.add(A, B, C)
        self.add(label_A, label_B, label_C)

        angle_CAB = always_redraw(lambda: Angle(CA, AB, quadrant=(-1, 1), color=BLUE))
        angle_CAB_filled = always_redraw(lambda: FilledAngle(CA, AB, quadrant=(-1, 1), color=BLUE))
        equality_sign_BC = always_redraw(lambda: SegmentEqualitySign1(BC, color=BLUE))

        angle_ABC = always_redraw(lambda: Angle2(AB, BC, quadrant=(-1, 1), color=GREEN))
        angle_ABC_filled = always_redraw(lambda: FilledAngle(AB, BC, quadrant=(-1, 1), color=GREEN))
        equality_sign_CA = always_redraw(lambda: SegmentEqualitySign2(CA, color=GREEN))

        angle_BCA = always_redraw(lambda: Angle3(BC, CA, quadrant=(-1, 1), color=ORANGE))
        angle_BCA_filled = always_redraw(lambda: FilledAngle(BC, CA, quadrant=(-1, 1), color=ORANGE))
        equality_sign_AB = always_redraw(lambda: SegmentEqualitySign3(AB, color=ORANGE))

        def sum_180_copies(center):
            _100 = center
            CAB_copy = always_redraw(lambda: angle_CAB_filled.copy().next_to(_100, UR, buff=0))
            BCA_copy = always_redraw(lambda: angle_BCA_filled.copy().next_to(_100, UL, buff=0))
            # ABC_copy = always_redraw(lambda: angle_ABC_filled.copy().rotate(PI).next_to(_100, UP, buff=0))
            # ABC_copy = always_redraw(lambda: Difference())
            line_100 = Line([1.4, 0, 0], [0.6, 0, 0])
            circle_100 = ArcBetweenPoints(*line_100.get_start_and_end(), radius=0.4, stroke_width=0).next_to(_100, UP, buff=0)
            line_points = line_100.reverse_direction().points
            circle_points = circle_100.points
            points = np.concatenate([line_points, circle_points])
            filled_circle = VMobject().set_points_as_corners(points)
            ABC_copy = always_redraw(lambda: 
                Difference(filled_circle, Union(CAB_copy, BCA_copy), color=GREEN, fill_opacity=1, stroke_width=0))
            
            return CAB_copy, ABC_copy, BCA_copy

        
        self.add(angle_CAB_filled, equality_sign_BC)
        self.add(angle_ABC_filled, equality_sign_CA)
        self.add(angle_BCA_filled, equality_sign_AB)
        
        



        



class shtest(Scene):
    def construct(self):
        
        CMA_CMB_equal_90 = MathTex(r'\angle CMA', r'=', r'\angle CMB', r'=', r'90^{\circ}')
        self.add(CMA_CMB_equal_90)
