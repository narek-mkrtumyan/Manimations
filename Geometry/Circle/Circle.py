from manim import *
import numpy as np

import sys
sys.path.append("../../")       # relative path to the root of the repository
from Functions.GeometryFunctions.GeometryFunctions import *




class Robber(Scene):
    def construct(self):

        map = ImageMobject('map_1.JPG')
        map.scale(2.5)
        map.shift(0*RIGHT + 0*UP)

        c = [-0.2, -0.44, 0]
        r_sign = MathTex(r'15 \textrm{կմ}', font_size=30, tex_template=armenian_tex_template)

        self.play(FadeIn(map))
        self.wait(2)

        circle, c = CircleFromSpinningRadius(self, 
            radius=3, center=c, center_color=RED, circle_color=RED, r_sign=r_sign, r_sign_angle=-20)
        self.wait(1)

        angles = [4, 38, 123, 162, 237, 309]
        points = VGroup()
        for angle in angles:
            points.add(Dot(circle.point_at_angle(angle * DEGREES), color=RED, radius=0.12))

        self.play(FadeIn(points))
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])




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
            self.play(Write(label_Center))
            self.play(Create(radius_line))
            self.play(Write(label_radius))
            self.wait(1)

            # Circle
            circle, c = CircleFromSpinningRadius(self, 2, center, create_center=False, create_radius=False, circle_color=GREEN)
            self.remove(c)
            self.play(Write(label_circle))
            self.wait(0.5)

            # FadeOut unnecessary things
            self.play(FadeOut(label_Center), FadeOut(label_radius), FadeOut(radius_line))
            self.wait(0.5)

        # Create Cord, Arcs, Diameter
            angle_a = ValueTracker(120*DEGREES)
            angle_b = ValueTracker(30*DEGREES)

            A = always_redraw(lambda: Dot(circle.point_at_angle(angle_a.get_value()), color=ORANGE))
            B = always_redraw(lambda: Dot(circle.point_at_angle(angle_b.get_value()), color=ORANGE))
            AB = always_redraw(lambda: Line(A.get_center(), B.get_center(), color=ORANGE))
            label_AB = always_redraw(lambda: 
                MathTex(r'\textrm{Լար}', tex_template=armenian_tex_template, font_size=30).next_to(AB.get_center(), DOWN*0.75))

            # Cord
            self.play(Create(A), Create(B))
            self.play(Create(AB))
            self.play(Write(label_AB))
            self.wait(2)

            # init Arcs
            small_arc = always_redraw(lambda: 
                Arc(radius=radius, arc_center=center, 
                    start_angle=angle_b.get_value(), angle=angle_a.get_value()-angle_b.get_value(), color=YELLOW))

            big_arc = always_redraw(lambda: 
                Arc(radius=radius, arc_center=center, 
                    start_angle=angle_a.get_value(), angle=360*DEGREES-(angle_a.get_value()-angle_b.get_value()), color=RED))
            
            label_small_arc = always_redraw(lambda: 
                MathTex(r'\textrm{Փոքր աղեղ}', tex_template=armenian_tex_template, font_size=30)
                .next_to(circle.point_at_angle((angle_a.get_value()+angle_b.get_value())/2), UP))
            
            label_big_arc = always_redraw(lambda: 
                MathTex(r'\textrm{Մեծ աղեղ}', tex_template=armenian_tex_template, font_size=30)
                .next_to(circle.point_at_angle((angle_a.get_value()+angle_b.get_value())/2 + 180*DEGREES), DOWN))

            # play Arcs
            self.play(FadeOut(label_circle))
            self.wait(1)
            self.play(FadeIn(small_arc), FadeIn(big_arc))
            self.wait(1)
            self.play(Write(label_big_arc))
            self.play(Write(label_small_arc))
            self.wait(1)

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
            self.wait(1)
            self.play(
                ReplacementTransform(label_AB, label_AB_diameter)
            )
            self.wait(2)

            self.play(Center.animate(rate_func=there_and_back, run_time=2).scale(2))
            self.wait(1)

            self.play(*[FadeOut(mob) for mob in self.mobjects])




class AngleFromCircumference(Scene):
    def construct(self):

        angle_40 = MathTex(r'40^{\circ}', font_size=25)

        center = np.array([1, 0.5, 0])
        radius=3
        circle = Circle(radius=radius, color=GREEN).move_to(center)
        A = Dot(circle.point_at_angle(240*DEGREES), color=ORANGE)
        Label_A = LabelPoint(A, 'A')
        B = Dot(circle.point_at_angle(320*DEGREES), color=ORANGE)
        Label_B = LabelPoint(B, 'B', DR*0.5)
        C = Dot(circle.point_at_angle(130*DEGREES), color=ORANGE)
        Label_C = LabelPoint(C, 'C', UL*0.5)

        CA = Line(C.get_center(), A.get_center(), color=ORANGE)
        CB = Line(C.get_center(), B.get_center(), color=ORANGE)

        angle_ACB = Angle(CA, CB)
        ACB_40 = angle_40.copy().next_to(angle_ACB, DOWN*0.5+0.01*RIGHT)


        angle_d = ValueTracker(70)
        D = always_redraw(lambda: Dot(circle.point_at_angle(angle_d.get_value()*DEGREES), color=RED))
        Label_D = always_redraw(lambda: LabelPoint(D, 'D', UR*0.5))

        DA = always_redraw(lambda: Line(D.get_center(), A.get_center(), color=RED))
        DB = always_redraw(lambda: Line(D.get_center(), B.get_center(), color=RED))

        angle_ADB = always_redraw(lambda: Angle(DA, DB))
        ADB_40 = always_redraw(lambda: angle_40.copy().next_to(angle_ADB, DOWN*0.5))


        self.wait(0.5)
        self.play(Create(circle, rate_func=linear))
        self.wait(1.5)
        self.play(Create(A), Write(Label_A))
        self.play(Create(B), Write(Label_B))
        self.wait(1)
        self.play(Create(C), Write(Label_C))
        self.wait(1)
        self.play(Create(CA))
        self.play(Create(CB))
        self.wait(1)
        self.play(Create(angle_ACB))
        self.wait(1.5)
        self.play(Create(ACB_40))
        self.wait(2)
        self.play(Create(D))
        self.wait(1)
        self.play(Create(DA))
        self.play(Create(DB))
        self.add(A, B)
        self.play(Create(Label_D))
        self.wait(1)
        self.play(Create(angle_ADB))
        self.wait(1)
        self.play(Create(ADB_40))
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
        self.wait(2)
        # self.play(*[FadeOut(mob) for mob in self.mobjects])










class Horse(Scene):
    def construct(self):

        self.camera.background_color=GREEN_E

        horse_1 = ImageMobject('horse.png').scale(0.2).move_to([9, 0, 0])
        man = ImageMobject('man.png').scale(0.2).move_to([10, -1.5, 0])

        center = [0, 0, 0]
        radius = 2
        starting_point_angle = 90
        circle_color=DARK_BROWN
        radius_color=WHITE
        circle_stroke_width=10

        Center = Dot(center)
        circle = Circle(radius=radius, color=circle_color, stroke_width=circle_stroke_width).move_to(center)
        fill_circle = Circle(radius=radius, stroke_width=0).set_fill(color=LIGHT_BROWN, opacity=0)

        moving_point_angle = ValueTracker(starting_point_angle)

        horse = always_redraw(lambda: 
            ImageMobject('horse.png').scale(0.2)
                .rotate((moving_point_angle.get_value()-starting_point_angle)*DEGREES, about_point=center)
                    .move_to(circle.point_at_angle((moving_point_angle.get_value() % 360)*DEGREES))
        )

        radius_line = always_redraw(lambda: Line(center, circle.point_at_angle((moving_point_angle.get_value() % 360)*DEGREES),
            color=radius_color))

        arc = always_redraw(lambda: Arc(start_angle=starting_point_angle*DEGREES, 
            angle=((moving_point_angle.get_value() - starting_point_angle) % 360)*DEGREES, 
            arc_center=center, radius=radius, color=circle_color, stroke_width=circle_stroke_width))
        
        radius_10m = MathTex(r'10 \textrm{մ}', font_size=25, tex_template=armenian_tex_template)
        radius_10m = always_redraw(lambda:
            radius_10m.copy().next_to(
                (Center.get_center() + circle.point_at_angle(
                    ((moving_point_angle.get_value() + 30)  % 360) * DEGREES)) / 2, buff=0))
        

        self.add(arc, fill_circle)
        self.add(horse_1, man)
        self.play(
            horse_1.animate(rate_func=linear).move_to([0, 2, 0]),
            man.animate(rate_func=linear).move_to([0.5, 0.5, 0]),
            run_time=3
        )
        self.wait(1)

        self.play(man.animate(rate_func=linear).move_to([0.2, 0.2, 0]), run_time=0.5)
        self.play(Create(Center))
        self.add(horse, man)
        self.remove(horse_1)
        self.play(
            Create(radius_line, run_time=1, rate_func=linear),
            man.animate(rate_func=linear, run_time=1).move_to([0.2, 2, 0])
        )
        self.play(Write(radius_10m))
        self.add(man)
        self.play(man.animate(rate_func=linear).move_to([1, 1, 0]), run_time=0.5)
        self.wait(3)

        self.play(moving_point_angle.animate(rate_func=linear).set_value(starting_point_angle + 360), run_time=6)
        self.add(circle, horse, radius_line)
        self.remove(arc)
        self.wait(1)

        self.play(fill_circle.animate(rate_func=linear).set_fill(opacity=1))
        self.wait(2)

        self.play(circle.animate(rate_func=there_and_back).set_stroke(width=15), run_time=3)
        self.wait(2)

        self.play(
            radius_line.animate(rate_func=there_and_back).set_stroke(width=8),
            radius_10m.animate(rate_func=there_and_back).scale(2),
            run_time=2.5)
        self.wait(1)

        self.play(Center.animate(rate_func=there_and_back).scale(2), run_time=2)
        self.wait(0.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects])




class RobberYerevan(Scene):
    def construct(self):

        map = ImageMobject('map.JPG')
        map.scale(2.4)
        map.shift(0.15*RIGHT)

        self.wait(0.5)
        self.play(FadeIn(map))
        self.wait(1)

        c = [0, -0.75, 0]
        r_sign = MathTex(r'15 \textrm{կմ}', font_size=30, tex_template=armenian_tex_template)

        self.wait(1)
        circle, c = CircleFromSpinningRadius(self, 
            radius=3, center=c, center_color=RED, circle_color=RED, r_sign=r_sign, r_sign_angle=-20)
        self.wait(1)

        angles = [258, 250, 242, 177, 116, 78, 61, 45, 12, 22]
        extra_angles = [308, 221, 206, 190, 157]
        points = VGroup()
        for angle in angles:
            points.add(Dot(circle.point_at_angle(angle * DEGREES), color=RED))

        self.play(FadeIn(points))
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)







class test(Scene):
    def construct(self):
        circle = Circle(radius=2)
        angle = ValueTracker(0)
        arc = always_redraw(lambda: Arc(radius=2, angle=angle.get_value()))
        self.add(circle, arc)
        self.play(angle.animate(rate_func=linear, run_time=4).set_value(100*PI))
        self.wait(0.5)


