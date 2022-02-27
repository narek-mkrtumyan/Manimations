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

    115սմ պարան, մեկի պարանը մյուսինից 5սմ երկար
    գծում ենք էրկուսն էլ, երկրորդը մի քիչ երկար
    առաջինը քոփի ենք անում իջացնում, ավել մասը ներկում նարնջագույն ու գրում 5
    ձևավոր փակագիծ ենք անում, գրում 115
    մկրատով կտրում ենք 5սմ-ն, հեռացնում ու օփասիթին փոքրացնում
    գրում ենք 115-5=110
    ինդիքեյթ անում էրկուսն էլ
    110/2=55
    տանում ենք դրանց վրա
    էն 5սմն բերում ենք տեղը
    վրեն գրում 55+5=60

'''



import sys
sys.path.append("../../../")
from Functions.QarakusiFunctions import *



class Pens(Scene):
    def construct(self):

# INITS

    # Children
        younger_child = Boy(2).scale(0.7)
        older_child = Boy(1).scale(1)

        children = VGroup(younger_child, older_child).arrange(aligned_edge=DOWN).move_to([0, 2.5, 0])

    # Pens
        # one_pen = Pen()
        # pens = VGroup(*[one_pen.copy() for i in range(6)])
        # pens.arrange().next_to(children, DOWN, buff=0.5)
        # pens_center = pens.get_center()


        pens = VGroup(
                Pencil().set_color(RED),
                Pencil().set_color(GREEN),
                Pencil().set_color(YELLOW),
                Pencil().set_color(BLUE),
                Pencil().set_color(ORANGE),
                Pencil().set_color(PURPLE)
            )
        pens.arrange(buff=0.15).next_to(children, DOWN, buff=0.5)
        pens_center = pens.get_center()



    # Rectangles over pens
        rect = Rectangle(height=1.6, width=4.4).move_to(pens.get_center())
        left_rect = Rectangle(height=1.6, width=2.2).move_to(pens.get_center()).shift(1.1 * LEFT)
        right_rect = Rectangle(height=1.6, width=2.2).move_to(pens.get_center()).shift(1.1 * RIGHT)

    # Numbers
        six = MathTex(r'6', font_size=75).next_to(pens, DOWN, buff=0.5)
        six_over_2 = MathTex(r'6', r':2', r'=', r'3', font_size=75).next_to(pens, DOWN, buff=2)

        left_number_location = pens[0:3].get_center() + np.array([-1.75, -1.5, 0])
        right_number_location = pens[0:3].get_center() + np.array([3.35, -1.5, 0])

        tree_a = MathTex(r'3', font_size=75).move_to(left_number_location)
        tree_b = MathTex(r'3', font_size=75).move_to(right_number_location)

        one_a = MathTex(r'1', font_size=75).move_to(left_number_location)
        five_b = MathTex(r'5', font_size=75).move_to(right_number_location)


# ANIMATIONS

    # Draw children and pens
        self.play(Create(children))
        self.play(Create(pens))
        self.play(Write(six))
        self.wait(1)

    # Split pens into groups of 1 and 5
        self.play(
            pens[0].animate.shift(1.2 * LEFT),
            pens[1:6].animate.shift(2.2 * RIGHT),
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

    # Bring pens in the middle
        self.play(
            pens.animate.arrange().move_to(pens_center),
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
            pens[0:3].animate().shift(LEFT * 1.5),
            left_rect.animate().shift(LEFT * 1.5),#.set_color(ORANGE),
            pens[3:6].animate().shift(RIGHT * 1.5),
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





#################################################################################################################
#################################################################################################################
#################################################################################################################



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
        scissors = Scissors(extra_point.get_center())


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
        self.play(Create(line_2_right[1].reverse_direction())) # revers direction to create from up to bottom
        self.wait(0.25)
        self.play(Create(line_2_right[0]))
        self.add(line_2_right, line_2_left)
        self.remove(line_2)
        self.wait(0.25)
        self.play(Create(extra_is_3))
        self.wait(0.25)
    
    # cut (split) second line
        scissors.cut(self)
        self.play(VGroup(line_2_right, extra_is_3).animate(rate_func=linear).shift(0.75*RIGHT))
        scissors.fade_out(self)
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





class test(Scene):
    def construct(self):
        
        self.wait()

