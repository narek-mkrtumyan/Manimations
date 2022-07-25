import sys

from numpy import gradient
sys.path.append('../../../')
from Functions.qarakusi import * 

class Problem11159_FirstSolution(ScalesScene):
    def construct(self):

# INIT
   # scales 1 


        goose = Goose().scale(0.8)
        duck = Duck().scale(0.8)
        sc_1 = Scales(5, 2.1).scale(0.7).shift(0.3*UP+0.5*RIGHT)

        sc_1_left_mobs = VGroup(duck.copy(), duck.copy(), goose.copy(), goose.copy(), goose.copy())
        sc_1_left_mobs.arrange(aligned_edge=DOWN, buff=0.1).next_to(sc_1.left_plate, UP, buff=0)

        sc_1_ducks = VGroup(*sc_1_left_mobs[:2]).copy()
        sc_1_geese = VGroup(*sc_1_left_mobs[2:]).copy()
        sc_1_ducks.add_updater(lambda mobs: mobs.next_to(sc_1.left_plate, UP, buff=0).align_to(sc_1_left_mobs[0:2], LEFT))
        sc_1_geese.add_updater(lambda mobs: mobs.next_to(sc_1.left_plate, UP, buff=0).align_to(sc_1_left_mobs[2:], LEFT))

        sc_1_left_mobs.add_updater(lambda mobs: mobs.next_to(sc_1.left_plate, UP, buff=0))

        sc_1_right_mobs = VGroup(Weight(6700, 600))
        sc_1_right_mobs.arrange(aligned_edge=DOWN).next_to(sc_1.right_plate, UP, buff=0)
        sc_1_right_mobs.add_updater(lambda mobs: mobs.next_to(sc_1.right_plate, UP, buff=0))

        sc_1_right_mobs_2 = VGroup(Weight(6100, 600), Weight(600, 150))
        sc_1_right_mobs_2.arrange(aligned_edge=DOWN).next_to(sc_1.right_plate, UP, buff=0)
        sc_1_right_mobs_2.add_updater(lambda mobs: mobs.next_to(sc_1.right_plate, UP, buff=0))
    

    # scales 2
        sc_2 = Scales(5, 2.1).scale(0.7).shift(3*DOWN+0.5*RIGHT)

        sc_2_left_mobs = VGroup(goose.copy(), goose.copy(), duck.copy(), duck.copy(), duck.copy())
        sc_2_left_mobs.arrange(aligned_edge=DOWN, buff=0.05).next_to(sc_2.left_plate, UP, buff=0)

        sc_2_geese = VGroup(*sc_2_left_mobs[:2]).copy()
        sc_2_ducks = VGroup(*sc_2_left_mobs[2:]).copy()
        sc_2_geese.add_updater(lambda mobs: mobs.next_to(sc_2.left_plate, UP, buff=0).align_to(sc_2_left_mobs[:2], LEFT))
        sc_2_ducks.add_updater(lambda mobs: mobs.next_to(sc_2.left_plate, UP, buff=0).align_to(sc_2_left_mobs[2:], LEFT))

        sc_2_left_mobs.add_updater(lambda mobs: mobs.next_to(sc_2.left_plate, UP, buff=0))


        sc_2_right_mobs = VGroup(Weight(7000, 600))
        sc_2_right_mobs.arrange(aligned_edge=DOWN).next_to(sc_2.right_plate, UP, buff=0)
        sc_2_right_mobs.add_updater(lambda mobs: mobs.next_to(sc_2.right_plate, UP, buff=0))

        sc_2_right_mobs_2 = VGroup(Weight(6700, 600), Weight(300, 150))
        sc_2_right_mobs_2.arrange(aligned_edge=DOWN).next_to(sc_2.right_plate, UP, buff=0)
        sc_2_right_mobs_2.add_updater(lambda mobs: mobs.next_to(sc_2.right_plate, UP, buff=0))

    # Equations

        eq_1 = MathTex("7000 - 6700 =", " 300", font_size=DEFAULT_FONT_SIZE).shift([4.5, 3, 0])
        eq_2 = MathTex("6700 - 2 \\cdot 300 = 6100", font_size=DEFAULT_FONT_SIZE).shift([4, 2, 0])
        eq_3 = MathTex("6100 : 5 = 1220", font_size=DEFAULT_FONT_SIZE).next_to(eq_2, DOWN, buff=0.5).align_to(eq_2, LEFT)
        eq_4 = MathTex("1220 + 300 = 1520", font_size=DEFAULT_FONT_SIZE).next_to(eq_3, DOWN, buff=0.5).align_to(eq_3, LEFT)
        

    


    # scales 3
        sc_3 = Scales(5, 1.2).scale(0.5).shift(4.15*RIGHT)

        sc_3_left_mobs = duck.copy()
        sc_3_left_mobs.arrange(aligned_edge=DOWN, buff=0.1).next_to(sc_3.left_plate, UP, buff=0)
        sc_3_left_mobs.add_updater(lambda mobs: mobs.next_to(sc_3.left_plate, UP, buff=0))

        sc_3_right_mobs = VGroup(goose.copy(), Weight(300, 150))
        sc_3_right_mobs.arrange(aligned_edge=DOWN).next_to(sc_3.right_plate, UP, buff=0)
        sc_3_right_mobs.add_updater(lambda mobs: mobs.next_to(sc_3.right_plate, UP, buff=0)) 

    # Given

        first = Tex("$2$ բադը", " և ", "$3$ սագը", " միասին", " կշռում են ", "$6700$ գ", font_size=DEFAULT_FONT_SIZE)
        first.shift(3*UP+1.85*LEFT)
        second = Tex("$2$ սագը", " և ", "$3$ բադը", " միասին", " կշռում են ", "$7$ կգ", font_size=DEFAULT_FONT_SIZE)
        second.next_to(sc_1, DOWN, buff=0.1)
        second.align_to(first, LEFT)



# ANIMATION

        self.wait()

    # Համառոտագրություն

        self.play(Write(first))
        self.wait()

        self.play(Write(second))
        self.wait()

    # 2 կշեռքներով հավասարություններ

        self.play(FadeIn(sc_1), FadeIn(sc_2))
        self.wait()
        
        x = first[0].copy()
        self.play(x.animate.move_to(sc_1_ducks))
        self.play(ReplacementTransform(x, sc_1_ducks))
        self.rotate_scales(sc_1, 0.4)
        self.wait()


        y = first[2].copy()
        self.play(y.animate.move_to(sc_1_geese.get_center() - np.array([0, 0.25, 0])))
        self.play(ReplacementTransform(y, sc_1_geese))
        self.rotate_scales(sc_1, 0.4)
        self.wait()

        self.play(ReplacementTransform(first[5].copy(), sc_1_right_mobs))
        self.rotate_scales(sc_1, -0.8)
        self.remove(sc_1_ducks, sc_1_geese)
        self.add(sc_1_left_mobs)
        self.wait()

        x = second[0].copy()
        self.play(x.animate.move_to(sc_2_geese))
        self.play(ReplacementTransform(x, sc_2_geese))
        self.rotate_scales(sc_2, 0.4)
        self.wait()

        y = second[2].copy()
        self.play(y.animate.move_to(sc_2_ducks.get_center() - np.array([0, 0.25, 0])))
        self.play(ReplacementTransform(y, sc_2_ducks))
        self.rotate_scales(sc_2, 0.4)
        self.wait()

        self.play(ReplacementTransform(second[5].copy(), sc_2_right_mobs))
        self.rotate_scales(sc_2, -0.8)
        self.remove(sc_2_ducks, sc_2_geese)
        self.add(sc_2_left_mobs)
        self.wait()

        self.play(
            FadeOut(first),
            FadeOut(second),
            sc_1.animate.shift(2.35*LEFT+UP),
            sc_2.animate.shift(2.35*LEFT)
        )
        self.wait()

        sc_1_left_mobs.clear_updaters()

        self.play(Circumscribe(sc_1_left_mobs[0:4]), Circumscribe(sc_2_left_mobs[0:4]))
        self.play(
            sc_1_left_mobs[0:4].animate.shift(0.2*LEFT),
            sc_2_left_mobs[0:4].animate.shift(0.2*LEFT)
        )
        self.wait()

        self.play(Circumscribe(sc_1_left_mobs[4]), Circumscribe(sc_2_left_mobs[4]))
        self.play(
            sc_1_left_mobs[4].animate.shift(0.2*RIGHT),
            sc_2_left_mobs[4].animate.shift(0.2*RIGHT)
        )
        self.wait()

        
        self.remove(sc_1_left_mobs)
        

    # Սագը փոխարինում ենք բադով

# INIT


    # scale
        sc_2_right_mobs_2 = VGroup(Weight(6700, 600), Weight(300, 150))
        sc_2_right_mobs_2.arrange(aligned_edge=DOWN, buff=0.6).next_to(sc_2.right_plate, UP, buff=0)
        sc_2_right_mobs_2.add_updater(lambda mobs: mobs.next_to(sc_2.right_plate, UP, buff=0))

        kshraqar = sc_2_right_mobs_2[1].copy()

        

        sc_1_birds = sc_1_left_mobs[0:4].copy()
        sc_1_birds.add_updater(lambda mobs: mobs.next_to(sc_1.left_plate, UP, buff=0).align_to(sc_1_left_mobs[0:4], LEFT))

        duck = sc_2_left_mobs[4].copy()
        goose = sc_1_left_mobs[4].copy()

        


# ANIMATIONS

        # self.add(goose, sc_1_birds)
        self.remove(sc_1_left_mobs)

        self.play(goose.animate.shift(0.5 * UP))
        self.play(goose.animate.shift(RIGHT))
        self.wait()

        self.play(duck.animate.next_to(sc_1.left_plate, UP, buff=0).align_to(sc_2_left_mobs[4], RIGHT))
        self.wait()

        duck.add_updater(lambda mobs: mobs.next_to(sc_1.left_plate, UP, buff=0).align_to(sc_2_left_mobs[4], RIGHT))
        self.add(sc_1_birds)

        self.rotate_scales(sc_1, 0.25)
        self.wait()

        self.play(
            Write(eq_1),
            ReplacementTransform(sc_2_right_mobs, sc_2_right_mobs_2),
            run_time=2
        )

        self.play(kshraqar.animate.next_to(sc_1_right_mobs, RIGHT, aligned_edge=DOWN))
        self.wait()

        kshraqar.add_updater(lambda x: x.align_to(sc_1_right_mobs, DOWN))
        
        self.rotate_scales(sc_1, -0.25)
        self.wait()
        

        



        
    # Երրորդ կշեռք
    
        self.play(FadeIn(sc_3))
        self.play(FadeIn(sc_3_left_mobs))

        self.add(sc_3_right_mobs)
        sc_3_right_mobs.set_opacity(0)

        self.rotate_scales(sc_3, 0.8)

        self.play(sc_3_right_mobs[0].animate.set_opacity(1))    
        

        self.rotate_scales(sc_3, -0.4)
        
        self.play(sc_3_right_mobs[1].animate.set_opacity(1))

        self.rotate_scales(sc_3, -0.4)
        self.wait()

        self.play(
            Write(eq_1),
            ReplacementTransform(sc_2_right_mobs, sc_2_right_mobs_2),
            run_time=2
        )
        self.wait()

        self.play()


    # Երկրորդ կշեռքը ֆեյդ աութ


        self.play(
            FadeOut(sc_2),
            FadeOut(sc_2_left_mobs),
            FadeOut(sc_2_right_mobs_2)
        )
        self.wait()
            
        self.play(
            sc_3.animate.next_to(sc_1, DOWN, buff=2),
            sc_1_left_mobs[0:4].animate.shift(0.2*RIGHT),
            sc_1_left_mobs[4].animate.shift(0.2*LEFT)
        )
        self.wait()

        sc_3_right_mobs.clear_updaters()


    # Բադը փոխարինում ենք սագ+300-ով


        self.play(
            Circumscribe(sc_1_left_mobs[0]),
            Circumscribe(sc_3_left_mobs),
            Circumscribe(sc_3_right_mobs)
        )
        x = sc_3_right_mobs.copy().move_to(sc_1_left_mobs[0].get_center()+0.15*LEFT).align_to(sc_1_left_mobs[2], DOWN)
        a = Dot(radius=0).move_to(x.get_center())
        y = sc_3_right_mobs.copy().move_to(sc_1_left_mobs[1].get_center()+0.15*RIGHT).align_to(sc_1_left_mobs[2], DOWN)
        b = Dot(radius=0).move_to(y.get_center())
        self.play(
            ReplacementTransform(sc_1_left_mobs[0], a),
            ReplacementTransform(a, x)
        )
        self.wait()

        self.play(
            Circumscribe(sc_1_left_mobs[1]),
            Circumscribe(sc_3_left_mobs),
            Circumscribe(sc_3_right_mobs)
        )
        self.play(
            ReplacementTransform(sc_1_left_mobs[1], b),
            ReplacementTransform(b, y),
            sc_1_left_mobs[2:].animate.shift(0.3*RIGHT)
        )
        self.wait()



    # Երկրորդ հարց


        # self.play(Write(eq_2))
        self.wait()
        self.wait()

    # 600, 300-նոցները հանում ենք

        self.play(ReplacementTransform(sc_1_right_mobs, sc_1_right_mobs_2))
        self.play(
            x[1].animate.shift(UP * 0.5),
            y[1].animate.shift(UP * 0.5),
            sc_1_right_mobs_2[1].animate.shift(UP * 0.5)
        )
        self.play(
            FadeOut(x[1]),
            FadeOut(y[1]),
            FadeOut(sc_1_right_mobs_2[1])
        )
        self.play(
            sc_1_right_mobs_2[0].animate.next_to(sc_1.right_plate, UP, buff=0),
            sc_1_left_mobs[2:].animate.next_to(y[0], RIGHT, buff=0.1),
            x[0].animate.next_to(y[0], LEFT, buff=0.1)
        )
        self.wait()
        

        self.play(Write(eq_3))
        self.wait()

        self.play(
            Circumscribe(sc_3_left_mobs),
            Circumscribe(sc_3_right_mobs)
        )

        self.play(Write(eq_4))
        self.wait()
