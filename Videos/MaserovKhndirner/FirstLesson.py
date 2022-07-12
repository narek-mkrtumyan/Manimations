'''
    6 մատիտ ստացան
    փոքրը չհետաքրքրվեց
    սկսեցին վիճել
    ավագը վերցրել է 5, միջնեկին տվել 1
    6 մատիտը դնեին, ում որը պետք էր
    բաժանեին հավասարաչափ
    մաթեմում կա բաժանելը
    6։2 նշանակում է 6 հատը 2 հոգու հավասար բաժանելու համար քանի հատ կստանա
    6։2=3 => երկուսն էլ կստանան 3-ական
'''



import sys
sys.path.append('../../')
from Functions.qarakusi import *



class Pencils(Scene):
    def construct(self):

# INITS

    # Children
        younger_child = Boy(2).scale(0.7)
        older_child = Boy(1).scale(1)

        children = VGroup(younger_child, older_child).arrange(aligned_edge=DOWN).move_to([0, 1, 0])

        thinking_bubble = ThinkingBubble(False, False, style=1).shift([0.8, 2.75, 0])
        thinking_bubble[0][-1].scale(1.2)
        thought = MathTex(r'\textrm{ես շատ եմ}', r'\textrm{նկարում}', tex_template=armenian_tex_template, font_size=25)
        thought.arrange(DOWN).move_to(thinking_bubble[0][-1].get_center())


    # pencils
        pencils = VGroup(
                Pencil().set_color(RED),
                Pencil().set_color(BLUE),
                Pencil().set_color(ORANGE),
                Pencil().set_color(GREEN),
                Pencil().set_color(LIGHT_BROWN),
                Pencil().set_color(YELLOW)
            )
        pencils.arrange(buff=0.15).next_to(children, DOWN, buff=0.5)
        pencils_center = pencils.get_center()

    # Rectangles over pencils
        rect = Rectangle(height=1.6, width=4.4).move_to(pencils.get_center())
        left_rect = Rectangle(height=1.6, width=2.2).move_to(pencils.get_center()).shift(1.1 * LEFT)
        right_rect = Rectangle(height=1.6, width=2.2).move_to(pencils.get_center()).shift(1.1 * RIGHT)

    # Numbers
        six = MathTex(r'6', font_size=75).next_to(pencils, DOWN, buff=0.5)
        six_over_2 = MathTex(r'6', r':2', r'=', r'3', font_size=75).next_to(pencils, DOWN, buff=1.5)

        left_number_location = pencils[0:3].get_center() + np.array([-1.75, -1.5, 0])
        right_number_location = pencils[0:3].get_center() + np.array([3.35, -1.5, 0])

        tree_a = MathTex(r'3', font_size=75).move_to(left_number_location)
        tree_b = MathTex(r'3', font_size=75).move_to(right_number_location)

        one_a = MathTex(r'1', font_size=75).move_to(left_number_location)
        five_b = MathTex(r'5', font_size=75).move_to(right_number_location)



# ANIMATIONS

    # Draw children and pencils
        self.play(Create(children))
        self.play(Create(pencils))
        self.play(Write(six))
        self.wait(1)

    # Split pencils into groups of 1 and 5
        self.play(
            pencils[0].animate.shift(1.2 * LEFT),
            pencils[1:6].animate.shift(2.2 * RIGHT),
            younger_child.animate.shift(2 * LEFT),
            older_child.animate.shift(2 * RIGHT),
            FadeOut(six),
            rate_func=linear, run_time=1.5
        )
        self.wait(0.5)

    # Write 5 and 1
        self.play(Write(five_b))
        self.wait(0.5)
        self.play(Write(one_a))
        self.wait(1)
    
    # Thinking bubble
        self.play(Write(thinking_bubble))
        self.wait(0.5)
        self.play(Write(thought))
        self.wait(1)
        self.play(FadeOut(thinking_bubble, thought))

    # Bring pencils in the middle
        self.play(
            pencils.animate.arrange().move_to(pencils_center),
            ReplacementTransform(VGroup(five_b, one_a), six),
            run_time=2
        )
        self.wait(1)

    # Write 6:2
        self.play(ReplacementTransform(six, six_over_2[0]))
        self.play(Write(six_over_2[1]))
        self.wait(1)
    
    # Draw a rectangle, divide into 2 equal groups
        self.play(Create(rect))
        self.wait(1)

        self.play(Create(left_rect), Create(right_rect))
        self.remove(rect)
        self.wait(1)
        self.play(
            pencils[0:3].animate().shift(LEFT * 1.5),
            left_rect.animate().shift(LEFT * 1.5),#.set_color(ORANGE),
            pencils[3:6].animate().shift(RIGHT * 1.5),
            right_rect.animate().shift(RIGHT * 1.5),#.set_color(GREEN),
            rate_func=linear, run_time=1.5
        )
        self.wait(1)
    
    # Write =3 and move 3 to equal groups
        self.play(Write(six_over_2[-2:]))
        self.wait(1)

        self.play(
            ReplacementTransform(six_over_2[-1].copy(), tree_a), 
            ReplacementTransform(six_over_2[-1].copy(), tree_b)
        )
        self.wait(1)


        self.play(*[FadeOut(mob) for mob in self.mobjects])










'''
    115սմ պարան, մեկի պարանը մյուսինից 5սմ երկար
    գծում ենք էրկուսն էլ, երկրորդը մի քիչ երկար
    առաջինը քոփի ենք անում իջացնում
    Ավել մասը ինդիքեյթ ենք անում, ներկում նարնջագույն ու գրում 5
    ձևավոր փակագիծ ենք անում, գրում 115
    մկրատով կտրում ենք 5սմ-ն, հեռացնում
    գրում ենք 115-5=110
    110-ը տանում ձևավոր փակագծի մոտ, ավել 5-ը օփասիթին փոքրացնում
    ինդիքեյթ անում երկու հատվածները
    110։2=55
    տանում ենք դրանց վրա
    էն 5սմն բերում ենք տեղը
    վրեն գրում 55+5=60
'''


class Rope(Scene):
    def construct(self):

        font_size = 50 # font size for the numbers written in MathTex


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
        line_2_right = Segment(extra_point, end_2, color=ORANGE)
        line_2_right_white = Segment(extra_point, end_2)

    # dashed line goes down from the end of the first line
        dashed_line_left = DashedLine(end_1, extra_point, dashed_ratio=0.4, dash_length=2 * DEFAULT_DASH_LENGTH)
        dashed_line_right = DashedLine(start_1, start_2, dashed_ratio=0.4, dash_length=2 * DEFAULT_DASH_LENGTH)

    # brace in the right side of the segments and number '115'
        brace_together = BraceBetweenPoints(end_1+np.array([1.25, 0.25, 0]), extra_point+np.array([1.25, -0.25, 0]), direction=[1, 0, 0])
        together_115 = MathTex(r'115', font_size=font_size + 10).next_to(brace_together)
        together_110 = MathTex(r'110', font_size=font_size + 10).next_to(brace_together)

    # number '5' on the extra part of the second line
        extra_is_5 = MathTex(r'5', font_size=font_size).next_to(line_2_right, UP)

    # '115-5=110', '110:2=55'
        difference_115_5 = MathTex(r'115', r'-', r'5', r'=', r'110', font_size=font_size).move_to([0, -2, 0])
        divide_110_2 = MathTex(r'110', r':2=', r'55', font_size=font_size).next_to(difference_115_5, 2*DOWN)

    # '55's on the lines
        line_1_is_55 = MathTex(r'55', font_size=font_size).next_to(line_1, UP)
        line_2_left_is_55 = MathTex(r'55', font_size=font_size).next_to(line_2_left, UP)

    # positions for '55+5=60' on the second line
        new_position_for_2_55 = line_2_left_is_55.get_center() + np.array([-0.75, 0, 0])
        plus_sign = MathTex(r'+', font_size=font_size).next_to(new_position_for_2_55, 1.5*RIGHT)
        new_position_for_5 = plus_sign.get_center() + np.array([0.5, 0, 0])
        line_2_is_60 = MathTex(r'=', r'60', font_size=font_size).move_to(new_position_for_5 + np.array([0.75, 0, 0]))
    
    # scissors
        scissors = Scissors(extra_point)


# ANIMATIONS
    # create lines, brace and write 115
        self.play(Create(line_1))
        self.wait(0.5)
        self.play(Create(line_2))
        self.wait(0.5)

    # create dashed line, write 5
        self.play(
            Create(dashed_line_left),
            Create(dashed_line_right),
            ReplacementTransform(line_1.copy(), line_2_left),
            rate_func=linear, run_time=1.5
        )
        self.wait(0.5)
        self.add(line_2_right_white)
        self.remove(line_2)
        self.play(ApplyWave(line_2_right_white, time_width=2, amplitude=0.25))
        self.wait(0.5)
    
    # color the extra part orange and write 5
        self.play(Create(line_2_right))
        self.remove(line_2_right_white)
        self.wait(0.5)
        self.play(Write(extra_is_5))
        self.wait(0.5)
    
    # create brace and write 115
        self.play(Write(brace_together))
        self.wait(0.25)
        self.play(Write(together_115))
        self.wait(0.5)
    
    # cut (split) second line
        scissors.cut(self)
        self.play(VGroup(line_2_right, extra_is_5).animate(rate_func=linear).shift(0.5*RIGHT))
        scissors.fade_out(self)
        self.wait(0.5)

    # write 115-5=110
        self.play(ReplacementTransform(together_115.copy(), difference_115_5[0:1]))
        self.wait(0.5)
        self.play(Write(difference_115_5[1]))
        self.wait(0.5)
        self.play(ReplacementTransform(extra_is_5.copy(), difference_115_5[2]))
        self.wait(0.5)
        self.play(Write(difference_115_5[3:]))
        self.wait(0.5)
    
    # replace 115 with 110
        self.play(
            VGroup(line_2_right, extra_is_5).animate.set_opacity(0.25),
            FadeOut(together_115),
            ReplacementTransform(difference_115_5[-1:].copy(), together_110),
            run_time=1.5
        )
        self.wait(0.5)
    
    # indicate 2 equal segments
        self.play(ApplyWave(line_1, UP, 0.4, time_width=2, run_time=1.5))
        self.play(ApplyWave(line_2_left, UP, 0.4, time_width=2, run_time=1.5))
        self.wait(0.5)
        self.play(FadeOut(dashed_line_right, dashed_line_left))
        self.wait(0.5)

    # write 110:2=55
        self.play(ReplacementTransform(difference_115_5[-1:].copy(), divide_110_2[0:1]))
        self.wait(0.5)
        self.play(Write(divide_110_2[1:]), run_time=2)
        self.wait(0.5)

    # write 55 on the coressponding lines
        self.play(ReplacementTransform(divide_110_2[-1:].copy(), line_1_is_55))
        self.play(ReplacementTransform(divide_110_2[-1:].copy(), line_2_left_is_55))
        self.wait(0.5)
    
    # join splitted parts of the second line and write '55+5=60'
        self.play(
            VGroup(line_2_right, extra_is_5).animate.set_opacity(1),
            together_110.animate.shift(DOWN).set_opacity(0),
            together_115.shift(UP).set_opacity(0).animate.shift(DOWN).set_opacity(1),
            rate_func=linear, run_time=1.5
        )
        self.wait(0.5)
        self.play(VGroup(line_2_right, extra_is_5).animate(rate_func=linear).shift(0.5*LEFT))
        self.wait(0.5)
        self.play(
            line_2_left_is_55.animate().move_to(new_position_for_2_55),
            extra_is_5.animate().move_to(new_position_for_5),
            rate_func=linear
        )
        self.wait(0.5)
        self.play(Write(plus_sign))
        self.wait(0.5)
        self.play(Write(line_2_is_60))
        self.add(line_2, line_2_right)
        self.wait(0.5)
        self.play(
            FadeOut(line_2_right, line_2_left, line_2_left_is_55, plus_sign, extra_is_5, line_2_is_60[0]),
            line_2_is_60[1].animate().shift(LEFT),
            rate_func=linear
        )
        self.wait(1)

        self.remove(*self.mobjects)
        self.wait(1)


        # add --disable_caching flag during rendering for the scissors cutting audio

