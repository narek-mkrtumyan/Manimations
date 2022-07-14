'''
    Առաջին լուծում

    խնդիրը համառոտագրել

    3 կշեռք

    առաջինի 
            ձախին - 3 սագ, 2 բադ
            աջին - 6700 գ
    
    երկրորդ 
            ձախին - 2 սագ, 3 բադ
            աջին - 7000 գ

    circumscribe 2 բադերն ու 2 սագերը ու հետո մի քիչ ձախ տանել
    circumscribe 1 բադ ու 1 սագ ու հետո մի քիչ աջ տանել

    7000-6700=300

    երրորդ
            ձախին - 1 բադ
            աջին - 1 սագ և 300 գ
    
    երկրորդ կշեռքը ֆեյդ-աութ

    երրորդ կշեռքը գալիս ա ձախ

    առաջին կշեռքում 1 բադը սաքրում ենք սագ+300
    

    2 նժարներից հանում ենք 600

    3-րդ հարց

    4-րդ հարց

'''




from io import DEFAULT_BUFFER_SIZE
from operator import add
from re import X
import sys
sys.path.append('../../../../')
from Functions.qarakusi import * 

class Problem_11159(ScalesScene):
    def construct(self):

# INIT
   # scales 1 
        
            
        goose = Goose().scale(0.8)
        duck = Duck().scale(0.8)
        sc_1 = Scales(5, 2.1).scale(0.8).shift(0.4*UP+1.5*RIGHT)

        sc_1_left_mobs = VGroup(duck.copy(), duck.copy(), goose.copy(), goose.copy(), goose.copy())
        sc_1_left_mobs.arrange(aligned_edge=DOWN, buff=0.1).next_to(sc_1.left_plate, UP, buff=0)
        sc_1_left_mobs.add_updater(lambda mobs: mobs.next_to(sc_1.left_plate, UP, buff=0))

        sc_1_right_mobs = VGroup(Weight(6700, 700))
        sc_1_right_mobs.arrange(aligned_edge=DOWN).next_to(sc_1.right_plate, UP, buff=0)
        sc_1_right_mobs.add_updater(lambda mobs: mobs.next_to(sc_1.right_plate, UP, buff=0))

        sc_1_right_mobs_2 = VGroup(Weight(6100, 750), Weight(600, 200))
        sc_1_right_mobs_2.arrange(aligned_edge=DOWN).next_to(sc_1.right_plate, UP, buff=0)
        sc_1_right_mobs_2.add_updater(lambda mobs: mobs.next_to(sc_1.right_plate, UP, buff=0))
        

    # scales 2
        sc_2 = Scales(5, 2.1).scale(0.8).shift(3*DOWN+1.5*RIGHT)

        sc_2_left_mobs = VGroup(goose.copy(), goose.copy(), duck.copy(), duck.copy(), duck.copy())
        sc_2_left_mobs.arrange(aligned_edge=DOWN, buff=0.05).next_to(sc_2.left_plate, UP, buff=0)
        sc_2_left_mobs.add_updater(lambda mobs: mobs.next_to(sc_2.left_plate, UP, buff=0))
        

        sc_2_right_mobs = VGroup(Weight(7000, 600))
        sc_2_right_mobs.arrange(aligned_edge=DOWN).next_to(sc_2.right_plate, UP, buff=0)
        sc_2_right_mobs.add_updater(lambda mobs: mobs.next_to(sc_2.right_plate, UP, buff=0))


        eq_1 = MathTex("7000 - 6700 = 300", font_size=DEFAULT_FONT_SIZE).shift(2*UR+2.5*RIGHT)
        eq_2 = MathTex("6700 - 2 \\cdot 300 = 6100", font_size=DEFAULT_FONT_SIZE).shift(4*RIGHT)
        eq_3 = MathTex("6100 : 5 = 1220", font_size=DEFAULT_FONT_SIZE).next_to(eq_2, DOWN, buff=0.5).align_to(eq_2, LEFT)
        eq_4 = MathTex("1220 + 300 = 1520", font_size=DEFAULT_FONT_SIZE).next_to(eq_3, DOWN, buff=0.5).align_to(eq_3, LEFT)
        


    # scales 3
        sc_3 = Scales(5, 1).scale(0.6).shift(4.15*RIGHT+DOWN)
        sc_3_left_mobs = duck.copy()
        sc_3_left_mobs.arrange(aligned_edge=DOWN, buff=0.1).next_to(sc_3.left_plate, UP, buff=0)
        sc_3_left_mobs.add_updater(lambda mobs: mobs.next_to(sc_3.left_plate, UP, buff=0))

        sc_3_right_mobs = VGroup(goose.copy(), Weight(300, 150))
        sc_3_right_mobs.arrange(aligned_edge=DOWN).next_to(sc_3.right_plate, UP, buff=0)
        sc_3_right_mobs.add_updater(lambda mobs: mobs.next_to(sc_3.right_plate, UP, buff=0)) 

# Given

        first = Tex("$3$ սագը", " և ", "$2$ բադը միասին", "\\\\ կշռում են $6$ կգ և $700$ գրամ").shift(3*UP+3.5*LEFT)
        second = Tex("$3$ բադը", " և ", "$2$ սագը միասին", "\\\\ կշռում են $7$ կգ").shift(DOWN)
        first[0:3].align_to(first[3], LEFT)
        second[0:3].align_to(second[3], LEFT)
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

        self.play(
                ReplacementTransform(first[0].copy(), sc_1_left_mobs[0:3]),
                ReplacementTransform(first[2].copy(), sc_1_left_mobs[3:])
        )

        self.add(sc_1_left_mobs)
        self.rotate_scales(sc_1)
        self.wait()

        self.play(FadeIn(sc_1_right_mobs))
        self.rotate_scales(sc_1, -1)
        self.wait()

        self.play(
                ReplacementTransform(second[0].copy(), sc_2_left_mobs[0:3]),
                ReplacementTransform(second[2].copy(), sc_2_left_mobs[3:])
        )
        self.add(sc_2_left_mobs)
        self.rotate_scales(sc_2)
        self.wait()

        self.play(FadeIn(sc_2_right_mobs))
        self.rotate_scales(sc_2, -1)
        self.wait()

        self.play(
                FadeOut(first),
                FadeOut(second),
                sc_1.animate.shift(3.35*LEFT),
                sc_2.animate.shift(3.35*LEFT)
        )
        self.wait()

        self.play(Circumscribe(sc_1_left_mobs[0:4]), Circumscribe(sc_2_left_mobs[0:4]))
        self.play(
                sc_1_left_mobs[0:4].animate.shift(0.1*LEFT),
                sc_2_left_mobs[0:4].animate.shift(0.1*LEFT)
        )
        self.wait()

        self.play(Circumscribe(sc_1_left_mobs[4]), Circumscribe(sc_2_left_mobs[4]))
        self.play(
                sc_1_left_mobs[4].animate.shift(0.1*RIGHT),
                sc_2_left_mobs[4].animate.shift(0.1*RIGHT)
        )
        self.wait()

        self.play(Write(eq_1))



       # Երրորդ կշեռք
        


        self.play(FadeIn(sc_3))
        self.play(FadeIn(sc_3_left_mobs))

        self.add(sc_3_right_mobs)
        sc_3_right_mobs.set_opacity(0)

        self.rotate_scales(sc_3)

        self.play(sc_3_right_mobs[0].animate.set_opacity(1))        
        

        self.rotate_scales(sc_3, -0.5)
        
        self.play(sc_3_right_mobs[1].animate.set_opacity(1))

        self.rotate_scales(sc_3, -0.5)
        self.wait()


        # Երկրորդ կշեռքը ֆեյդ աութ


        self.play(
                FadeOut(sc_2),
                FadeOut(sc_2_left_mobs),
                FadeOut(sc_2_right_mobs)
        )
        self.wait()
             
        self.play(
                sc_3.animate.shift(DL+5*LEFT),
                sc_1_left_mobs[0:4].animate.shift(0.1*RIGHT),
                sc_1_left_mobs[4].animate.shift(0.1*LEFT)
        )
        self.wait()

        sc_3_right_mobs.clear_updaters()


        # Բադը փոխարինում ենք սագ+300-ով


        self.play(
                Circumscribe(sc_1_left_mobs[0]),
                Circumscribe(sc_1_left_mobs[1]),
                Circumscribe(sc_3_left_mobs),
                Circumscribe(sc_3_right_mobs)
        )
        x = sc_3_right_mobs.copy().move_to(sc_1_left_mobs[0].get_center()+0.15*LEFT).align_to(sc_1_left_mobs[2], DOWN)
        y = sc_3_right_mobs.copy().move_to(sc_1_left_mobs[1].get_center()+0.15*RIGHT).align_to(sc_1_left_mobs[2], DOWN)
        self.play(
                ReplacementTransform(sc_1_left_mobs[0], x),
                ReplacementTransform(sc_1_left_mobs[1], y),
                sc_1_left_mobs[2:].animate.shift(0.3*RIGHT)
        )
        self.wait()


        # Երկրորդ հարց


        self.play(Write(eq_2))
        self.wait()

        # 600-նոցները հանում ենք

        self.play(ReplacementTransform(sc_1_right_mobs, sc_1_right_mobs_2))
        self.play(
                x[1].animate.shift(UP),
                y[1].animate.shift(UP),
                sc_1_right_mobs_2[1].animate.shift(UP)
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



class Problem__11159(ScalesScene):
        def construct(self):

# INIT
   # scales 1 
        
            
                goose = Goose().scale(0.8)
                duck = Duck().scale(0.8)
                sc_1 = Scales(5, 2.2).scale(0.9).shift(UP)

                sc_1_left_mobs = VGroup(duck.copy(), duck.copy(), goose.copy(), goose.copy(), goose.copy())
                sc_1_left_mobs.arrange(aligned_edge=DOWN, buff=0.2).next_to(sc_1.left_plate, UP, buff=0)

                sc_1_right_mobs = VGroup(Weight(6700, 700))
                sc_1_right_mobs.arrange(aligned_edge=DOWN).next_to(sc_1.right_plate, UP, buff=0)


        # scales 2
                sc_2 = Scales(5, 2.2).scale(0.9).shift(2*DOWN)

                sc_2_left_mobs = VGroup(goose.copy(), goose.copy(), duck.copy(), duck.copy(), duck.copy())
                sc_2_left_mobs.arrange(aligned_edge=DOWN, buff=0.2).next_to(sc_2.left_plate, UP, buff=0)
                sc_2_left_mobs.add_updater(lambda mobs: mobs.next_to(sc_2.left_plate, UP, buff=0))
                

                sc_2_right_mobs = VGroup(Weight(7000, 600))
                sc_2_right_mobs.arrange(aligned_edge=DOWN).next_to(sc_2.right_plate, UP, buff=0)

                sc_2_right_mobs_2 = VGroup(Weight(7000, 600), Weight(6700, 700))
                sc_2_right_mobs_2.arrange(aligned_edge=DOWN).next_to(sc_2.right_plate, UP, buff=0)

                sc_2_right_mobs_3 = Weight(13700, 400).next_to(sc_2.right_plate, UP, buff=0)

        # scales 3
                sc_3 = Scales(5, 1).scale(0.6).shift(UL)
                
                sc_3_left_mobs = VGroup(duck.copy(), goose.copy())
                sc_3_left_mobs.arrange(aligned_edge=DOWN, buff=0.1).next_to(sc_3.left_plate, UP, buff=0)
                sc_3_left_mobs.add_updater(lambda mobs: mobs.next_to(sc_3.left_plate, UP, buff=0))

                sc_3_right_mobs = VGroup(Weight(2720, 300))
                sc_3_right_mobs.arrange(aligned_edge=DOWN, buff=0.1).next_to(sc_3.right_plate, UP, buff=0)
                sc_3_right_mobs.add_updater(lambda mobs: mobs.next_to(sc_3.right_plate, UP, buff=0))


        # Equations
                eq_1 = MathTex("7000+6700=13700").shift(3*UR+RIGHT)
                eq_2 = MathTex("13700 : 5 = 2740").next_to(eq_1, DOWN, buff=0.3)





# ANIMATIONS

        # scales

                self.add(
                        sc_1, sc_1_left_mobs, sc_1_right_mobs,
                        sc_2, sc_2_left_mobs, sc_2_right_mobs
                )

                self.play(
                        Circumscribe(sc_1_left_mobs),
                        Circumscribe(sc_2_left_mobs)
                )
                self.wait()

                

                self.play(
                        sc_1_left_mobs[0].animate.next_to(sc_2_left_mobs[0], UP, buff=0.15),
                        sc_1_left_mobs[1].animate.next_to(sc_2_left_mobs[1], UP, buff=0.15),
                        sc_1_left_mobs[2].animate.next_to(sc_2_left_mobs[2], UP, buff=0.15),
                        sc_1_left_mobs[3].animate.next_to(sc_2_left_mobs[3], UP, buff=0.15),
                        sc_1_left_mobs[4].animate.next_to(sc_2_left_mobs[4], UP, buff=0.15),
                        sc_2_right_mobs.animate.move_to(sc_2_right_mobs_2[0]),
                        sc_1_right_mobs.animate.move_to(sc_2_right_mobs_2[1]),
                        FadeOut(sc_1)
                )
                self.wait()

                self.add(sc_2_right_mobs_2)
                self.remove(sc_1_right_mobs, sc_2_right_mobs)

                sc_1_left_mobs[0].add_updater(lambda mob: mob.next_to(sc_2_left_mobs[0], UP, buff=0.15))
                sc_1_left_mobs[1].add_updater(lambda mob: mob.next_to(sc_2_left_mobs[1], UP, buff=0.15))
                sc_1_left_mobs[2].add_updater(lambda mob: mob.next_to(sc_2_left_mobs[2], UP, buff=0.15))
                sc_1_left_mobs[3].add_updater(lambda mob: mob.next_to(sc_2_left_mobs[3], UP, buff=0.15))
                sc_1_left_mobs[4].add_updater(lambda mob: mob.next_to(sc_2_left_mobs[4], UP, buff=0.15))

                self.play(Write(eq_1))
                self.wait()

                self.play(ReplacementTransform(sc_2_right_mobs_2, sc_2_right_mobs_3))
                self.wait()

                self.play(sc_2_left_mobs.animate.arrange(aligned_edge=DOWN, buff=0.4).next_to(sc_2.left_plate, UP, buff=0))
                self.wait()

                self.play(Write(eq_2))
                self.wait()

                self.play(FadeIn(sc_3))
                self.play(
                        sc_1_left_mobs[0].copy().animate.move_to(sc_3_left_mobs[0]),
                        sc_2_left_mobs[0].copy().animate.move_to(sc_3_left_mobs[1]),
                        FadeIn(sc_3_right_mobs)
                )
                self.wait()


