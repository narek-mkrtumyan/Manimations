from manim import *
import numpy as np

import sys
sys.path.append("../../../")
from Functions.QarakusiFunctions import *


class Pens(Scene):
    def construct(self):

# INITS
    # Names
        Aram = MathTex(r'\textrm{Արամ}', tex_template=armenian_tex_template, font_size=50).set_color(ORANGE)
        Babken = MathTex(r'\textrm{Բաբկեն}', tex_template=armenian_tex_template, font_size=50).set_color(GREEN)
        yev = MathTex(r'\textrm{և}', tex_template=armenian_tex_template, font_size=50)
        aram_yev_babken = VGroup(Aram, yev, Babken).arrange().move_to([0, 2.5, 0])
        yev.shift(0.05*UP)

    # Pens
        one_pen = SVGMobject('pen.svg').set_color(WHITE).scale(0.5).rotate(PI/7)
        pens = VGroup(*[one_pen.copy() for i in range(6)])
        pens.arrange().next_to(aram_yev_babken, DOWN, buff=1)
    
    # Rectangles over pens
        rect = Rectangle(height=1.6, width=3.2).move_to(pens.get_center())
        left_rect = Rectangle(height=1.6, width=1.6).move_to(pens.get_center()).shift(0.8*LEFT)
        right_rect = Rectangle(height=1.6, width=1.6).move_to(pens.get_center()).shift(0.8*RIGHT)

    # Numbers
        six = MathTex(r'6', font_size=75).next_to(pens, DOWN, buff=0.5)
        six_over_2 = MathTex(r'6', r':2=', r'3', font_size=75).next_to(pens, DOWN, buff=2)

        tree_a = MathTex(r'3', font_size=75, color=ORANGE).move_to(pens[0:3].get_center()).shift(2*LEFT, 1.5*DOWN)
        tree_b = MathTex(r'3', font_size=75, color=GREEN).move_to(pens[3:6].get_center()).shift(2*RIGHT, 1.5*DOWN)

        zero_a = MathTex(r'0', font_size=75, color=ORANGE).move_to(pens[0:3].get_center()).shift(2*LEFT, 1.5*DOWN)
        six_b = MathTex(r'6', font_size=75, color=GREEN).move_to(pens[3:6].get_center()).shift(2*RIGHT, 1.5*DOWN)

        four_a = MathTex(r'4', font_size=75, color=ORANGE).move_to(pens[0:3].get_center()).shift(2*LEFT, 1.5*DOWN)
        two_b = MathTex(r'2', font_size=75, color=GREEN).move_to(pens[3:6].get_center()).shift(2*RIGHT, 1.5*DOWN)

        tree_a_1 = MathTex(r'3', font_size=75, color=ORANGE).move_to(pens[0:3].get_center()).shift(2*LEFT, 1.5*DOWN)
        tree_b_1 = MathTex(r'3', font_size=75, color=GREEN).move_to(pens[3:6].get_center()).shift(2*RIGHT, 1.5*DOWN)


# ANIMATIONS
        self.play(Write(aram_yev_babken))
        self.play(Create(pens))
        self.play(Write(six))
        self.wait(1)

        self.play(ReplacementTransform(six, six_over_2[0]))
        self.play(Write(six_over_2[1:]))
        self.play(
            pens[0:3].animate().shift(2*LEFT),
            pens[3:6].animate().shift(2*RIGHT),
            Aram.animate().shift(1.5*LEFT),
            Babken.animate().shift(1.75*RIGHT),
            FadeOut(yev),
            rate_func=linear, run_time=1.5
        )
        self.play(ReplacementTransform(six_over_2[-1].copy(), tree_a), ReplacementTransform(six_over_2[-1].copy(), tree_b))
        self.wait(1)

        self.play(FadeOut(six_over_2))

        self.play(
            pens[0:3].animate().next_to(pens[3:6], LEFT),
            ReplacementTransform(tree_a, zero_a),
            ReplacementTransform(tree_b, six_b),
            rate_func=linear, run_time=1.5
        )
        self.wait(1)

        self.play(
            pens[0:4].animate().next_to(Aram, DOWN, buff=1),
            ReplacementTransform(zero_a, four_a),
            ReplacementTransform(six_b, two_b),
            rate_func=linear, run_time=1.5
        )
        self.wait(1)

        self.play(
            pens[3].animate().next_to(pens[4], LEFT),
            ReplacementTransform(four_a, tree_a_1),
            ReplacementTransform(two_b, tree_b_1),
            rate_func=linear, run_time=1.5
        )
        self.wait(1)

        self.play(
            FadeOut(tree_a_1, tree_b_1),
            FadeIn(six_over_2),
            pens.animate().arrange().next_to(six_over_2, UP, buff=2),
            rate_func=linear, run_time=1.5
        )
        self.wait(1)

        self.play(Create(rect))
        self.wait(1)

        self.play(Create(left_rect), Create(right_rect))
        self.remove(rect)
        self.play(
            pens[0:3].animate().shift(LEFT*2),
            left_rect.animate().shift(LEFT*2).set_color(ORANGE),
            pens[3:6].animate().shift(RIGHT*2),
            right_rect.animate().shift(RIGHT*2).set_color(GREEN),
            rate_func=linear, run_time=1.5
        )    



class Rope(Scene):
    def construct(self):

        font_size = 50 # font size for the numbers written in MathTex
        
        self.add(bounds)
        # this are bounds on the left and the right quarters of the screen, imperted from QarakusiFunctions.py
        # everything on the screen must be between the bounds
        

# INITS

    # first line
        start_1 = np.array([-2.5, 2, 0])
        end_1 = np.array([0, 2, 0])
        line_1 = Segment(start_1, end_1)

    # second line
        start_2 = np.array([-2.5, 0, 0])
        end_2 = np.array([0.5, 0, 0])
        extra_point = np.array([0, 0, 0])
        line_2 = Segment(start_2, end_2)

    # 2 parts of the second line (line_2_right is the difference between second and first)
        line_2_left = Segment(start_2, extra_point)
        line_2_right = Segment(extra_point, end_2, color=RED)

    # dashed line goes down from the end of the first line
        dashed_line = DashedLine(end_1, extra_point)

    # brace in the right side of the segments and number '85'
        brace_together = BraceBetweenPoints(end_1+np.array([1.5, 0.25, 0]), extra_point+np.array([1.5, -0.25, 0]), direction=[1, 0, 0])
        together_85 = MathTex(r'85', font_size=font_size).next_to(brace_together)

    # number '3' on the extra part of the second line
        extra_is_3 = MathTex(r'3', font_size=font_size).next_to(line_2_right, UP)

    # '85-3=82', '82:2=41'
        difference_85_3 = MathTex(r'85', r'-', r'3', r'=', r'82', font_size=font_size).move_to([0, -2, 0])
        divide_82_2 = MathTex(r'82', r':2=', r'41', font_size=font_size).next_to(difference_85_3, 2*DOWN)

    # '41's on the lines
        line_1_is_41 = MathTex(r'41', font_size=font_size).next_to(line_1, UP)
        line_2_left_is_41 = MathTex(r'41', font_size=font_size).next_to(line_2_left, UP)

    # positions for '41+3=44' on the second line
        new_position_for_2_41 = line_2_left_is_41.get_center() + np.array([-0.75, 0, 0])
        plus_sign = MathTex(r'+', font_size=font_size).next_to(new_position_for_2_41, 1.5*RIGHT)
        new_position_for_3 = plus_sign.get_center() + np.array([0.5, 0, 0])
        line_2_is_44 = MathTex(r'=', r'44', font_size=font_size).move_to(new_position_for_3 + np.array([0.75, 0, 0]))
    
    # scissors
        open_scissors = SVGMobject('open.svg').set_color(WHITE).rotate(PI/10).scale(0.5)
        closed_scissors = ImageMobject('closed.png').set_color(WHITE).scale(0.26).shift(0.1*DOWN).rotate(PI*(1/5)).scale(0.5)


# ANIMATIONS
    # create lines, brace and write 85
        self.play(Create(line_1))
        self.wait(0.25)
        self.play(Create(line_2))
        self.wait(0.25)
        self.play(Create(brace_together))
        self.wait(0.25)
        self.play(Create(together_85))

    # create dashed line, write 3
        self.play(Create(dashed_line))
        self.wait(0.25)
        self.play(Create(line_2_right[1].reverse_direction())) # revers direction to create from up to down
        self.wait(0.25)
        self.play(Create(line_2_right[0]))
        self.add(line_2_right, line_2_left)
        self.remove(line_2)
        self.wait(0.25)
        self.play(Create(extra_is_3))
        self.wait(0.25)
    
    # cut (split) second line
        self.play(FadeIn(open_scissors.move_to([-0.2, -1, 0])))
        self.wait(0.25)
        self.play(open_scissors.animate().move_to([-0.2, -0.4, 0]))
        self.wait(0.25)
        self.remove(open_scissors)
        self.add(closed_scissors.move_to([-0.3, -0.5, 0]))
        self.wait(0.25)
        self.play(FadeOut(closed_scissors))
        self.wait(0.25)
        self.play(VGroup(line_2_right, extra_is_3).animate(rate_func=linear).shift(0.75*RIGHT))
        self.wait(0.25)

    # write 85-3=82
        self.play(ReplacementTransform(together_85.copy(), difference_85_3[0]))
        self.wait(0.25)
        self.play(Write(difference_85_3[1]))
        self.wait(0.25)
        self.play(ReplacementTransform(extra_is_3.copy(), difference_85_3[2]))
        self.wait(0.25)
        self.play(Write(difference_85_3[3:]))
        self.wait(0.25)

    # write 82:2=41
        self.play(ReplacementTransform(difference_85_3[-1].copy(), divide_82_2[0]))
        self.wait(0.25)
        self.play(Write(divide_82_2[1:]))
        self.wait(0.25)

    # write 41 on the coressponding lines
        self.play(ReplacementTransform(divide_82_2[-1].copy(), line_1_is_41))
        self.play(ReplacementTransform(divide_82_2[-1].copy(), line_2_left_is_41))
    
    # join splitted parts of the second line and write '41+3=44'
        self.play(FadeOut(dashed_line))
        self.play(VGroup(line_2_right, extra_is_3).animate(rate_func=linear).shift(0.75*LEFT))
        self.play(
            line_2_left_is_41.animate().move_to(new_position_for_2_41),
            extra_is_3.animate().move_to(new_position_for_3),
            rate_func=linear
        )
        self.play(Write(plus_sign))
        self.play(Write(line_2_is_44))
        self.add(line_2)
        self.play(
            FadeOut(line_2_right, line_2_left, line_2_left_is_41, plus_sign, extra_is_3, line_2_is_44[0]),
            line_2_is_44[1].animate().shift(LEFT),
            rate_func=linear
        )
        self.wait(1)

        self.remove(*self.mobjects)
        self.wait(1)
