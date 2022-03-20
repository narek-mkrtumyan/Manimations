from lib2to3.pgen2.token import RIGHTSHIFT
import sys
from tokenize import Number
from cairo import OPERATOR_CLEAR

from numpy import broadcast_arrays
sys.path.append('../../')
from Functions.QarakusiFunctions import *


class Problem12248(Scene):
    def construct(self):
#INIT
        Problem = Tex("Դիցուք $N \\times N$ չափանի տախտակի վանդակներից ոչ մեկը ներկած չէ:"
                      " Յուրաքանչյուր քայլի թույլատրվում է ներկել մեկ վանդակ,"
                      " որն ունի առնվազն երկու չներկած հարևան վանդակ:"
                      " Պարզել, թե առավելագույնը քանի՞ վանդակ է հնարավոր ներկել:",
                      tex_template=armenian_tex_template, font_size=27).shift(3.2*UP)
        board = Board(stroke_width=1, rows=6, columns=6).shift(4*LEFT)
        n = Tex("$N$", tex_template=armenian_tex_template, font_size=27).next_to(board, LEFT)
        n1 = n.copy().next_to(board, UP)

        V = []
        E = []
        G = Graph(V, E)
        for i in range(6):
            for j in range(6):
                G.add_vertices((i, j))
                G[(i, j)].move_to(board.cells[i][j].get_center()).set_color(ORANGE)
        for i in range(5):
            for j in range(6):
                G.add_edges(((i, j), (i+1, j))).set_color(ORANGE)
        for i in range(6):
            for j in range(5):
                G.add_edges(((i, j), (i, j+1))).set_color(ORANGE)

        
        for i in range(6):
            for j in range(6):
                self.remove(G[(i, j)])

        vertical_edges0 = VGroup()
        for i in range(6):
            vertical_edges0 += G.edges[(0, i), (1, i)]
        vertical_edges1 = VGroup()
        for i in range(6):
            vertical_edges1 += G.edges[(1, i), (2, i)]
        vertical_edges2 = VGroup()
        for i in range(6):
            vertical_edges2 += G.edges[(2, i), (3, i)]
        vertical_edges3 = VGroup()
        for i in range(6):
            vertical_edges3 += G.edges[(3, i), (4, i)]
        vertical_edges4 = VGroup()
        for i in range(6):
            vertical_edges4 += G.edges[(4, i), (5, i)]
        vertical_edges = vertical_edges4 + vertical_edges3 + vertical_edges2 + vertical_edges1 + vertical_edges0
        vertical_copies = VGroup(vertical_edges.copy())

        horizontal_edges0 = VGroup()
        for i in range(6):
            horizontal_edges0 += G.edges[(i, 0), (i, 1)]
        horizontal_edges1 = VGroup()
        for i in range(6):
            horizontal_edges1 += G.edges[(i, 1), (i, 2)]
        horizontal_edges2 = VGroup()
        for i in range(6):
            horizontal_edges2 += G.edges[(i, 2), (i, 3)]
        horizontal_edges3 = VGroup()
        for i in range(6):
            horizontal_edges3 += G.edges[(i, 3), (i, 4)]
        horizontal_edges4 = VGroup()
        for i in range(6):
            horizontal_edges4 += G.edges[(i, 4), (i, 5)]
        horizontal_edges = horizontal_edges4 + horizontal_edges3 + horizontal_edges2 + horizontal_edges1 + horizontal_edges0
        horizontal_copies = VGroup(horizontal_edges.copy())

        number_of_vertical_edges = MathTex("N(N-1)")
        number_of_horizontal_edges = MathTex("N(N-1)").shift(3*RIGHT)
        plus = MathTex("+").shift(1.5*RIGHT)
        all_edges = VGroup(number_of_vertical_edges, number_of_horizontal_edges, plus)
        number_of_edges = MathTex("2N(N-1)").shift(1.5*RIGHT)
        l = Line([0, 0, 0], [2.5, 0, 0]).next_to(number_of_edges, 0.5*DOWN)
        haytarar = MathTex("2").next_to(l, 0.5*DOWN)
        final_answer = MathTex("=", "N(N-1)").next_to(l, RIGHT).shift(0.115*UP)
        box = SurroundingRectangle(final_answer[1], color=GREEN, buff=SMALL_BUFF)


    #init for wiggle        
        A = G[(0, 0)].copy() 


#INIT
        case_1 = MathTex("N=2").shift(6*LEFT+2*UP)
        board_2 = Board(stroke_width=1, rows=2, columns=2).next_to(case_1, DOWN+0.5*RIGHT)
        box_0 = MathTex("?", color=ORANGE).move_to(board_2.cells[0][0])
        box_1 = MathTex("?", color=ORANGE).move_to(board_2.cells[0][1])
        box_2 = MathTex("?", color=ORANGE).move_to(board_2.cells[1][0])
        box_3 = MathTex("?", color=ORANGE,).move_to(board_2.cells[1][1])
        answer = MathTex("2").set_color(GREEN).next_to(board_2, RIGHT, buff=0.1)


        board_2_ = Board(stroke_width=1, rows=2, columns=2).next_to(board_2, RIGHT, buff=1)
        box_0_ = MathTex("?", color=ORANGE).move_to(board_2_.cells[0][0])
        box_1_ = MathTex("?", color=ORANGE).move_to(board_2_.cells[0][1])
        box_2_ = MathTex("?", color=ORANGE).move_to(board_2_.cells[1][0])
        box_3_ = MathTex("?", color=ORANGE).move_to(board_2_.cells[1][1])
        answer_ = MathTex("2").set_color(GREEN).next_to(board_2_, RIGHT, buff=0.1)

        glob_answer = MathTex("2").set_color(GREEN).next_to(answer_, RIGHT, buff=1)
        answer_box = SurroundingRectangle(glob_answer, color=ORANGE, buff=SMALL_BUFF)

        case_2 = MathTex("N=3").next_to(case_1, DOWN, buff=2.5)
        board_3_1 = Board(stroke_width=1, rows=3, columns=3).next_to(case_2, DOWN+0.5*RIGHT)
        box_1_1 = MathTex("?", color=ORANGE).move_to(board_3_1.cells[1][0])
        box_2_1 = MathTex("?", color=ORANGE).move_to(board_3_1.cells[1][1])
        box_3_1 = MathTex("?", color=ORANGE).move_to(board_3_1.cells[2][2])
        box_4_1 = MathTex("?", color=ORANGE).move_to(board_3_1.cells[0][2])
        answer_1 = MathTable("4").set_color(GREEN).next_to(board_3_1, RIGHT, buff=0.1)

        board_3_2 = Board(stroke_width=1, rows=3, columns=3).next_to(board_3_1, RIGHT, buff=1)
        box_1_2 = MathTex("?", color=ORANGE).move_to(board_3_2.cells[1][1])
        box_2_2 = MathTex("?", color=ORANGE).move_to(board_3_2.cells[2][0])
        box_3_2 = MathTex("?", color=ORANGE).move_to(board_3_2.cells[2][2])
        box_4_2 = MathTex("?", color=ORANGE).move_to(board_3_2.cells[0][2])
        box_5_2 = MathTex("?", color=ORANGE).move_to(board_3_2.cells[0][0])
        answer_2 = MathTex("5").set_color(GREEN).next_to(board_3_2, RIGHT, buff=0.1)

        board_3_3 = Board(stroke_width=1, rows=3, columns=3).next_to(board_3_2, RIGHT, buff=1)
        box_1_3 = MathTex("?", color=ORANGE).move_to(board_3_3.cells[0][0])
        box_2_3 = MathTex("?", color=ORANGE).move_to(board_3_3.cells[0][1])
        box_3_3 = MathTex("?", color=ORANGE).move_to(board_3_3.cells[1][0])
        box_4_3 = MathTex("?", color=ORANGE).move_to(board_3_3.cells[2][2])
        box_5_3 = MathTex("?", color=ORANGE).move_to(board_3_3.cells[1][2])
        box_6_3 = MathTex("?", color=ORANGE).move_to(board_3_3.cells[2][1])
        answer_3 = MathTex("6").set_color(GREEN).next_to(board_3_3, RIGHT, buff=0.1)

        glob_answer_3 = MathTex("6", "  ?").next_to(answer_3, RIGHT, buff=1)
        glob_answer_3[0].set_color(GREEN)
        glob_answer_3[1].set_color(YELLOW).next_to(glob_answer_3[0], RIGHT, buff=0.3)
        answer_box_3 = SurroundingRectangle(glob_answer_3[0], color=ORANGE, buff=SMALL_BUFF)
        glob_answer_box_3 = VGroup(glob_answer_3, answer_box_3)

        l1 = Line([1, 2, 0], [1, -5, 0])

        case_3 = MathTex("N=5").shift(UR+RIGHT)
        board_5 = Board(size=0.6, stroke_width=1, rows=5, columns=5).shift(2*RIGHT).next_to(case_3, DR)
        answer_5 = MathTex("20", "  ?").next_to(board_5, RIGHT, buff=0.2)
        answer_5[0].set_color(GREEN)
        answer_5[1].set_color(YELLOW).next_to(answer_5[0], RIGHT, buff=0.3)
        box_answer_5 = SurroundingRectangle(answer_5[0], color=ORANGE, buff=SMALL_BUFF)

        
        first_question = Tex(
            "Հարց 1․"," Արդյո՞ք ցանկացած $N$-ի համար ներկվող\\\\ վանդակների առավելագույն քանակը $N(N-1)$ է։",
            tex_template=armenian_tex_template, font_size=27).shift(UP+4*RIGHT)
        second_question = Tex(
            "Հարց 2․"," Ո՞րն է վանդակները ներկելու\\\\ ամենաօպտիմալ եղանակը։",
            tex_template=armenian_tex_template, font_size=27).next_to(first_question, DOWN, buff=0.5)
        first_question[0].set_color(YELLOW)
        second_question[0].set_color(YELLOW)


        
        
        

#ANIMATION
        self.play(Write(Problem), run_time=9)
        self.wait()

        self.play(Write(case_1))
        self.play(Create(board_2))
        self.play(Create(box_0))
        self.play(
            Indicate(board_2.cells[0][1]),
            Indicate(board_2.cells[1][0])
        )
        self.play(
            board_2.cells[0][0].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_0)
        )
        
        self.play(Create(box_1))
        self.play(Indicate(board_2.cells[1][1]))
        self.play(FadeOut(box_1))

        self.play(Create(box_2))
        self.play(Indicate(board_2.cells[1][1]))
        self.play(FadeOut(box_2))

        self.play(Create(box_3))
        self.play(
            Indicate(board_2.cells[0][1]),
            Indicate(board_2.cells[1][0])
        )
        self.play(
            board_2.cells[1][1].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_3)
        )
        
        self.play(Write(answer))


        # self.play(Create(board_2_))
        # self.play(Create(box_1_))
        # self.play(
        #     Indicate(board_2_.cells[0][0]),
        #     Indicate(board_2_.cells[1][1])
        # )
        # self.play(
        #     board_2_.cells[0][1].animate.set_fill(GREEN, opacity=0.5),
        #     FadeOut(box_1_)
        # )
        
        # self.play(Create(box_0_))
        # self.play(Indicate(board_2_.cells[1][0]))
        # self.play(FadeOut(box_0_))

        # self.play(Create(box_3_))
        # self.play(Indicate(board_2_.cells[1][0]))
        # self.play(FadeOut(box_3_))

        # self.play(Create(box_2_))
        # self.play(
        #     Indicate(board_2_.cells[0][0]),
        #     Indicate(board_2_.cells[1][1])
        # )
        # self.play(
        #     board_2_.cells[1][0].animate.set_fill(GREEN, opacity=0.5),
        #     FadeOut(box_2_)
        # )
        # self.play(Write(answer_))

        board_2_2 = board_2.copy()
        self.play(board_2_2.animate.shift(3*RIGHT).rotate(angle=PI/2))
        answer_2_2 = MathTex("2").set_color(GREEN).next_to(board_2_2, RIGHT, buff=0.1)
        self.play(Write(answer_2_2))

        self.play(
            Circumscribe(answer),
            Circumscribe(answer_2_2)
        )

        self.play(
            answer.animate.move_to(glob_answer),
            answer_2_2.animate.move_to(glob_answer)
        )
        self.play(Create(answer_box))
        self.add(glob_answer)
        self.remove(answer, answer_2_2)


        self.play(Write(case_2))
        self.play(Create(board_3_1))
        self.play(Create(box_1_1))
        self.play(
            Indicate(board_3_1.cells[0][0]),
            Indicate(board_3_1.cells[2][0]),
            Indicate(board_3_1.cells[1][1])
        )
        self.play(
            board_3_1.cells[1][0].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_1_1)
        )

        self.play(Create(box_2_1))
        self.play(
            Indicate(board_3_1.cells[2][1]),
            Indicate(board_3_1.cells[0][1]),
            Indicate(board_3_1.cells[1][2])
        )
        self.play(
            board_3_1.cells[1][1].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_2_1)
        )

        self.play(Create(box_3_1))
        self.play(
            Indicate(board_3_1.cells[2][1]),
            Indicate(board_3_1.cells[1][2]),
        )
        self.play(
            board_3_1.cells[2][2].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_3_1)
        )

        self.play(Create(box_4_1))
        self.play(
            Indicate(board_3_1.cells[0][1]),
            Indicate(board_3_1.cells[1][2]),
        )
        self.play(
            board_3_1.cells[0][2].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_4_1)
        )
        self.play(Write(answer_1))


        self.play(Create(board_3_2))

        self.play(Create(box_1_2))
        self.play(
            Indicate(board_3_2.cells[1][0]),
            Indicate(board_3_2.cells[0][1]),
            Indicate(board_3_2.cells[1][2]),
            Indicate(board_3_2.cells[2][1])
        )
        self.play(
            board_3_2.cells[1][1].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_1_2)
        )
        
        self.play(Create(box_2_2))
        self.play(
            Indicate(board_3_2.cells[2][1]),
            Indicate(board_3_2.cells[1][0])
        )
        self.play(
            board_3_2.cells[2][0].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_2_2)
        )


        self.play(Create(box_3_2))
        self.play(
            Indicate(board_3_2.cells[2][1]),
            Indicate(board_3_2.cells[1][2])
        )
        self.play(
            board_3_2.cells[2][2].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_3_2)
        )


        self.play(Create(box_4_2))
        self.play(
            Indicate(board_3_2.cells[0][1]),
            Indicate(board_3_2.cells[1][2])
        )
        self.play(
            board_3_2.cells[0][2].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_4_2)
        )
        

        self.play(Create(box_5_2))
        self.play(
            Indicate(board_3_2.cells[0][1]),
            Indicate(board_3_2.cells[1][0])
        )
        self.play(
            board_3_2.cells[0][0].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_5_2)
        )
        

        self.play(Write(answer_2))

        
        self.play(Create(board_3_3))

        self.play(Create(box_1_3))
        self.play(
            Indicate(board_3_3.cells[1][0]),
            Indicate(board_3_3.cells[0][1])
        )
        self.play(
            board_3_3.cells[0][0].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_1_3)
        )

        
        self.play(Create(box_2_3))
        self.play(
            Indicate(board_3_3.cells[0][2]),
            Indicate(board_3_3.cells[1][1])
        )
        self.play(
            board_3_3.cells[0][1].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_2_3)
        )


        self.play(Create(box_3_3))
        self.play(
            Indicate(board_3_3.cells[2][0]),
            Indicate(board_3_3.cells[1][1])
        )
        self.play(
            board_3_3.cells[1][0].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_3_3)
        )

        self.play(Create(box_4_3))
        self.play(
            Indicate(board_3_3.cells[2][1]),
            Indicate(board_3_3.cells[1][2])
        )
        self.play(
            board_3_3.cells[2][2].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_4_3)
        )

        self.play(Create(box_5_3))
        self.play(
            Indicate(board_3_3.cells[1][1]),
            Indicate(board_3_3.cells[0][2])
        )
        self.play(
            board_3_3.cells[1][2].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_5_3)
        )
        


        self.play(Create(box_6_3))
        self.play(
            Indicate(board_3_3.cells[1][1]),
            Indicate(board_3_3.cells[2][0]),
        )
        self.play(
            board_3_3.cells[2][1].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_6_3)
        )
        

        self.play(Write(answer_3))

        self.play(
            Circumscribe(answer_1),
            Circumscribe(answer_2),
            Circumscribe(answer_3)
        )

        self.play(
            ReplacementTransform(answer_1, glob_answer_3[0]),
            ReplacementTransform(answer_2, glob_answer_3[0]),
            ReplacementTransform(answer_3, glob_answer_3[0]),
        )
        self.play(Create(answer_box_3))
        self.play(Write(glob_answer_3[1]))
        
        self.play(
            FadeOut(board_3_1),
            FadeOut(board_3_2),
            board_3_3.animate.move_to(board_3_1),
            glob_answer_box_3.animate.move_to(board_3_2.cells[1][0]),
            run_time=2 
        )

        self.play(Write(l1), run_time=2)

        self.play(Write(case_3))

        self.play(Create(board_5))

        for i in range(4):
            self.play(board_5.cells[0][i].animate.set_fill(GREEN, opacity=0.5))
        for i in range(3):
            self.play(board_5.cells[i+1][0].animate.set_fill(GREEN, opacity=0.5))
        for i in range(4):
            self.play(board_5.cells[4-i][4].animate.set_fill(GREEN, opacity=0.5))
        for i in range(3):
            self.play(board_5.cells[4][3-i].animate.set_fill(GREEN, opacity=0.5))

#init
        board_3 = board_3_3.copy()
        board_5_final = VGroup(board_5, board_3)

        All_boards = VGroup(
            board_2, board_2_2, board_5_final, board_3_3, 
            glob_answer, glob_answer_box_3, answer_box, l1, answer_5,
            case_1, case_2, case_3, box_answer_5
        )


        self.play(board_3.animate.move_to(board_5).scale(0.6/0.75), run_time=2)
        self.play(Write(answer_5[0]))
        self.play(Create(box_answer_5))
        self.play(Write(answer_5[1]))
        self.play(All_boards.animate.move_to([-3,0,0]).scale(0.5))

        self.play(Write(first_question), run_time=2)

        self.play(FadeOut(All_boards))


        
        self.play(FadeOut(Problem))
        self.play(first_question.animate.shift(2.2*UP+LEFT))
        second_question.shift(2.2*UP+LEFT)
        self.play(Create(board), run_time=3)
        
        self.play(Write(n), Write(n1))
        self.wait()


        self.play(Create(G), run_time=9)
        self.wait()


        self.add(A)
        self.remove(G[(0, 0)])
        

        self.play(board.cells[0][0].animate.set_fill(GREEN, opacity=0.5))
        self.play(
            Wiggle(G.edges[(0, 0), (0, 1)], scale_value=1.5),
            Wiggle(G.edges[(0, 0), (1, 0)], scale_value=1.5)
        )
        self.play(
            FadeOut(
                G.edges[(0, 0), (0, 1)],
                G.edges[(0, 0), (1, 0)])
            )
        self.wait()
        self.play(board.cells[2][3].animate.set_fill(GREEN, opacity=0.5))
        self.play(
            Wiggle(G.edges[(1, 3), (2, 3)], scale_value=1.5),
            Wiggle(G.edges[(2, 3), (3, 3)], scale_value=1.5),
            Wiggle(G.edges[(2, 2), (2, 3)], scale_value=1.5),
            Wiggle(G.edges[(2, 3), (2, 4)], scale_value=1.5)
        )
        self.play(
            FadeOut(
                G.edges[(1, 3), (2, 3)],
                G.edges[(2, 3), (3, 3)],
                G.edges[(2, 2), (2, 3)],
                G.edges[(2, 3), (2, 4)])
            )
        self.wait()
        self.play(board.cells[5][4].animate.set_fill(GREEN, opacity=0.5))
        self.play(
            Wiggle(G.edges[(5, 4), (5, 5)], scale_value=1.5),
            Wiggle(G.edges[(4, 4), (5, 4)], scale_value=1.5),
            Wiggle(G.edges[(5, 3), (5, 4)], scale_value=1.5)
        )
        self.play(
            FadeOut(
                G.edges[(5, 4), (5, 5)],
                G.edges[(4, 4), (5, 4)],
                G.edges[(5, 3), (5, 4)])
            )
        self.wait()
        self.play(board.cells[5][5].animate.set_fill(RED, opacity=0.5))
        self.wait()
        self.play(
            G[(4, 5)].animate(rate_func=there_and_back).set_color(YELLOW),
            Circumscribe(board.cells[4][5], run_time=1.5)
        )
        self.play(Wiggle(G.edges[(4, 5), (5, 5)], scale_value=1.5, rotation_angle=0.03*TAU))
        self.wait()
        self.play(board.cells[5][5].animate.set_fill(RED, opacity=0))
        self.wait()
        self.play(
            board.cells[5][4].animate.set_fill(GREEN, opacity=0),
            board.cells[2][3].animate.set_fill(GREEN, opacity=0),
            board.cells[0][0].animate.set_fill(GREEN, opacity=0),
            FadeIn(G.edges[(0, 0), (0, 1)],
                   G.edges[(0, 0), (1, 0)]
            ),
            FadeIn(G.edges[(1, 3), (2, 3)],
                   G.edges[(2, 3), (3, 3)],
                   G.edges[(2, 2), (2, 3)],
                   G.edges[(2, 3), (2, 4)]
            ),
            FadeIn(G.edges[(5, 4), (5, 5)],
                   G.edges[(4, 4), (5, 4)],
                   G.edges[(5, 3), (5, 4)]
            )
        )
        self.play(Write(second_question))
        self.play(second_question.animate.set_opacity(0.3))
        
        self.play(
            vertical_edges0.animate.shift(4*RIGHT).scale(0.75),
            vertical_edges1.animate.shift(4*RIGHT).scale(0.75),
            vertical_edges2.animate.shift(4*RIGHT).scale(0.75),
            vertical_edges3.animate.shift(4*RIGHT).scale(0.75),
            vertical_edges4.animate.shift(4*RIGHT).scale(0.75)
        )
        self.wait()
        self.play(Transform(vertical_edges, number_of_vertical_edges))
        self.wait()


        
        self.play(
            horizontal_edges0.animate.shift(7.5 * RIGHT).scale(0.75),
            horizontal_edges1.animate.shift(7.5 * RIGHT).scale(0.75),
            horizontal_edges2.animate.shift(7.5 * RIGHT).scale(0.75),
            horizontal_edges3.animate.shift(7.5 * RIGHT).scale(0.75),
            horizontal_edges4.animate.shift(7.5 * RIGHT).scale(0.75)
        )
        self.wait()
        self.play(Transform(horizontal_edges, number_of_horizontal_edges))
        self.wait()
        
        self.play(Create(plus))
        self.add(number_of_vertical_edges, number_of_horizontal_edges)
        self.remove(horizontal_edges)
        self.remove(vertical_edges)

        
        self.wait()
        self.play(Transform(all_edges, number_of_edges))
        self.wait()
   
        self.play(Create(l))        
        self.play(Write(haytarar))
        self.wait()

        self.play(Write(final_answer), run_time=2)
        self.wait()

        self.play(Create(box))
        self.wait(2)

        self.play(FadeIn(horizontal_copies, vertical_copies))

        self.play(
            first_question.animate.set_opacity(0.3),
            second_question.animate.set_opacity(1)
        )

        V1 = []
        E1 = []
        G1 = Graph(V1, E1)
        for i in range(6):
            for j in range(6):
                G1.add_vertices((i, j))
                G1[(i, j)].move_to(board.cells[i][j].get_center()).set_color(ORANGE)
        for i in range(5):
            for j in range(6):
                G1.add_edges(((i, j), (i + 1, j))).set_color(ORANGE)
        for i in range(6):
            for j in range(5):
                G1.add_edges(((i, j), (i, j + 1))).set_color(ORANGE)
        
        self.add(G1)
        self.remove(vertical_copies, horizontal_copies)

        for i in range(6):
            for j in range(6):
                self.remove(G1[(i, j)])

        # for i in range(5):
        #     for j in range(5):
        #         if i+j<5:
        #             self.play(board.cells[i][j].animate.set_fill(GREEN, opacity=0.5), run_time=0.5)
        #             self.play(
        #                 Wiggle(G1.edges[(i, j), (i+1, j)], scale_value=1.5),
        #                 Wiggle(G1.edges[(i, j), (i, j+1)], scale_value=1.5)
        #             )
        #             self.play(FadeOut(G1.edges[(i, j), (i+1, j)], G1.edges[(i, j), (i, j+1)]), run_time=0.5)

        # for i in range(5):
        #     for j in range(5):
        #         if i+j<5:
        #             self.play(board.cells[5-i][5-j].animate.set_fill(GREEN, opacity=0.5), run_time=0.5)
        #             self.play(
        #                 Wiggle(G1.edges[(4-i, 5-j), (5-i, 5-j)], scale_value=1.5),
        #                 Wiggle(G1.edges[(5-i, 4-j), (5-i, 5-j)], scale_value=1.5)
        #             )
        #             self.play(FadeOut(G1.edges[(4-i, 5-j), (5-i, 5-j)], G1.edges[(5-i, 4-j), (5-i, 5-j)]), run_time=0.5)
        # self.wait()

        for i in range(5):
            self.play(board.cells[0][i].animate.set_fill(GREEN, opacity=0.5), run_time=0.5)
            self.play(
                Wiggle(G1.edges[(0, i), (1, i)], scale_value=1.5),
                Wiggle(G1.edges[(0, i), (0, i+1)], scale_value=1.5)
            )
            self.play(FadeOut(G1.edges[(0, i), (1, i)], G1.edges[(0, i), (0, i+1)]), run_time=0.5)

        for i in range(4):
            self.play(board.cells[i+1][0].animate.set_fill(GREEN, opacity=0.5), run_time=0.5)
            self.play(
                Wiggle(G1.edges[(i+1, 0), (i+2, 0)], scale_value=1.5),
                Wiggle(G1.edges[(i+1, 0), (i+1, 1)], scale_value=1.5)
            )
            self.play(FadeOut(G1.edges[(i+1, 0), (i+2, 0)], G1.edges[(i+1, 0), (i+1, 1)]), run_time=0.5)

        for i in range(5):
            self.play(board.cells[5-i][5].animate.set_fill(GREEN, opacity=0.5), run_time=0.5)
            self.play(
                Wiggle(G1.edges[(4-i, 5), (5-i, 5)], scale_value=1.5),
                Wiggle(G1.edges[(5-i, 4), (5-i, 5)], scale_value=1.5)
            )
            self.play(FadeOut(G1.edges[(4-i, 5), (5-i, 5)], G1.edges[(5-i, 4), (5-i, 5)]), run_time=0.5)

        for i in range(4):
            self.play(board.cells[5][4-i].animate.set_fill(GREEN, opacity=0.5), run_time=0.5)
            self.play(
                Wiggle(G1.edges[(5, 3-i), (5, 4-i)], scale_value=1.5),
                Wiggle(G1.edges[(4, 4-i), (5, 4-i)], scale_value=1.5)
            )
            self.play(FadeOut(G1.edges[(5, 3-i), (5, 4-i)], G1.edges[(4, 4-i), (5, 4-i)]), run_time=0.5)

        board_center = VGroup()
        
        for i in range(4):
            for j in range(4):
                board_center += board.cells[i+1][j+1]
        
        self.play(FocusOn(board_center), opacity=0.75)

        # board_edges = VGroup()
        # for i in range(5):
        #     board_edges += board.cells[0][i]
        #     board_edges += board.cells[5][i]
        # for i in range(3):
        #     board_edges += board.cells[i+1][0]
        #     board_edges += board.cells[i+1][5]

        # self.play(board_edges.animate.set_opacity(0.4))

        for i in range(1, 4):
            self.play(board.cells[1][i].animate.set_fill(GREEN, opacity=0.5), run_time=0.25)
            self.play(FadeOut(G1.edges[(1, i), (2, i)], G1.edges[(1, i), (1, i+1)]), run_time=0.25)

        for i in range(2, 4):
            self.play(board.cells[i][1].animate.set_fill(GREEN, opacity=0.5), run_time=0.25)
            self.play(FadeOut(G1.edges[(i, 1), (i+1, 1)], G1.edges[(i, 1), (i, 2)]), run_time=0.25)

        for i in range(1, 4):
            self.play(board.cells[5-i][4].animate.set_fill(GREEN, opacity=0.5), run_time=0.25)
            self.play(FadeOut(G1.edges[(4-i, 4), (5-i, 4)], G1.edges[(5-i, 3), (5-i, 4)]), run_time=0.25)

        for i in range(2, 4):
            self.play(board.cells[4][5-i].animate.set_fill(GREEN, opacity=0.5), run_time=0.25)
            self.play(FadeOut(G1.edges[(4, 4-i), (4, 5-i)], G1.edges[(3, 5-i), (4, 5-i)]), run_time=0.25)

        self.play(board.cells[2][2].animate.set_fill(GREEN, opacity=0.5), run_time=0.25)
        self.play(FadeOut(G1.edges[(2, 2), (2, 3)], G1.edges[(2, 2), (3, 2)]), run_time=0.25)

        self.play(board.cells[3][3].animate.set_fill(GREEN, opacity=0.5), run_time=0.25)
        self.play(FadeOut(G1.edges[(2, 3), (3, 3)], G1.edges[(3, 2), (3, 3)]), run_time=0.25)

        self.play(first_question.animate.set_opacity(1))
        self.play(Circumscribe(first_question))
        self.play(Circumscribe(second_question))

















































class test1(Scene):
    def construct(self):
        s = Square()
        self.play(s.animate(rate_func=there_and_back).scale(3))
        self.play(FadeOut(s))
        self.wait()

class test2(Scene):
    def construct(self):
        V = [1, 2]
        E = [(1, 2)]
        G = Graph(V, E)
        self.play(Create(G))
        #self.remove(G[1], G[2])
        self.play(Wiggle(G.edges[(1, 2)], scale_value=1.5))
        self.play(Wiggle(G.edges[(1, 2)], scale_value=1.5))
        self.wait()


class first_case(Scene):
    def construct(self):
#INIT
        board_2 = Board(stroke_width=1, rows=2, columns=2).shift(3*LEFT)
        box_0 = MathTex("?", color=ORANGE).move_to(board_2[0][0])
        box_1 = SurroundingRectangle(board_2.cells[0][1], color=ORANGE, buff=SMALL_BUFF)
        box_2 = SurroundingRectangle(board_2.cells[1][0], color=ORANGE, buff=SMALL_BUFF)
        box_3 = SurroundingRectangle(board_2.cells[1][1], color=ORANGE, buff=SMALL_BUFF)
        answer = MathTex("2").set_color(GREEN).next_to(board_2, RIGHT, buff=0.1)

        board_2_ = Board(stroke_width=1, rows=2, columns=2)
        box_0_ = SurroundingRectangle(board_2_.cells[0][0], color=ORANGE, buff=SMALL_BUFF)
        box_1_ = SurroundingRectangle(board_2_.cells[0][1], color=ORANGE, buff=SMALL_BUFF)
        box_2_ = SurroundingRectangle(board_2_.cells[1][0], color=ORANGE, buff=SMALL_BUFF)
        box_3_ = SurroundingRectangle(board_2_.cells[1][1], color=ORANGE, buff=SMALL_BUFF)
        answer_ = MathTex("2").set_color(GREEN).next_to(board_2_, RIGHT, buff=0.1)

        glob_answer = MathTex("2").set_color(GREEN).next_to(answer_, RIGHT, buff=2)
        answer_box = SurroundingRectangle(glob_answer, color=ORANGE, buff=SMALL_BUFF)

#ANIMATION
        self.play(Create(board_2))
        self.play(Create(box_0))
        self.play(
            Indicate(board_2.cells[0][1]),
            Indicate(board_2.cells[1][0])
        )
        self.play(board_2.cells[0][0].animate.set_fill(GREEN, opacity=0.5))
        self.play(FadeOut(box_0))
        
        self.play(Create(box_1))
        self.play(
            Indicate(board_2.cells[0][0]),
            Indicate(board_2.cells[1][1])
        )
        self.play(FadeOut(box_1))

        self.play(Create(box_2))
        self.play(
            Indicate(board_2.cells[0][0]),
            Indicate(board_2.cells[1][1])
        )
        self.play(FadeOut(box_2))

        self.play(Create(box_3))
        self.play(
            Indicate(board_2.cells[0][1]),
            Indicate(board_2.cells[1][0])
        )
        self.play(board_2.cells[1][1].animate.set_fill(GREEN, opacity=0.5))
        self.play(FadeOut(box_3))
        self.play(Write(answer))


        self.play(Create(board_2_))
        self.play(Create(box_1_))
        self.play(
            Indicate(board_2_.cells[0][0]),
            Indicate(board_2_.cells[1][1])
        )
        self.play(board_2_.cells[0][1].animate.set_fill(GREEN, opacity=0.5))
        self.play(FadeOut(box_1_))
        
        self.play(Create(box_0_))
        self.play(
            Indicate(board_2_.cells[0][1]),
            Indicate(board_2_.cells[1][0])
        )
        self.play(FadeOut(box_0_))

        self.play(Create(box_3_))
        self.play(
            Indicate(board_2_.cells[0][1]),
            Indicate(board_2_.cells[1][0])
        )
        self.play(FadeOut(box_3_))

        self.play(Create(box_2_))
        self.play(
            Indicate(board_2_.cells[0][0]),
            Indicate(board_2_.cells[1][1])
        )
        self.play(board_2_.cells[1][0].animate.set_fill(GREEN, opacity=0.5))
        self.play(FadeOut(box_2_))
        self.play(Write(answer_))

        self.play(
            Circumscribe(answer),
            Circumscribe(answer_)
        )

        self.play(
            answer.animate.move_to(glob_answer),
            answer_.animate.move_to(glob_answer)
        )
        self.play(Create(answer_box))


class second_case(Scene):
    def construct(self):

#INIT
        board_3_1 = Board(stroke_width=1, rows=3, columns=3).shift(5.5*LEFT+2*DOWN)
        box_1_1 = SurroundingRectangle(board_3_1.cells[1][0], color=ORANGE, buff=SMALL_BUFF)
        box_2_1 = SurroundingRectangle(board_3_1.cells[1][1], color=ORANGE, buff=SMALL_BUFF)
        box_3_1 = SurroundingRectangle(board_3_1.cells[2][2], color=ORANGE, buff=SMALL_BUFF)
        box_4_1 = SurroundingRectangle(board_3_1.cells[0][2], color=ORANGE, buff=SMALL_BUFF)
        answer_1 = MathTable("4").set_color(GREEN).next_to(board_3_1, RIGHT, buff=0.1)

#ANIMATION
        self.play(Create(board_3_1))
        self.play(Create(box_1_1))
        self.play(
            Indicate(board_3_1.cells[0][0]),
            Indicate(board_3_1.cells[2][0]),
            Indicate(board_3_1.cells[1][1])
        )
        self.play(board_3_1.cells[1][0].animate.set_fill(GREEN, opacity=0.5))
        self.play(FadeOut(box_1_1))

        self.play(Create(box_2_1))
        self.play(
            Indicate(board_3_1.cells[1][0]),
            Indicate(board_3_1.cells[2][1]),
            Indicate(board_3_1.cells[0][1]),
            Indicate(board_3_1.cells[1][2])
        )
        self.play(board_3_1.cells[1][1].animate.set_fill(GREEN, opacity=0.5))
        self.play(FadeOut(box_2_1))

        self.play(Create(box_3_1))
        self.play(
            Indicate(board_3_1.cells[2][1]),
            Indicate(board_3_1.cells[1][2]),
        )
        self.play(board_3_1.cells[2][2].animate.set_fill(GREEN, opacity=0.5))
        self.play(FadeOut(box_3_1))

        self.play(Create(box_4_1))
        self.play(
            Indicate(board_3_1.cells[0][1]),
            Indicate(board_3_1.cells[1][2]),
        )
        self.play(board_3_1.cells[0][2].animate.set_fill(GREEN, opacity=0.5))
        self.play(FadeOut(box_4_1))

        self.play(Write(answer_1))

#INIT
        board_3_2 = Board(stroke_width=1, rows=3, columns=3).next_to(board_3_1, RIGHT, buff=1)
        box_1_2 = SurroundingRectangle(board_3_2.cells[1][1], color=ORANGE, buff=SMALL_BUFF)
        box_2_2 = SurroundingRectangle(board_3_2.cells[2][0], color=ORANGE, buff=SMALL_BUFF)
        box_3_2 = SurroundingRectangle(board_3_2.cells[2][2], color=ORANGE, buff=SMALL_BUFF)
        box_4_2 = SurroundingRectangle(board_3_2.cells[0][2], color=ORANGE, buff=SMALL_BUFF)
        box_5_2 = SurroundingRectangle(board_3_2.cells[0][0], color=ORANGE, buff=SMALL_BUFF)
        answer_2 = MathTable("5").set_color(GREEN).next_to(board_3_2, RIGHT, buff=0.1)


#ANIMATION
        self.play(Create(board_3_2))

        self.play(Create(box_1_2))
        self.play(
            Indicate(board_3_2.cells[1][0]),
            Indicate(board_3_2.cells[0][1]),
            Indicate(board_3_2.cells[1][2]),
            Indicate(board_3_2.cells[2][1])
        )
        self.play(board_3_2.cells[1][1].animate.set_fill(GREEN, opacity=0.5))
        self.play(FadeOut(box_1_2))
        
        self.play(Create(box_2_2))
        self.play(
            Indicate(board_3_2.cells[2][1]),
            Indicate(board_3_2.cells[1][0])
        )
        self.play(board_3_2.cells[2][0].animate.set_fill(GREEN, opacity=0.5))
        self.play(FadeOut(box_2_2))

        self.play(Create(box_3_2))
        self.play(
            Indicate(board_3_2.cells[2][1]),
            Indicate(board_3_2.cells[1][2])
        )
        self.play(board_3_2.cells[2][2].animate.set_fill(GREEN, opacity=0.5))
        self.play(FadeOut(box_3_2))

        self.play(Create(box_4_2))
        self.play(
            Indicate(board_3_2.cells[0][1]),
            Indicate(board_3_2.cells[1][2])
        )
        self.play(board_3_2.cells[0][2].animate.set_fill(GREEN, opacity=0.5))
        self.play(FadeOut(box_4_2))

        self.play(Create(box_5_2))
        self.play(
            Indicate(board_3_2.cells[0][1]),
            Indicate(board_3_2.cells[1][0])
        )
        self.play(board_3_2.cells[0][0].animate.set_fill(GREEN, opacity=0.5))
        self.play(FadeOut(box_5_2))

        self.play(Write(answer_2))

#INIT
        board_3_3 = Board(stroke_width=1, rows=3, columns=3).next_to(board_3_2, RIGHT, buff=1)
        box_1_3 = SurroundingRectangle(board_3_3.cells[0][0], color=ORANGE, buff=SMALL_BUFF)
        box_2_3 = SurroundingRectangle(board_3_3.cells[0][1], color=ORANGE, buff=SMALL_BUFF)
        box_3_3 = SurroundingRectangle(board_3_3.cells[1][0], color=ORANGE, buff=SMALL_BUFF)
        box_4_3 = SurroundingRectangle(board_3_3.cells[2][2], color=ORANGE, buff=SMALL_BUFF)
        box_5_3 = SurroundingRectangle(board_3_3.cells[1][2], color=ORANGE, buff=SMALL_BUFF)
        box_6_3 = SurroundingRectangle(board_3_3.cells[2][1], color=ORANGE, buff=SMALL_BUFF)
        
        answer_3 = MathTable("6").set_color(GREEN).next_to(board_3_3, RIGHT, buff=0.1)

#ANIMATION
        
        self.play(Create(board_3_3))

        self.play(Create(box_1_3))
        self.play(
            Indicate(board_3_3.cells[1][0]),
            Indicate(board_3_3.cells[0][1])
        )
        self.play(board_3_3.cells[0][0].animate.set_fill(GREEN, opacity=0.5))
        self.play(FadeOut(box_1_3))
        
        self.play(Create(box_2_3))
        self.play(
            Indicate(board_3_3.cells[0][0]),
            Indicate(board_3_3.cells[0][2]),
            Indicate(board_3_3.cells[1][1])
        )
        self.play(board_3_3.cells[0][1].animate.set_fill(GREEN, opacity=0.5))
        self.play(FadeOut(box_2_3))

        self.play(Create(box_3_3))
        self.play(
            Indicate(board_3_3.cells[0][0]),
            Indicate(board_3_3.cells[2][0]),
            Indicate(board_3_3.cells[1][1])
        )
        self.play(board_3_3.cells[1][0].animate.set_fill(GREEN, opacity=0.5))
        self.play(FadeOut(box_3_3))

        self.play(Create(box_4_3))
        self.play(
            Indicate(board_3_3.cells[2][1]),
            Indicate(board_3_3.cells[1][2])
        )
        self.play(board_3_3.cells[2][2].animate.set_fill(GREEN, opacity=0.5))
        self.play(FadeOut(box_4_3))

        self.play(Create(box_5_3))
        self.play(
            Indicate(board_3_3.cells[1][1]),
            Indicate(board_3_3.cells[2][2]),
            Indicate(board_3_3.cells[0][2])
        )
        self.play(board_3_3.cells[1][2].animate.set_fill(GREEN, opacity=0.5))
        self.play(FadeOut(box_5_3))


        self.play(Create(box_6_3))
        self.play(
            Indicate(board_3_3.cells[1][1]),
            Indicate(board_3_3.cells[2][0]),
            Indicate(board_3_3.cells[2][2])
        )
        self.play(board_3_3.cells[2][1].animate.set_fill(GREEN, opacity=0.5))
        self.play(FadeOut(box_6_3))

        self.play(Write(answer_3))

#INIT
        glob_answer_3 = MathTex("6").next_to(answer_3, RIGHT, buff=1).set_color(GREEN)
        answer_box = SurroundingRectangle(glob_answer_3, color=ORANGE, buff=SMALL_BUFF)

        self.play(
            ReplacementTransform(answer_1, glob_answer_3),
            ReplacementTransform(answer_2, glob_answer_3),
            ReplacementTransform(answer_3, glob_answer_3),
        )
        self.play(Create(answer_box))
        self.wait()


class induction(Scene):
    def construct(self):
        board_5 = Board(size=0.6, stroke_width=1, rows=5, columns=5).shift(2*RIGHT)

        self.play(Create(board_5))

        for i in range(4):
            self.play(board_5.cells[0][i].animate.set_fill(GREEN, opacity=0.5))
        for i in range(3):
            self.play(board_5.cells[i+1][0].animate.set_fill(GREEN, opacity=0.5))
        for i in range(4):
            self.play(board_5.cells[4-i][4].animate.set_fill(GREEN, opacity=0.5))
        for i in range(3):
            self.play(board_5.cells[4][3-i].animate.set_fill(GREEN, opacity=0.5))
            


        #self.play(Create(board_3))
        #self.play(board_3.cells[1][1].animate.set_fill(GREEN, opacity=0.5))
        #self.play(board_3.animate.move_to(board_5).scale(0.6/0.75))

        self.wait()


class first_second(Scene):
    def construct(self):

#INIT
        case_1 = MathTex("N=2").shift(6*LEFT+2*UP)
        board_2 = Board(stroke_width=1, rows=2, columns=2).next_to(case_1, DOWN+0.5*RIGHT)
        box_0 = MathTex("?", color=ORANGE).move_to(board_2.cells[0][0])
        box_1 = MathTex("?", color=ORANGE).move_to(board_2.cells[0][1])
        box_2 = MathTex("?", color=ORANGE).move_to(board_2.cells[1][0])
        box_3 = MathTex("?", color=ORANGE,).move_to(board_2.cells[1][1])
        answer = MathTex("2").set_color(GREEN).next_to(board_2, RIGHT, buff=0.1)

        board_2_ = Board(stroke_width=1, rows=2, columns=2).next_to(board_2, RIGHT, buff=1)
        box_0_ = MathTex("?", color=ORANGE).move_to(board_2_.cells[0][0])
        box_1_ = MathTex("?", color=ORANGE).move_to(board_2_.cells[0][1])
        box_2_ = MathTex("?", color=ORANGE).move_to(board_2_.cells[1][0])
        box_3_ = MathTex("?", color=ORANGE).move_to(board_2_.cells[1][1])
        answer_ = MathTex("2").set_color(GREEN).next_to(board_2_, RIGHT, buff=0.1)

        glob_answer = MathTex("2").set_color(GREEN).next_to(answer_, RIGHT, buff=0.5)
        answer_box = SurroundingRectangle(glob_answer, color=ORANGE, buff=SMALL_BUFF)

        case_2 = MathTex("N=3").next_to(case_1, DOWN, buff=2.5)
        board_3_1 = Board(stroke_width=1, rows=3, columns=3).next_to(case_2, DOWN+0.5*RIGHT)
        box_1_1 = MathTex("?", color=ORANGE).move_to(board_3_1.cells[1][0])
        box_2_1 = MathTex("?", color=ORANGE).move_to(board_3_1.cells[1][1])
        box_3_1 = MathTex("?", color=ORANGE).move_to(board_3_1.cells[2][2])
        box_4_1 = MathTex("?", color=ORANGE).move_to(board_3_1.cells[0][2])
        answer_1 = MathTable("4").set_color(GREEN).next_to(board_3_1, RIGHT, buff=0.1)

        board_3_2 = Board(stroke_width=1, rows=3, columns=3).next_to(board_3_1, RIGHT, buff=1)
        box_1_2 = MathTex("?", color=ORANGE).move_to(board_3_2.cells[1][1])
        box_2_2 = MathTex("?", color=ORANGE).move_to(board_3_2.cells[2][0])
        box_3_2 = MathTex("?", color=ORANGE).move_to(board_3_2.cells[2][2])
        box_4_2 = MathTex("?", color=ORANGE).move_to(board_3_2.cells[0][2])
        box_5_2 = MathTex("?", color=ORANGE).move_to(board_3_2.cells[0][0])
        answer_2 = MathTex("5").set_color(GREEN).next_to(board_3_2, RIGHT, buff=0.1)

        board_3_3 = Board(stroke_width=1, rows=3, columns=3).next_to(board_3_2, RIGHT, buff=1)
        box_1_3 = MathTex("?", color=ORANGE).move_to(board_3_3.cells[0][0])
        box_2_3 = MathTex("?", color=ORANGE).move_to(board_3_3.cells[0][1])
        box_3_3 = MathTex("?", color=ORANGE).move_to(board_3_3.cells[1][0])
        box_4_3 = MathTex("?", color=ORANGE).move_to(board_3_3.cells[2][2])
        box_5_3 = MathTex("?", color=ORANGE).move_to(board_3_3.cells[1][2])
        box_6_3 = MathTex("?", color=ORANGE).move_to(board_3_3.cells[2][1])
        answer_3 = MathTable("6").set_color(GREEN).next_to(board_3_3, RIGHT, buff=0.1)

        glob_answer_3 = MathTex("6").next_to(answer_3, RIGHT, buff=1).set_color(GREEN)
        answer_box_3 = SurroundingRectangle(glob_answer_3, color=ORANGE, buff=SMALL_BUFF)
        glob_answer_box_3 = VGroup(glob_answer_3, answer_box_3)

        l1 = Line([1, 2, 0], [1, -5, 0])

        case_3 = MathTex("N=5").shift(UR+RIGHT)
        board_5 = Board(size=0.6, stroke_width=1, rows=5, columns=5).shift(2*RIGHT).next_to(case_3, DR)
        answer_5 = MathTex("20").set_color(GREEN).next_to(board_5, RIGHT, buff=0.1)
        box_answer_5 = SurroundingRectangle(answer_5, color=ORANGE, buff=SMALL_BUFF)
        


#ANIMATION
        self.play(Write(case_1))
        self.play(Create(board_2))
        self.play(Create(box_0))
        self.play(
            Indicate(board_2.cells[0][1]),
            Indicate(board_2.cells[1][0])
        )
        self.play(
            board_2.cells[0][0].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_0)
        )
        
        self.play(Create(box_1))
        self.play(
            Indicate(board_2.cells[0][0]),
            Indicate(board_2.cells[1][1])
        )
        self.play(FadeOut(box_1))

        self.play(Create(box_2))
        self.play(
            Indicate(board_2.cells[0][0]),
            Indicate(board_2.cells[1][1])
        )
        self.play(FadeOut(box_2))

        self.play(Create(box_3))
        self.play(
            Indicate(board_2.cells[0][1]),
            Indicate(board_2.cells[1][0])
        )
        self.play(
            board_2.cells[1][1].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_3)
        )
        
        self.play(Write(answer))


        self.play(Create(board_2_))
        self.play(Create(box_1_))
        self.play(
            Indicate(board_2_.cells[0][0]),
            Indicate(board_2_.cells[1][1])
        )
        self.play(
            board_2_.cells[0][1].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_1_)
        )
        
        self.play(Create(box_0_))
        self.play(
            Indicate(board_2_.cells[0][1]),
            Indicate(board_2_.cells[1][0])
        )
        self.play(FadeOut(box_0_))

        self.play(Create(box_3_))
        self.play(
            Indicate(board_2_.cells[0][1]),
            Indicate(board_2_.cells[1][0])
        )
        self.play(FadeOut(box_3_))

        self.play(Create(box_2_))
        self.play(
            Indicate(board_2_.cells[0][0]),
            Indicate(board_2_.cells[1][1])
        )
        self.play(
            board_2_.cells[1][0].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_2_)
        )
        self.play(Write(answer_))

        self.play(
            Circumscribe(answer),
            Circumscribe(answer_)
        )

        self.play(
            answer.animate.move_to(glob_answer),
            answer_.animate.move_to(glob_answer)
        )
        self.play(Create(answer_box))
        self.add(glob_answer)
        self.remove(answer, answer_)


        self.play(Write(case_2))
        self.play(Create(board_3_1))
        self.play(Create(box_1_1))
        self.play(
            Indicate(board_3_1.cells[0][0]),
            Indicate(board_3_1.cells[2][0]),
            Indicate(board_3_1.cells[1][1])
        )
        self.play(
            board_3_1.cells[1][0].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_1_1)
        )

        self.play(Create(box_2_1))
        self.play(
            Indicate(board_3_1.cells[1][0]),
            Indicate(board_3_1.cells[2][1]),
            Indicate(board_3_1.cells[0][1]),
            Indicate(board_3_1.cells[1][2])
        )
        self.play(
            board_3_1.cells[1][1].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_2_1)
        )

        self.play(Create(box_3_1))
        self.play(
            Indicate(board_3_1.cells[2][1]),
            Indicate(board_3_1.cells[1][2]),
        )
        self.play(
            board_3_1.cells[2][2].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_3_1)
        )

        self.play(Create(box_4_1))
        self.play(
            Indicate(board_3_1.cells[0][1]),
            Indicate(board_3_1.cells[1][2]),
        )
        self.play(
            board_3_1.cells[0][2].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_4_1)
        )
        self.play(Write(answer_1))


        self.play(Create(board_3_2))

        self.play(Create(box_1_2))
        self.play(
            Indicate(board_3_2.cells[1][0]),
            Indicate(board_3_2.cells[0][1]),
            Indicate(board_3_2.cells[1][2]),
            Indicate(board_3_2.cells[2][1])
        )
        self.play(
            board_3_2.cells[1][1].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_1_2)
        )
        
        self.play(Create(box_2_2))
        self.play(
            Indicate(board_3_2.cells[2][1]),
            Indicate(board_3_2.cells[1][0])
        )
        self.play(
            board_3_2.cells[2][0].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_2_2)
        )


        self.play(Create(box_3_2))
        self.play(
            Indicate(board_3_2.cells[2][1]),
            Indicate(board_3_2.cells[1][2])
        )
        self.play(
            board_3_2.cells[2][2].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_3_2)
        )


        self.play(Create(box_4_2))
        self.play(
            Indicate(board_3_2.cells[0][1]),
            Indicate(board_3_2.cells[1][2])
        )
        self.play(
            board_3_2.cells[0][2].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_4_2)
        )
        

        self.play(Create(box_5_2))
        self.play(
            Indicate(board_3_2.cells[0][1]),
            Indicate(board_3_2.cells[1][0])
        )
        self.play(
            board_3_2.cells[0][0].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_5_2)
        )
        

        self.play(Write(answer_2))

        
        self.play(Create(board_3_3))

        self.play(Create(box_1_3))
        self.play(
            Indicate(board_3_3.cells[1][0]),
            Indicate(board_3_3.cells[0][1])
        )
        self.play(
            board_3_3.cells[0][0].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_1_3)
        )

        
        self.play(Create(box_2_3))
        self.play(
            Indicate(board_3_3.cells[0][0]),
            Indicate(board_3_3.cells[0][2]),
            Indicate(board_3_3.cells[1][1])
        )
        self.play(
            board_3_3.cells[0][1].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_2_3)
        )


        self.play(Create(box_3_3))
        self.play(
            Indicate(board_3_3.cells[0][0]),
            Indicate(board_3_3.cells[2][0]),
            Indicate(board_3_3.cells[1][1])
        )
        self.play(
            board_3_3.cells[1][0].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_3_3)
        )

        self.play(Create(box_4_3))
        self.play(
            Indicate(board_3_3.cells[2][1]),
            Indicate(board_3_3.cells[1][2])
        )
        self.play(
            board_3_3.cells[2][2].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_4_3)
        )

        self.play(Create(box_5_3))
        self.play(
            Indicate(board_3_3.cells[1][1]),
            Indicate(board_3_3.cells[2][2]),
            Indicate(board_3_3.cells[0][2])
        )
        self.play(
            board_3_3.cells[1][2].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_5_3)
        )
        


        self.play(Create(box_6_3))
        self.play(
            Indicate(board_3_3.cells[1][1]),
            Indicate(board_3_3.cells[2][0]),
            Indicate(board_3_3.cells[2][2])
        )
        self.play(
            board_3_3.cells[2][1].animate.set_fill(GREEN, opacity=0.5),
            FadeOut(box_6_3)
        )
        

        self.play(Write(answer_3))

        self.play(
            ReplacementTransform(answer_1, glob_answer_3),
            ReplacementTransform(answer_2, glob_answer_3),
            ReplacementTransform(answer_3, glob_answer_3),
        )
        self.play(Create(answer_box_3))
        
        self.play(
            FadeOut(board_3_1),
            FadeOut(board_3_2),
            board_3_3.animate.move_to(board_3_1),
            glob_answer_box_3.animate.move_to(board_3_2.cells[1][0]),
            run_time=2 
        )

        self.play(Write(case_3))

        self.play(Create(board_5))

        for i in range(4):
            self.play(board_5.cells[0][i].animate.set_fill(GREEN, opacity=0.5))
        for i in range(3):
            self.play(board_5.cells[i+1][0].animate.set_fill(GREEN, opacity=0.5))
        for i in range(4):
            self.play(board_5.cells[4-i][4].animate.set_fill(GREEN, opacity=0.5))
        for i in range(3):
            self.play(board_5.cells[4][3-i].animate.set_fill(GREEN, opacity=0.5))

#init
        board_3 = board_3_3.copy()
        board_5_final = VGroup(board_5, board_3)

        self.play(board_3.animate.move_to(board_5).scale(0.6/0.75), run_time=2)
        self.play(Write(answer_5))
        self.play(Create(box_answer_5))

        
        
        self.play(board_5_final.animate.shift(LEFT))
        self.play(board_3_3.animate.shift(RIGHT))


class test7(Scene):
    def construct(self):
        
        first_question = Tex(
            "Հարց 1․ Արդյո՞ք ցանկացած $N$-ի համար ներկվող \nվանդակների առավելագույն քանակը $N(N-1)$ է։",
            tex_template=armenian_tex_template, font_size=27).shift(UP+4*RIGHT)
        second_question = Tex(
            "Հարց 2․ Ո՞րն է վանդակները ներկելու "
             "ամենաօպտիմալ եղանակը։",
            tex_template=armenian_tex_template, font_size=27).next_to(first_question, DOWN, buff=0.5)

        self.play(Write(first_question), Write(second_question))
        self.wait()

        

def outline(up_side, down_side, left_side, right_side):
    square = Square()
    coord = np.array.square.get_center()
    first_vertex_coord = coord+
        



