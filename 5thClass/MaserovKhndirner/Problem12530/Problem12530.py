from manim import *
import numpy as np
import sys

from pyparsing import Or

sys.path.append('../../../')
sys.path.append('../../')
sys.path.append('../')
sys.path.append('../../../Functions')
from Functions.QarakusiFunctions import *

# ԽՆԴԻՐ
# Աշոտը Հասմիկից 3 անգամ ավելի քիչ մատիտ ունի։ 
# Գտնել, թե քանի՞ մատիտ ունեն նրանք միասին, եթե Հասմիկի մատիտները շատ են Աշոտի մատիտներից 8-ով։


class Problem12530(Scene):
    def construct(self):
        self.add(bounds)

    # init segments and names
        segment_ashot = Segment([-3, 2, 0], [-1.5, 2, 0])
        segment_hasmik_1 = segment_ashot.copy()
        name_ashot = MathTex(r'\textrm{Աշոտ}', tex_template=armenian_tex_template, font_size=50).next_to(segment_ashot, 1.5*UP)
        name_ashot.shift(0.5*LEFT)
        name_hasmik = MathTex(r'\textrm{Հասմիկ}', tex_template=armenian_tex_template, font_size=50).next_to(segment_hasmik_1, 1.5*UP)
        name_hasmik.shift(0.25*LEFT + 2.5*DOWN)

    # animations segments and names
        self.play(Create(segment_ashot))
        self.play(Create(name_ashot))

        self.play(segment_hasmik_1.animate(rate_func=linear).shift(2.5*DOWN))
        self.play(Create(name_hasmik))

    # init dashed line
        dashed_line = DashedLine(segment_ashot[0][0].get_start_and_end()[1], segment_hasmik_1[0][0].get_start_and_end()[1])

    # init and animation (multiply Hasmik's segment by 3)
        segments_hasmik = MultiplySegmentRotating(self, segment_hasmik_1, factor=3, merge_segments=False)

    # inits
        extra_is_8 = MathTex(r'8', font_size=50, color=ORANGE)
        segment_extra = Segment(segments_hasmik[0][0][0].get_start_and_end()[1], segments_hasmik[2][0][0].get_start_and_end()[1],
                            color=ORANGE, mathtex=extra_is_8)

        eight_over_2_is_4 = MathTex(r'8', r':2=', r'4', font_size=50, color=ORANGE).next_to(segments_hasmik, DOWN).shift(2.5*DOWN)
        eight_over_2_is_4[1].set_color(WHITE)
        
        half_of_extra_is_4_left = MathTex(r'4', font_size=50, color=ORANGE).next_to(segments_hasmik[1], UP).shift(0.3*DOWN)
        half_of_extra_is_4_right = MathTex(r'4', font_size=50, color=ORANGE).next_to(segments_hasmik[2], UP).shift(0.3*DOWN)

        segment_hasmik_1_is_4 = MathTex(r'4', font_size=50, color=WHITE).next_to(segments_hasmik[0], UP).shift(0.3*DOWN)

        four_plus_4_plus_4_is_12 = MathTex(r'4', r'+', r'4', r'+', r'4', r'=', r'12', font_size=50)
        four_plus_4_plus_4_is_12[2].set_color(ORANGE)
        four_plus_4_plus_4_is_12[4].set_color(ORANGE)
        four_plus_4_plus_4_is_12.next_to(eight_over_2_is_4, UP*2)

        ashot_is_4 = MathTex(r'4', font_size=50).next_to(segment_ashot, UP).shift(0.3*DOWN)

        hasmik_is_12 = MathTex(r'12', font_size=50)
        segment_hasmik = Segment(
                segments_hasmik[0][0][0].get_start_and_end()[0], segments_hasmik[-1][0][0].get_start_and_end()[1], mathtex=hasmik_is_12
            )
        
        four_plus_12_is_16 = MathTex(r'4', r'+', r'12', r'=', r'16',font_size=50)
        # four_plus_12_is_16.next_to(name_hasmik).shift(UP + RIGHT*0.5)
        four_plus_12_is_16.next_to(four_plus_4_plus_4_is_12, UP*2)

        brace = BraceBetweenPoints(
                segments_hasmik[-1][0][0].get_start_and_end()[1] + np.array([0.5, 3, 0]),
                segments_hasmik[-1][0][0].get_start_and_end()[1] + np.array([0.5, -0.5, 0]),
                direction=([1, 0, 0])
            )
        answer_16 = MathTex(r'16', font_size=70).next_to(brace)
        
        
    # animmations
        self.play(Create(dashed_line))
        self.play(Create(segment_extra))
        self.wait(0.5)
        
        self.play(ReplacementTransform(extra_is_8.copy(), eight_over_2_is_4[0]))
        self.play(Write(eight_over_2_is_4[1:]))
        self.wait(0.5)

        self.play(ReplacementTransform(extra_is_8, VGroup(half_of_extra_is_4_left, half_of_extra_is_4_right)))
        self.wait(0.5)
        self.play(ReplacementTransform(half_of_extra_is_4_left.copy(), segment_hasmik_1_is_4))

        self.play(ReplacementTransform(segment_hasmik_1_is_4.copy(), ashot_is_4))

        self.play(
            ReplacementTransform(segment_hasmik_1_is_4.copy(), four_plus_4_plus_4_is_12[0]),
            ReplacementTransform(half_of_extra_is_4_right.copy(), four_plus_4_plus_4_is_12[4]),
            ReplacementTransform(half_of_extra_is_4_left.copy(), four_plus_4_plus_4_is_12[2])
        )
        self.play(
            Write(four_plus_4_plus_4_is_12[1]),
            Write(four_plus_4_plus_4_is_12[3]),
            Write(four_plus_4_plus_4_is_12[5]),
            Write(four_plus_4_plus_4_is_12[-1]),
        )
        self.play(FadeOut(segment_extra, dashed_line))
        self.add(segment_hasmik[0])
        self.play(
            ReplacementTransform(VGroup(segment_hasmik_1_is_4, half_of_extra_is_4_left, half_of_extra_is_4_right), hasmik_is_12),
            FadeOut(*segments_hasmik)
        )

        self.play(Create(brace))

        self.play(ReplacementTransform(ashot_is_4.copy(), four_plus_12_is_16[0]))
        self.play(Write(four_plus_12_is_16[1]))
        self.play(ReplacementTransform(hasmik_is_12.copy(), four_plus_12_is_16[2]))
        self.play(Write(four_plus_12_is_16[3:]))

        self.play(ReplacementTransform(four_plus_12_is_16[-1].copy(), answer_16))
        self.wait(1)

