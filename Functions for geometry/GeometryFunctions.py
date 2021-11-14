from manim import *
import numpy as np

def distance_between_points(a, b):
    return np.sqrt(sum((np.array(a)-np.array(b))**2))

class GeometryFunctions(Scene):

    def CircleFromSpinningRadius(self, radius=1, center=[0, 0, 0], starting_point_angle=0, radius_color=WHITE, circle_color=GREEN, run_time=4):
        '''
        This function Creates a Circle using it's radius like a Compass Drawing tool (կարկին)
        Arguments - radius, center, point from which to start (angle in DEGREES), colors and run time
        Returns the Circle
        '''
    
        Center = Dot(center, color=radius_color)
        circle = Circle(radius=radius, color=circle_color).move_to(center)

        moving_point_angle = ValueTracker(starting_point_angle)

        moving_point = always_redraw(lambda: Dot(circle.point_at_angle((moving_point_angle.get_value() % 360)*DEGREES), color=circle_color))

        radius_line = always_redraw(lambda: Line(center, circle.point_at_angle((moving_point_angle.get_value() % 360)*DEGREES),
            color=radius_color))

        arc = always_redraw(lambda: Arc(start_angle=starting_point_angle*DEGREES, 
            angle=((moving_point_angle.get_value() - starting_point_angle) % 360)*DEGREES, 
            arc_center=center, radius=radius, color=circle_color))

        self.play(Create(Center))
        self.play(Create(radius_line))
        self.play(Create(moving_point))
        self.wait(0.5)
        self.add(arc)
        self.play(moving_point_angle.animate(run_time=run_time, rate_finc=linear).set_value(starting_point_angle + 360))
        self.add(circle)
        self.play(Uncreate(moving_point), Uncreate(radius_line))

        return circle




class test(Scene):
    def construct(self):
        self.wait()
        
