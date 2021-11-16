from manim import *
import numpy as np

armenian_tex_template = TexTemplate()
armenian_tex_template.add_to_preamble(r"\usepackage{armtex}")

def LabelPoint(point, label, position=DL*0.5, font_size=25):
    '''
    Adds label to a point

    Arguments - point(Dot), label(string)

    Optional Arguments - Position relative to the point=DL, font_size=25

    Returns - the Text mobject of label
    '''
    laebl_point = Text(label, font_size=font_size, color=point.get_color())
    laebl_point.next_to(point.get_center(), position)
    return laebl_point

def DistanceBetweenCoordinates(a, b):
    '''
    Calculates distance betwwen 2 coordinates

    Arguments - a([x_1, y_1, z_1]), b([x_2, y_2, z_2])

    Returns - Distance (float)
    '''
    return np.sqrt(sum((np.array(a) - np.array(b))**2))

def DistanceBetweenPoints(A, B):
    '''
    Calculates distance betwwen 2 Dots

    Arguments - A(Dot_1), B(Dot_2)

    Returns - Distance (float)
    '''
    return DistanceBetweenCoordinates(A.get_center(), B.get_center())

def SegmentLength(AB):
    '''
    Calculates the Length of a Segmnet

    Arguments - AB(Line)

    Returns - Length(float)
    '''
    a, b = AB.get_start_and_end()
    return DistanceBetweenCoordinates(a, b)

def SegmentsEqualitySign_1(AB, sign_size=0.2, color=WHITE):
    '''
    Equality sign with 1 small line for a segment

    Arguments - AB(Line)

    Optional Arguments - sign_size=0.2, Color=WHITE

    Returns - sign Mobject
    '''
    a, b = AB.get_start_and_end()
    length_AB = np.sqrt(sum((np.array(a) - np.array(b))**2))
    sign = AB.copy()
    sign = sign.scale(sign_size / length_AB)
    sign = sign.set_color(color)
    sign = sign.rotate(PI / 2)
    return sign

def SegmentsEqualitySign_2(AB, sign_size=0.2, color=WHITE):
    '''
    Equality sign with 2 small lines for a segment

    Arguments - AB(Line)

    Optional Arguments - sign_size=0.2, Color=WHITE

    Returns - sign Mobject
    '''
    a, b = AB.get_start_and_end()
    length_AB = np.sqrt(sum((np.array(a) - np.array(b))**2))
    unit_vector = AB.get_unit_vector()
    sign = AB.copy()
    sign = sign.scale(sign_size / length_AB)
    sign = sign.set_color(color)
    sign = sign.rotate(PI / 2)
    sign_1 = sign.copy().shift((unit_vector[0] * RIGHT + unit_vector[1] * UP) * 0.05)
    sign_2 = sign.copy().shift((-unit_vector[0] * RIGHT - unit_vector[1] * UP) * 0.05)
    sign = VGroup(sign_1, sign_2)

    return sign


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
        
