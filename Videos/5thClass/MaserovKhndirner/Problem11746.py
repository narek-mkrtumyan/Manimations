import sys
sys.path.append('../../../')
from Functions.qarakusi import *


class prob_11746(Scene):
    def construct(self):

        task = Task(
                MathTex(r'\#11746', font_size=35), 
                MathTex(
                    r'\textrm{Որդու և դստեր ապրած տարիների ընդհանուր գումարը հավա-}',
                    r'\textrm{սար է իրենց հոր տարիքին։ Որդին } 2 \textrm{ անգամ մեծ է իր քրոջից}',
                    r'\textrm{և } 20 \textrm{ տարով փոքր է հորից։ Քանի՞ տարեկան է հայրը։}',
                    tex_template=armenian_tex_template, font_size=35
                )
            )

        parts = [
            [[2000, False]], 
            [[3001, False]],
            [[2000, False], [3001, False]],
            [[4002, False], [1998, False]]
        ]

        copy_list = [
            [1],
            [2],
            [1, 2],
            [-1, -1]
        ]

        names = [
            MathTex(r'\textrm{Դուստր}', tex_template=armenian_tex_template,  font_size=25),
            MathTex(r'\textrm{Որդի}', tex_template=armenian_tex_template, font_size=25),
            MathTex(r'\textrm{Հայր}', tex_template=armenian_tex_template,  font_size=25),
            MathTex(r'\textrm{.}', tex_template=armenian_tex_template, font_size=1)
        ]


        diagram = Diagram(parts, names, brace=False)

        VGroup(*diagram.player[3]).set_opacity(0)
        for s in diagram.player[3]:
            s.set_superopacity(0)
        VGroup(task, diagram).arrange(DOWN)
        diagram.shift(0.5*UP)
        diagram.align_to(task.text, LEFT)
        
        self.play(Write(task), run_time = 10)
        task.up(self)
        diagram.create_by_copying(self, copy_list)
        # self.wait(2)

        new_lengths = [
            [2000], 
            [4000],
            [2000, 4000],
            [4000, 2000]
        ]
        equal_parts = [
            [0],
            [1, 1],
            [0, 0],
            [0, 0]
        ]
        diagram.update_length(self, new_lengths, time = 3)
        diagram.segment_perpendicular_projection(self, [0, 0], 1, replace=True, apply_to=[0, 1, 2])
        diagram.show_equal_parts(self, equal_parts)
        
        diagram.player[1][1].set_color(WHITE)
        
        self.wait()        
        diagram.div_segment(self, 2, 1)

        self.play(VGroup(*diagram.player[3]).animate.set_opacity(1))
        # self.add(*diagram.player[3])

        diagram.segment_perpendicular_projection(self, project_from=[3, 0], project_to=1, apply_to=[0, 1, 2, 3])
        diagram.player[3][1].set_text(MathTex(r'20', font_size=25), self)

        diagram.player[3][1].set_color(WHITE)

        diagram.segment_perpendicular_projection(self, project_from=[3, 1], project_to=2, apply_to=[0, 1, 2, 3])
        diagram.player[2][2].set_text(MathTex(r'20', font_size=25))
        self.play(Indicate(diagram.player[2][2].text), diagram.player[3][1].animate.set_color(WHITE))

                
        diagram.group(self, 2)

        diagram.player[2][0].set_text(MathTex(r'20', font_size=25), self)
        diagram.player[2][1].set_text(MathTex(r'20', font_size=25), self)

        diagram.player[1][0].set_text(MathTex(r'20', font_size=25), self)
        diagram.player[1][1].set_text(MathTex(r'20', font_size=25), self)
        
        diagram.player[0][0].set_text(MathTex(r'20', font_size=25), self)

        self.wait()

        self.play(FadeOut(task.text, run_time = 0.5), diagram.animate(run_time = 1.5).align_to(task.text, UP))

        #new_order = [1, 0]
        #diagram.reorder(self, 2, new_order)

        self.wait()

        diagram.player[0][0].set_text(MathTex(r'20', font_size=25))

        self.wait()

        formula_0 = MathTex(r'20', r'+', r'20', r'= 40').move_to([0, -0.5, 0])

        self.play(Write(formula_0), run_time = 3)

        diagram.integrate(self, 1, MathTex(r'40', font_size=25))

        formula_1_3 = MathTex(r'20 \cdot', r'3', r'= 60').next_to(formula_0, DOWN)
        formula_1_2 = MathTex(r'20 \cdot', r'2', r'= 60').next_to(formula_0, DOWN)
        formula_1_1 = MathTex(r'20 \cdot', r'1', r'= 60').next_to(formula_0, DOWN)

        self.play(Write(formula_1_3[0], run_time = 2))
        self.play(ReplacementTransform(diagram.player[2][0].line.copy(), formula_1_1[1]))
        self.play(
            ReplacementTransform(diagram.player[2][1].line.copy(),
            formula_1_2[1]), formula_1_1[1].animate.shift(DOWN).set_opacity(0)
        )
        self.remove(formula_1_1[1])

        self.play(
            ReplacementTransform(diagram.player[2][2].line.copy(), formula_1_3[1]),
            formula_1_2[1].animate.shift(DOWN).set_opacity(0)
        )
        self.remove(formula_1_2[1])

        self.play(Write(formula_1_3[2]), run_time=2)

        diagram.integrate(self, 2, MathTex(r'60', font_size=25))







# class Scrole:
#     def __init__(self, br_start, txt, mob_of_br_end, value_start, value_end, pos = UP):
#         self.br_start = br_start
#         self.br_end = Brace(mob_of_br_end, 0.1 * pos).align_to(self.br_start, DOWN + LEFT)
#         self.value_start = value_start
#         self.value_end = value_end
#         self.txt = txt
#         self.__pos =  txt.get_center()

#     def play(self, screen, run_time=3):
#         def scrole(mob, t):
#             p_end = self.br_end.get_center()
#             p_start = self.__pos
#             p_inst= p_start.copy()
#             p_inst[0] = p_end[0] * t + (1 - t) * p_start[0]
#             i = round((1 - t) * self.value_start + t*self.value_end)
#             mob.set_value(i).move_to(p_inst)

#         screen.play(UpdateFromAlphaFunc(self.txt, scrole, rate_func=smooth),
#                     Transform(self.br_start, self.br_end, rate_func=smooth), run_time=run_time)

# class Scroles:
#     def __init__(self, br_start, txt, start_end, value_start, value_end):
#         self.br_start = br_start
#         self.br_end = Segment(start_end[0], start_end[1], color=GREEN).align_to(self.br_start, DOWN + LEFT)
#         self.value_start = value_start
#         self.value_end = value_end
#         self.txt = txt
#         self.__pos =  txt.get_center()

#     def play(self, screen, run_time=3):
#         def scrole(mob, t):
#             p_end = self.br_end.get_center()
#             p_start = self.__pos
#             p_inst= p_start.copy()
#             p_inst[0] = p_end[0] * t + (1 - t) * p_start[0]
#             i = round((1 - t) * self.value_start + t*self.value_end)
#             mob.set_value(i).move_to(p_inst)

#         screen.play(UpdateFromAlphaFunc(self.txt, scrole, rate_func=smooth),
#                     Transform(self.br_start, self.br_end, rate_func=smooth), run_time=run_time)

# def first_half(x):
#     if x < 0.5:
#         return 0
#     else:
#         return 2*x - 1

# def second_half(x):
#     if x < 0.5:
#         return 2*x
#     else:
#         return 1


# def segments_without_endmarks(group):
#     group_without_endmarks = VGroup()
#     group_of_endmarks = VGroup()
#     l = len(group)
#     for i in range(l):
#         if i != 0 and i != l-1:
#             group_without_endmarks.add(group[i][0][0])
#             group_of_endmarks.add(group[i][0][1])
#             group_of_endmarks.add(group[i][0][2])
#         else:
#             if i == 0:
#                 group_without_endmarks.add(group[i][0][1])
#                 group_without_endmarks.add(group[i][0][0])
#                 group_of_endmarks.add(group[i][0][2])
#             else:
#                 group_without_endmarks.add(group[i][0][0])
#                 group_without_endmarks.add(group[i][0][2])
#                 group_of_endmarks.add(group[i][0][1])
#     return (group_without_endmarks, group_of_endmarks)

# def half_back(x):
#     return (np.sin(3 / 4 * PI * x)) ** 2



