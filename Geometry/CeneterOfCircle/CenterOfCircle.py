from manim import *
import numpy as np
import sys

sys.path.append("../../")
# sys.path.append("../../Functions/GeometryFunctions/GeometryFunctions.py")
from Functions.GeometryFunctions.GeometryFunctions import *

font_size = 30 # font_size for MathTex

class Scene1(MovingCameraScene):
    def construct(self):
        '''
            Drawing
                Create points A, B in the middle of the screen
                Create a segment on the top-left part of the screen
                Create a circle with that segment as radius (orange)


            Solution
                
        '''
       
# INIT Points, Lines, equality_signs

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

    # Point O with coordinates as ValueTrackers
        # o_x = ValueTracker(-4.5)
        # o_y = ValueTracker(-0.5)
        # O = always_redraw(lambda: Dot([o_x.get_value(), o_y.get_value(), 0]))
        O = Dot([-4.5, -0.5, 0])
        label_o = 'O'
        label_O = always_redraw(lambda: LabelPoint(O, label_o, UP*0.75))

    # Radius line on the upper left part, and the moving_circle
        radius = 2
        template_radius = Line([-6.5, 2.5, 0], [-6.5+radius, 2.5, 0], color=ORANGE)
        radius_R = MathTex(r'R', font_size=30).next_to(template_radius, UP)
        moving_circle = always_redraw(lambda : Circle(radius=radius, arc_center=O.get_center(), color=GREEN))

    # Equality signs for MA and MB with 2 small lines
        MA = Line(M.get_center(), A.get_center())
        MB = Line(M.get_center(), B.get_center())
        equality_sign_MA = SegmentEqualitySign2(MA)
        equality_sign_MB = SegmentEqualitySign2(MB)


# ANIMATIONS FOR DRAWING 1

    # Create A, B, O
        self.wait(0.5)
        self.play(Create(A), Create(label_A))
        self.play(Create(B), Create(label_B))
        self.wait(0.3)

    # Create tamplate radius line point P
        self.play(Create(template_radius))
        self.play(Create(radius_R))
        self.play(Create(O), Create(label_O))

    # Copy move radius next to O and draw the circle
        temp_radius_copy = template_radius.copy()
        self.play(temp_radius_copy.animate.next_to(O.get_center(), LEFT, buff=0))
        self.remove(temp_radius_copy)

        temp_circle, temp_O = CircleFromSpinningRadius(self, radius=radius, center=O.get_center(), starting_point_angle=180, 
            circle_color=GREEN, radius_color=ORANGE, create_center=False, create_radius=False)

        self.remove(temp_circle, temp_O)
        self.add(moving_circle)
        self.wait(1)

    #  Move O to Perpendicular bisector while changing colors of OA and OB
        self.play(O.animate(rate_func=linear).shift((3-np.sqrt(3.75))*RIGHT))
        self.wait(0.5)
        self.play(A.animate(rate_func=there_and_back).scale(2))
        self.add(A)
        self.wait(0.5)
        self.play(Rotating(O, about_point=A.get_center(), radians=np.arcsin(0.25)+np.arccos(0.75)-PI))
        self.wait(0.5)
        self.play(B.animate(rate_func=there_and_back, run_time=1.5).scale(2))
        self.add(B)
        self.wait(0.5)

# NOT ANIMATION: init new mobjects dependent on ValueTracker value (OM, equality signs, triangle fills)

    # Lines OA OB with color using ValueTracker
        OA = always_redraw(lambda: Line(O.get_center(), A.get_center(), color=ORANGE))
        OB = always_redraw(lambda: Line(O.get_center(), B.get_center(), color=ORANGE))

    # Equality signs for OA and OB with 1 small line and segment OM
        equality_sign_OA = always_redraw(lambda: SegmentEqualitySign1(OA))
        equality_sign_OB = always_redraw(lambda: SegmentEqualitySign1(OB))
        OM = always_redraw(lambda: Line(O.get_center(), M.get_center(), color=GREEN))

    # fill_AOM and fill_BOM triangles
        color_AOM = YELLOW
        color_BOM = BLUE

        fill_AOM = always_redraw(lambda: 
                Polygon(A.get_center(), O.get_center(), M.get_center(), fill_opacity=0.3)
                .set_fill(color_AOM).set_stroke(width=0)
            )

        fill_BOM = always_redraw(lambda: 
                Polygon(B.get_center(), O.get_center(), M.get_center(), fill_opacity=0.3)
                .set_fill(color_BOM).set_stroke(width=0)
            )


# ANIMATIONS FOR DRAWING 2

    # Put equality signs, Create AB, M, OM
        self.play(Create(OA), Create(OB))
        self.add(O, A, B)
        self.wait(0.5)
        self.play(Create(equality_sign_OA), Create(equality_sign_OB))
        self.wait(0.5)
        self.play(Create(AB))
        self.wait(0.5)
        self.play(Create(M), Create(label_M))
        self.play(Create(equality_sign_MA), Create(equality_sign_MB))
        self.wait(0.5)
        self.play(Create(OM))
        self.add(O, M)
        self.wait(0.5)

    # Shift camera
        self.play(
            self.camera.frame.animate.shift(3*RIGHT), 
            template_radius.animate(rate_fun=linear).shift(3*RIGHT),
            radius_R.animate(rate_fun=linear).shift(3*RIGHT)
        )
        self.wait(1)

    # Fill triangles AOM and BOM with colors
        self.play(FadeIn(fill_AOM))
        self.play(FadeIn(fill_BOM))
        self.wait(0.5)


# INITS for SOLUTION

        fc = self.camera.frame_center     # Camera frame center after shifting ([3, 0, 0])

    # INIT triangle equality AMO and BMO SSS
        AO_BO_equality = MathtexSegmentsEquality((label_a, label_o, label_o, label_b))
        AM_MB_equality = MathtexSegmentsEquality((label_a, label_m, label_m, label_b))
        OM_is_common = MathtexCommonSegment((label_o, label_m))
        common_segment_sign_OM = always_redraw(lambda: CommonSegmentSign(OM))

        triangles_AMO_BMO_equality = MathTexTrianglesEquality(label_a+label_m+label_o, label_b+label_m+label_o)

        triangles_equality = ConcludeFromSSS((AO_BO_equality, AM_MB_equality, OM_is_common), triangles_AMO_BMO_equality)
        triangles_equality.next_to(fc + np.array([-1, 2, 0]), RIGHT, buff=0)
    
    # INIT angles, and OMA=OMB=90
        rightarrow_1 = Rightarrow().next_to(triangles_equality, RIGHT)

        angle_OMA = Angle(OM, MA, quadrant=(-1, 1), radius=0.3, color=color_AOM)
        angle_OMB = Angle(OM, MB, quadrant=(-1, 1), other_angle=True, radius=0.4, color=color_BOM)

        right_angle_OMA = RightAngle(OM, MA, quadrant=(-1, 1), length=0.3, color=color_AOM)
        right_angle_OMB = RightAngle(OM, MB, quadrant=(-1, 1), length=0.4, color=color_BOM)

        OMA_OMB_equal_90 = MathTex(r'\angle OMA', r'=', r'\angle OMB', r'= 90^{\circ}', font_size=font_size)
        OMA_OMB_equal_90.next_to(fc, RIGHT, buff=0)


# ANIMATIONS FOR SOLUTION

    # Show triangles congruence with 3 sides (AOM, BOM)
        PlayTwoSegmentsEqualityWiggling(self, ((OA, A, O, label_A, label_O), (OB, O, B, label_O, label_B)), AO_BO_equality)
        PlayTwoSegmentsEqualityWiggling(self, ((MA, M, A, label_A, label_M), (MB, M, B, label_M, label_B)), AM_MB_equality)
        PlaySegmentIsCommonWiggling(self, (OM, O, M, label_O, label_M), OM_is_common, sign=common_segment_sign_OM)

        PlayConcludeTriangleCongruence(self, triangles_equality)

    # Add angles OMA and OMB and write their equality

        self.play(Write(rightarrow_1))
        self.play(Create(angle_OMA), Create(angle_OMB))
        PlayTwoAnglesEqualityWiggling(self, angle_OMA, angle_OMB, OMA_OMB_equal_90[:3])
        self.wait(0.5)

        self.play(
            Wiggle(angle_OMA, rotation_angle=0.08*TAU, scale_value=1.3), 
            Wiggle(angle_OMB, rotation_angle=0.08*TAU, scale_value=1.3)
        )
        self.wait(0.5)
        self.play(
            ReplacementTransform(angle_OMA, right_angle_OMA),
            ReplacementTransform(angle_OMB, right_angle_OMB)
        )

        self.play(Write(OMA_OMB_equal_90[3]))
        self.wait(1)

    # Move everything to te left of the screen
        self.play(FadeOut(template_radius, radius_R))
        
        system = VGroup(*triangles_equality[:-1])

        self.play(
            self.camera.frame.animate.shift(2*RIGHT, 1.25*DOWN),
            system.animate(rate_func=linear).next_to([0, -2, 0], DOWN, buff=0),
            triangles_equality[-1].animate(rate_func=linear).next_to([-0.25, -3.75, 0], DOWN, buff=0),
            rightarrow_1.animate(rate_func=linear).next_to([1.25, -3.9, 0], RIGHT),
            OMA_OMB_equal_90.animate(rate_func=linear).next_to([0, -4.5, 0], DOWN, buff=0), 
            run_time=2
        )
        self.wait(1)

    # Divide screen into 2 parts by vertical line
        fc = self.camera.frame_center    # np.array([5, -1.25, 0])
        height = self.camera.frame_height
        
        divide_line = DashedLine(fc + np.array([-2.75, height/2, 0]), fc + np.array([-2.75, -height/2, 0]))

        self.play(Create(divide_line))
        self.wait(1)


# ALL THE THING UNDER THE LEFT TRIANGLE
        under_first_triangle = VGroup(*triangles_equality, rightarrow_1, OMA_OMB_equal_90)
        return under_first_triangle


         


class Scene2(MovingCameraScene):
    def construct(self):

        self.camera.frame_center = np.array([5, -1.25, 0])          # frame_height is 8
        fc = np.array([5, -1.25, 0])

        divide_line = DashedLine([2.25, 2.25, 0], [2.25, -5.75, 0])
        divide_line = DashedLine(np.array(([-2.75, 4, 0])) + fc, np.array([-2.75, -4, 0]) + fc)
        self.add(divide_line)

# INIT points, lines
        a = np.array([-1.5, -1, 0]) + fc
        b = np.array([1.5, -1, 0]) + fc
        m = (a + b) / 2
        o = m + np.array([0, 3.5, 0])

        label_a = 'A'
        label_b = 'B'
        label_m = 'M'
        label_o = 'O'

        A = Dot(a)
        B = Dot(b)
        M = Dot(m)
        O = Dot(o)

        label_A = LabelPoint(A, label_a)
        label_B = LabelPoint(B, label_b, DR*0.5)
        label_M = LabelPoint(M, label_m)
        label_O = LabelPoint(O, label_o, UL*0.5)

        AB = Line(a, b)
        AO = Line(a, o, color=ORANGE)
        BO = Line(b, o, color=ORANGE)
        AM = Line(a, m)
        BM = Line(b, m)
        OM = Line(o, m, color=GREEN)
        perp_bisect = Line(m + np.array([0, 4.5, 0]), m - np.array([0, 1, 0]), color=GREEN)

        equality_signs_AM_BM = VGroup( SegmentEqualitySign2(AM), SegmentEqualitySign2(BM) )
        equality_signs_AO_BO = VGroup( SegmentEqualitySign1(AO), SegmentEqualitySign1(BO) )

        common_sign_OM = CommonSegmentSign(OM)

        color_AMO = YELLOW
        color_BMO = BLUE

        angle_AMO = RightAngle(OM, AM, quadrant=(-1, -1), color=color_AMO, length=0.3)
        angle_BMO = RightAngle(OM, BM, quadrant=(-1, -1), color=color_BMO)

# INIT equalities
        angles_AMO_BMO_equality = MathTexAnglesEquality(label_a + label_m + label_o, label_b + label_m + label_o)
        AM_MB_equality = MathtexSegmentsEquality((label_a, label_m, label_m, label_b))
        OM_common = MathtexCommonSegment((label_o, label_m))

        triangles_AMO_BMO_equality = MathTexTrianglesEquality(label_a + label_m + label_o, label_b + label_m + label_o)

        conclude_from_sas = ConcludeFromSAS((angles_AMO_BMO_equality, AM_MB_equality, OM_common), triangles_AMO_BMO_equality)
        conclude_from_sas[-1].next_to(conclude_from_sas[:-1], DOWN, buff=0.75)
        conclude_from_sas.next_to(np.array([2, 1, 0])+fc, RIGHT, buff=0)
        rightarrow = Rightarrow().next_to(conclude_from_sas[-1], RIGHT)
        AO_BO_equality = MathtexSegmentsEquality((label_a, label_o, label_b, label_o)).next_to(conclude_from_sas[-1], DOWN, buff=0.758)

        fill_AMO = Polygon(A.get_center(), O.get_center(), M.get_center(), fill_opacity=0.3)
        fill_AMO.set_fill(color_AMO).set_stroke(width=0)
        fill_BMO = Polygon(B.get_center(), O.get_center(), M.get_center(), fill_opacity=0.3)
        fill_BMO.set_fill(color_BMO).set_stroke(width=0)

# ANIMATIONS
        self.wait(1)
        self.play(Create(A), Write(label_A), Create(B), Write(label_B))
        self.play(Create(AB))
        self.play(Create(M), Write(label_M))
        self.play(Create(equality_signs_AM_BM))
        self.play(Create(perp_bisect))
        self.add(M)
        self.play(Create(angle_AMO), Create(angle_BMO))
        self.play(Create(O), Write(label_O))
        self.play(Create(OM), Create(AO), Create(BO))
        self.add(O, A, B, M)

        PlayTwoAnglesEqualityWiggling(self, angle_AMO, angle_BMO, angles_AMO_BMO_equality)
        PlayTwoSegmentsEqualityWiggling(self, ((AM, A, M, label_A, label_M), (BM, B, M, label_M, label_B)), AM_MB_equality)
        PlaySegmentIsCommonWiggling(self, (OM, O, M, label_O, label_M), OM_common, common_sign_OM)

        self.play(FadeIn(fill_BMO), FadeIn(fill_AMO))
        PlayConcludeTriangleCongruence(self, conclude_from_sas)

        PlayTwoSegmentsWiggling(self, (AO, A, O, label_A, label_O), (BO, B, O, label_B, label_O))
        self.play(Create(equality_signs_AO_BO))
        self.play(Write(rightarrow))
        self.play(Write(AO_BO_equality))

        # circle, center = CircleFromSpinningRadius(self, radius=SegmentLength(AO), center=O.get_center(), 
        #                     starting_point_angle=(PI*3/2 - np.arcsin(SegmentLength(AM)/SegmentLength(AO)))/DEGREES,
        #                     radius_color=ORANGE, equality_sign=1, create_center=False, create_radius=False, direction=-1)
        self.wait(1)





class PerpendicularBisector(MovingCameraScene):
    def construct(self):
        self.wait(0.5)
        under_first_triangle = Scene1.construct(self)
        Scene2.construct(self)
        self.wait(1)
        self.wait(0.5)


