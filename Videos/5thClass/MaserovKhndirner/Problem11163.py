from ctypes.wintypes import DWORD
from gc import get_stats
from lib2to3.pgen2.token import RIGHTSHIFT
import sys
sys.path.append('../../../')
from Functions.QarakusiFunctions import *




##   ԷՍ ԱՌԱՋԻՆԸ ՀԵՉ ՀԼԸ ՈՐ

class Problem11163(Scene):
    def construct(self):
#INIT
        
        #all_seg = Segment([-3,3,0], [3,3,0])
        

        
        paper1 = Paper().paper_2.move_to(5*LEFT).scale(0.6)
        plus = MathTex(r"+").next_to(paper1, RIGHT, buff=1.2)
        paper2 = Paper().paper_3.next_to(plus, RIGHT, buff=0.5).scale(0.6)
        equal = MathTex(r'=').next_to(paper2, RIGHT)
        paper3 = Paper().paper_1.next_to(equal, RIGHT, buff=0.5).scale(0.6)

        first_half = MathTex(r"\frac{1}{3} ", r"\textrm{մաս}", tex_template=armenian_tex_template).next_to(paper1, DOWN)
        second_half = MathTex("10").next_to(paper2, DOWN)
        together = MathTex(r'\frac{1}{2} ', r'\textrm{մաս}', tex_template=armenian_tex_template).next_to(paper3, DOWN)

        first_seg = Segment([0, 0, 0], [3, 0, 0]).move_to(paper1)
        second_seg = Segment([0, 0, 0], [1.5, 0, 0]).move_to(paper2).set_color(ORANGE)
        a = VGroup(first_seg, second_seg)
        third_seg = Segment([0, 0, 0], [4.5, 0, 0]).move_to(paper3)

        brace_1 = Brace(first_seg, UP)
        

        



        
        

        

#ANIMATION

        self.play(FadeIn(paper1))
        self.play(Write(first_half))
        self.play(FadeIn(paper2))
        self.play(Write(second_half))
        self.play(Write(plus))
        self.play(Write(equal))
        self.play(FadeIn(paper3))
        self.play(Write(together))
        # self.play(
        #     ReplacementTransform(paper1, first_seg),
        #     ReplacementTransform(paper2, second_seg),
        #     ReplacementTransform(paper3, third_seg)
        # )
        self.play(
            second_seg.animate.move_to(first_seg.get_center()+2.25*RIGHT),
            FadeOut(plus, equal),
        )
        self.play(Write(brace_1))
        self.play(
            first_half[0].animate.next_to(brace_1, UP*0.5),
            FadeOut(first_half[1])
        )
        self.play(
            second_half.animate.next_to(second_seg, UP*0.5).set_color(ORANGE)
            #second_half.animate.set_color(ORANGE)
        )

        self.play(third_seg.animate.move_to(first_seg.get_center()+2.5*DOWN+0.75*RIGHT))
        brace_3 = Brace(third_seg, DOWN)
        self.play(Write(brace_3))
        self.play(
            together[0].animate.next_to(brace_3, DOWN*0.5),
            FadeOut(together[1])
        )
        a = DashedLine(first_seg.get_center()+1.5*LEFT, third_seg.get_center()+2.25*LEFT)
        b = DashedLine(first_seg.get_center()+1.5*RIGHT, third_seg.get_center()+0.75*RIGHT)
        self.play(
            Create(a),
            Create(b)
        )
        first_seg_2 = Segment(third_seg.get_center()+2.25*LEFT, third_seg.get_center()+0.75*RIGHT)
        self.play(FadeIn(first_seg_2))
        brace_2 = Brace(first_seg_2, UP)
        x = MathTex(r'\frac{1}{3}').next_to(brace_2, 0.5*UP)
        self.play(Write(brace_2))
        self.play(Write(x))
        seg = Segment(third_seg.get_center()+0.75*RIGHT, third_seg.get_center()+2.25*RIGHT)
        brace_4 = Brace(seg, UP)
        y = MathTex(r'?').next_to(brace_4, 0.5*UP)
        self.play(Write(brace_4))
        self.play(Write(y))

        self.play(together[0].animate.move_to([1,1,0]))


        minus = MathTex(r'-').next_to(together[0], RIGHT)
        self.play(Write(minus))
        self.play(x.animate.next_to(minus, RIGHT))
        equal_2 = MathTex(r'=').next_to(x, RIGHT)
        self.play(Write(equal_2))
        
        z = MathTex(r'\frac{1}{6}').next_to(equal_2, RIGHT)
        self.play(Write(z))
        t = z.copy()
        

        self.play(
            t.animate.next_to(brace_4, 0.5*UP),
            FadeOut(y)
        )
        second_half_2 = second_half.copy()
        s = t.copy()

        
        self.play(second_half_2.animate.next_to(together[0], DOWN, buff=1.3).set_color(WHITE))
        rat = MathTex(r':').next_to(second_half_2, RIGHT)
        self.play(Write(rat))
        self.play(s.animate.next_to(rat, RIGHT))
        equal_3 = MathTex(r'=').next_to(s, RIGHT)
        answer = MathTex(r'60').next_to(equal_3)
        box = SurroundingRectangle(answer, color=GREEN, buff=SMALL_BUFF)
        self.play(Write(equal_3))
        self.play(Write(answer))
        self.play(Write(box))



        
class Problem_11163(Scene):
    def construct(self):

        all_seg = Segment([0.5, 0, 0], [6.5, 0, 0])
        all_seg_2 = Segment([0.5, -1.5, 0], [6.5, -1.5, 0])
        

        
        paper1 = Paper().paper_2.move_to(6*LEFT).scale(0.6)
        plus = MathTex(r"+").next_to(paper1, RIGHT, buff=0.3)
        paper2 = Paper().paper_3.next_to(plus, RIGHT, buff=0.0001).scale(0.6)
        equal = MathTex(r'=').next_to(paper2, RIGHT, buff=0.3)
        paper3 = Paper().paper_1.next_to(equal, RIGHT, buff=0.0001).scale(0.6)

        first_half = MathTex(r"\frac{1}{3}", r"\textrm{ մաս}", font_size=30, tex_template=armenian_tex_template).next_to(paper1, DOWN)
        second_half = MathTex("10", font_size=30).next_to(paper2, DOWN)
        together = MathTex(r'\frac{1}{2}', r'\textrm{ մաս}', font_size=30, tex_template=armenian_tex_template).next_to(paper3, DOWN)

        first_seg = Segment([0.5, 0, 0], [2.5, 0, 0])
        first_seg.line.set_color(ORANGE)
        #fuck_seg = Segment([2.5, 0, 0], [4.5, 0, 0])
        second_seg = Segment([2.5, 0, 0], [3.5, 0, 0])
        second_seg.line.set_color(GREEN)
        third_seg = Segment([0.5, -1.5, 0], [3.5, -1.5, 0])
        third_seg.line.set_color(YELLOW)

        brace_1 = Brace(first_seg, UP)
        brace_3 = Brace(third_seg, DOWN)

        graphic = VGroup(
            first_seg, first_half[0], brace_1,
            second_seg, second_half,
            third_seg, together[0], brace_3
        )


#ANIMATION

        self.play(FadeIn(paper1))
        self.play(Write(first_half))
        self.play(FadeIn(paper2))
        self.play(Write(second_half))
        self.play(Write(plus))
        self.play(Write(equal))
        self.play(FadeIn(paper3))
        self.play(Write(together))

        self.play(Write(all_seg))

        self.play(
            Create(first_seg),
            #Create(fuck_seg),
            paper1.animate.set_color(ORANGE)
        )

        self.play(Write(brace_1))
        self.play(
            first_half[0].animate.next_to(brace_1, UP, buff=0.06),
            FadeOut(first_half[1])    
        )

        #self.play(FadeOut(fuck_seg))

        #self.play(Create(second_seg))

        self.play(
            paper2.animate.set_color(GREEN),
            Create(second_seg)
        )
        
        self.play(second_half.animate.next_to(second_seg, UP, buff=0.06))

        self.play(Create(all_seg_2))

        self.play(
            Create(third_seg),
            paper3.animate.set_color(YELLOW)
        )


        #self.add(third_seg)
        #self.remove(all_seg)

        self.play(Write(brace_3))
        self.play(
            together[0].animate.next_to(brace_3, DOWN, buff=0.06),
            FadeOut(together[1])
        )


        self.play(
            Uncreate(all_seg.endmark_right),
            Uncreate(all_seg_2.endmark_right)
        )
        self.play(
            Uncreate(all_seg.line),
            Uncreate(all_seg_2.line),
            Uncreate(all_seg.endmark_left),
            Uncreate(all_seg_2.endmark_left)
        )

        self.play(FadeOut(paper1, plus, paper2, equal, paper3))

        self.play(graphic.animate.shift(5.5*LEFT))

#INIT

        d1 = DashedLine(first_seg.endmark_left, third_seg.endmark_left)
        d2 = DashedLine(first_seg.endmark_right, first_seg.endmark_right.get_center()+1.5*DOWN)

        forth_seg = Segment(third_seg.endmark_left, first_seg.endmark_right.get_center()+1.5*DOWN)
        forth_seg.line.set_color(ORANGE)
        fifth_seg = Segment(first_seg.endmark_right.get_center()+1.5*DOWN, third_seg.endmark_right)
        brace_5 = Brace(fifth_seg, UP, buff=0.1)
        mas = MathTex(r'?', font_size=30).next_to(brace_5, UP, buff=0.1)

        self.play(
            Create(d1),
            Create(d2)
        )
        
        # self.add(forth_seg, fifth_seg)
        # self.remove(third_seg)
        # self.play(Write(brace_5))
        # self.play(Write(mas))

        self.play(Create(forth_seg))        
        third_seg.shift(DOWN)




        








class test(Scene):
    def construct(self):
        a = DashedLine()
        self.play(Create(a))