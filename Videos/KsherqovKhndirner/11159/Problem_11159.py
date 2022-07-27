"""
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

"""


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
        eq_2 = MathTex("6700 - 600 = 6100", font_size=DEFAULT_FONT_SIZE).shift([4, 1, 0]).align_to(eq_1, LEFT)
        eq_3 = MathTex("6100 : 5 = 1220", font_size=DEFAULT_FONT_SIZE).next_to(eq_2, DOWN, buff=0.5).align_to(eq_2, LEFT)
        eq_4 = MathTex("1220 + 300 = 1520", font_size=DEFAULT_FONT_SIZE).next_to(eq_3, DOWN, buff=0.5).align_to(eq_3, LEFT)
        

    


    # scales 3
        sc_3 = Scales(5, 1.2).scale(0.5).shift(4.15 * RIGHT + 0.5 * DOWN)

        sc_3_left_mobs = duck.copy()
        sc_3_left_mobs.arrange(aligned_edge=DOWN, buff=0.1).next_to(sc_3.left_plate, UP, buff=0)
        sc_3_left_mobs.add_updater(lambda mobs: mobs.next_to(sc_3.left_plate, UP, buff=0))

        sc_3_right_mobs = VGroup(goose.copy(), Weight(300, 150))
        sc_3_right_mobs.arrange(aligned_edge=DOWN).next_to(sc_3.right_plate, UP, buff=0)
        sc_3_right_mobs.add_updater(lambda mobs: mobs.next_to(sc_3.right_plate, UP, buff=0)) 

    # Given

        first = Tex("$3$ սագը", " և ", "$2$ բադը", " միասին", " կշռում են ", "$6700$ գ", font_size=DEFAULT_FONT_SIZE)
        first.shift(3 * UP + 1.85 * LEFT)
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
        self.play(x.animate.move_to(sc_1_geese))
        self.play(ReplacementTransform(x, sc_1_geese))
        self.rotate_scales(sc_1, 0.4)
        self.wait()


        y = first[2].copy()
        self.play(y.animate.move_to(sc_1_ducks.get_center() - np.array([0, 0.25, 0])))
        self.play(ReplacementTransform(y, sc_1_ducks))
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
            sc_1.animate.shift(2.35 * LEFT + 0.5 * UP),
            sc_2.animate.shift(2.35 * LEFT)
        )
        self.wait()

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


    # Սագը փոխարինում ենք սագով

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

        self.play(sc_1_left_mobs.animate.shift(0.0001 * UP))
        self.add(goose, sc_1_birds)
        self.remove(sc_1_left_mobs)

        self.play(goose.animate.shift(UP))
        self.play(goose.animate.shift(0.8 * RIGHT).set_opacity(0.5))
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

        self.play(
            goose.animate.shift(0.8 * LEFT +DOWN).set_opacity(1),
            FadeOut(duck, kshraqar)
        )
        self.wait()

        self.play(sc_1_left_mobs.animate.shift(0.0001 * DOWN))
        self.add(sc_1_left_mobs)
        self.remove(goose, sc_1_birds)


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


        self.play(Write(eq_2))
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

"""
Երկրորդ լուծում

1․  ունենք 2 կշեռք
    առաջին կշեռքի ամեն ինչը բերում ենք 2-րդ կշեռքի վրա, ու առաջին կշեռքը անհետացնում

2․  աջ կողմում հաշվում ենք գումարային զանգվածը
    հետո ձախ նժարը բաժանում ենք 5 միանման խմբերի

3․  ստանում ենք որ 1 խմբի զանգվածը 2740 է, ու այն պատկերում ենք 3-րդ կշեռքի վրա

4․  հետո վերադառնում ենք առաջին կշեռքին, ունենալով 2 խումբ և 1 սագ
    խմբերը փոխարինում ենք կշռաքարերով, կրճատում ենք կշեռքի վրա, ու ստանում սագի քաշը

5․  ստանում ենք բադի քաշը
"""


class Problem11159_SecondSolution(ScalesScene):
    def construct(self):

# INIT
    # scales 1 
    
        
        goose = Goose().scale(0.8)
        duck = Duck().scale(0.8)
        sc_1 = Scales(5, 2.2).scale(0.8).shift(UP)

        sc_1_left_mobs = VGroup(duck.copy(), duck.copy(), goose.copy(), goose.copy(), goose.copy())
        sc_1_left_mobs.arrange(aligned_edge=DOWN, buff=0.3).next_to(sc_1.left_plate, UP, buff=0)

        sc_1_right_mobs = VGroup(Weight(6700, 700))
        sc_1_right_mobs.arrange(aligned_edge=DOWN).next_to(sc_1.right_plate, UP, buff=0)


    # scales 2
        sc_2 = Scales(5, 2.2).scale(0.8).shift(2.5*DOWN)

        sc_2_left_mobs = VGroup(goose.copy(), goose.copy(), duck.copy(), duck.copy(), duck.copy())
        sc_2_left_mobs.arrange(aligned_edge=DOWN, buff=0.3).next_to(sc_2.left_plate, UP, buff=0)
        sc_2_left_mobs.add_updater(lambda mobs: mobs.next_to(sc_2.left_plate, UP, buff=0))
        

        sc_2_right_mobs = VGroup(Weight(7000, 600))
        sc_2_right_mobs.arrange(aligned_edge=DOWN).next_to(sc_2.right_plate, UP, buff=0)

        sc_2_right_mobs_2 = VGroup(Weight(7000, 600), Weight(6700, 700))
        sc_2_right_mobs_2.arrange(aligned_edge=DOWN).next_to(sc_2.right_plate, UP, buff=0)

        sc_2_right_mobs_3 = Weight(13700, 400).next_to(sc_2.right_plate, UP, buff=0)

        sc_2_right_mobs_4 = VGroup(Weight(2740, 300), Weight(2740, 300), Weight(2740, 300), Weight(2740, 300), Weight(2740, 300))
        sc_2_right_mobs_4.arrange(aligned_edge=DOWN).next_to(sc_2.right_plate, UP, buff=0)

    # scales 3
        sc_3 = Scales(5, 1).scale(0.6).shift(1.5*UL+0.5*LEFT)
        
        sc_3_left_mobs = VGroup(duck.copy(), goose.copy())
        sc_3_left_mobs.arrange(aligned_edge=DOWN, buff=0.1).next_to(sc_3.left_plate, UP, buff=0)
        sc_3_left_mobs.add_updater(lambda mobs: mobs.next_to(sc_3.left_plate, UP, buff=0))

        sc_3_right_mobs = VGroup(Weight(2740, 300))
        sc_3_right_mobs.arrange(aligned_edge=DOWN, buff=0.1).next_to(sc_3.right_plate, UP, buff=0)
        sc_3_right_mobs.add_updater(lambda mobs: mobs.next_to(sc_3.right_plate, UP, buff=0))

        sc_3_left_mobs_1 = VGroup(duck.copy(), Weight(1220, 300))
        sc_3_left_mobs_1.arrange(aligned_edge=DOWN, buff=0.1).next_to(sc_3.left_plate, UP, buff=0)
        sc_3_left_mobs_1.add_updater(lambda mobs: mobs.next_to(sc_3.left_plate, UP, buff=0))

        sc_3_right_mobs_1 = VGroup(Weight(1220, 300), Weight(1520, 300))
        sc_3_right_mobs_1.arrange(aligned_edge=DOWN, buff=0.1).next_to(sc_3.right_plate, UP, buff=0)
        sc_3_right_mobs_1.add_updater(lambda mobs: mobs.next_to(sc_3.right_plate, UP, buff=0))

    # scales 4 
        sc_4 = Scales(5, 2.2).scale(0.8).shift(2.5*DOWN)

        sc_4_left_mobs = VGroup(duck.copy(), duck.copy(), goose.copy(), goose.copy(), goose.copy())
        sc_4_left_mobs.arrange(aligned_edge=DOWN, buff=0.4).next_to(sc_4.left_plate, UP, buff=0)

        sc_4_right_mobs = VGroup(Weight(6700, 700))
        sc_4_right_mobs.arrange(aligned_edge=DOWN).next_to(sc_4.right_plate, UP, buff=0)

        sc_4_left_mobs_1 = VGroup(Weight(2740, 300), Weight(2740, 300), goose.copy())
        sc_4_left_mobs_1.arrange(aligned_edge=DOWN, buff=0.4).next_to(sc_4.left_plate, UP, buff=0)

        sc_4_right_mobs_1 = VGroup(Weight(2740, 300), Weight(3960, 300))
        sc_4_right_mobs_1.arrange(aligned_edge=DOWN, buff=0.4).next_to(sc_4.right_plate, UP, buff=0)

        sc_4_right_mobs_2 = VGroup(Weight(2740, 300), Weight(1220, 300))
        sc_4_right_mobs_2.arrange(aligned_edge=DOWN, buff=0.4).next_to(sc_4.right_plate, UP, buff=0)




    # Equations
        eq_1 = MathTex("7000 + 6700 = 13700").shift(3*UR+RIGHT)
        eq_2 = MathTex("13700 : 5 = 2740").next_to(eq_1, DOWN, buff=0.3)
        eq_3 = Tex("Սագ - $1220$ գ").next_to(eq_2, DOWN, buff=1)
        eq_4 = Tex("Բադ - $1520$ գ").next_to(eq_3, DOWN, buff=0.5)

        ans_box = SurroundingRectangle(VGroup(eq_3, eq_4), color=GREEN)





# ANIMATIONS

    # scales

        self.add(
            sc_1, sc_1_left_mobs, sc_1_right_mobs,
            sc_2, sc_2_left_mobs, sc_2_right_mobs
        )
        self.wait()

        self.play(
            Circumscribe(sc_1_left_mobs),
            Circumscribe(sc_2_left_mobs)
        )
        self.wait()

        
    # առաջին կշեռքն անհետանում է

        self.play(
            sc_1_left_mobs[0].animate.next_to(sc_2_left_mobs[0], UP, buff=0.1),
            sc_1_left_mobs[1].animate.next_to(sc_2_left_mobs[1], UP, buff=0.1),
            sc_1_left_mobs[2].animate.next_to(sc_2_left_mobs[2], UP, buff=0.1),
            sc_1_left_mobs[3].animate.next_to(sc_2_left_mobs[3], UP, buff=0.1),
            sc_1_left_mobs[4].animate.next_to(sc_2_left_mobs[4], UP, buff=0.1),
            sc_2_right_mobs.animate.move_to(sc_2_right_mobs_2[0]),
            sc_1_right_mobs.animate.move_to(sc_2_right_mobs_2[1]),
            FadeOut(sc_1)
        )
        self.wait()

        self.add(sc_2_right_mobs_2)
        self.remove(sc_1_right_mobs, sc_2_right_mobs)

        sc_1_left_mobs[0].add_updater(lambda mob: mob.next_to(sc_2_left_mobs[0], UP, buff=0.1))
        sc_1_left_mobs[1].add_updater(lambda mob: mob.next_to(sc_2_left_mobs[1], UP, buff=0.1))
        sc_1_left_mobs[2].add_updater(lambda mob: mob.next_to(sc_2_left_mobs[2], UP, buff=0.1))
        sc_1_left_mobs[3].add_updater(lambda mob: mob.next_to(sc_2_left_mobs[3], UP, buff=0.1))
        sc_1_left_mobs[4].add_updater(lambda mob: mob.next_to(sc_2_left_mobs[4], UP, buff=0.1))


    # առաջին հարց և կշռաքարերի համապատասխան միավորում

        self.play(Write(eq_1))
        self.wait()

        self.play(ReplacementTransform(sc_2_right_mobs_2, sc_2_right_mobs_3))
        self.wait()

    # Ձախ նժարի վրա 5 խմբերի առանձնացում

        self.play(sc_2_left_mobs.animate.arrange(aligned_edge=DOWN, buff=0.5).next_to(sc_2.left_plate, UP, buff=0))
        self.wait()

# INIT
    # boxes
        box_0 = SurroundingRectangle(VGroup(sc_1_left_mobs[0], sc_2_left_mobs[0]), color=ORANGE, corner_radius=0.3, buff=0.05)
        box_1 = SurroundingRectangle(VGroup(sc_1_left_mobs[1], sc_2_left_mobs[1]), color=ORANGE, corner_radius=0.3, buff=0.05)
        box_2 = SurroundingRectangle(VGroup(sc_1_left_mobs[2], sc_2_left_mobs[2]), color=ORANGE, corner_radius=0.3, buff=0.05)
        box_3 = SurroundingRectangle(VGroup(sc_1_left_mobs[3], sc_2_left_mobs[3]), color=ORANGE, corner_radius=0.3, buff=0.05)
        box_4 = SurroundingRectangle(VGroup(sc_1_left_mobs[4], sc_2_left_mobs[4]), color=ORANGE, corner_radius=0.3, buff=0.05)
        box_5 = SurroundingRectangle(sc_3_left_mobs, color=ORANGE, corner_radius=0.3)

###

        self.play(
            Create(box_0),
            Create(box_1),
            Create(box_2),
            Create(box_3),
            Create(box_4)
        )
        self.wait()

        sc_1_left_mobs[0].clear_updaters()

        self.play(Write(eq_2))
        self.wait()

    # Երրորդ կշեռք
        
        self.play(ReplacementTransform(sc_2_right_mobs_3, sc_2_right_mobs_4))
        self.wait()

        self.play(FadeIn(sc_3))
        x = sc_1_left_mobs[0].copy()
        y = sc_2_left_mobs[0].copy()
        z = box_0.copy()
        t = sc_2_right_mobs_4[0].copy()
        self.play(
            x.animate.move_to(sc_3_left_mobs[0]),
            y.animate.move_to(sc_3_left_mobs[1]),
            Transform(z, box_5),
            t.animate.move_to(sc_3_right_mobs)
        )
        self.add(sc_3_left_mobs, sc_3_right_mobs, box_5)
        self.remove(x, y, z, t) # ֆսյո, էս x, y, z, t-ները էլ չկան, եթե ինչ
        self.wait()

        self.play(FadeOut(box_5))
        self.wait()



    # Չորրորդ (Առաջին) կշեռք

        self.play(
            FadeOut(sc_2),
            FadeOut(sc_2_left_mobs),
            FadeOut(sc_2_right_mobs_4),
            FadeOut(box_0),
            FadeOut(box_1),
            FadeOut(box_2),
            FadeOut(box_3),
            FadeOut(box_4),
            FadeOut(sc_1_left_mobs)
        )
        self.wait()

        self.play(
            FadeIn(sc_4),
            FadeIn(sc_4_left_mobs),
            FadeIn(sc_4_right_mobs)
        )
        self.wait()

        self.play(
            sc_4_left_mobs[1].animate.next_to(sc_4_left_mobs[3], LEFT, buff=0.4).align_to(sc_4_left_mobs[3], DOWN),
            sc_4_left_mobs[2].animate.next_to(sc_4_left_mobs[0], RIGHT, buff=0.4).align_to(sc_4_left_mobs[0], DOWN)
        )
        self.wait()

# INIT
    # box
        box_6 = SurroundingRectangle(VGroup(sc_4_left_mobs[0], sc_4_left_mobs[2]), color=ORANGE, corner_radius=0.3)
        box_7 = SurroundingRectangle(VGroup(sc_4_left_mobs[1], sc_4_left_mobs[3]), color=ORANGE, corner_radius=0.3)

###
        self.play(
            Create(box_6),
            Create(box_7)
        )
        self.wait()


    # Խմբերի փոխարինում կշռաքարերով
        
        self.play(ReplacementTransform(VGroup(box_6, sc_4_left_mobs[0], sc_4_left_mobs[2]), sc_4_left_mobs_1[0]))
        self.wait()

        self.play(ReplacementTransform(VGroup(box_7, sc_4_left_mobs[1], sc_4_left_mobs[3]), sc_4_left_mobs_1[1]))
        self.wait()

        self.play(sc_4_left_mobs[4].animate.move_to(sc_4_left_mobs_1[2]))
        self.add(sc_4_left_mobs_1[2])
        self.remove(sc_4_left_mobs[4])
        self.wait()

        self.play(ReplacementTransform(sc_4_right_mobs, sc_4_right_mobs_1))
        self.wait()


    # կշռաքարերի կրճատում

        self.play(
            sc_4_left_mobs_1[0].animate.shift(UP),
            sc_4_right_mobs_1[0].animate.shift(UP)
        )
        self.wait()

        self.play(
            FadeOut(sc_4_left_mobs_1[0]),
            FadeOut(sc_4_right_mobs_1[0])
        )
        self.wait()

        self.play(ReplacementTransform(sc_4_right_mobs_1[1], sc_4_right_mobs_2))
        self.wait()

        self.play(
            sc_4_left_mobs_1[1].animate.shift(UP),
            sc_4_right_mobs_2[0].animate.shift(UP)
        )
        self.wait()

        self.play(
            FadeOut(sc_4_left_mobs_1[1]),
            FadeOut(sc_4_right_mobs_2[0])
        )
        self.wait()

        self.play(
            sc_4_left_mobs_1[2].animate.next_to(sc_4.left_plate, UP, buff=0),
            sc_4_right_mobs_2[1].animate.next_to(sc_4.right_plate, UP, buff=0)
        )
        self.wait()

    # Սագի կշիռ
        
        self.play(Circumscribe(sc_4_left_mobs_1[2], Circle))
        self.wait()

        self.play(Circumscribe(sc_4_right_mobs_2[1], Circle))
        self.wait()

        self.play(Write(eq_3))
        self.wait()

    # Բադի կշիռ
        
        self.play(sc_3.animate.shift(0.5*DOWN))
        self.wait()

        self.play(Circumscribe(sc_3_left_mobs, Circle, time_width=2))
        self.wait()

        self.play(Circumscribe(sc_3_right_mobs, Circle, time_width=2))
        self.wait()

        self.play(ReplacementTransform(sc_3_right_mobs, sc_3_right_mobs_1))
        self.wait()

        sc_3_left_mobs.clear_updaters()
        sc_3_right_mobs_1.clear_updaters()

        self.play(
            sc_3_left_mobs[1].animate.shift(UP),
            sc_3_right_mobs_1[0].animate.shift(UP)
        )
        self.wait()

        self.play(
            FadeOut(sc_3_left_mobs[1]),
            FadeOut(sc_3_right_mobs_1[0])
        )
        self.wait()

        self.play(
            sc_3_left_mobs[0].animate.next_to(sc_3.left_plate, UP, buff=0),
            sc_3_right_mobs_1[1].animate.next_to(sc_3.right_plate, UP, buff=0)
        )
        self.wait()

        self.play(Write(eq_4))
        self.wait()

        self.play(Create(ans_box))
        self.wait()



