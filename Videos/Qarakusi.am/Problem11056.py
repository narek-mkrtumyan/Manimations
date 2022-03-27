import sys
sys.path.append('../../')
from Functions.qarakusi import *


# class MathSequence(VGroup):
#     def __init__(
#         self,
#         start=1,
#         end=10,
#         name=None, # name='a' means the sequence will be a_1, a_2, ...
#         number_of_items_from_start=3,
#         number_of_items_in_the_end=1,

#     ):
#         pass

class BoyThinking(VMobject):
    def __init__(self, style=1):
        VMobject.__init__(self)

        if style == 1:
            thinking_boy = SVGMobject(os.path.join(path_to_SVG, 'people', 'thinking', 'thinking_boy_filled'))
        elif style == 2:
            thinking_boy = SVGMobject(os.path.join(path_to_SVG, 'people', 'thinking', 'thinking_boy_outlines'))

        thinking_boy.set_color(WHITE)
        self.add(thinking_boy)


class Problem11056(Scene):
    def construct(self):

        sequence = MathTex('1,', '2,', '3,', '4,', '...,', '999,', '1000')
        sequence.arrange(buff=0.5, aligned_edge=DOWN).to_edge(UP)
        sequence[-1].align_to(sequence[:-1], UP)

        # self.add(sequence)


        man_with_thinking_bubble = SVGMobject(os.path.join(path_to_SVG, 'people', 'thinking', 'man_with_thinking_bubble'))
        man_with_thinking_bubble.set_color(WHITE).scale(2.25).shift(LEFT)
        VGroup(man_with_thinking_bubble[0], man_with_thinking_bubble[2], man_with_thinking_bubble[3]).shift(0.15 * UR)
        hmmm = Text('հմմմ...', font_size=25).move_to(man_with_thinking_bubble[0].get_center())


        # self.wait()
        # self.play(
        #     Write(man_with_thinking_bubble[1]),
        #     Write(man_with_thinking_bubble[4]),
        #     Write(man_with_thinking_bubble[5]),
        #     Write(man_with_thinking_bubble[6]), 
        #     run_time=1
        # )
        self.add(
            man_with_thinking_bubble[1],
            man_with_thinking_bubble[4],
            man_with_thinking_bubble[5],
            man_with_thinking_bubble[6]
        )

        self.play(Write(man_with_thinking_bubble[3]), run_time=0.25)
        self.play(Write(man_with_thinking_bubble[2]), run_time=0.25)
        self.play(Write(man_with_thinking_bubble[0]), run_time=0.25)
        self.wait(0.5)

        self.play(Write(hmmm))
        self.wait()
        self.play(
            FadeOut(
                hmmm, 
                man_with_thinking_bubble[3],
                man_with_thinking_bubble[2],
                man_with_thinking_bubble[0]
            )
        )


