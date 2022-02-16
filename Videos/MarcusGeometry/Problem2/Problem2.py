from manim import *

import sys
sys.path.append("../../")       # relative path to the root of the repository
from Functions.GeometryFunctions.GeometryFunctions import *    # or import specific function


class Problem2(Scene):
    def construct(self):
        fs = 35  # label font_size

# Problem   (animations 0-22)
    # Draw point orange point O, then green circle with center O.
        pointO = Dot(color=ORANGE)
        labelO = LabelPoint(pointO, 'O', font_size=40)
        O = VGroup(pointO, labelO)

        circle = Circle(radius=2.0, color=GREEN)

        self.wait(0.5)
        self.play(
            Write(O, run_time=1),
            Create(circle, run_time=2, rate_func=linear)
        )
        self.wait(1)

    # Then draw horizontal diameter AB, then chord AC.
        pointA = Dot(color=ORANGE).shift(2 * LEFT)
        labelA = LabelPoint(pointA, 'A', font_size=fs)
        A = VGroup(pointA, labelA)

        pointB = Dot(color=ORANGE).shift(2 * RIGHT)
        labelB = LabelPoint(pointB, 'B', 0.5 * DR, font_size=fs)
        B = VGroup(pointB, labelB)

        pointC = Dot(color=ORANGE).move_to(circle.point_at_angle(PI / 3))
        labelC = LabelPoint(pointC, 'C', 0.5 * UR, font_size=fs)
        C = VGroup(pointC, labelC)

        diameter = Line(pointA.get_center(), pointB.get_center(), color=ORANGE)

        chord = Line(pointA.get_center(), pointC.get_center(), color=ORANGE)

        self.play(Write(A))
        self.wait(0.5)

        self.play(Create(diameter, run_time=1.5))
        self.play(Write(B))
        self.wait(0.25)

        self.play(Create(chord, run_time=1.2))
        self.play(Write(C))
        self.wait(4.5)

    # Choose midpoint of AC, mention it K and draw sign of equal segments for AK and KC.
        pointK = Dot(color=ORANGE).move_to(chord.get_midpoint())
        labelK = LabelPoint(pointK, 'K', 0.5 * UL, font_size=fs)
        K = VGroup(pointK, labelK)

        AK = Line(pointA.get_center(), pointK.get_center(), color=ORANGE)
        KC = Line(pointK.get_center(), pointC.get_center(), color=ORANGE)

        self.play(Write(K))
        self.add(AK, KC)
        self.remove(chord)
        self.wait(0.5)

        equality_sign_AK = SegmentEqualitySign1(AK)
        equality_sign_KC = SegmentEqualitySign1(KC)

        self.play(
            Create(equality_sign_AK),
            Create(equality_sign_KC)
        )
        self.wait(0.5)

    # Connect O and K, then draw 4 close to the segment OK.
        OK = Line(pointK.get_center(), pointO.get_center(), color=WHITE)
        four = MathTex(r"4", color=WHITE, font_size=32).next_to(OK.get_midpoint(), UR, buff=SMALL_BUFF)

        self.play(Create(OK, run_time=2))
        self.add(O, K)
        self.wait(2.5)

    # Connect B and C.
        BC = Line(pointB.get_center(), pointC.get_center(), color=WHITE)
        find_BC = MathTex(r'?', font_size=40).next_to(BC.get_midpoint(), LEFT)

        self.play(Write(four))
        self.wait(0.5)
        self.play(Create(BC, run_time=2))
        self.add(B, C)
        self.wait(0.2)
        self.play(Create(find_BC))
        self.wait(3)


# Hint1     (animations 23-33)
    # Mention the sign of equal segments for AO and OB.
        AO = Line(pointA, pointO, color=ORANGE)
        OB = Line(pointO, pointB, color=ORANGE)

        self.add(AO, OB)
        self.remove(diameter)

        equality_sign_AO = SegmentEqualitySign2(AO)
        equality_sign_OB = SegmentEqualitySign2(OB)

        self.wait(1)
        PlayTwoSegmentsWiggling(self, (AO, pointO, pointA, labelA, labelO), (OB, pointO, pointB, labelB, labelO))
        self.wait(0.5)
        self.play(
            Create(equality_sign_AO),
            Create(equality_sign_OB)
        )
        self.wait(1)

    # Wiggle AK and KC
        PlayTwoSegmentsWiggling(self, (AK, pointA, pointK, labelA, labelK), (KC, pointK, pointC, labelK, labelC))
        self.wait(1)
    
    # Fill triangle ABC and Wiggle OK
        fill_ABC = Polygon(pointA.get_center(), pointB.get_center(), pointC.get_center()).set_stroke(width=0).set_fill(BLUE, 0.5)

        self.play(FadeIn(fill_ABC))
        self.add(BC, B, C, A, AK, KC, AO, OB, four, find_BC, OK)
        self.wait(1)
        PlaySegmentWiggling(self, (OK, pointO, pointK, labelO, labelK))
        self.wait(1)


# Solution1     (animations 34)
    # Write below of the graph   BC = 2 * OK = 2 * 4 = 8. (Write 4 by moving the copy of the number 4 from the graph).
        eqn = MathTex(r"OK", "=", "\\frac{BC}{2} \\\ ",
                      "BC", "=", "2\cdot OK", "=", "2\cdot", "4", "=", "8", font_size=42)
        eqn.next_to(circle, RIGHT)

        picture = VGroup(O, A, B, C, K, circle, AO, AK, OB, KC, OK, BC, four,
                         equality_sign_AO, equality_sign_OB, equality_sign_AK, equality_sign_KC, fill_ABC, find_BC)

        self.wait(1)
        PlaySegmentWiggling(self, (OK, pointO, pointK, labelO, labelK))
        self.wait(1)

        self.play(picture.animate.shift(UL))
        self.wait(0.5)

        eqn[0:3].shift(LEFT*1.2)
        eqn[3:11].shift(0.2*LEFT)

        self.play(Write(eqn[0:3], run_time=2, rate_func=linear))
        self.wait()
        self.play(Write(eqn[3:8], run_time=3.2, rate_func=linear))

        self.play(ReplacementTransform(four.copy(), eqn[8], run_time=1.0))
        self.wait(0.5)

        self.play(Write(eqn[9]))
        self.play(Write(eqn[10]))

    # Move the copy of 8 close to the segment BC.
        eight = MathTex(r"8", color=WHITE, font_size=32).next_to(BC.get_midpoint(), LEFT)

        self.play(FadeOut(find_BC))
        self.play(ReplacementTransform(eqn[10].copy(), eight, run_time=1.0))
        self.wait(1)














class Problem2Solution(Scene):
    def construct(self):
        fs = 35  # label font_size

# Drawing
    # Draw point orange point O, then green circle with center O.
        pointO = Dot(color=ORANGE)
        labelO = LabelPoint(pointO, 'O', font_size=40)
        O = VGroup(pointO, labelO)
        circle = Circle(radius=2.0, color=GREEN)

    # Then draw horizontal diameter AB, then chord AC.
        pointA = Dot(color=ORANGE).shift(2 * LEFT)
        labelA = LabelPoint(pointA, 'A', font_size=fs)
        A = VGroup(pointA, labelA)
        pointB = Dot(color=ORANGE).shift(2 * RIGHT)
        labelB = LabelPoint(pointB, 'B', 0.5 * DR, font_size=fs)
        B = VGroup(pointB, labelB)
        pointC = Dot(color=ORANGE).move_to(circle.point_at_angle(PI / 3))
        labelC = LabelPoint(pointC, 'C', 0.5 * UR, font_size=fs)
        C = VGroup(pointC, labelC)
        diameter = Line(pointA.get_center(), pointB.get_center(), color=ORANGE)
        chord = Line(pointA.get_center(), pointC.get_center(), color=ORANGE)

    # Choose midpoint of AC, mention it K and draw sign of equal segments for AK and KC.
        pointK = Dot(color=ORANGE).move_to(chord.get_midpoint())
        labelK = LabelPoint(pointK, 'K', 0.5 * UL, font_size=fs)
        K = VGroup(pointK, labelK)
        AK = Line(pointA.get_center(), pointK.get_center(), color=ORANGE)
        KC = Line(pointK.get_center(), pointC.get_center(), color=ORANGE)
        equality_sign_AK = SegmentEqualitySign1(AK)
        equality_sign_KC = SegmentEqualitySign1(KC)

    # Connect O and K, then draw 4 close to the segment OK.
        OK = Line(pointK.get_center(), pointO.get_center(), color=WHITE)
        four = MathTex(r"4", color=WHITE, font_size=32).next_to(OK.get_midpoint(), UR, buff=SMALL_BUFF)

    # Connect B and C.
        BC = Line(pointB.get_center(), pointC.get_center(), color=WHITE)
        find_BC = MathTex(r'?', font_size=40).next_to(BC.get_midpoint(), LEFT)

# Add everything
        self.add(circle, A, diameter, B, C, K, AK, KC, equality_sign_AK, equality_sign_KC, OK, O, K, four, BC, B, C, find_BC)

# Animations
        self.wait(0.5)
        self.play(pointO.animate(rate_func=there_and_back, run_time=1.5).scale(2))

        AO = Line(pointA, pointO, color=ORANGE)
        OB = Line(pointO, pointB, color=ORANGE)

        self.add(AO, OB)
        self.remove(diameter)

        equality_sign_AO = SegmentEqualitySign2(AO)
        equality_sign_OB = SegmentEqualitySign2(OB)

        self.wait(0.5)
        self.play(
            Create(equality_sign_AO),
            Create(equality_sign_OB)
        )
        self.wait(0.5)

        self.play(pointK.animate(rate_func=there_and_back, run_time=1.5).scale(2))

    # Write below of the graph   BC = 2 * OK = 2 * 4 = 8. (Write 4 by moving the copy of the number 4 from the graph).
        eqn = MathTex(r"OK", "=", "\\frac{BC}{2} \\\ ",
                      "BC", "=", "2\cdot OK", "=", "2\cdot", "4", "=", "8", font_size=42)
        eqn.next_to(circle, RIGHT)
        
        fill_ABC = Polygon(pointA.get_center(), pointB.get_center(), pointC.get_center()).set_stroke(width=0).set_fill(BLUE, 0.5)

        self.wait(1)
        PlaySegmentWiggling(self, (OK, pointO, pointK, labelO, labelK))
        self.wait(0.2)
        self.play(FadeIn(fill_ABC))
        self.wait(0.5)

        picture = VGroup(O, A, B, C, K, circle, AO, AK, OB, KC, OK, BC, four,
                         equality_sign_AO, equality_sign_OB, equality_sign_AK, equality_sign_KC, find_BC, fill_ABC)

        self.play(picture.animate.shift(UL))
        self.wait(0.5)

        eqn[0:3].shift(LEFT*1.2)
        eqn[3:11].shift(0.2*LEFT)

        self.play(Write(eqn[0:3], run_time=2, rate_func=linear))
        self.wait()
        self.play(Write(eqn[3:8], run_time=3.2, rate_func=linear))

        self.play(ReplacementTransform(four.copy(), eqn[8], run_time=1.0))
        self.wait(0.5)

        self.play(Write(eqn[9]))
        self.play(Write(eqn[10]))

    # Move the copy of 8 close to the segment BC.
        eight = MathTex(r"8", color=WHITE, font_size=32).next_to(BC.get_midpoint(), LEFT)

        self.play(FadeOut(find_BC))
        self.play(ReplacementTransform(eqn[10].copy(), eight, run_time=1.0))
        self.wait(1)
