import sys
sys.path.append('../../')
from Functions.qarakusi import *        



class Problem11163(Scene):
    def construct(self):

        papers = Papers(48).scale(0.8).shift(3*DL)


        first_seg = Segment([0, 0, 0], [4.71, 0, 0]).rotate(PI/2).next_to(papers, LEFT, buff=0.2).shift(0.1*DOWN)
        second_seg = Segment([0, 0, 0], [4.71, 0, 0]).rotate(PI/2).move_to(first_seg.get_center()+4.71*RIGHT)
        
        first_seg_half = Segment([0, 0, 0], [2.355, 0, 0]).rotate(-PI/2)
        second_seg_half = Segment([0, 0, 0], [2.355, 0, 0]).rotate(PI/2)


        self.add(papers.papers)

        self.play(Create(first_seg), Create(second_seg))

        seg_1_length = ValueTracker(0)
        seg_1 = always_redraw(
            lambda: Segment(first_seg.endmark_right.get_center(), first_seg.endmark_right.get_center()+seg_1_length.get_value()*RIGHT, color=ORANGE, endmark_color=WHITE).rotate(-PI/2, about_point=first_seg.endmark_right.get_center())
        )        

        seg_2_length = ValueTracker(0)
        seg_2 = always_redraw(
            lambda: Segment(seg_1.endmark_right.get_center(), seg_1.endmark_right.get_center()+seg_2_length.get_value()*RIGHT, color=GREEN, endmark_color=WHITE).rotate(-PI/2, about_point=seg_1.endmark_right.get_center())
        )

        seg_3_length = ValueTracker(0)
        seg_3 = always_redraw(
            lambda: Segment(second_seg.endmark_left.get_center(), second_seg.endmark_left.get_center()+seg_3_length.get_value()*RIGHT, color=YELLOW, endmark_color=WHITE).rotate(PI/2, about_point=second_seg.endmark_left.get_center())
        )

        self.add(seg_1)
        self.add(seg_2)
        self.add(seg_3)


        for i in range(1, 17):

        # տանում ա աջ, իջացնում ներքև ու շարում իրար վրա
            self.play(
                Create(papers[-i].texts),
                seg_1_length.animate.set_value(4.71*i/48),
                seg_3_length.animate.set_value(4.71*i/48),
                run_time=0.25
            )
            self.play(papers[-i].animate.shift(5.21 * RIGHT), run_time=0.25)
            if i == 1:
                self.play(papers[-i].animate.align_to(papers[0], DOWN), run_time=0.25)
            else:
                self.play(
                    papers[-i].animate.move_to(papers[-i+1].get_center() + 0.8*DEFAULT_PAPERS_BUFF * UP),
                    run_time=0.25
                )

        brace_1 = Brace(seg_1, LEFT)
        day_1 = MathTex(r'\frac{1}{3}', r"\textrm{մաս}", font_size=32)
        day_1[1].next_to(day_1[0], DOWN, buff=0.1)
        day_1.next_to(brace_1, LEFT, buff=0.1)

        self.play(Create(brace_1))
        self.play(Write(day_1))
        

        for i in range(17, 25):
            self.play(
                Create(papers[-i].texts),
                seg_2_length.animate.set_value(4.71*(i-16)/48),
                seg_3_length.animate.set_value(4.71*i/48),
                run_time=0.25
            )
            self.play(papers[-i].animate.shift(5.21 * RIGHT), run_time=0.25)
            if i == 1:
                self.play(papers[-i].animate.align_to(papers[0], DOWN), run_time=0.25)
            else:
                self.play(
                    papers[-i].animate.move_to(papers[-i+1].get_center() + 0.8*DEFAULT_PAPERS_BUFF * UP),
                    run_time=0.25
                )

        day_2 = MathTex(r'10', r"\textrm{էջ}", font_size=32)
        day_2[1].next_to(day_2[0], DOWN, buff=0.1)
        day_2.next_to(seg_2, LEFT, buff=0.15)
        brace_3 = Brace(seg_3, LEFT)
        day_3 = MathTex(r"\frac{1}{2}", r"\textrm{մաս}", font_size=32)
        day_3[1].next_to(day_3[0], DOWN, buff=0.1)
        day_3.next_to(brace_3, LEFT, buff=0.1)

        self.play(Write(day_2))
        self.play(Create(brace_3))
        self.play(Write(day_3))

        # # ուղղակի ներկում ա իբր էդ թղթի վրա գրվեց
        #     if i == 1:
        #         self.play(Create(papers[-i].texts))
        #         self.play(papers.colors[-i].animate.set_color(GREY))
        #     else:
        #         self.play(papers.colors[-i].animate.set_color(GREY))


        # self.play(
        #     FadeOut(first_seg),
        #     FadeOut(second_seg),
        #     FadeOut(papers[0:24])
        # )



        seg_1.clear_updaters()
        seg_2.clear_updaters()
        seg_3.clear_updaters()
        

        first_seg_half.next_to(seg_2.endmark_right, DOWN, buff=0)
        second_seg_half.next_to(seg_3.endmark_right, UP, buff=0)
        
        segs_1 = VGroup(seg_1, seg_2, first_seg_half)
        segs_2 = VGroup(seg_3, second_seg_half)

        self.add(first_seg_half, second_seg_half)
        self.remove(first_seg, second_seg)

        self.play(
            FadeOut(day_1),
            FadeOut(day_2),
            FadeOut(day_3),
            FadeOut(brace_1),
            FadeOut(brace_3)
        )

        self.play(
            FadeOut(papers[0:24]),
            FadeOut(papers[47:23:-1])
        )


        self.play(
            segs_1.animate.rotate(PI/2, about_point=seg_1.endmark_left.get_center()).scale(1.5),
            segs_2.animate.rotate(-PI/2, about_point=second_seg_half.endmark_right.get_center()).shift(2*DOWN).scale(1.5),
        )

        seg_1.line.set_stroke(width=5),
        seg_2.line.set_stroke(width=5),
        first_seg_half.line.set_stroke(width=5),
        seg_3.line.set_stroke(width=5),
        second_seg_half.line.set_stroke(width=5)
        


        dline_1 = always_redraw(
            lambda: DashedLine(seg_1.endmark_left, seg_3.endmark_left)
        )
        dline_2 = always_redraw(
            lambda: DashedLine(seg_2.endmark_right, seg_3.endmark_right)
        )

        

        self.play(
            Write(dline_1), 
            Write(dline_2),
            run_time=0.5
        )

        dline_3 = DashedLine(seg_1.endmark_right, (seg_3.endmark_left.get_center()+2*seg_3.endmark_right.get_center())/3)
        seg_1c = seg_1.copy()
        seg_2c = seg_2.copy()
        seg_2c.line.set_stroke(color=WHITE)

        # self.play(segs_2.animate.shift(2*DOWN))

        brace_1 = Brace(seg_1, UP)
        brace_3 = Brace(seg_3, DOWN)
        day_1 = MathTex(r'\frac{1}{3}', font_size=40).next_to(brace_1, UP, buff=0.1)
        day_2 = MathTex(r'10', font_size=40).next_to(seg_2, UP, buff=0.2)
        day_3 = MathTex(r'\frac{1}{2}', font_size=40).next_to(brace_3, DOWN, buff=0.1)
        
        self.play(
            Write(brace_1),
            Write(brace_3)
        )
    
        self.play(
            Write(day_1),
            Write(day_2),
            Write(day_3)
        )

        seg_1c.shift(2*DOWN)
        seg_2c.shift(2*DOWN)

        self.play(Write(dline_3), run_time=0.5)
        # self.play(
        #     seg_1c.animate.shift(2*DOWN),
        #     seg_2c.animate.shift(2*DOWN)
        # )
        self.add(seg_1c, seg_2c)
        self.remove(seg_3)
        
        brace_5 = Brace(seg_2c, UP)
        harc = MathTex("?", font_size=40).next_to(brace_5, UP, buff=0.1)

        self.play(Write(brace_5))

        self.play(Write(harc))

        day_1c = day_1.copy()
        day_2c = day_2.copy()
        day_3c = day_3.copy()
        minus = MathTex("-", font_size=40)
        equal = MathTex("=", font_size=40)
        x = MathTex(r"\frac{1}{6}", font_size=40)


        self.play(day_3c.animate.next_to(segs_1, RIGHT, buff=1))
        minus.next_to(day_3c, RIGHT, buff=0.15)
        self.play(Write(minus))
        self.play(day_1c.animate.next_to(minus, RIGHT, buff=0.15))
        equal.next_to(day_1c, RIGHT, buff=0.15)
        self.play(Write(equal))
        x.next_to(equal, RIGHT, buff=0.15)
        self.play(Write(x))
        y = x.copy()
        self.play(
            y.animate.next_to(brace_5, UP, buff=0.1),
            FadeOut(harc)
        )

        z = y.copy()
        mek_vec = MathTex(r"\frac{1}{6}", r"\textrm{ մաս}", r"\longrightarrow", r"10", font_size=40).shift(DOWN+0.5*RIGHT)
        mek = MathTex(r"1", r"\textrm{ մաս}", r"\longrightarrow", r"?", font_size=40).next_to(mek_vec, DOWN, buff=0.5)
        self.play(z.animate.move_to(mek_vec[0]))
        self.add(mek_vec[0])
        self.play(Write(mek_vec[1]))
        self.play(Write(mek_vec[2]))
        self.play(day_2c.animate.move_to(mek_vec[3]))
        self.play(Write(mek))

        t = mek[0].copy()
        self.play(t.animate.next_to(day_3c, DOWN, buff=0.5))
        mult = MathTex(r"\cdot", font_size=40).next_to(t, RIGHT, buff=0.15)
        self.play(Write(mult))
        r = mek_vec[3].copy()
        self.play(r.animate.next_to(mult, RIGHT, buff=0.15))
        div = MathTex(':', font_size=40).next_to(r, RIGHT, buff=0.15)
        self.play(Write(div))
        self.play(z.animate.next_to(div, RIGHT, buff=0.15))
        equal_2 = MathTex('=', font_size=40).next_to(z, RIGHT, buff=0.15)
        self.play(Write(equal_2))
        ans = MathTex("60", font_size=40).next_to(equal_2, RIGHT, buff=0.15)
        self.play(Write(ans))

        box = SurroundingRectangle(ans, color=GREEN)
        self.play(Write(box))


        
        # self.play(papers[47:23:-1].animate.next_to(seg_3, LEFT, buff=0.5))
        # self.play(segs.animate.next_to(papers[24:48], LEFT, buff=0.5))

        # self.play(FadeOut(papers[47:23:-1]))
    
        self.wait()




class test2(Scene):
    def construct(self):
        
        p = Papers(6).scale(0.5)
        q = Papers(6).shift(2*RIGHT)

        #self.add(p, q)


        t = Segment()
        self.play(Create(t))

        self.play(t.animate.stroke_width(30))