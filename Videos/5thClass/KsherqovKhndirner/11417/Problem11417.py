'''

2 կշեռք

առաջինի ձախին 2 սունկ
աջին 3 խնձոր 
և 60 գրամ

երկրորդի ձախին 2 խնձոր 2 սունկ
աջին 3 սունկ

circumscribe առաջինի ձախ ու աջ նժարները
circumscribe երկրորդ կշեռքը

circumscribe երկուական սունկերը 
բարձրացնում ենք ու fade out անում դրանք

circumscribe 2 խնձորը ու 1 սունկը

առաջին կշեռքի մեկ սունկ circumscribe ու փոխարինել 2 խնձոր
նույնը երկրորդ սնկի հետ

հանում ենք 3 խնձորները

circumscribe խնձոր
circumscribe կշռաքար

կշեռքը ֆեյդաութ ենք անում, մեկ խնձոր - 60 գրամ

սունկ - 2x60 = 120

'''





import sys

sys.path.append('../../../../')
from Functions.qarakusi import *
from arm_texs import *


class Problem11417(ScalesScene):
    def construct(self):

# INITS
    # scales 1
        mushroom = Mushroom().scale(1.5)
        sc_1 = Scales(5, 1.3).scale(0.8).move_to([-2, 1, 0])

        sc_1_left_mobs = VGroup(mushroom.copy(), mushroom.copy())
        sc_1_left_mobs.arrange(aligned_edge=DOWN).next_to(sc_1.left_plate, UP, buff=0)
        sc_1_left_mobs.add_updater(lambda mobs: mobs.next_to(sc_1.left_plate, UP, buff=0))

        sc_1_right_mobs = VGroup(Apple(RED), Apple(RED), Apple(RED), Weight(60, 30))
        sc_1_right_mobs.arrange(aligned_edge=DOWN).next_to(sc_1.right_plate, UP, buff=0)
        sc_1_right_mobs.add_updater(lambda mobs: mobs.next_to(sc_1.right_plate, UP, buff=0))
        weight = sc_1_right_mobs[-1]

    # scales 2
        sc_2 = Scales(5, 1.3).scale(0.8).move_to([-2, -2.75, 0])

        sc_2_left_mobs = VGroup(Apple(RED), Apple(RED), mushroom.copy(), mushroom.copy())
        sc_2_left_mobs.arrange(aligned_edge=DOWN).next_to(sc_2.left_plate, UP, buff=0)
        sc_2_left_mobs.add_updater(lambda mobs: mobs.next_to(sc_2.left_plate, UP, buff=0))
        apples = VGroup(sc_2_left_mobs[0], sc_2_left_mobs[1])

        sc_2_right_mobs = VGroup(mushroom.copy(), mushroom.copy(), mushroom.copy())
        sc_2_right_mobs.arrange(aligned_edge=DOWN).next_to(sc_2.right_plate, UP, buff=0)
        sc_2_right_mobs.add_updater(lambda mobs: mobs.next_to(sc_2.right_plate, UP, buff=0))
        mushroom = sc_2_right_mobs[-1]


# ANIMATIONS

    # fade in scales and fruits

        self.play(FadeIn(sc_1), FadeIn(sc_2))
        self.wait()

        self.play(FadeIn(sc_1_left_mobs))
        self.rotate_scales(sc_1)
        self.wait()

        self.play(FadeIn(sc_1_right_mobs))
        self.rotate_scales(sc_1, -1)
        self.wait()

        self.play(FadeIn(sc_2_left_mobs))
        self.rotate_scales(sc_2)
        self.wait()

        self.play(FadeIn(sc_2_right_mobs))
        self.rotate_scales(sc_2, -1)
        self.wait()

        self.play(
            Circumscribe(sc_1_left_mobs, fade_out=True, run_time=2),
            Circumscribe(sc_1_right_mobs, fade_out=True, run_time=2)
        )
        self.wait()

        self.play(Circumscribe(VGroup(sc_2, sc_2_left_mobs, sc_2_right_mobs), fade_out=True, run_time=2))
        self.wait()
    

    # remove 2 mushrooms from both sides of the second scales

        sc_1_left_mobs.clear_updaters()
        sc_1_right_mobs.clear_updaters()
        sc_2_left_mobs.clear_updaters()
        sc_2_right_mobs.clear_updaters()

        self.play(
            Circumscribe(sc_2_left_mobs[2:], fade_out=True, run_time=2),
            Circumscribe(sc_2_right_mobs[:2], fade_out=True, run_time=2),
        )
        self.wait()

        self.play(VGroup(*sc_2_left_mobs[2:], *sc_2_right_mobs[:2]).animate.shift(UP * 0.75))
        self.wait()
        self.play(
            FadeOut(VGroup(*sc_2_left_mobs[2:], *sc_2_right_mobs[:2])),
            apples.animate.next_to(sc_2.left_plate, UP, buff=0),
            mushroom.animate.next_to(sc_2.right_plate, UP, buff=0)
        )
        self.wait()

    # replace mushroom with 2 apples on the left side of the first scales

        self.play(
            Circumscribe(apples, fade_out=True, run_time=2),
            Circumscribe(mushroom, fade_out=True, run_time=2),
        )
        self.wait()

        self.play(Circumscribe(sc_1_left_mobs[0]))
        self.wait(0.5)
        self.play(
            Transform(
                sc_1_left_mobs[0],
                VGroup(Apple(RED), Apple(RED)).arrange().next_to(sc_1_left_mobs[-1], LEFT, aligned_edge=DOWN)
            )
        )
        self.wait()

        self.play(Circumscribe(sc_1_left_mobs[1]))
        self.wait(0.5)
        self.wait()
        self.play(
            Transform(
                sc_1_left_mobs[1],
                VGroup(Apple(RED), Apple(RED)).arrange().next_to(sc_1_left_mobs[0], RIGHT, aligned_edge=DOWN)
            )
        )
        self.wait()

        sc_1_left_mobs = VGroup(*sc_1_left_mobs[0], *sc_1_left_mobs[1])
        apple = sc_1_left_mobs[-1]

    # remove 3 apples from both sides of the first scales

        self.play(VGroup(sc_1_left_mobs[:-1], sc_1_right_mobs[:-1]).animate.shift(0.75 * UP))
        self.wait()

        self.play(
            FadeOut(VGroup(*sc_1_left_mobs[:-1], *sc_1_right_mobs[:-1])),
            apple.animate.next_to(sc_1.left_plate, UP, buff=0),
            weight.animate.next_to(sc_1.right_plate, UP, buff=0)
        )
        self.wait()

        self.play(FadeOut(sc_1))
        self.wait()

    # show answers

        self.play(weight.animate.next_to(apple, buff=1))
        self.wait()
        
        sixty.move_to(weight.get_center())
        two_times_sixty.next_to(sixty, DOWN, buff=0.75, aligned_edge=LEFT)

        sixty[0].shift(0.2 * LEFT)
        two_times_sixty[0].shift(0.2 * LEFT)

        self.play(Write(sixty[0]))
        self.play(ReplacementTransform(weight, sixty[1]))
        self.play(Write(gram.next_to(sixty)))
        self.wait()

        self.play(
            FadeIn(mushroom.copy().next_to(apple, DOWN, buff=0.5)),
            Write(two_times_sixty[0])
        )
        self.wait()

        self.play(Write(two_times_sixty[1]))
        self.play(Write(gram.copy().next_to(two_times_sixty)))
        self.wait()

