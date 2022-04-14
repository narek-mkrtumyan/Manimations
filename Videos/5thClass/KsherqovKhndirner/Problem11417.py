import sys

from numpy import arange
sys.path.append('../../../')
from Functions.qarakusi import *


class Problem11417(ScalesScene):
    def construct(self):

        left_part_list_of_str_1 = ['mushroom', 'mushroom']
        right_part_list_of_str_1 = ['weight_60_kg', 'red_apple', 'red_apple', 'red_apple']
        sc_1 = ScalesWithItems(left_part_list_of_str_1, right_part_list_of_str_1, 0.34, 1, 0.75, 1.2).shift([-2, 1.5, 0])

        left_part_list_of_str_2 = ['red_apple', 'red_apple', 'mushroom', 'mushroom']
        right_part_list_of_str_2 = ['mushroom', 'mushroom', 'mushroom']
        sc_2 = ScalesWithItems(left_part_list_of_str_2, right_part_list_of_str_2, 0.34, 1, 0.75, 1.2).shift([-2, -2.5, 0])


        self.add(sc_1, sc_2)
        self.wait()

        # self.play(FadeIn(sc_1.scales))
        # self.wait()
        # self.add_scales_items(sc_1, unit_creation_runtime=0.1)
        # self.wait()

        # self.play(FadeIn(sc_2.scales))
        # self.wait()
        # self.add_scales_items(sc_2, unit_creation_runtime=0.1)
        # self.wait()

        self.remove_objects_from_both_sides(sc_2, [2, 3], [0, 1])
        self.wait(0.25)

        self.play(
            sc_2.left_mobs.animate.next_to(sc_2.scales.left_plate, UP, buff=DEFAULT_SCALES_BUFF),
            sc_2.right_mobs.animate.next_to(sc_2.scales.right_plate, UP, buff=DEFAULT_SCALES_BUFF)
        )
        self.wait(0.25)

        self.play(Circumscribe(sc_2.right_mobs))
        self.wait(0.25)
        self.play(Circumscribe(sc_2.left_mobs))
        self.wait(0.25)

        self.play(Circumscribe(sc_1.left_mobs[0]))
        self.wait(0.25)
        self.play(Transform(sc_1.left_mobs[0], VGroup(Apple(RED), Apple(RED)).arrange(buff=0.1).next_to(sc_1.left_mobs[-1], LEFT, buff=0.1)))
        self.wait(0.25)

        sc_1.left_mobs = VGroup(*sc_1.left_mobs[0], sc_1.left_mobs[1])

        self.play(Circumscribe(sc_1.left_mobs[2]))
        self.wait(0.25)
        self.play(Transform(sc_1.left_mobs[2], VGroup(Apple(RED), Apple(RED)).arrange(buff=0.1).next_to(sc_1.left_mobs[1], RIGHT, buff=0.1)))
        self.wait(0.25)

        sc_1.left_mobs = VGroup(sc_1.left_mobs[0], sc_1.left_mobs[1], *sc_1.left_mobs[2])
        final_apple = sc_1.left_mobs[0][0]
        final_weight = sc_1.right_mobs[0]

        self.remove_objects_from_both_sides(sc_1, [1, 2, 3], [1, 2, 3])

        self.wait(0.25)

        self.play(FadeOut(sc_1.scales, sc_2))
        self.wait(0.25)

        equality_sign = Tex('=', font_size=100).move_to(VGroup(final_apple, final_weight).get_center()).shift(0.2 * DOWN)

        self.play(
            Write(equality_sign),
            final_apple.animate.next_to(equality_sign, LEFT),
            final_weight.animate.next_to(equality_sign, RIGHT).shift(0.2 * UP)
        )
        self.wait(0.25)



