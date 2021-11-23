from manim import *

import sys
sys.path.append("../../")       # relative path to the root of the repository
from Functions.GeometryFunctions.GeometryFunctions import *    # or import specific function

class Problem2(Scene):
    def construct(self):
        
        fs = 35   # label font_size
        
    # Draw point orange point O, then green circle with center O. 
        pointO = Dot(color=ORANGE)
        labelO = LabelPoint(pointO, 'O', font_size=40)
        O = VGroup(pointO,labelO)

        circle = Circle(radius=2.0, color=GREEN)

        self.play(
            Write(O, run_time=1),
            Create(circle, run_time=2, rate_func=linear)
        )
        self.wait(1)

    # Then draw horizontal diameter AB, then chord AC. 
        pointA = Dot(color=ORANGE).shift(2*LEFT)
        labelA = LabelPoint(pointA, 'A', font_size=fs)
        A = VGroup(pointA,labelA)

        pointB = Dot(color=ORANGE).shift(2*RIGHT)
        labelB = LabelPoint(pointB, 'B', 0.5*DR, font_size=fs)
        B = VGroup(pointB,labelB)                          

        pointC = Dot(color=ORANGE).move_to(circle.point_at_angle(PI/3))
        labelC = LabelPoint(pointC, 'C', 0.5*UR, font_size=fs)
        C = VGroup(pointC,labelC)

        diameter = Line(pointA.get_center(), pointB.get_center(), color=ORANGE)

        chord = Line(pointA.get_center(), pointC.get_center(), color=ORANGE)

        self.play(Write(A), Write(B))
        self.wait(0.5)

        self.play(Create(diameter, run_time=2))
        self.wait(1)

        self.play(Write(C))
        self.wait(0.5)

        self.play(Create(chord, run_time=2))
        self.wait(1)

    # Choose midpoint of AC, mention it K and draw sign of equal segments for AK and KC.
        pointK = Dot(color=ORANGE).move_to(chord.get_midpoint())
        labelK = LabelPoint(pointK, 'K', 0.5*UL, font_size=fs)
        K = VGroup(pointK,labelK)

        AK = Line(pointA.get_center(), pointK.get_center(), color=ORANGE)
        KC = Line(pointK.get_center(), pointC.get_center(), color=ORANGE)

        self.play(Write(K))
        self.add(AK,KC)
        self.remove(chord)
        self.wait(0.5)

        equality_sign_AK = SegmentEqualitySign1(AK)
        equality_sign_KC = SegmentEqualitySign1(KC)

        self.play(
            Create(equality_sign_AK),
            Create(equality_sign_KC)
        )
        self.wait(1)

    # Connect O and K, then draw 4 close to the segment OK. 
        OK = Line(pointO.get_center(), pointK.get_center(), color=WHITE)
        four = MathTex(r"4", color=WHITE, font_size=32).next_to(OK.get_midpoint(), UR, buff=SMALL_BUFF)

        self.play(Create(OK, run_time=3.0))
        self.add(O, K)
        self.wait(0.5)

        self.play(Write(four))
        self.wait(1)

    # Connect B and C.
        BC = Line(pointB.get_center(), pointC.get_center(), color=WHITE)

        self.play(Create(BC, run_time=3.0))
        self.add(B, C)
        self.wait(1)

    # Mention the sign of equal segments for AO and OB.
        AO = Line(pointA,pointO, color=ORANGE)
        OB = Line(pointO,pointB, color=ORANGE)

        self.add(AO,OB)
        self.remove(diameter)

        equality_sign_AO = SegmentEqualitySign2(AO)
        equality_sign_OB = SegmentEqualitySign2(OB)

        self.play(
            Create(equality_sign_AO),
            Create(equality_sign_OB)
        )
        self.wait(1)

    # Make AK thinner then thicker.
        self.play(
            AK.animate(run_time=2.0, rate_func=there_and_back).set_stroke_width(10)
        )
        self.wait(1)

    # Make KC thinner then thicker.
        self.play(
            KC.animate(run_time=2.0, rate_func=there_and_back).set_stroke_width(10)
        )
        self.wait(1)

    # Make AO thinner then thicker.

        self.play(
            AO.animate(run_time=2.0, rate_func=there_and_back).set_stroke_width(10)
        )
        self.wait(1)

    # Make OB thinner then thicker.
        self.play(
            OB.animate(run_time=2.0, rate_func=there_and_back).set_stroke_width(10)
        )
        self.wait(1)

    # Write below of the graph   BC = 2 * OK = 2 * 4 = 8. (Write 4 by moving the copy of the number 4 from the graph).
        eqn = MathTex(r"BC", "=", "2\cdot OK", "=", "2\cdot",  "4", "=", "8", font_size=42)
        eqn.next_to(circle, DOWN)

        self.play(Write(eqn[0:5], run_time=2, rate_func=linear))

        self.play(ReplacementTransform(four.copy(),eqn[5], run_time=2.5))
        self.wait(0.5)

        self.play(Write(eqn[6]))
        self.wait(0.5)

        self.play(Write(eqn[7]))
        self.wait(0.5)

    # Move the copy of 8 close to the segment BC.
        eight = MathTex(r"8", color=WHITE, font_size=32).next_to(BC.get_midpoint(), LEFT)

        self.play(ReplacementTransform(eqn[7].copy(),eight, run_time=3.0))
        self.wait(0.5)

    # Draw green rectangle (box) around the number 8.
        box = SurroundingRectangle(eqn[7], color=GREEN, buff=SMALL_BUFF)

        self.play(Create(box))
        self.wait(1)
