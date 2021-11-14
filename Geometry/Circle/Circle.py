from manim import *
import numpy as np

class SheepCircle(Scene):
    def construct(self):

        self.camera.background_color=GREEN_E

        def CircleFromSpinningRadiusSheep(radius=1, center=[0, 0, 0], starting_point_angle=0,
            radius_color=WHITE, circle_color=GREEN, run_time=4, circle_stroke_width=10):
    
            Center = Dot(center)
            circle = Circle(radius=radius, color=circle_color, stroke_width=circle_stroke_width).move_to(center)

            moving_point_angle = ValueTracker(starting_point_angle)

            moving_point = always_redraw(lambda: Dot(circle.point_at_angle((moving_point_angle.get_value() % 360)*DEGREES), color=circle_color))

            sheep = always_redraw(lambda: ImageMobject('sheep.png').scale(0.3)
                .rotate((moving_point_angle.get_value()-starting_point_angle)*DEGREES, about_point=center)
                    .move_to(circle.point_at_angle((moving_point_angle.get_value() % 360)*DEGREES)))

            radius_line = always_redraw(lambda: Line(center, circle.point_at_angle((moving_point_angle.get_value() % 360)*DEGREES),
             color=radius_color))

            arc = always_redraw(lambda: Arc(start_angle=starting_point_angle*DEGREES, 
                angle=((moving_point_angle.get_value() - starting_point_angle) % 360)*DEGREES, 
                arc_center=center, radius=radius, color=circle_color, stroke_width=circle_stroke_width))

            self.add(sheep)
            self.play(Create(Center))
            self.play(Create(radius_line))
            self.wait(0.5)
            self.add(arc)
            self.play(moving_point_angle.animate(rate_func=linear, run_time=run_time).set_value(starting_point_angle + 360))
            self.add(circle)
            self.remove(sheep)
            self.play(Uncreate(radius_line))

            return circle

        center = [0, 0, 0]
        radius = 2
        starting_point_angle = 90

        self.wait(0.5)
        CircleFromSpinningRadiusSheep(radius=radius, starting_point_angle=starting_point_angle, circle_color=DARK_BROWN)
        self.wait(0.5)
        