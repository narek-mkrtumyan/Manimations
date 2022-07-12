'''


բոլոր տղամարդիկ եկան իրենց կանանց հետ
տղամարդկանց կեսը 1 երեխայի հետ էր
ևս 20 կին, ովքեր տղամարդկանց հետ չէին
480 տոմս վաճառվել է
քանի՞ երեխա է եկել

նկարում ենք թատրոնը
նստած են մարդիկ

սպիտակ - երեխա
կանաչ - տղամարդիկ
կարմիր - կանայք

երեխաներին բերում շարում ենք
տղամարդիկ 2 անգամ շատ են
կանայք՝ + 20

միասին 480

սարքում ենք հատվածներ

20-ը կտրում հանում

480-20=460

ինդիքեյթ ենք անում 5 հավասար հատվածները

460:5=92 

'''


import sys
sys.path.append('../../')
from Functions.qarakusi import *

import random

N_CHILDREN = 92
N_MEN = 2*N_CHILDREN
N_WOMEN = N_MEN+20

N_ALL = N_MEN+N_WOMEN+N_CHILDREN

CHILD_COLOR = '#F5EFE0'
MAN_COLOR = '#23B99A'
WOMAN_COLOR = '#E74C3B'

class prob_10323(QarakusiScene):
    def construct(self):

        task = Tex(
            r'Բոլոր տղամարդիկ եկել էին կանանց հետ։\\',
            r'Տղամարդկանց կեսը եկել էր 1 երեխայի հետ:\\',
            r'20 կին եկել էր առանց տղամարդու:\\',
            r'Բոլոր 480 տոմսերը վաճառվել էին։\\'
        )
        task.arrange(DOWN, aligned_edge=LEFT)

        self.play(Write(task[0], run_time=2))
        self.wait(0.5)
        self.play(Write(task[1], run_time=2))
        self.wait(0.5)
        self.play(Write(task[2], run_time=2))
        self.wait(0.5)
        self.play(Write(task[3], run_time=2))
        self.wait(0.5)
        self.play(task.animate.shift(2.5 * UP).scale(0.75))
        self.wait(0.5)

        seats = VGroup(*[Circle(stroke_width=1).scale(0.1) for _ in range(N_ALL)])
        seats.arrange_in_grid(16, 30, buff=0.05).next_to(task, DOWN).align_to(task, LEFT)

        screen = RoundedRectangle(height=1.5, width=35, stroke_width=0.3).set_opacity(0.7).match_width(seats)
        screen.next_to(seats, DOWN, buff=0.5)
        screen_text = Tex(r'Է \; \; Կ \; \; Ր \; \; Ա \; \; Ն', font_size=25)
        screen_text.set_color(BLACK).move_to(screen.get_center())
        screen.add(screen_text)

        exit_dor = Rectangle(height= 0.225, width=0.5, color='#43A047', stroke_color = WHITE, stroke_width=0.8)
        exit_dor.set_opacity(1).align_to(task, LEFT).align_to(seats, UP).shift(LEFT * 0.6)
        exit_dor_text = Tex(r'ԵԼՔ', font_size=18).move_to(exit_dor.get_center())
        exit_dor.add(exit_dor_text)

        VGroup(seats, screen, exit_dor).shift(0.75 * RIGHT)

        woman = SVGMobject(os.path.join(path_to_SVG, '10323', 'woman.svg')).set_stroke(WOMAN_COLOR, 3)
        man = SVGMobject(os.path.join(path_to_SVG, '10323', 'man.svg')).set_stroke(MAN_COLOR, 3)
        kid = SVGMobject(os.path.join(path_to_SVG, '10323', 'kid.svg')).set_stroke(CHILD_COLOR, 3).scale(0.6)

        people = VGroup(woman, man, kid)
        people.arrange(DOWN).match_height(seats).align_to(task, LEFT).shift(2.5 * LEFT).align_to(seats, UP)

        self.play(FadeIn(seats), FadeIn(screen), FadeIn(exit_dor))
        self.wait(0.5)

        pe_ic = VGroup(*[ Circle(stroke_width=1).scale(0.1) for _ in range(3)])
        pe_ic.arrange(DOWN, buff= 1.1).align_to(seats, DOWN).align_to(task, LEFT).shift(2.5 * LEFT)
        pe_ic[0].set_color(WOMAN_COLOR).set_opacity(0.9)
        pe_ic[1].set_color(MAN_COLOR).set_opacity(0.9)
        pe_ic[2].set_color(CHILD_COLOR).set_opacity(0.9)

        who = Tex(
            r'- կանայք',
            r'- տղամարդիկ',
            r'- երեխաներ',
            font_size=35
        )
        who.arrange(DOWN, buff=1)


        for i in range(3):
            who[i].align_to(task, LEFT)
        
        who.next_to(pe_ic, RIGHT)

        # self.play(AnimationGroup(*[ReplacementTransform(people[i], pe_ic[i]) for i in range(3)], lag_ratio=0.1))
        # self.play(AnimationGroup(*[Write(who[i]) for i in range(3)], lag_ratio=0.1))
    

        order = list(range(N_ALL))
        random.shuffle(order)

        for i in range(20):
            f = i

            seats[order[f]].set_color(WOMAN_COLOR).set_opacity(1)
            # self.play(seats[order[f]].animate.set_color(WOMAN_COLOR).set_opacity(1), run_time = 0.002)

        for i in range(92):
            for j in range(2,-1,-1):
                if j == 2:
                    f = 388 + i
                    color = CHILD_COLOR

                if j == 1:
                    f = 204 + 2*i
                    color = MAN_COLOR
                    c = 2*i

                if j == 0:
                    f = 20 + 2*i
                    color = WOMAN_COLOR
                    c = f

                seats[order[f]].set_color(color).set_opacity(1)
                # self.play(seats[order[f]].animate.set_color(color).set_opacity(1), run_time = 0.002 * (50 * ((i/92)**80) + 1))

                if j != 2:
                    seats[order[f + 1]].set_color(color).set_opacity(1)
                    # self.play(seats[order[f+1]].animate.set_color(color).set_opacity(1), run_time = 0.002 * (50 * ((i/92)**80) + 1))

        self.wait(0.5)

        self.play(AnimationGroup(*[Write(p) for p in people], lag_ratio=0.1))

        self.play(ReplacementTransform(people[2], pe_ic[2]), Write(who[2]))
        self.play(ReplacementTransform(people[1], pe_ic[1]), Write(who[1]))
        self.play(ReplacementTransform(people[0], pe_ic[0]), Write(who[0]))

        self.play(FadeOut(exit_dor), FadeOut(screen))

        id_who = VGroup(pe_ic, who)

        self.play(
            seats.animate.shift(3.5 * RIGHT + UP).scale(0.5),
        )

        women = VGroup(*[seats[order[i]].copy() for i in range(204)])
        men = VGroup(*[seats[order[i]].copy() for i in range(204, 388)])
        children = VGroup(*[seats[order[i]].copy() for i in range(388, 480)])


        children_row = VGroup(*[Circle().scale(0.015).set_color(CHILD_COLOR).set_opacity(1) for _ in range(92)])
        children_row.arrange(RIGHT, buff=0)
        children_row.next_to(who[2], RIGHT, buff=1)

        men_row = VGroup(*[Circle().scale(0.015).set_color(MAN_COLOR).set_opacity(1) for _ in range(184)])
        men_row.arrange(RIGHT, buff=0)
        men_row.next_to(who[1], RIGHT).align_to(children_row, LEFT)

        women_row = VGroup(*[Circle().scale(0.015).set_color(WOMAN_COLOR).set_opacity(1) for _ in range(204)])
        women_row.arrange(RIGHT, buff=0)
        women_row.next_to(who[0], RIGHT).align_to(children_row, LEFT)


        seats.set_opacity(0.05)
        self.add(seats, women, men, children)

        # rows = VGroup(women_row, men_row, children_row)
        # rows.match_width(seats)

        seg_children = Segment(children_row.get_left(), children_row.get_right(), CHILD_COLOR, 5)

        seg_men = Segment(men_row.get_left(), men_row.get_right(), MAN_COLOR, 5)
        seg_men_left = Segment(men_row.get_left(), seg_men.line.get_center(), MAN_COLOR, 5)
        seg_men_right = Segment(seg_men.line.get_center(), men_row.get_right(), MAN_COLOR, 5)

        seg_women = Segment(women_row.get_left(), women_row.get_right(), WOMAN_COLOR, 5)
        seg_women_left = Segment(women_row.get_left(), women_row.get_left()+seg_men.line.get_center()-men_row.get_left(), WOMAN_COLOR, 5)
        seg_women_right = seg_women_left.copy().next_to(seg_women_left, RIGHT, 0)
        seg_women_extra = Segment(seg_women_right.line.get_right(), women_row.get_right(), WOMAN_COLOR, 5)

        checks = VGroup(*[Check().scale(0.2).next_to(task_line, LEFT) for task_line in task])

        self.play(AnimationGroup(
                *[ReplacementTransform(children[i], children_row[i], run_time=0.5) for i in range(92)],
                lag_ratio=0.05
        ))
        self.wait(0.5)
        self.play(
            FadeOut(children_row),
            FadeIn(seg_children)
        )
        self.wait(0.5)

        self.play(AnimationGroup(
            *[ReplacementTransform(men[i], men_row[i], run_time = 0.5) for i in range(184)],
            lag_ratio=0.05
        ), run_time=2)
        self.wait(0.5)
        self.play(
            FadeOut(men_row),
            FadeIn(seg_men)
        )
        self.wait(0.25)

        self.play(Create(seg_men_left), Create(seg_men_right))
        self.remove(seg_men)
        self.wait(0.25)

        self.play(
            VGroup(task[0], task[2], task[3]).animate.set_opacity(0.3), 
            task[1].animate.set_color(GREEN), 
            run_time=0.5
        )
        self.add_sound(os.path.join(path_to_Objects, 'sounds', 'check'))
        self.play(Create(checks[1]), run_time=0.5)
        self.wait(0.25)
        self.play(VGroup(task[0], task[2], task[3]).animate.set_opacity(1), run_time=0.5)
        self.wait(0.25)

        self.play(AnimationGroup(
            *[ReplacementTransform(women[i], women_row[i], run_time = 0.5) for i in range(204)],
            lag_ratio=0.05
        ), run_time=2)
        self.wait(0.5)
        self.play(
            FadeOut(women_row),
            FadeIn(seg_women)
        )
        self.wait(0.25)
        self.play(Create(seg_women_left), Create(seg_women_right), Create(seg_women_extra))
        self.remove(seg_women)
        self.play(
            VGroup(task[1], task[2], task[3], checks[1]).animate.set_opacity(0.3),
            task[0].animate.set_color(GREEN),
            run_time=0.5
        )
        self.add_sound(os.path.join(path_to_Objects, 'sounds', 'check'))
        self.play(Create(checks[0]), run_time=0.5)
        self.wait(0.25)
        self.play(VGroup(task[1], task[2], task[3], checks[1]).animate.set_opacity(1), run_time=0.5)
        self.wait(0.25)


        seg_women_extra_tex = Tex('20', font_size=40).next_to(seg_women_extra, 0.5 * UP)

        brace = BraceBetweenPoints(seg_women_right.get_right() + RIGHT + 0.2 * UP, seg_women_right.get_right() + RIGHT + 2.75 * DOWN, RIGHT)
        brace_tex = Tex('480', font_size=50).next_to(brace)

        self.play(Write(seg_women_extra_tex))
        self.play(
            VGroup(task[1], task[3], task[0], checks[1], checks[0]).animate.set_opacity(0.3),
            task[2].animate.set_color(GREEN),
            run_time=0.5
        )
        self.add_sound(os.path.join(path_to_Objects, 'sounds', 'check'))
        self.play(Create(checks[2]), run_time=0.5)
        self.wait(0.25)
        self.play(VGroup(task[1], task[3], task[0], checks[1], checks[0]).animate.set_opacity(1), run_time=0.5)
        self.wait(0.25)
        self.play(Write(brace), Write(brace_tex))
        self.play(
            VGroup(task[1], task[2], task[0], checks[1], checks[0], checks[2]).animate.set_opacity(0.3),
            task[3].animate.set_color(GREEN),
            run_time=0.5
        )
        self.add_sound(os.path.join(path_to_Objects, 'sounds', 'check'))
        self.play(Create(checks[3]), run_time=0.5)
        self.wait(0.25)
        self.play(VGroup(task[1], task[2], task[0]).animate.set_opacity(1), run_time=0.5)
        self.wait(0.25)
        
        self.play(
            FadeOut(task, checks),
            VGroup(
                seg_children, seg_men_left, seg_men_right, seg_women_left, 
                seg_women_right, seg_women_extra, seg_women_extra_tex,
                brace, brace_tex, id_who
            ).animate.shift(2.5 * UP)
        )

        scissors = Scissors(seg_women_extra.line.get_left())

        scissors.cut(self, 2)
        self.wait(0.15)
        self.play(VGroup(seg_women_extra, seg_women_extra_tex).animate.shift(0.25 * RIGHT))
        self.wait(0.15)
        scissors.fade_out(self, run_time=0.5)
        self.wait(0.15)

        together_minus_extra = Tex('480 ', '- ', '20 ', '= ', '460', font_size=50)
        together_minus_extra.align_to(seg_children, LEFT).shift(1.25 * DOWN)

        self.play(ReplacementTransform(brace_tex.copy(), together_minus_extra[:1]))
        self.play(Write(together_minus_extra[1], run_time=0.5))
        self.play(ReplacementTransform(seg_women_extra_tex.copy(), together_minus_extra[2:3]))
        self.play(Write(together_minus_extra[3], run_time=0.5))
        self.play(Write(together_minus_extra[4], run_time=0.75))

        division_by_5 = Tex('460 ', ': ', '5 ', '= ', '92', font_size=50)
        division_by_5.next_to(together_minus_extra, 2 * DOWN, aligned_edge=LEFT)

        counts = VGroup(
            Tex('1').next_to(seg_children, UP),
            Tex('2').next_to(seg_men_left, UP),
            Tex('3').next_to(seg_men_right, UP),
            Tex('4').next_to(seg_women_left, UP),
            Tex('5').next_to(seg_women_right, UP)
        ).set_color(YELLOW).set_opacity(0)
        self.add(counts)

        children_92 = Tex('92').next_to(seg_children, UP)
        children_92_rect = SurroundingRectangle(children_92, WHITE)

        self.play(
            seg_children.animate(rate_func=there_and_back_with_pause, run_time=1).shift(0.2 * UP).set_color(YELLOW),
            counts[0].animate(rate_func=there_and_back_with_pause, run_time=1).set_opacity(1)
        )
        self.wait(0.1)
        self.play(
            seg_men_left.animate(rate_func=there_and_back_with_pause, run_time=1).shift(0.2 * UP).set_color(YELLOW),
            counts[1].animate(rate_func=there_and_back_with_pause, run_time=1).set_opacity(1)
        )
        self.wait(0.1)
        self.play(
            seg_men_right.animate(rate_func=there_and_back_with_pause, run_time=1).shift(0.2 * UP).set_color(YELLOW),
            counts[2].animate(rate_func=there_and_back_with_pause, run_time=1).set_opacity(1)
        )
        self.wait(0.1)
        self.play(
            seg_women_left.animate(rate_func=there_and_back_with_pause, run_time=1).shift(0.2 * UP).set_color(YELLOW),
            counts[3].animate(rate_func=there_and_back_with_pause, run_time=1).set_opacity(1)
        )
        self.wait(0.1)
        self.play(
            seg_women_right.animate(rate_func=there_and_back_with_pause, run_time=1).shift(0.2 * UP).set_color(YELLOW),
            counts[4].animate(rate_func=there_and_back_with_pause, run_time=1).set_opacity(1)
        )
        self.wait(0.1)

        self.play(ReplacementTransform(together_minus_extra[-1:].copy(), division_by_5[:1]))
        self.play(Write(division_by_5[1]))
        self.play(Write(division_by_5[2]))
        self.play(Write(division_by_5[3]))
        self.play(Write(division_by_5[4]))
        self.wait(0.5)

        self.play(Write(children_92))
        self.wait(0.5)
        self.play(Create(children_92_rect))
        self.wait(0.5)



