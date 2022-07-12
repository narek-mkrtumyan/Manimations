'''
Given

240.000 դրամ
մեկ բաճկոն
մեկ շալվար
մեկ կոշիկ

շալվարի համար բաճկոնի կեսից 10.000-ով ավել

կոշիկի համար շալվարի կեսից 8.000-ով ավել


ShorerScales

բաճկոնը ինչ-որ կշռի մեծ արկղ
բաճկոնը սարքում ենք 2 միջին արկղ

շալվարը մեկ միջին արկղ և ևս 10.000 գրամ

10.000-ը բաժանում ենք 2 հատ 5.000

շալվարի միջին արկղը բաժանում ենք 2 հատ փոքր արկղի

հետո վերևի միջին արկղերն էլ ենք բաժանում 2 հատ փոքրի

circumscribe բաճկոն
հետ ենք միացնում 2 հատ 5-երը շալվար
նկարում ենք կոշիկը

բոլորը միասին 240.000 գրամ

դնում ենք ձախ նժարին, իջնում ա
աջին դնում ենք 240.000, հավասարվում են

պոկում ենք մի հատ 10.000, մի հատ 5.000, մի հատ 8.000 ու մնում ա 217.000


'''

import sys
sys.path.append('../../')
from Functions.qarakusi import *


SMALL_BOX_SCALE_FACTOR = 0.75
MID_BOX_SCALE_FACTOR = 1.2
BIG_BOX_SCALE_FACTOR = 2.3


class ShorerScales(ScalesScene):
    def construct(self):

        dividing_line = DashedLine(4 * UP, 4 * DOWN).shift(0.75 * RIGHT)

# INITS
        scales = Scales(5, 1.8).scale(0.5).to_corner(DR).shift(0.21 * RIGHT)

        big_box = Box().scale(BIG_BOX_SCALE_FACTOR).next_to(dividing_line).shift(3 * UP)
        mid_boxes = VGroup(Box().scale(MID_BOX_SCALE_FACTOR), Box().scale(MID_BOX_SCALE_FACTOR))
        mid_boxes.arrange().next_to(dividing_line).shift(3 * UP)

        mid_box = Box().scale(MID_BOX_SCALE_FACTOR).next_to(dividing_line).shift(1.7 * UP)

        small_box = Box().scale(SMALL_BOX_SCALE_FACTOR).next_to(dividing_line).shift(0.7 * UP)

        weight_240 = Weight(240000, 7000)
        weight_240.next_to(scales.right_plate, UP, buff=0)

        weight_5 = Weight(5000, 5000).shift(2 * LEFT)
        weight_5.next_to(small_box, aligned_edge=DOWN)

        weight_8 = Weight(8000, 5000).shift(LEFT)
        weight_8.next_to(weight_5, aligned_edge=DOWN)

        weight_10 = Weight(10000, 5000)
        weight_10.next_to(mid_box, aligned_edge=DOWN)

        weights_5_5 = VGroup(weight_5.copy(), weight_5.copy()).arrange()
        weights_5_5.next_to(mid_box)

        small_boxes_2 = VGroup(Box().scale(SMALL_BOX_SCALE_FACTOR), Box().scale(SMALL_BOX_SCALE_FACTOR)).arrange()
        small_boxes_2.next_to(dividing_line).shift(1.7 * UP)

        weight_10_copy = weight_10.copy().next_to(small_boxes_2, aligned_edge=DOWN)

        small_boxes_4 = VGroup(*[Box().scale(SMALL_BOX_SCALE_FACTOR) for _ in range(4)]).arrange()
        small_boxes_4.next_to(dividing_line).shift(3 * UP)

        left_row_1 = VGroup(small_box, *small_boxes_2, *small_boxes_4[0])
        left_row_2 = VGroup(*small_boxes_4[1:])
        left_weights = VGroup(weight_10_copy, weight_5, weight_8)

        right_weight_10 = Weight(10000, 5000)
        right_weight_230 = Weight(230000, 7000)
        right_weight_5 = Weight(5000, 5000)
        right_weight_225 = Weight(225000, 7000)
        right_weight_8 = Weight(8000, 5000)
        right_weight_217 = Weight(217000, 7000)

        weights_10_230 = VGroup(right_weight_10.copy(), right_weight_230)
        weights_10_230.arrange(aligned_edge=DOWN).next_to(scales.right_plate, UP, buff=0)

        weights_10_5_225 = VGroup(right_weight_10.copy(), right_weight_5.copy(), right_weight_225)
        weights_10_5_225.arrange(aligned_edge=DOWN, buff=0.175).next_to(scales.right_plate, UP, buff=0)

        weights_10_5_8_217 = VGroup(right_weight_10, right_weight_5, right_weight_8, right_weight_217)
        weights_10_5_8_217.arrange(aligned_edge=DOWN, buff=0.075).next_to(scales.right_plate, UP, buff=0)


# ANIMATIONS
    # արկղերի պատկերում, բաժանում ավելի փոքր մասերի
        self.play(Create(dividing_line))
        self.wait()

        self.play(FadeIn(big_box))
        self.wait()

        self.play(ReplacementTransform(big_box, mid_boxes))
        self.wait()

        self.play(FadeIn(mid_box))
        self.wait()

        self.play(FadeIn(weight_10))
        self.wait()

        self.play(ReplacementTransform(weight_10, weights_5_5))
        self.wait()

        self.play(
            ReplacementTransform(mid_box, small_boxes_2),
            weights_5_5.animate.next_to(small_boxes_2, aligned_edge=DOWN)
        )
        self.wait()

        self.play(ReplacementTransform(mid_boxes, small_boxes_4))
        self.wait()

        self.play(Circumscribe(small_boxes_4, fade_out=True))
        self.wait()

        self.play(ReplacementTransform(weights_5_5, weight_10_copy))
        self.wait()

        self.play(FadeIn(small_box))
        self.wait(0.25)
        self.play(FadeIn(weight_5))
        self.wait(0.25)
        self.play(FadeIn(weight_8))
        self.wait(0.25)

        self.play(FadeIn(scales))
        self.wait()

    # տեղափոխում կշեռքի վրա, 240 կշռաքարի ստեղծում
        self.play(
            AnimationGroup(
                left_row_1.animate.add_updater(
                    lambda left_row_1: left_row_1.arrange(buff=0.1).next_to(scales.left_plate, UP, buff=0)
                ),
                left_row_2.animate.add_updater(
                    lambda left_row_2: left_row_2.arrange(buff=0.1).next_to(left_row_1, UP, buff=-0.02)
                ),
                left_weights.animate.add_updater(
                    lambda left_weights: left_weights.arrange(buff=0.22, aligned_edge=DOWN).next_to(left_row_2, UP, buff=0)
                ),
                scales.rotating_part.animate.rotate(PI/15, about_point=scales.rotation_dot.get_center()),
                lag_ratio=0.2
            ),
            run_time=2.75
        )
        self.wait()

        weight_240.add_updater(lambda weight_240: weight_240.next_to(scales.right_plate, UP, buff=0))

        self.play(FadeIn(weight_240))

        self.play(scales.rotating_part.animate(run_time=2).rotate(-PI/15, about_point=scales.rotation_dot.get_center()))
        self.wait()

        for item in VGroup(left_row_1, left_row_2, left_weights, weight_240):
            item.clear_updaters()

    # ԼՈՒԾՈՒՄ
    
    # 240-նոցը քայլ-քայլ բաժանում ենք 10 5 8 217 ենք ստանում
        self.play(ReplacementTransform(weight_240, weights_10_230))
        self.wait()

        self.play(
            ReplacementTransform(weights_10_230[0], weights_10_5_225[0]),
            ReplacementTransform(weights_10_230[1], weights_10_5_225[1:])
        )
        self.wait()

        self.play(
            ReplacementTransform(weights_10_5_225[0], weights_10_5_8_217[0]),
            ReplacementTransform(weights_10_5_225[1], weights_10_5_8_217[1]),
            ReplacementTransform(weights_10_5_225[2], weights_10_5_8_217[2:]),
        )
        self.wait()

    # 2 կողմից հանում ենք 10 5 8-ը
        self.play(VGroup(left_weights, weights_10_5_8_217[:-1]).animate.shift(UP))
        self.wait(0.25)
        self.play(
            AnimationGroup(
                FadeOut(VGroup(left_weights, weights_10_5_8_217[:-1])),
                right_weight_217.animate.next_to(scales.right_plate, UP, buff=0),
                lag_ratio=0.5
            )
        )
        self.wait()




