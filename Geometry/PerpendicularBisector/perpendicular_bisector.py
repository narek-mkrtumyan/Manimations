from manim import *
from manim.utils import tex_templates
import numpy as np
import sys

from numpy.lib.index_tricks import unravel_index
sys.path.append("../../")
# sys.path.append("../../Functions/GeometryFunctions/GeometryFunctions.py")
from Functions.GeometryFunctions.GeometryFunctions import *

font_size = 30 # font_size for MathTex

class Scene1(MovingCameraScene):
    # AO=OB => O lies on the perpendicular bisector of segment AB
    def construct(self):
        '''
            Drawing
                Վերցնել որևէ A և B կետեր, որոնք լինելու են հատվածի ծայրակետերը և ցանկացած O կետ, որը միացնել A և B կետերին
                Քանի որ AO < BO, ուստի AC ներկել կարմիր, իսկ BO-ն կանաչ
                O-ն տեղաշարժել ու տանել AB-ի միջնակետ, որին զուգահեռ երկու հատվածների գույները մոտենում են նարնջագույնին
                Երբ հատվածները դառնում են իրար հավասար հատվածները սարքել մեր ստանդարտ նարնջագույնը
                AO և BO հատվածների վրա դնել հավասար հատվածների նշանները
                O կետը բարձրացնել վերև, պահելով հավասարության նշանները
                Կառուցել AB հատվածը և նշել AB հատվածի M միջնակետը՝ նշելով որ AM=MB
                Տանել բարակ MO բաց կանաչ ուղիղը
                AOM եռանկյունը ներկել դեղին, իսկ BOM եռանկյունը ներկել բաց կանաչ
                Էկրանը տեղափոխել աջ, լուծման համար տեղ բացվի

            Solution
                Հերթով հաստացնել ու բարակացնելով եռանկյունների համապատասխան կողմերը և աջի վրա գրել հավասարությունները
                Եռանկյունների կողմերի հավասարություններից եզրակացնել, որ եռանկյունները հավասար են և գծագրի վրա նշել, 
                որ \angle AMO = \angle BMO = 90^o:
                O կետը տանել վերև-ներքև ու միշտ AO և BO վրա նշել իրար հավասար։
            
            Այս ամբողջը տեղավորել էկրանի ձախ 1/3 մասում։
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
        o_x = ValueTracker(-3)
        o_y = ValueTracker(1)
        O = always_redraw(lambda: Dot([o_x.get_value(), o_y.get_value(), 0]))
        label_o = 'O'
        label_O = always_redraw(lambda: LabelPoint(O, label_o, UP*0.75))

    # Lines OA OB with color using ValueTracker
        color_frac = ValueTracker(0)
        OA = always_redraw(lambda: Line(O.get_center(), A.get_center(),
            color=rgb_to_hex(hex_to_rgb(RED)*(1-color_frac.get_value()) + hex_to_rgb(ORANGE)*color_frac.get_value())))
        OB = always_redraw(lambda: Line(O.get_center(), B.get_center(),
            color=rgb_to_hex(hex_to_rgb(GREEN)*(1-color_frac.get_value()) + hex_to_rgb(ORANGE)*color_frac.get_value())))

    # Equality signs for MA and MB with 2 small lines
        MA = Line(M.get_center(), A.get_center())
        MB = Line(M.get_center(), B.get_center())
        equality_sign_MA = SegmentEqualitySign2(MA)
        equality_sign_MB = SegmentEqualitySign2(MB)
            

# ANIMATIONS FOR DRAWING 1
        
    # Create A, B, O, OA, OB
        self.play(Create(A), Create(label_A))
        self.play(Create(B), Create(label_B))
        self.wait(0.3)
        self.play(Create(O), Create(label_O))
        self.wait(3)
        self.play(Create(OA), Create(OB))
        self.add(A, B)
        self.wait(2)

    #  Move O to Perpendicular bisector while changing colors of OA and OB
        self.play(
            o_x.animate(rate_func=linear).set_value((a[0] + b[0]) / 2), 
            o_y.animate(rate_func=linear).set_value(a[1]), 
            color_frac.animate(rate_func=linear).set_value(1), run_time=3
        )
        self.wait(1)

# NOT ANIMATION: init OM, equality signs OA and OB
        equality_sign_OA = always_redraw(lambda: SegmentEqualitySign1(OA))
        equality_sign_OB = always_redraw(lambda: SegmentEqualitySign1(OB))


# ANIMATIONS FOR DRAWING 2
    # Add equality signs
        self.play(Create(equality_sign_OA), Create(equality_sign_OB))
        self.wait(2)

    # Move C up
        self.play(o_y.animate(rate_func=linear, run_time=2).set_value(2.5))
        self.add(A, B, O)
        self.wait(1)

# NOT ANIMATION: init fill_AOM and fill_BOM triangles

        OM = always_redraw(lambda: Line(O.get_center(), M.get_center(), color=GREEN))

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


# ANIMATIONS FOR DRAWING 3

    # Put equality signs, Create AB, M, OM
        self.play(Create(AB))
        self.wait(1)
        self.play(Create(M), Create(label_M))
        self.wait(1)
        self.play(Create(equality_sign_MA), Create(equality_sign_MB))
        self.wait(1)
        self.play(Create(OM))
        self.add(O, M) # To put the points on top of the lines
        self.wait(1)
    # Fill triangles AOM and BOM with colors
        self.play(FadeIn(fill_AOM))
        self.play(FadeIn(fill_BOM))
        self.wait(0.5)
    # Shift camera
        self.play(self.camera.frame.animate.shift(3*RIGHT))
        self.wait(1)


# INITS for SOLUTION

        fc = self.camera.frame_center     # Camera frame center after shifting ([3, 0, 0])

    # INIT triangle equality AMO and BMO SSS
        AO_BO_equality = MathtexSegmentsEquality((label_a, label_o, label_o, label_b))
        AM_MB_equality = MathtexSegmentsEquality((label_a, label_m, label_m, label_b))
        OM_is_common = MathtexCommonSegment((label_o, label_m))
        common_segment_sign_OM = always_redraw(lambda: CommonSegmentSign(OM))

        triangles_AMO_BMO_equality = MathTexTrianglesEquality(label_a+label_o+label_m, label_b+label_o+label_m)

        triangles_equality = ConcludeFromSSS((AO_BO_equality, AM_MB_equality, OM_is_common), triangles_AMO_BMO_equality)
        triangles_equality.next_to(fc + np.array([-1, 2, 0]), RIGHT, buff=0)
    
    # INIT angles, and OMA=OMB=90
        rightarrow_1 = Rightarrow().next_to(triangles_equality, RIGHT)

        angle_OMA = Angle(OM, MA, quadrant=(-1, 1), radius=0.3, color=color_AOM)
        angle_OMB = Angle(OM, MB, quadrant=(-1, 1), other_angle=True, radius=0.4, color=color_BOM)

        right_angle_OMA = RightAngle(OM, MA, quadrant=(-1, 1), length=0.3, color=color_AOM)
        right_angle_OMB = RightAngle(OM, MB, quadrant=(-1, 1), length=0.4, color=color_BOM)

        AMO_BMO_equal_90 = MathTex(r'\angle AMO', r'=', r'\angle BMO', r'= 90^{\circ}', font_size=font_size)
        AMO_BMO_equal_90.next_to(fc, RIGHT, buff=0)


# ANIMATIONS FOR SOLUTION

    # Show triangles congruence with 3 sides (AOM, BOM)
        PlayTwoSegmentsEqualityWiggling(self, ((OA, A, O, label_A, label_O), (OB, O, B, label_O, label_B)), AO_BO_equality)
        self.wait(0.5)
        PlayTwoSegmentsEqualityWiggling(self, ((MA, M, A, label_A, label_M), (MB, M, B, label_M, label_B)), AM_MB_equality)
        self.wait(0.5)
        PlaySegmentIsCommonWiggling(self, (OM, O, M, label_O, label_M), OM_is_common, sign=common_segment_sign_OM)
        self.wait(1)

        PlayConcludeTriangleCongruence(self, triangles_equality)

    # Add angles OMA and OMB and write their equality

        self.play(Write(rightarrow_1))
        self.play(Create(angle_OMA), Create(angle_OMB))
        PlayTwoAnglesEqualityWiggling(self, angle_OMA, angle_OMB, AMO_BMO_equal_90[:3])
        self.wait(1)

        self.play(
            Wiggle(angle_OMA, rotation_angle=0.08*TAU, scale_value=1.3), 
            Wiggle(angle_OMB, rotation_angle=0.08*TAU, scale_value=1.3)
        )
        self.wait(1)
        self.play(
            ReplacementTransform(angle_OMA, right_angle_OMA),
            ReplacementTransform(angle_OMB, right_angle_OMB)
        )

        self.play(Write(AMO_BMO_equal_90[3]))
        self.wait(3)

    # Move O up then down
        self.play(o_y.animate(rate_func=linear).set_value(3.5), run_time=1.5)
        self.wait(0.5)
        self.play(o_y.animate(rate_func=linear).set_value(1.5), run_time=1.5)
        self.wait(0.5)

    # Move everything to te left of the screen
        
        system = VGroup(*triangles_equality[:-1])

        self.play(
            self.camera.frame.animate.shift(2*RIGHT, 1.75*DOWN),
            system.animate(rate_func=linear).next_to([0, -2, 0], DOWN, buff=0),
            triangles_equality[-1].animate(rate_func=linear).next_to([-0.25, -3.75, 0], DOWN, buff=0),
            rightarrow_1.animate(rate_func=linear).next_to([1.25, -3.9, 0], RIGHT),
            AMO_BMO_equal_90.animate(rate_func=linear).next_to([0, -4.5, 0], DOWN, buff=0), 
            run_time=1.5
        )
        self.wait(0.5)

    # Divide screen into 2 parts by vertical line
        fc = self.camera.frame_center    # np.array([5, -1.75, 0])
        height = self.camera.frame_height
        
        divide_line = DashedLine(fc + np.array([-2.75, height/2, 0]), fc + np.array([-2.75, -height/2, 0]))

        self.play(Create(divide_line))
        self.wait(0.5)


# return
        under_drawing_1 = Group(*triangles_equality, rightarrow_1, AMO_BMO_equal_90)
        drawing_1 = Group(*[mob for mob in self.mobjects]).remove(*under_drawing_1)
        return drawing_1, under_drawing_1


         


class Scene2(MovingCameraScene):
    # O lies on the perpendicular bisector of segment AB => OA=OB
    def construct(self):
        self.camera.frame_center = np.array([5, -1.75, 0])          # frame_height is 8
        fc = np.array([5, -1.75, 0])

        # divide_line = DashedLine([2.25, 2.25, 0], [2.25, -5.75, 0])
        # divide_line = DashedLine(np.array(([-2.75, 4, 0])) + fc, np.array([-2.75, -4, 0]) + fc)
        # self.add(divide_line)

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
        OA = Line(o, a, color=ORANGE)
        OB = Line(o, b, color=ORANGE)
        AM = Line(a, m)
        BM = Line(b, m)
        OM = Line(o, m, color=GREEN)
        perp_bisect = Line(m + np.array([0, 4.5, 0]), m - np.array([0, 1, 0]), color=GREEN)

        equality_signs_AM_BM = VGroup( SegmentEqualitySign2(AM), SegmentEqualitySign2(BM) )
        equality_signs_OA_OB = VGroup( SegmentEqualitySign1(OA), SegmentEqualitySign1(OB) )

        common_sign_OM = CommonSegmentSign(OM)

        color_AMO = YELLOW
        color_BMO = BLUE

        angle_AMO = RightAngle(OM, AM, quadrant=(-1, -1), color=color_AMO, length=0.3)
        angle_BMO = RightAngle(OM, BM, quadrant=(-1, -1), color=color_BMO)

# INIT equalities
        AM_MB_equality = MathtexSegmentsEquality((label_a, label_m, label_m, label_b))
        OM_common = MathtexCommonSegment((label_o, label_m))
        angles_AMO_BMO_equality = MathTexAnglesEquality(label_a + label_m + label_o, label_b + label_m + label_o)

        triangles_AMO_BMO_equality = MathTexTrianglesEquality(label_a + label_m + label_o, label_b + label_m + label_o)

        conclude_from_sas = ConcludeFromSAS((AM_MB_equality, OM_common, angles_AMO_BMO_equality), triangles_AMO_BMO_equality)
        conclude_from_sas[-1].next_to(conclude_from_sas[:-1], DOWN, buff=0.75)
        conclude_from_sas.next_to(np.array([2, 1, 0])+fc, RIGHT, buff=0)
        rightarrow = Rightarrow().next_to(conclude_from_sas[-1], RIGHT)
        OA_OB_equality = MathtexSegmentsEquality((label_o, label_a, label_o, label_b)).next_to(conclude_from_sas[-1], DOWN, buff=0.758)

        fill_AMO = Polygon(A.get_center(), O.get_center(), M.get_center(), fill_opacity=0.3)
        fill_AMO.set_fill(color_AMO).set_stroke(width=0)
        fill_BMO = Polygon(B.get_center(), O.get_center(), M.get_center(), fill_opacity=0.3)
        fill_BMO.set_fill(color_BMO).set_stroke(width=0)

# ANIMATIONS
        self.wait(1)
        self.play(Create(A), Write(label_A), Create(B), Write(label_B))
        self.wait(0.5)
        self.play(Create(AB))
        self.wait(0.5)
        self.play(Create(M), Write(label_M))
        self.wait(0.5)
        self.play(Create(equality_signs_AM_BM))
        self.wait(0.5)
        self.play(Create(perp_bisect))
        self.add(M)
        self.play(Create(angle_AMO), Create(angle_BMO))
        self.wait(0.5)
        self.play(Create(O), Write(label_O))
        self.wait(0.5)
        self.add(OM, M)
        self.play(Create(OA))
        self.play(Create(OB))
        self.add(O, A, B)
        self.wait(0.5)

        self.play(FadeIn(fill_BMO), FadeIn(fill_AMO))
        self.wait(0.5)

        PlayTwoSegmentsEqualityWiggling(self, ((AM, A, M, label_A, label_M), (BM, B, M, label_M, label_B)), AM_MB_equality)
        self.wait(0.5)
        PlaySegmentIsCommonWiggling(self, (OM, O, M, label_O, label_M), OM_common, common_sign_OM)
        self.wait(0.5)
        PlayTwoAnglesEqualityWiggling(self, angle_AMO, angle_BMO, angles_AMO_BMO_equality)
        self.wait(1)

        PlayConcludeTriangleCongruence(self, conclude_from_sas)
        self.wait(1)

        PlayTwoSegmentsWiggling(self, (OA, A, O, label_A, label_O), (OB, B, O, label_B, label_O))
        self.play(Create(equality_signs_OA_OB))
        self.play(Write(rightarrow))
        self.play(Write(OA_OB_equality))
        
        self.wait(1)

# return
        under_drawing_2 = Group(*conclude_from_sas, rightarrow, OA_OB_equality)
        drawing_2 = Group(*[mob for mob in self.mobjects]).remove(*under_drawing_2)
        return drawing_2, under_drawing_2





class PerpendicularBisector(MovingCameraScene):
    def construct(self):
        self.wait(0.5)
        drawing_1, under_drawing_1 = Scene1.construct(self)
        drawing_2, under_drawing_2 = Scene2.construct(self)
        self.wait(2)
        self.play(*[FadeOut(mob_1) for mob_1 in Group(*drawing_1, *under_drawing_1, *under_drawing_2)])
        self.wait(2)










        

class test(Scene):
    def construct(self):
    
    # init points, segments, labels, MathTex equalities
        a = [-5, 0.5, 0]
        b = [-4, 2.5, 0]
        o = [-1, 0.5, 0]
        x = [-5, -2.5, 0]
        y = [-4, -0.5, 0]
        z = [-1, -2.5, 0]

        A = Dot(a)
        B = Dot(b)
        O = Dot(o)
        vertices_1 = [A, B, O]
        X = Dot(x)
        Y = Dot(y)
        Z = Dot(z)
        vertices_2 = [X, Y, Z]

        AB = always_redraw(lambda: Line(A.get_center(), B.get_center()))
        BO = always_redraw(lambda: Line(B.get_center(), O.get_center()))
        OA = always_redraw(lambda: Line(O.get_center(), A.get_center()))
        sides_1 = [AB, BO, OA]
        XY = always_redraw(lambda: Line(X.get_center(), Y.get_center()))
        YZ = always_redraw(lambda: Line(Y.get_center(), Z.get_center()))
        ZX = always_redraw(lambda: Line(Z.get_center(), X.get_center()))
        sides_2 = [XY, YZ, ZX]

        label_a = 'A'
        label_b = 'B'
        label_o = 'O'
        label_A = always_redraw(lambda: LabelPoint(A, label_a))
        label_B = always_redraw(lambda: LabelPoint(B, label_b, UP*0.75))
        label_O = always_redraw(lambda: LabelPoint(O, label_o, DR*0.5))
        labels_1 = [label_a, label_b, label_o]
        mob_labels_1  = Group(label_A, label_B, label_O)


        label_x = 'X_1'
        label_y = 'Y_1'
        label_z = 'Z_1'
        label_X = always_redraw(lambda: LabelPoint(X, label_x))
        label_Y = always_redraw(lambda: LabelPoint(Y, label_y, UP*0.75))
        label_Z = always_redraw(lambda: LabelPoint(Z, label_z, DR*0.5))
        labels_2 = [label_x, label_y, label_z]
        mob_labels_2 = Group(label_X, label_Y, label_Z)

        abo = label_a + label_b + label_o
        xyz = label_x + label_y + label_z

        triangle_ABO = [vertices_1, sides_1, mob_labels_1, labels_1]
        triangle_XYZ = [vertices_2, sides_2, mob_labels_2, labels_2]

        equality_AB_XY = MathtexSegmentsEquality((label_a, label_b, label_x, label_y))
        equality_BO_YZ = MathtexSegmentsEquality((label_b, label_o, label_y, label_z))
        equality_OA_ZX = MathtexSegmentsEquality((label_o, label_a, label_z, label_x))

        segment_AB = (AB, A, B, label_A, label_B)
        segment_BO = (BO, B, O, label_B, label_O)
        segment_OA = (OA, O, A, label_O, label_A)

        segment_XY = (XY, X, Y, label_X, label_Y)
        segment_YZ = (YZ, Y, Z, label_Y, label_Z)
        segment_ZX = (ZX, Z, X, label_Z, label_X)

        ABO_XYZ_equality = MathTexTrianglesEquality(abo, xyz)

    # end init
        self.camera.frame_shape = (14, 8)
        
        self.add(Dot([0, 0, 0]), Dot([0, 4.5, 0]), Dot([0, -4.5, 0]), Dot([-3.5, 0, 0]), Dot([3.5, 0, 0]))
