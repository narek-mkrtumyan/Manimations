from manim import *
import numpy as np

import sys
sys.path.append("../../")       # relative path to the root of the repository
from Functions.GeometryFunctions.GeometryFunctions import *


class Map(Scene):
    def construct(self):
        
        # self.camera.background_color = GREEN
        map = ImageMobject('qartez_tsakats.PNG')
        map.scale(0.5)
        map.shift(0*RIGHT + 0*UP)

        self.play(FadeIn(map))
        self.wait(2)

        c = [1, 0, 0]
        r_sign = MathTex(r'15 \textrm{կմ}', font_size=30, tex_template=armenian_tex_template)

        self.wait(1)
        circle, c = CircleFromSpinningRadius(self, 
            radius=3, center=c, center_color=WHITE, circle_color=RED, r_sign=r_sign, r_sign_angle=-20)
        self.wait(1)

        angles = [56, 161, 265]
        points = VGroup()
        for angle in angles:
            points.add(Dot(circle.point_at_angle(angle * DEGREES), color=RED, radius=0.12))

        self.play(FadeIn(points))
        self.wait(3)
        # self.play(*[FadeOut(mob) for mob in self.mobjects])



class Definitions(Scene):
    def construct(self):
     
            radius = 2
            center = np.array([0, 0, 0])
            Center = Dot(center)
            circle = Circle(radius=radius, color=GREEN).move_to(center)

        # Create Center, Radius, Circle, and labels
            radius_line = Line(center, np.array([radius, 0, 0]))
            label_Center = MathTex(r'\textrm{Կենտրոն}', 
                tex_template=armenian_tex_template, font_size=30).next_to(Center, UP*0.5)
            label_radius = MathTex(r'\textrm{Շառավիղ}', 
                tex_template=armenian_tex_template, font_size=30).next_to(radius_line, DOWN*0.5)
            label_circle = MathTex(r'\textrm{Շրջանագիծ}', 
                tex_template=armenian_tex_template, font_size=30, color=GREEN).move_to(center + np.array([0, radius+0.5, 0]))

            # Center and Radius
            self.wait(0.1)
            self.play(Create(Center))
            self.play(Create(radius_line))
            self.wait(0.5)

            # Circle
            circle, c = CircleFromSpinningRadius(self, 2, center, create_center=False, create_radius=False, circle_color=GREEN, run_time=2)
            self.remove(c)
            self.play(Write(label_circle))
            self.wait(1.5)
            self.play(Write(label_Center))
            self.wait(3.5)
            self.play(Write(label_radius))
            self.wait(1.5)

            # FadeOut unnecessary things
            self.play(FadeOut(label_Center), FadeOut(label_radius), FadeOut(radius_line))
            self.wait(1)

        # Create Cord, Arcs, Diameter
            angle_a = ValueTracker(120*DEGREES)
            angle_b = ValueTracker(30*DEGREES)

            A = always_redraw(lambda: Dot(circle.point_at_angle(angle_a.get_value()), color=ORANGE))
            B = always_redraw(lambda: Dot(circle.point_at_angle(angle_b.get_value()), color=ORANGE))
            AB = always_redraw(lambda: Line(A.get_center(), B.get_center(), color=ORANGE))
            label_AB = always_redraw(lambda: 
                MathTex(r'\textrm{Լար}', tex_template=armenian_tex_template, font_size=30).next_to(AB.get_center(), DOWN*0.75))
            
            copy_A_small = A.copy()
            copy_B_small = B.copy()
            copy_A_big = A.copy()
            copy_B_big = B.copy()

            # Cord
            self.play(Create(A), Create(B))
            self.play(Create(AB))
            self.play(Write(label_AB))
            self.wait(0.5)

        # init Arcs
            small_arc = Arc(radius=radius, arc_center=center, start_angle=angle_b.get_value(), 
                            angle=angle_a.get_value()-angle_b.get_value(), color=YELLOW)

            big_arc = Arc(radius=radius, arc_center=center, start_angle=angle_a.get_value(), 
                            angle=360*DEGREES-(angle_a.get_value()-angle_b.get_value()), color=RED)

        # play Arcs
            self.play(FadeOut(label_circle))
            self.add(copy_A_small, copy_B_small, copy_A_big, copy_B_big)
            self.play(FadeOut(AB), FadeOut(A), FadeOut(B), FadeOut(label_AB), FadeOut(Center))
            self.play(FadeIn(small_arc), FadeIn(big_arc))
            self.remove(circle)
            self.play(
                VGroup(copy_A_small, copy_B_small, small_arc).animate(rate_func=linear).shift(UR*0.5),
                VGroup(copy_A_big, copy_B_big, big_arc).animate(rate_func=linear).shift(DL*0.5)
            )
            self.wait(0.5)

        # init arc labels
            label_small_arc = always_redraw(lambda: 
                MathTex(r'\textrm{Փոքր աղեղ}', tex_template=armenian_tex_template, font_size=30)
                .next_to(small_arc, UP))
            
            label_big_arc = always_redraw(lambda: 
                MathTex(r'\textrm{Մեծ աղեղ}', tex_template=armenian_tex_template, font_size=30)
                .next_to(big_arc, DOWN))
        # 
            self.play(Write(label_big_arc))
            self.play(Write(label_small_arc))
            self.wait(0.2)
            self.play(
                VGroup(copy_A_small, copy_B_small, small_arc).animate(rate_func=linear).shift(DL*0.5),
                VGroup(copy_A_big, copy_B_big, big_arc).animate(rate_func=linear).shift(UR*0.5)
            )
            self.play(FadeIn(A), FadeIn(B), FadeIn(AB), FadeIn(label_AB), FadeIn(Center))
            self.remove(copy_A_small, copy_B_small, copy_A_big, copy_B_big)
            self.wait(0.5)
        
        # re init arcs
            self.remove(small_arc, big_arc)
            small_arc = always_redraw(lambda: 
                Arc(radius=radius, arc_center=center, 
                    start_angle=angle_b.get_value(), angle=angle_a.get_value()-angle_b.get_value(), color=YELLOW))

            big_arc = always_redraw(lambda: 
                Arc(radius=radius, arc_center=center, 
                    start_angle=angle_a.get_value(), angle=360*DEGREES-(angle_a.get_value()-angle_b.get_value()), color=RED))
            self.add(small_arc, big_arc)

        # Cord becomes Diameter
            self.play(
                angle_a.animate(rate_func=linear).set_value(180*DEGREES),
                angle_b.animate(rate_func=linear).set_value(0),
                run_time=2
            )
            self.add(A, B)
            self.wait(1)

            label_half_circle_1 = always_redraw(lambda: 
                MathTex(r'\textrm{Կիսաշրջանագիծ}', tex_template=armenian_tex_template, font_size=30)
                .next_to(circle.point_at_angle((angle_a.get_value()+angle_b.get_value())/2), UP))
            
            label_half_circle_2 = always_redraw(lambda: 
                MathTex(r'\textrm{Կիսաշրջանագիծ}', tex_template=armenian_tex_template, font_size=30)
                .next_to(circle.point_at_angle((angle_a.get_value()+angle_b.get_value())/2 + 180*DEGREES), DOWN))
            
            label_AB_diameter = always_redraw(lambda: 
                MathTex(r'\textrm{Տրամագիծ}', tex_template=armenian_tex_template, font_size=30).next_to(AB.get_center(), DOWN*0.75))
            
        # labels change
            self.play(
                ReplacementTransform(label_small_arc, label_half_circle_1),
                ReplacementTransform(label_big_arc, label_half_circle_2))
            self.wait(8.5)
            self.play(
                ReplacementTransform(label_AB, label_AB_diameter)
            )
            self.wait(5.5)

            self.play(Center.animate(rate_func=there_and_back, run_time=2).scale(2))

            self.play(*[FadeOut(mob) for mob in self.mobjects])



class Property(Scene):
    def construct(self):

        center = np.array([1, 0.5, 0])
        radius=3
        circle = Circle(radius=radius, color=GREEN).move_to(center)

        angle_a = ValueTracker(240)
        A = always_redraw(lambda: Dot(circle.point_at_angle(angle_a.get_value()*DEGREES), color=ORANGE))
        Label_A = always_redraw(lambda: LabelPoint(A, 'A'))

        angle_b = ValueTracker(320)
        B = always_redraw(lambda: Dot(circle.point_at_angle(angle_b.get_value()*DEGREES), color=ORANGE))
        Label_B = always_redraw(lambda: LabelPoint(B, 'B', DR*0.5))

        C = Dot(circle.point_at_angle(130*DEGREES), color=ORANGE)
        Label_C = LabelPoint(C, 'C', UL*0.5)

        arc_BA = Arc(arc_center=center, radius=radius, start_angle=320*DEGREES, angle=280*DEGREES, color=RED)

        CA = always_redraw(lambda: Line(C.get_center(), A.get_center(), color=ORANGE))
        CB = always_redraw(lambda: Line(C.get_center(), B.get_center(), color=ORANGE))

        angle_ACB = always_redraw(lambda: Angle(CA, CB))
        angle_value_ACB = always_redraw(lambda: 
                MathTex(fr'{int(Angle(CA, CB).get_value(degrees=True))+1}' + r'^{\circ}', font_size=25)
                .next_to(angle_ACB.get_center(), DOWN*0.5+0.01*RIGHT)
            )

        angle_d = ValueTracker(70)
        D = always_redraw(lambda: Dot(circle.point_at_angle(angle_d.get_value()*DEGREES), color=WHITE))
        Label_D = always_redraw(lambda: LabelPoint(D, 'D', UR*0.5))

        DA = always_redraw(lambda: Line(D.get_center(), A.get_center(), color=WHITE))
        DB = always_redraw(lambda: Line(D.get_center(), B.get_center(), color=WHITE))

        angle_ADB = always_redraw(lambda: Angle(DA, DB))
        angle_value_ADB = always_redraw(lambda: angle_value_ACB.copy().next_to(angle_ADB, DOWN*0.5))


    # Animations
        self.wait(0.5)
        self.play(Create(circle, rate_func=linear))
        self.wait(2)
        self.play(Create(A), Write(Label_A))
        self.play(Create(B), Write(Label_B))
        self.wait(3.2)
        self.play(Create(C), Write(Label_C))
        self.wait(2)
        self.play(Create(CA))
        self.wait(0.2)
        self.play(Create(CB))
        self.wait(2.3)
        self.play(Create(angle_ACB))
        self.wait(3)
        self.play(Create(angle_value_ACB))
        self.wait(2)
        self.play(FadeIn(arc_BA))
        self.wait(1.5)
        self.play(FadeOut(arc_BA))
        self.wait(1)
        self.play(Create(D), Create(Label_D))
        self.wait(1.5)
        self.play(Create(DA))
        self.play(Create(DB))
        self.wait(1.5)
        self.play(Create(angle_ADB))
        self.wait(1.5)
        self.play(Create(angle_value_ADB))
        self.wait(2)

        self.play(
            angle_d.animate(rate_func=linear).set_value(110),
            run_time=3
        )
        self.wait(2)
        
        self.play(
            angle_d.animate(rate_func=linear).set_value(30),
            run_time=4
        )
        self.wait(3)

        self.play(angle_b.animate(rate_func=linear, run_time=3).set_value(355))
        self.wait(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)





class test(Scene):
    def construct(self):

        circle = Circle(2, GREEN)
        A = Dot(circle.point_at_angle(240*DEGREES))
        B = Dot(circle.point_at_angle(320*DEGREES))
        O = Dot(circle.point_at_angle(0*DEGREES))

        OA = always_redraw(lambda: Line(O.get_center(), A.get_center()))
        OB = always_redraw(lambda: Line(O.get_center(), B.get_center()))

        angle_AOB = always_redraw(lambda: Angle(OA, OB))
        # angle_AOB_dot_OA = always_redraw(lambda: Dot(angle_AOB.points[0]))
        # angle_AOB_dot_OB = always_redraw(lambda: Dot(angle_AOB.points[-1]))

        arc_AB = Arc(2, 240*DEGREES, 80*DEGREES, color=RED)

        self.add(circle, A, B, O, OA, OB, angle_AOB, arc_AB)
        self.wait(1)
        self.play(Transform(arc_AB, angle_AOB), run_time=3)
        self.wait(1)

