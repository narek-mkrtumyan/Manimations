'''

մեծը փոքրից մեծ է 150-ով
մեծը փոքրի եռապատիկից մեծ է 10-ով

ձախ մասում մասերով


1:00 - 1:20
աջ կողմում 2 արկղ, մի և փոքր
մեծը փոքրից ծանր է 150-ով
մեծը սարքում ենք փոքր + 150

1:45 - 2:25
մեկ արկղ և 150կգ = 3 արկղ և ևս 10 կգ
կշեռքի ձախ նժարին 1 + 150
աջին 3 + 10

3:00 - 3:40
երկու կողմերից հանում ենք մեկական արկղ
150ը բաժանում ենք 140 ու 10
երկու կողմից էլ հանում ենք 10

4:00 - 
2 իրար նման արկեղերը 140 կգ
մեկ արկղը 70 կգ

փոքր արկղը 70
մեծը 70+150

'''



import sys
sys.path.append('../../../')
from Functions.qarakusi import *


class Prob10540Scales(ScalesScene):
    def construct(self):

        dividing_line = DashedLine(4 * UP, 4 * DOWN).shift(0.15 * RIGHT)
        
        box = Box().next_to(dividing_line).shift(3 * UP).shift(0.5 * RIGHT)
        big_box = Box().scale(2).next_to(dividing_line).shift(UP).shift(0.5 * RIGHT)

        second_box = Box().next_to(dividing_line).shift(UP).shift(0.5 * RIGHT)
        weight_150 = Weight(150, 9).next_to(second_box, aligned_edge=DOWN)

        equality_sign = Tex('=', font_size=100).next_to(weight_150, buff=0.4).shift(0.4 * DOWN)

        boxes = VGroup(Box(), Box(), Box()).arrange(buff=0.1).next_to(weight_150, buff=1.2, aligned_edge=DOWN)
        weight_10 = Weight(10, 7).next_to(boxes, buff=0.1, aligned_edge=DOWN)

        scales = Scales(plate_stretch_factor=1.7).scale(0.57).to_corner(DR).shift(0.25 * RIGHT + UP)

        small_70 = Tex('70կգ (փոքրը)').next_to(box, buff=1)
        big_220 = Tex('70+150 = 220կգ (մեծը)').next_to(small_70, DOWN, buff=1, aligned_edge=RIGHT)


# ANIMATIONS

        self.play(Create(dividing_line))
        self.wait()

        self.play(FadeIn(big_box))
        self.wait()
        self.play(FadeIn(box))
        self.wait()

        self.play(ReplacementTransform(big_box, VGroup(second_box, weight_150)))
        self.wait()

        self.play(Write(equality_sign))
        self.wait()

        self.play(
            AnimationGroup(
                *[FadeIn(b) for b in boxes],
                FadeIn(weight_10),
                lag_ratio=0.25
            )
        )
        self.wait()

        self.play(FadeIn(scales))
        self.wait()

        self.play(VGroup(second_box, weight_150).animate.arrange(aligned_edge=DOWN).next_to(scales.left_plate, UP, buff=0))
        self.play(
            scales.rotating_part.animate.rotate(PI/12, about_point=scales.rotation_dot.get_center()),
            VGroup(second_box, weight_150).animate.shift(0.51 * DOWN)
        )
        self.wait()

        self.play(
            VGroup(boxes, weight_10).animate.arrange(buff=0.1, aligned_edge=DOWN).next_to(scales.right_plate, UP, buff=0),
            FadeOut(equality_sign)
        )
        self.play(
            scales.rotating_part.animate.rotate(-PI/12, about_point=scales.rotation_dot.get_center()),
            VGroup(second_box, weight_150).animate.shift(0.51 * UP),
            VGroup(boxes, weight_10).animate.shift(0.51 * DOWN)
        )
        self.wait()

        self.play(VGroup(second_box, boxes[0]).animate.shift(UP))
        self.wait()

        self.play(FadeOut(VGroup(second_box, boxes[0])))
        self.wait()

        self.play(
            weight_150.animate.next_to(scales.left_plate, UP, buff=0),
            VGroup(boxes[1], boxes[2], weight_10).animate.next_to(scales.right_plate, UP, buff=0)
        )
        self.wait()

        self.play(Transform(
                weight_150,
                VGroup(Weight(140, 9), Weight(10, 7)).arrange(aligned_edge=DOWN).next_to(scales.left_plate, UP, buff=0)
            ))
        self.wait()

        self.play(VGroup(weight_150[1], weight_10).animate.shift(UP))
        self.wait()

        self.play(FadeOut(VGroup(weight_150[1], weight_10)))
        self.wait()

        self.play(
            weight_150[0].animate.next_to(scales.left_plate, UP, buff=0),
            boxes[1:].animate.next_to(scales.right_plate, UP, buff=0)
        )
        self.wait()

        self.play(Transform(
            weight_150[0], 
            VGroup(Weight(70, 10), Weight(70, 10)).arrange(aligned_edge=DOWN).next_to(scales.left_plate, UP, buff=0)
        ))
        self.wait()

        self.play(Write(small_70))
        self.wait()

        self.play(Write(big_220))
        self.wait()


class Given(QarakusiScene):
    def construct(self):

        first = Tex('Մեծը փոքրից մեծ է 150-ով', font_size=60).to_edge(LEFT).shift(RIGHT)
        second = Tex('Մեծը փոքրի եռապատիկից մեծ է 10-ով', font_size=60).next_to(first, DOWN, buff=1, aligned_edge=LEFT)

        checks = VGroup(
            Check().scale(0.2).next_to(first, LEFT),
            Check().scale(0.2).next_to(second, LEFT)
        )

        self.play(Write(first, run_time=2))
        self.wait()
        self.play(Write(second, run_time=3))
        self.wait()

        self.play(first.animate.set_color(GREEN))
        self.add_sound(os.path.join(path_to_Objects, 'sounds', 'check'))
        self.play(Create(checks[0]), run_time=0.5)
        self.wait()

        self.play(second.animate.set_color(GREEN))
        self.add_sound(os.path.join(path_to_Objects, 'sounds', 'check'))
        self.play(Create(checks[1]), run_time=0.5)

        self.play(FadeOut(first, second, checks))

