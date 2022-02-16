from manim import *
import sys

sys.path.append("../../")       # relative path to the root of the repository
from Functions.GeometryFunctions.GeometryFunctions import *

class Problem8(Scene):
    def construct(self):

# Problem     animations 0-10
    # Draw a green circle with center O. 
        pointO = Dot()
        labelO = MathTex("O", font_size=30).next_to(pointO, DOWN, buff=SMALL_BUFF)
        O = VGroup(pointO,labelO)

        circle = Circle(radius=2.0, color=GREEN)

        self.play(
            Create(circle, run_time=3.0),
            Write(O, run_time=3.0)
        )
        self.wait(1)

    # Draw a chord AB, such that \angle AOB is about 40 degree.
        pointA = Dot().move_to(circle.point_at_angle(5*PI/6))
        labelA = MathTex("A", font_size=30).next_to(pointA, LEFT, buff=SMALL_BUFF)
        A = VGroup(pointA,labelA)

        pointB = Dot().move_to(circle.point_at_angle(11*PI/18))
        labelB = MathTex("B", font_size=30).next_to(pointB, UP, buff=SMALL_BUFF)
        B = VGroup(pointB,labelB)

        AB = Line(pointA.get_center(),pointB.get_center())

        pointM = Dot().move_to(AB.get_midpoint())
        labelM = MathTex("M", font_size=30).next_to(pointM, UL)#, buff=SMALL_BUFF)
        M = VGroup(pointM,labelM)

        AM = Line(pointA.get_center(),pointM.get_center())
        MB = Line(pointM.get_center(),pointB.get_center())

        self.play(
            Write(A, run_time=2.0),
            Write(B, run_time=2.0)
        )
        self.play(
            Create(AB, run_time=2)
        )
        self.wait(1)

    # Draw a midpoint of AB, denote it by M. 
        self.play(
            Write(M, run_time=1.5)
        )    
        self.wait(0.5)

    # Draw the sign of equal segments for AM and MB.
        line1 = Line(pointA.get_center(),pointM.get_center()).copy().rotate(PI/2).scale(0.2)
        line2 = Line(pointB.get_center(),pointM.get_center()).copy().rotate(PI/2).scale(0.2)

        self.play(
            Create(line1),
            Create(line2)
        )
        self.wait(1)
    
    # Connect O to M.
        OM = Line(pointO.get_center(),pointM.get_center())

        self.play(
            Create(OM, run_time=2)
        ) 
        self.wait(1)


# Hint1    animations 10-16

    # Connect O to A and B.
        OA = Line(pointO.get_center(), pointA.get_center(), color=ORANGE)
        OB = Line(pointO.get_center(), pointB.get_center(), color=ORANGE)

        self.play(Create(OA, run_time=1.5))
        self.play(Create(OB, run_time=1.5))

        self.wait(1)
    
    # Fill triangles AMO and BMO
        fill_AMO = Polygon(pointA.get_center(), pointM.get_center(), pointO.get_center()).set_stroke(width=0).set_fill(BLUE, opacity=0.5)
        fill_BMO = Polygon(pointB.get_center(), pointM.get_center(), pointO.get_center()).set_stroke(width=0).set_fill(YELLOW, opacity=0.5)

        self.play(FadeIn(fill_AMO))
        self.play(FadeIn(fill_BMO))
        self.add(pointO, pointA, pointB)
        self.wait(1)


# Hint2     animations 16-20
    # Draw the sign of equal segments for OA and OB.
        
        segment_equality_sign_AO_BO = VGroup(
            SegmentEqualitySign2(OA),
            SegmentEqualitySign2(OB),
        )
        self.play(Create(segment_equality_sign_AO_BO))
        self.wait(1)
    
    # Wiggle AM and BM
        PlayTwoSegmentsWiggling(self, (AM, pointA, pointM, labelA, labelM), (MB, pointB, pointM, labelA, labelM), color=RED)
        self.wait(1)

# Solution  animations 21
    # Crate OA and OB, fill triangles AMO and BMO
        self.remove(fill_BMO, fill_AMO, OA, OB, segment_equality_sign_AO_BO)
        self.wait(1)
        self.play(Create(OA))
        self.wait(0.25)
        self.play(Create(OB))
        self.wait(0.25)
        self.play(Create(segment_equality_sign_AO_BO))
        self.add(A, B)
        self.play(FadeIn(fill_AMO), FadeIn(fill_BMO))
        self.wait(1)

    # Show triangles AMO and BMO equality
        common_segment_sign = CommonSegmentSign(OM)

        AO_BO_equality = MathtexSegmentsEquality(('A', 'O', 'B', 'O'))
        AM_MB_equality = MathtexSegmentsEquality(('A', 'M', 'M', 'B'))
        OM_is_common = MathtexCommonSegment(('O', 'M'))
        AMO_BMO_triangles_equality = MathTexTrianglesEquality('AMO', 'BMO')

        conclude_form_sss = ConcludeFromSSS((AO_BO_equality, AM_MB_equality, OM_is_common), AMO_BMO_triangles_equality)
        conclude_form_sss.next_to([2.5, 1, 0], RIGHT, buff=0)
        conclude_form_sss[-1].next_to(conclude_form_sss[:-1], DOWN, buff=0.75).shift(LEFT*0.5)

        PlayTwoSegmentsEqualityWiggling(self, ((OA, pointO, pointA, labelA, labelO), (OB, pointO, pointB, labelB, labelO)), AO_BO_equality)
        self.wait(0.1)
        PlayTwoSegmentsEqualityWiggling(self, ((AM, pointA, pointM, labelA, labelM), (MB, pointM, pointB, labelM, labelB)), AM_MB_equality)
        self.wait(0.3)
        PlaySegmentIsCommonWiggling(self, (OM, pointO, pointM, labelO, labelM), OM_is_common, sign=common_segment_sign)
        self.wait(0.3)
        PlayConcludeTriangleCongruence(self, conclude_form_sss)
        self.wait(2.5)

    # Conclude angles AMO and BMO are equal 90

        rightarrow = Rightarrow().next_to(conclude_form_sss[-1], RIGHT, buff=0.5)
        AMO_BMO_equality = MathTexAnglesEquality('AMO', 'BMO').next_to(conclude_form_sss, DOWN, buff=0.75).shift(LEFT*0.5)
        angles_90 = MathTex(r'=\ 90^{\circ}', font_size=30).next_to(AMO_BMO_equality, RIGHT)


        angle_AMO = Angle(AM, OM, quadrant=(-1, -1), radius=0.4, color=BLUE)
        angle_BMO = Angle(MB, OM, quadrant=(1, -1), other_angle=True, radius=0.25, color=YELLOW)

        AMO_90 = RightAngle(AM, OM, quadrant=(-1, -1), length=0.4, color=BLUE)
        BMO_90 = RightAngle(MB, OM, quadrant=(1, -1), other_angle=True, length=0.25, color=YELLOW)

        MO_is_perp_bisect = MathTex(r'MO\textrm{-ն}\ AB\ \textrm{հատվածի միջնուղղահայացն է}', font_size=40, tex_template=armenian_tex_template)
        MO_is_perp_bisect.next_to([-1.5, -3, 0], RIGHT, buff=0)

        self.play(Create(angle_AMO, rate_func=linear, run_time=1.5))
        self.wait(1.5)
        self.play(Create(angle_BMO, rate_func=linear, run_time=1.5))
        self.wait(0.25)

        self.play(Write(rightarrow))
        PlayTwoAnglesEqualityWiggling(self, angle_AMO, angle_BMO, AMO_BMO_equality)
        self.wait(0.5)
        self.play(Write(angles_90))
        self.wait(0.5)
        self.play(ReplacementTransform(angle_AMO, AMO_90), ReplacementTransform(angle_BMO, BMO_90))
        self.wait(2)
        self.play(pointM.animate(rate_func=there_and_back, run_time=2).scale(2))
        self.wait(0.5)
        self.play(Wiggle(AMO_90, scale_value=1.5, rotation_angle=0.05*TAU), Wiggle(BMO_90, scale_value=1.5, rotation_angle=0.05*TAU))
        self.wait(1)
    
    # Write MO-ն AB-ի միջնուղղահայացն է
        self.play(Write(MO_is_perp_bisect))
        self.wait(1)









class test(Scene):
    def construct(self):
        
        A = Dot()

        crc = Circle(radius=2)

        b_alpha = ValueTracker(0.3)

        B = always_redraw(lambda: Dot(crc.point_at_angle(b_alpha.get_value())))

        AB = always_redraw(lambda: Line(A.get_center(), B.get_center()))

        sign = always_redraw(lambda: CommonSegmentSign(AB))

        self.add(A, B, AB, sign)

        self.play(b_alpha.animate(rate_func=linear, run_time=8).set_value(2*PI))

