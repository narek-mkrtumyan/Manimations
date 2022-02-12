from manim import *
from colour import Color
import os
import sys
sys.path.append('../')

import Objects.helpers as helpers

path_to_SVG = os.path.join(helpers.root(), 'Objects', 'SVG_files')



class Pigeon(VMobject):
    def __init__(self):
        VMobject.__init__(self)
        pigeon = SVGMobject(os.path.join(path_to_SVG, 'pigeon.svg'))
        pigeon.set_color(WHITE).scale(0.5)

        self.add(pigeon)


class Rabbit(VMobject):
    def __init__(self):
        VMobject.__init__(self)
        rabbit = SVGMobject(os.path.join(path_to_SVG, 'rabbit.svg'))
        rabbit.set_color(WHITE).scale(0.55)

        self.add(rabbit)




class CageSquare(VMobject):
    def __init__(self):
        VMobject.__init__(self)
        cage_square = SVGMobject(os.path.join(path_to_SVG, 'cage_square.svg'))
        cage_square.set_color(GOLD).scale(1.5)

        self.add(cage_square)


class CageBird(VMobject):
    def __init__(self):
        VMobject.__init__(self)
        cage_bird = SVGMobject(os.path.join(path_to_SVG, 'cage_bird.svg'))
        cage_bird.set_color(GOLD).scale(2)

        self.add(cage_bird)


class OpenScissors(VMobject):
    def __init__(self):
        VMobject.__init__(self)
        open_scissors = SVGMobject(os.path.join(path_to_SVG, 'open_scissors.svg'))
        open_scissors.set_color(WHITE).rotate(PI/10).scale(0.5)

        self.add(open_scissors)


class ClosedScissors(VMobject):
    def __init__(self):
        VMobject.__init__(self)
        closed_scissors = SVGMobject(os.path.join(path_to_SVG, 'closed_scissors.svg'))
        closed_scissors.set_color(WHITE).scale(0.4).rotate(PI/5)

        self.add(closed_scissors)


class ThinkingBubble(VMobject):
    def __init__(self, smooth=True, from_left_to_right=True, style=1):
        VMobject.__init__(self)

        if smooth:
            if from_left_to_right:
                if style == 1:
                    thinking_bubble = SVGMobject(
                            os.path.join(path_to_SVG, 'smooth_thinking_bubble_left_1.svg')
                        )
                else:
                    thinking_bubble = SVGMobject(
                            os.path.join(path_to_SVG, 'smooth_thinking_bubble_left_2.svg')
                        )
            else:
                if style == 1:
                    thinking_bubble = SVGMobject(
                            os.path.join(path_to_SVG, 'smooth_thinking_bubble_right_1.svg')
                        )
                else:
                    thinking_bubble = SVGMobject(
                            os.path.join(path_to_SVG, 'smooth_thinking_bubble_right_2.svg')
                        )
        else:
            if from_left_to_right:
                if style == 1:
                    thinking_bubble = SVGMobject(
                            os.path.join(path_to_SVG, 'thinking_bubble_left_1.svg')
                        )
                else:
                    thinking_bubble = SVGMobject(
                            os.path.join(path_to_SVG, 'thinking_bubble_left_2.svg')
                        )
            else:
                if style == 1:
                    thinking_bubble = SVGMobject(
                            os.path.join(path_to_SVG, 'thinking_bubble_right_1.svg')
                        )
                else:
                    thinking_bubble = SVGMobject(
                            os.path.join(path_to_SVG, 'thinking_bubble_right_2.svg')
                        )
        
        thinking_bubble.set_color(WHITE).scale(0.5)

        self.add(thinking_bubble)





class Weight(VGroup):
    def __init__(self, kg=1, unit_kg=1):
        VGroup.__init__(self)
        self.weight = VGroup(
            SVGMobject(os.path.join(path_to_SVG, 'weight.svg')).scale(0.5),
            MathTex(f"{kg}", color=BLACK, font_size=30)).scale((kg/(2*unit_kg)) ** (1./3.)
        )

        self.kettlebell = self.weight[0]
        self.weight_value = self.weight[1]








class Scissors():
    def __init__(self, cut_point=ORIGIN):
        self.cut_point = cut_point
        scissor_1 = SVGMobject(os.path.join(path_to_SVG, 'scissors_1.svg')).set_color(WHITE)
        scissor_2 = SVGMobject(os.path.join(path_to_SVG, 'scissors_2.svg')).set_color(WHITE)
        dot = Dot().scale(0.2)
        self.__p_end = [a + b for a, b in zip([0, -0.35, 0], cut_point)]
        VGroup(scissor_1, scissor_2).arrange(RIGHT, buff=0.1)
        scissor_1.shift(0.08 * DOWN + 0.6 * RIGHT)
        scissor_2.shift(0.08 * DOWN - 0.6 * RIGHT)
        scissors_with_dot = VGroup(scissor_1, scissor_2, dot).scale(0.5)
        point = scissors_with_dot[2].get_center()
        scissors_with_dot[0].rotate(angle=-0.02, about_point=point)
        scissors_with_dot[1].rotate(angle=0.02, about_point=point)
        scissors_with_dot.move_to(self.__p_end)
        scissors_with_dot.shift(DOWN)
        self.siz = scissors_with_dot


    def cut_in(self, screen):

        def cut_with_scissors(mobject, t):
            dt = 1/60
            dl= [0, 1/60, 0]
            if t < 1/2:
                angle = PI / 6 * dt
            else:
                angle = -PI / 6 * dt
            #p_end = [a+b for a, b in zip([0, -0.25, 0], mobject[3].get_center())]
            mobject.shift(dl)
            point = mobject[2].get_center()
            mobject[0].rotate(angle=angle, about_point=point)
            mobject[1].rotate(angle=-angle, about_point=point)
        screen.play(UpdateFromAlphaFunc(self.siz, cut_with_scissors, run_time=1, rate_func=linear))
        self.siz.move_to(self.__p_end)

    def cut_out(self, screen):
        def cut_with_scissors(mobject, t):
            dt = 1/60
            dl = [0, -1/60, 0]
            angle = PI / 6 * dt
            mobject.shift(dl)
            point = mobject[2].get_center()
            color = Color(hue=1, saturation=t/3, luminance=1-t)
            mobject.set_color(color)
            mobject[0].rotate(angle=angle, about_point=point)
            mobject[1].rotate(angle=-angle, about_point=point)
        screen.play(UpdateFromAlphaFunc(self.siz, cut_with_scissors, run_time=1, rate_func=linear))
        screen.remove(self.siz)


