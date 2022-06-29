'''

-------IntroScales-------
տեղափոխվում ենք գրամների և կշեռքի աշխարհ

Circumscribe նժարավոր կշեռք
Circumscribe նժարներ
ճոճում ենք նժարները
10-10 դրինք, հետո 5-5 ավելացրինք
հետո մի 5-ը սարքինք 10 ու էդ կողմն իջացրինք

-------ProblemMandarins-------
միասին 27
երկրորդ = առաջինի կես + 3

առաջին - մեկ մեծ արկղ
մեծ արկղը բաժանում ենք 2 փոքր արկղի
երկրորդը կլինի 1 փոքր արկղ + 1 դույլ
միասին 27

կշեռքի ձախ նժար - 3 արկղ + 1 դույլ (3 կգ)
աջ նժար - 27կգ կշռաքար
երկու կողմերին էլ ավելացնում ենք 1կգ, մնում ա հավասարակշռված
27-ը բաժանում ենք 24 ու 3
երկու կողմից էլ հանում ենք 3-ը
24-ը բաժանում ենք 3 հատ 8-ի

գրում ենք 24։3 = 8կգ, մեկ արկղի զանգվածը

2*8 = 16
8+3=11

'''



import sys
sys.path.append('../../../')

from Functions.qarakusi import *


class IntroScales(QarakusiScene):
    def construct(self):

        scales = Scales().scale(0.8).shift(DOWN)

        weights = VGroup(Weight(10, 2), Weight(10, 2), Weight(5, 2), Weight(5, 2)).arrange(RIGHT, 0.5).to_edge(UP)

# ANIMATIONS

        self.add(scales, weights)
        self.wait()

# CIRCUMSCRIBE SCALES AND PLATES
        self.play(Circumscribe(scales, fade_out=True), run_time=2)
        self.wait()

        self.play(Circumscribe(scales.left_plate, fade_out=True), run_time=2)
        self.play(Circumscribe(scales.right_plate, fade_out=True), run_time=2)
        self.wait()

# TILT THE SCALES
        self.play(
            scales.rotating_part.animate.rotate(PI/12, about_point=scales.rotation_dot.get_center()),
            run_time=2, rate_func=there_and_back
        )
        self.play(
            scales.rotating_part.animate.rotate(-PI/12, about_point=scales.rotation_dot.get_center()),
            run_time=2, rate_func=there_and_back
        )
        self.wait()

# PLACE WEIGHTS ON PLATES
        self.play(
            weights[0].animate.next_to(scales.left_plate, UP, buff=0.01),
            weights[1].animate.next_to(scales.right_plate, UP, buff=0.01)
        )
        self.wait()

        self.play(
            VGroup(weights[2], weights[0]).animate.arrange(RIGHT, buff=0.5, aligned_edge=DOWN).next_to(scales.left_plate, UP, buff=0.01),
            VGroup(weights[3], weights[1]).animate.arrange(RIGHT, buff=0.5, aligned_edge=DOWN).next_to(scales.right_plate, UP, buff=0.01),
        )
        self.wait()

        left_weights = always_redraw(lambda: VGroup(weights[2], weights[0]).next_to(scales.left_plate, UP, buff=0.01))
        right_weights = always_redraw(lambda: VGroup(weights[3], weights[1]).next_to(scales.right_plate, UP, buff=0.01))
        self.add(left_weights)
        self.add(right_weights)

# TRANSFORM 5KG INTO 10KG AND TILT THE SCALES
        self.play(Circumscribe(weights[2]))
        self.wait()

        self.play(Transform(weights[2], Weight(10, 2).move_to(weights[2]).align_to(weights[2], DOWN)))
        self.play(scales.rotating_part.animate.rotate(PI/12, about_point=scales.rotation_dot.get_center()), run_time=2)
        self.wait()





class ProblemMandarins(QarakusiScene):
    def construct(self):

        shop_1 = SVGMobject(os.path.join(path_to_SVG, 'mandarin_store_1')).scale(0.75).shift([-3.5, 1.5, 0])
        shop_2 = SVGMobject(os.path.join(path_to_SVG, 'mandarin_store_2')).scale(0.75).shift([-3.5, -1.75, 0])

        shop_1_tex = Tex('Առաջին խանութ', font_size=25).next_to(shop_1, UP)
        shop_2_tex = Tex('Երկրորդ խանութ', font_size=25).next_to(shop_2, UP)

        half_plus_3 = Tex('Առաջինի կեսից ', '3կգ ավելի', font_size=30).next_to(shop_2).shift(1.1 * RIGHT)
        together_27 = Tex('Միասին 27կգ').to_edge(UP)

        box_big = BoxOfOranges().scale(1.2).next_to(shop_1).shift(1.5 * RIGHT)
        box_1 = BoxOfOranges().scale(0.7)
        box_2 = BoxOfOranges().scale(0.7)
        first_boxes = VGroup(box_1, box_2).arrange(buff=0.5).move_to(box_big.get_center())

        box_3 = BoxOfOranges().scale(0.7).next_to(shop_2).shift(1.25 * RIGHT)
        bucket = BucketOfOranges().scale(0.9).next_to(box_3, buff=0.5)
        bucket.add(Tex('3կգ', font_size=22).move_to(bucket).shift(0.15 * DOWN))

        initial_positions_copy = VGroup(shop_1, shop_1_tex, shop_2, shop_2_tex, 
            box_1.copy(), box_2.copy(), box_3.copy(), bucket.copy()
            )
        final_answers = VGroup(
            Tex(r'---\;\; ', '16 կգ'),
            Tex(r'---\;\; ', '8+3=11 կգ')
        )
        final_answers[0].next_to(box_2, buff=0.75)
        final_answers[1].next_to(bucket).align_to(final_answers[0], LEFT)

        scales = Scales(5, 2).move_to([0, -1, 0])

        weight_27 = Weight(27, 2).next_to(scales.right_plate, UP, buff=0)

        left_plate_stuff = VGroup(box_1, box_2, box_3, bucket)
        left_plate_boxes = VGroup(box_1, box_2, box_3)

        weight_1_1 = Weight(1, 2)
        weight_1_2 = Weight(1, 2)
        VGroup(weight_1_1, weight_1_2).arrange().to_edge(UP)

        weight_24 = Weight(24, 2)
        weight_3 = Weight(3, 2)
        VGroup(weight_24, weight_3).arrange(aligned_edge=DOWN).next_to(scales.right_plate, UP, buff=0)

        weights_8 = VGroup(Weight(8, 2), Weight(8, 2), Weight(8, 2))
        weights_8.arrange().next_to(scales.right_plate, UP, buff=0)

        divide_24_3 = Tex('24:3=', '8կգ').to_edge(UP).shift(0.5 * DOWN)


# ANIMATIONS
    
        self.play(FadeIn(shop_1, shop_2, shop_1_tex, shop_2_tex))
        self.play(Write(together_27))
        self.play(Write(half_plus_3[0]))
        self.wait(0.25)
        self.play(Write(half_plus_3[1]))
        self.play(FadeIn(box_big))
        self.wait()

        self.play(
            ReplacementTransform(box_big, Dot(box_big.get_center(), radius=0)),
            ReplacementTransform(Dot(box_big.get_center(), radius=0), first_boxes)
        )
        self.wait()

        self.play(ReplacementTransform(half_plus_3[0], box_3))
        self.wait()

        self.play(ReplacementTransform(half_plus_3[1], bucket))
        self.wait()

        self.play(Circumscribe(together_27))
        self.wait()

        self.play(FadeOut(shop_1, shop_1_tex, shop_2, shop_2_tex))

        self.play(
            left_plate_stuff.animate.arrange(aligned_edge=DOWN).next_to(scales.left_plate, UP, buff=0),
            together_27.animate.next_to(scales.right_plate, UP, buff=0)
        )

        self.play(FadeIn(scales))
        self.wait()

        self.play(ReplacementTransform(together_27, weight_27))
        self.wait()

        self.play(FadeIn(weight_1_1, weight_1_2))
        self.wait()

        self.play(
            left_plate_stuff.animate.shift(0.25 * LEFT),
            weight_27.animate.shift(0.25 * LEFT),
            weight_1_1.animate.next_to(left_plate_stuff, aligned_edge=DOWN),
            weight_1_2.animate.next_to(weight_27, aligned_edge=DOWN)
        )
        self.wait()

        self.play(VGroup(weight_1_1, weight_1_2).animate.shift(UP))
        self.play(
            left_plate_stuff.animate.shift(0.25 * RIGHT),
            weight_27.animate.shift(0.25 * RIGHT),
            FadeOut(VGroup(weight_1_1, weight_1_2))
        )
        self.wait()

        self.play(ReplacementTransform(weight_27, VGroup(weight_24, weight_3)))
        self.wait()

        self.play(
            Circumscribe(bucket, fade_out=True),
            Circumscribe(weight_3, fade_out=True),
            run_time=3
        )
        self.wait()

        self.play(VGroup(bucket, weight_3).animate.shift(UP))
        self.wait()
        self.play(FadeOut(VGroup(bucket, weight_3)))
        self.wait()

        self.play(
            left_plate_boxes.animate.next_to(scales.left_plate, UP, buff=0),
            weight_24.animate.next_to(scales.right_plate, UP, buff=0)
        )
        self.wait()

        self.play(ReplacementTransform(weight_24, weights_8))
        self.wait()

        self.play(Write(divide_24_3))
        self.wait()

        self.play(FadeOut(left_plate_boxes, scales, weights_8, divide_24_3))
        self.wait()

        self.play(FadeIn(initial_positions_copy))
        self.play(Write(final_answers[0]))
        self.wait()
        self.play(Write(final_answers[1]))
        self.wait()


