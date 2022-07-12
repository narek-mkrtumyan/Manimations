import sys

sys.path.append('../../')
from Functions.qarakusi import *

class Problem12510(Scene):

    
    def construct(self):

#INITS
        Prob = Tex("$1$–ից $2n$ բնական թվերից ընտրել են որևէ $n+1$ հատը: "
                   "Ապացուցել, որ ընտրած թվերից որևէ երկուսը կլինեն փոխադարձաբար պարզ:",
                   tex_template=armenian_tex_template, font_size=30).shift(3*UP)
        Numbers = MathTex("1", ", \ ", "2", ", \ ", "3", ", \ ", 
                          "\\dots", "2n-2", ", \ ", "2n-1", ", \ ", "2n").shift(2*UP+2*LEFT)
        Final_nums = MathTex("3", ", \ ", "\\dots \ ", "n", ", \ ", "n+1", ", \ ", "\\dots \ ", "2n-2").shift(2*UL)
        Final_nums_copy = Final_nums.copy()

        plus = MathTex("+").shift(2*LEFT)
        special_number = MathTex("=","2n+1")
        special_number[1].set_color(GREEN)
        comma = MathTex(",").shift(2*LEFT+0.19*DOWN)

        left_bracket1 = MathTex("(")
        right_bracket1 = MathTex(")")
        comma_copy1 = comma.copy()

        left_bracket2 = MathTex("(")
        right_bracket2 = MathTex(")")
        comma_copy2 = comma.copy()

        left_bracket3 = MathTex("(")
        right_bracket3 = MathTex(")")
        comma_copy3 = comma.copy()

        left_bracket4 = MathTex("(")
        right_bracket4 = MathTex(")")
        comma_copy4 = comma.copy()

        pairs_color = ORANGE
        mid_nums = VGroup(Numbers[4:8])
        vdots = MathTex("\\vdots").set_color(ORANGE).shift(3*RIGHT)

        cage1 = Cage().scale(0.3)
        cage2 = Cage().scale(0.3)
        cage3 = Cage().scale(0.3)
        cage4 = Cage().scale(0.3)
        cages = VGroup(cage1, cage2, cage3, cage4)

        rabbits = VGroup(*[Rabbit() for i in range(5)]).arrange(DOWN, buff=1).scale(0.4).shift(UR).shift(0.5*UP)
        rabbits[3].shift(DOWN)
        rabbits[4].shift(DOWN)
        rdots = MathTex("\\vdots")
        rdots.move_to((rabbits[2].get_center()+rabbits[3].get_center())/2)

        rabbits_brace = Brace(rabbits, LEFT)
        number_of_rabbits = MathTex("n+1").next_to(rabbits_brace, LEFT)


        

#Խնդրի ձևակերպում
        self.play(Write(Prob), run_time=5)
        self.wait(3)

#Ներածական մաս
        self.play(Write(Numbers), run_time=4)
        self.play(FadeOut(Prob))
        


#Զույգերի տրոհում
        self.play(
            Circumscribe(Numbers[0], color=GREEN, run_time=1.2),
            Circumscribe(Numbers[11], color=GREEN), run_time=1.2
        )

        self.play(
            Numbers[0].animate.next_to(plus, LEFT*0.5), 
            Numbers[11].animate.next_to(plus, RIGHT*0.5),
            FadeOut(Numbers[1], Numbers[10]), run_time=2
        )
        self.play(Write(plus))
        self.play(Write(special_number.next_to(Numbers[11], RIGHT), run_time=1.5), run_time=1)
        self.play(FadeOut(plus, special_number))
        self.play(
            Write(comma),
            Numbers[0].animate.shift(0.1*RIGHT),
            Numbers[11].animate.shift(0.1*LEFT)
        )
        self.play(
            Write(left_bracket1.next_to(Numbers[0], 0.3*LEFT)),
            Write(right_bracket1.next_to(Numbers[11], RIGHT*0.3))
        )
        self.remove(comma)
#init
        pair1 = VGroup(Numbers[0], Numbers[11], left_bracket1, right_bracket1, comma_copy1)
        self.play(pair1.animate.set_fill(pairs_color).shift(5*RIGHT+3*UP), run_time=2)



        self.play(
            Circumscribe(Numbers[2], color=GREEN, run_time=1.2),
            Circumscribe(Numbers[9], color=GREEN, run_time=1.2)
        )

        self.play(
            Numbers[2].animate.next_to(plus, LEFT*0.5), 
            Numbers[9].animate.next_to(plus, RIGHT*0.5),
            FadeOut(Numbers[3], Numbers[8])
        )
        self.play(Write(plus))
        self.play(Write(special_number.next_to(Numbers[9], RIGHT)), run_time=1)
        self.play(FadeOut(plus, special_number))
        self.play(Write(comma_copy2),
                  Numbers[2].animate.shift(0.1*RIGHT),
                  Numbers[9].animate.shift(0.1*LEFT))
        self.play(Write(left_bracket2.next_to(Numbers[2], 0.3*LEFT)),
                  Write(right_bracket2.next_to(Numbers[9], RIGHT*0.3)))
#init
        pair2 = VGroup(Numbers[2], Numbers[9], left_bracket2, right_bracket2, comma_copy2)
        self.play(pair2.animate.set_fill(pairs_color).shift(5*RIGHT+2*UP))
 
        
        self.play(Transform(mid_nums, Final_nums), run_time=2)
        self.add(Final_nums_copy)
        self.remove(mid_nums)


        
        self.play(Circumscribe(Final_nums_copy[0], color=GREEN, run_time=1.2),
                  Circumscribe(Final_nums_copy[8], color=GREEN, run_time=1.2))

        self.play(Final_nums_copy[0].animate.next_to(plus, LEFT*0.5), 
                  Final_nums_copy[8].animate.next_to(plus, RIGHT*0.5),
                  FadeOut(Final_nums_copy[1]))
        self.play(Write(plus))
        self.play(Write(special_number.next_to(Final_nums_copy[8], RIGHT)), run_time=1)
        self.play(FadeOut(plus, special_number))
        self.play(
            Write(comma),
            Final_nums_copy[0].animate.shift(0.1*RIGHT),
            Final_nums_copy[8].animate.shift(0.1*LEFT)
        )
        self.play(
            Write(left_bracket3.next_to(Final_nums_copy[0], 0.3*LEFT)),
            Write(right_bracket3.next_to(Final_nums_copy[8], RIGHT*0.3))
        )
        self.remove(comma)
#init
        pair3 = VGroup(Final_nums_copy[0], Final_nums_copy[8], left_bracket3, right_bracket3, comma_copy3)
        self.play(pair3.animate.set_fill(pairs_color).shift(5*RIGHT+UP))


        self.play(
            ApplyWave(
                Final_nums_copy[2],
                time_width=2,
                amplitude=0.2,
                wave_func=linear,
                run_time=1.5), 
            ApplyWave(
                Final_nums_copy[7],
                time_width=2,
                amplitude=0.2,
                wave_func=linear,
                run_time=1.5)
        )
        
        self.play(
            Circumscribe(Final_nums_copy[3], color=GREEN, run_time=1.2),
            Circumscribe(Final_nums_copy[5], color=GREEN, run_time=1.2)
        )
        self.play(
            Final_nums_copy[3].animate.next_to(plus, LEFT*0.5), 
            Final_nums_copy[5].animate.next_to(plus, RIGHT*0.5),
            FadeOut(Final_nums_copy[2],Final_nums_copy[4], Final_nums_copy[6], Final_nums_copy[7])
        )
        self.play(Write(plus))
        self.play(Write(special_number.next_to(Final_nums_copy[5], RIGHT)), run_time=1)
        self.play(FadeOut(plus, special_number))
        self.play(
            Write(comma_copy4),
            Final_nums_copy[3].animate.shift(0.1*RIGHT),
            Final_nums_copy[5].animate.shift(0.1*LEFT)
        )
        self.play(
            Write(left_bracket4.next_to(Final_nums_copy[3], 0.3*LEFT)),
            Write(right_bracket4.next_to(Final_nums_copy[5], RIGHT*0.3))
        )
#init
        pair4 = VGroup(Final_nums_copy[3], Final_nums_copy[5], left_bracket4, right_bracket4, comma_copy4)
        self.play(
            pair4.animate.set_fill(pairs_color).shift(5.05*RIGHT+DOWN),
            Write(vdots)
        )
#init
        pairs = VGroup(pair1, pair2, pair3, pair4)
        pair_brace = Brace(pairs, RIGHT)
        number_of_pairs = MathTex("n").next_to(pair_brace, RIGHT)
        vdots_copy = vdots.copy().shift(RIGHT)

        self.play(Write(pair_brace))
        self.play(Write(number_of_pairs))
                  
        
#RABBITS VS CAGES
        cage1.move_to(pair1).shift(0.2*LEFT+RIGHT)
        cage2.move_to(pair2).shift(0.57*LEFT+RIGHT)
        cage3.move_to(pair3).shift(0.554*LEFT+RIGHT)
        cage4.move_to(pair4).shift(0.45*LEFT+RIGHT)
        

        self.play(
            ReplacementTransform(pair1, cage1), 
            ReplacementTransform(pair2, cage2),
            ReplacementTransform(pair3, cage3),
            ReplacementTransform(pair4, cage4),
            ReplacementTransform(vdots, vdots_copy)
        )
        self.play(Create(rabbits), Write(rdots))
        self.play(Write(rabbits_brace))
        self.play(Write(number_of_rabbits))









        



class test1(Scene):
        def construct(self):
            a = MathTex("1, \ ", "4 \ ", "5 \ ", "x")
            b = MathTex("2").next_to(a, RIGHT)
            c = VGroup(a[0:3], b)
            d = MathTex("(1, \ 2)")
            self.add(a, b)
            self.wait()
            self.play(Transform(c, d))
            self.remove(c)
            self.play(d.animate.shift(DOWN))



class test2(Scene):
        def construct(self):
            T = MathTex('\\dots')
            self.add(T)
            self.wait()
            self.play(ApplyWave(T,
                      time_width=1.5,
                      amplitude=0.2,
                      wave_func=linear,
                      ripples=2,
                      run_time=3))

class test3(Scene):
        def construct(self):
            t = MathTex("11111")
            self.add(t)
            self.play(Circumscribe(t, color=PURE_GREEN))


class test4(Scene):
        def construct(self):
            cages = VGroup(*[Cage() for i in range(4)]).arrange(buff=0.75).scale(0.3)
            nums = VGroup(*[MathTex("i") for i in range(4)]).arrange(buff=0.75)
            self.play(Create(nums))
            self.play(Transform(nums, cages))

class test5(Scene):
        def construct(self):
            cages = VGroup(*[Cage() for i in range(4)]).arrange(buff=0.75).scale(0.3)
            self.add(cages)   
            #brace = Brace(cages)
            self.add(Brace(cages))