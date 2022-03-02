from curses.textpad import rectangle
from symtable import Function
from manim import *
import numpy as np
import sys

sys.path.append('../../../')
from Functions.QarakusiFunctions import *


class Rabbits_4(Scene):
    def construct(self):

# INITS

        up_cage = np.array([0, 0.75, 0])
        right_cage = np.array([0.75, -0.5, 0])
        left_cage = np.array([-0.75, -0.5, 0])
        down_cage = np.array([0, -0.5, 0])

        rabbits = VGroup(*[Rabbit() for i in range(4)]).arrange(buff=0.75).shift(2*UP + RIGHT)
        cages = VGroup(*[Cage() for i in range(3)]).arrange(buff=0.75).shift(DOWN + RIGHT)

        number_of_rabbits = MathTex(r'4', font_size=100).to_edge(LEFT, buff=1).shift(2*UP)
        number_of_cages = MathTex(r'3', font_size=100, color=GOLD).to_edge(LEFT, buff=1).shift(DOWN)

        greater = MathTex(r'>', font_size=100).shift(2*UP)

        thinking_bubble_right = ThinkingBubble(from_left_to_right=False, smooth=False).scale(1.3)
        thinking_bubble_left = ThinkingBubble(smooth=False, style=2)

        thinking_bubble_left.move_to(rabbits[3].get_center()).shift(0.8*UP + 1.75*RIGHT)
        text_1 = MathTex(r'\textrm{տեղ տվեք,}', r'\textrm{ես էլ գամ}', tex_template=armenian_tex_template, font_size=30)
        text_1.arrange(DOWN, buff=0.15).move_to(thinking_bubble_left.get_center())

        thinking_bubble_right.move_to(cages[2].get_center() + down_cage).shift(1.5*UP + LEFT)
        text_2 = MathTex(r'\textrm{արի, արի}', tex_template=armenian_tex_template, font_size=30)
        text_2.move_to(thinking_bubble_right.get_center()).shift(0.5*UP)


# ANIMATIONS
        self.play(Create(rabbits))
        self.wait(0.5)
        self.play(Create(cages))
        self.wait(0.5)
        self.play(Write(number_of_rabbits))
        self.wait(0.5)
        self.play(Write(number_of_cages))
        self.wait(0.5)

        self.play(rabbits[0].animate(rate_fun=linear).move_to(cages[0].get_center() + down_cage))
        self.wait(0.25)
        self.play(rabbits[1].animate(rate_fun=linear).move_to(cages[1].get_center() + down_cage))
        self.wait(0.25)
        self.play(rabbits[2].animate(rate_fun=linear).move_to(cages[2].get_center() + down_cage))
        self.wait(0.25)

        self.play(Circumscribe(rabbits[3], color=GREEN))
        self.play(FadeIn(thinking_bubble_left))
        self.play(Create(text_1))
        self.play(FadeIn(thinking_bubble_right))
        self.play(Create(text_2))
        self.wait(1)
        self.play(
            rabbits[2].animate().move_to(cages[2].get_center() + left_cage),
            thinking_bubble_right.animate().shift(0.75*LEFT),
            text_2.animate().shift(0.75*LEFT),
            rate_fun=linear
        )
        self.wait(0.25)
        self.play(FadeOut(thinking_bubble_right, thinking_bubble_left, text_1, text_2))

        self.play(rabbits[3].animate(rate_fun=linear).move_to(cages[2].get_center() + right_cage))
        self.wait(0.25)

        self.play(
            number_of_rabbits.animate(rate_func=linear).next_to(greater, LEFT),
            number_of_cages.animate(rate_func=linear).next_to(greater, RIGHT)
        )
        self.wait(0.25)
        self.play(Write(greater))
        self.wait(0.25)

        self.play(Wiggle(cages[2], scale_value=1.3, rotation_angle=0.02*TAU, run_time=3))
        self.wait(0.25)

        self.play(rabbits[1].animate(rate_fun=linear).move_to(cages[2].get_center() + up_cage))
        self.wait(0.25)

        self.play(Wiggle(cages[1], scale_value=1.3, rotation_angle=0.02*TAU, run_time=3))
        self.wait(0.25)



class Rabbits_14(Scene):
    def construct(self):

        rabbits = VGroup(*[Rabbit().scale(0.6) for i in range(14)])
        rabbits.arrange_in_grid(cols=5)
        rabbits.shift(2 * UP)

        cages = VGroup(*[Cage().scale(1.1) for i in range(3)])
        cages.arrange(buff=0.75).shift(1.5 * DOWN + RIGHT)

        number_of_rabbits = MathTex(r'14', font_size=100)
        number_of_rabbits.to_edge(LEFT, buff=1).shift(2 * UP)
        number_of_cages = MathTex(r'3', font_size=100, color=GOLD)
        number_of_cages.to_edge(LEFT, buff=1).shift(1.5 * DOWN)

        self.add(rabbits, cages, number_of_rabbits, number_of_cages)



class Triangle(Scene):
    def construct(self):

# INITS
        coord_vertices = [
            np.array([-2, -1, 0]),
            np.array([0, np.sqrt(12) - 1, 0]),
            np.array([2, -1, 0]),
        ]

        vertices = VGroup(*[Dot(coord) for coord in coord_vertices], color=WHITE)
        sides = VGroup(
            Line(coord_vertices[0], coord_vertices[1], color=WHITE),
            Line(coord_vertices[1], coord_vertices[2], color=WHITE),
            Line(coord_vertices[2], coord_vertices[0], color=WHITE)
        )

        unit_vectors = [*[side.get_unit_vector() for side in sides]]
        
        dots = VGroup(*[Dot(coord_vertices[i] + unit_vectors[i], color=ORANGE) for i in range(len(coord_vertices))])

        self.add(*vertices, *sides, *dots)



class Calendar(Scene):
    def construct(self):
        
        calendar = CalendarMonth(year=2022, month=3, first_weekday=4).shift(DOWN)

        squares = VGroup(*[Square(1) for i in range(7)]).arrange(buff=0.5).shift(DOWN)

        cages = VGroup(*[Cage().scale(0.4) for i in range(7)])
        for i in range(len(cages)):
            cages[i].move_to(squares[i].get_center())

        people = VGroup(*[Man(i).scale(0.7) for i in range(1, 9)])
        people.arrange(buff=0.5).shift(2.5*UP)

        rabbits = VGroup(*[Rabbit().scale(0.5).move_to(people[i].get_center()) for i in range(len(people))])

        self.play(Create(people))
        self.wait()

        self.play(Create(calendar))
        self.wait()
        self.play(FadeOut(calendar.VMyear, calendar.outline, calendar.VMmonth, calendar.background, calendar.full_days))
        self.wait()

        self.play(
            ReplacementTransform(calendar.week_blocks, squares),
            *[calendar.week_days[i].animate.move_to(squares[i].get_center()).scale(2) for i in range(7)]
        )
        self.wait()
        self.play(ReplacementTransform(people, rabbits))
        self.wait()
        self.play(
            ReplacementTransform(squares, cages),
            *[calendar.week_days[i].animate.next_to(cages[i], UP, buff=0.1) for i in range(len(cages))]
        )
        self.wait()

        self.play(*[rabbits[i].animate.move_to(cages[i].get_center()) for i in range(len(rabbits) - 1)])
        self.wait()




class ChessKings(Scene):
    def construct(self):
        board = Board().make_chess()
        board.color4()
        board.scale(0.8)
        self.add(board)

        _groups_of_four = [[[], [], [], []], [[], [], [], []], [[], [], [], []], [[], [], [], []]]
        for i in range(8):
            for j in range(8):
                _groups_of_four[int(i/2)][int(j/2)].append(board.cells[i][j])
        for i in range(len(_groups_of_four)):
            for j in range(len(_groups_of_four[i])):
                _groups_of_four[i][j] = VGroup(*_groups_of_four[i][j])
            _groups_of_four[i] = VGroup(*_groups_of_four[i])
        groups_of_four = VGroup()
        for i in range(len(_groups_of_four)-1, -1, -1):
            for j in range(len(_groups_of_four[i])):
                groups_of_four.add(_groups_of_four[i][j])



        white_king = ChessFigures().white_king.scale(0.8).shift(UL*1.2)

        # kings = VGroup(white_king.copy() for i in range(16))

        
        # self.play(groups_of_four.animate.arrange_in_grid(4, 4, buff=0.5))

        self.wait()






class test(Scene):
    def construct(self):

        scissors = Scissors()
        scissors.cut_in(self)
        scissors.cut_out(self)

