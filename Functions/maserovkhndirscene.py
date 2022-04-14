from .qarakusiscene import *
from .maserovkhndirner import *



class MaserovKhndirScene(QarakusiScene):

    def PlayProblemCopying(
        self,
        problem : SimpleTwoPartsProblem,
    ):

    # Create segments and write names
        self.play(Create(problem.drawing.first_segment))
        self.wait(0.5)
        self.play(Write(problem.drawing.first_name))
        self.wait(0.5)

        self.play(ReplacementTransform(problem.drawing.first_segment.copy(), problem.drawing.second_segment))
        self.wait(0.5)
        self.play(Create(problem.drawing.extra_segment, run_time = 2))
        self.wait(0.5)
        self.play(Write(problem.drawing.second_name))
        self.wait(0.5)

    # brace
        self.play(Write(problem.drawing.brace))
        self.wait(0.5)


    def PlayProblemProjecting(
        self,
        problem : SimpleTwoPartsProblem
    ):

    # Create segments and write names
        self.play(Create(problem.drawing.first_segment))
        self.wait(0.5)
        self.play(Write(problem.drawing.first_name))
        self.wait(0.5)
        self.play(Create(VGroup(
                    problem.drawing.second_segment_combined.endmark_left,
                    problem.drawing.second_segment_combined.line,
                    problem.drawing.second_segment_combined.endmark_right,
                )))
        self.wait(0.5)
        self.play(Write(problem.drawing.second_name))
        self.wait(0.5)

    # project the first on the second
        self.play(
            ReplacementTransform(problem.drawing.first_segment.copy(), problem.drawing.second_segment),
            Create(problem.drawing.dashed_lines[0]),
            Create(problem.drawing.dashed_lines[1]),
            rate_func=linear, run_time=1.5
        )
        self.wait(0.5)
        self.play(Create(problem.drawing.extra_segment))
        self.remove(
            problem.drawing.second_segment_combined.endmark_left,
            problem.drawing.second_segment_combined.line,
            problem.drawing.second_segment_combined.endmark_right,
        )
        self.wait(0.5)
        self.play(
            Uncreate(problem.drawing.dashed_lines[0]),
            Uncreate(problem.drawing.dashed_lines[1])
        )

    # brace
        self.play(Write(problem.drawing.brace))
        self.wait(0.5)


    def PlaySolution(
        self,
        problem : SimpleTwoPartsProblem,
        indication=Indicate # ApplyWave
    ):

    # cut with scissors
        problem.solution.scissors.cut(self)
        self.play(problem.drawing.extra_segment.animate.shift(0.5 * RIGHT))
        problem.solution.scissors.fade_out(self)
        self.wait(0.5)

    # 24 - 10 =14
        self.play(Write(problem.solution.total_minus_extra[0]))
        self.wait(0.5)
        self.play(ReplacementTransform(problem.drawing.brace.label.copy(), problem.solution.total_minus_extra[1:2]))
        self.wait(0.5)
        self.play(Write(problem.solution.total_minus_extra[2]))
        self.wait(0.5)
        self.play(ReplacementTransform(problem.drawing.extra_segment.text.copy(), problem.solution.total_minus_extra[3:4]))
        self.wait(0.5)
        self.play(Write(problem.solution.total_minus_extra[4]))
        self.wait(0.5)
        self.play(Write(problem.solution.total_minus_extra[5]))
        self.wait(0.5)

        self.play(problem.drawing.extra_segment.animate.set_opacity(0.3))
        self.wait(0.5)

    # count equal segments by indicating
        problem.drawing.first_segment.set_color(ORANGE)
        self.play(indication(problem.drawing.first_segment, amplitude=0.15, time_width=2, run_time=1, color=problem.counting_color))
        problem.drawing.first_segment.set_color(WHITE)
        self.wait(0.25)
        self.play(Write(problem.solution.count_one_part))
        self.wait(0.25)
        problem.drawing.second_segment.set_color(ORANGE)
        self.play(indication(problem.drawing.second_segment, amplitude=0.15, time_width=2, run_time=1, color=problem.counting_color))
        problem.drawing.second_segment.set_color(WHITE)
        self.wait(0.25)
        self.play(ReplacementTransform(problem.solution.count_one_part[0], problem.solution.divide_by_two[3]))
        self.wait(0.5)
        self.play(FadeOut(problem.solution.count_one_part[1]))
        self.wait(0.5)

    # write 14 : 2 = 7
        self.play(Write(problem.solution.divide_by_two[0]))
        self.wait(0.5)
        self.play(ReplacementTransform(problem.solution.total_minus_extra[5:].copy(), problem.solution.divide_by_two[1:2]))
        self.wait(0.5)
        self.play(Write(problem.solution.divide_by_two[2]))
        self.wait(0.5)
        self.play(Write(problem.solution.divide_by_two[4]))
        self.wait(0.5)
        self.play(Write(problem.solution.divide_by_two[5]))
        self.wait(0.5)

    # write 7 on the equal segments
        self.play(
            Indicate(problem.drawing.first_segment, color=problem.counting_color),
            Indicate(problem.drawing.second_segment, color=problem.counting_color),
            Indicate(problem.solution.divide_by_two[5], color=problem.counting_color),
            run_time = 1.5
        )
        self.wait(0.5)

        self.play(
            Write(problem.solution.first_segment_text),
            Write(problem.solution.second_segment_text)
        )
        self.wait(0.5)

    # bring back extra segment
        self.play(problem.drawing.extra_segment.animate.set_opacity(1).shift(0.5 * LEFT))
        self.wait(0.5)

    # WANTED
        if problem.wanted == 'first':
            self.play(Create(problem.solution.first_rect))
            self.wait(0.5)

        else:
            self.play(Write(problem.solution.equal_length_plus_extra, run_time=3))
            self.wait(0.5)
            self.play(
                FadeIn(
                    problem.drawing.second_segment_combined.line, 
                    problem.drawing.second_segment_combined.endmark_left,
                    problem.drawing.second_segment_combined.endmark_right
                ),
                ReplacementTransform(
                    VGroup(problem.solution.second_segment_text, problem.drawing.extra_segment.text),
                    problem.drawing.second_segment_combined.text
                ),
                FadeOut(
                    problem.drawing.second_segment,
                    problem.drawing.extra_segment.line,
                    problem.drawing.extra_segment.endmark_left,
                    problem.drawing.extra_segment.endmark_right
                )
            )
            self.wait(0.5)

            if problem.wanted == 'second':
                self.play(Create(problem.solution.second_rect))
                self.wait(0.5)

            elif problem.wanted == 'both':
                self.play(Create(problem.solution.first_rect))
                self.wait(0.5)
                self.play(Create(problem.solution.second_rect))
                self.wait(0.5)






