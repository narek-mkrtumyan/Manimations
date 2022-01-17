from math import degrees, radians
from manim import *
from manim.mobject.svg.svg_path import vector_angle
import numpy as np


armenian_tex_template = TexTemplate()
armenian_tex_template.add_to_preamble(r"\usepackage{armtex}")


def set_frame_half():
    config.frame_width = 9
    config.frame_height = 8

    config.pixel_width = 1080
    config.pixel_height = 960


# Functions that only return something


def LabelPoint(point, label, position=DL*0.5, font_size=30, color=0):
    '''
        Adds label to a point

        Arguments - point(Dot), label(string)

        Optional - Position relative to the point=DL, font_size=25

        Returns - the Text mobject of label
    '''
    if color == 0:
        dot_color = point.get_color()
    else:
        dot_color = color
    label_point = MathTex(r'' + label, font_size=font_size, color=dot_color)
    label_point.next_to(point.get_center(), position)
    return label_point


def DistanceBetweenCoordinates(a, b):
    '''
        Calculates distance between 2 coordinates

        Arguments - a([x_1, y_1, z_1]), b([x_2, y_2, z_2])

        Returns - Distance (float)
    '''
    return np.sqrt(sum((np.array(a) - np.array(b))**2))


def DistanceBetweenPoints(A, B):
    '''
        Calculates distance between 2 Dots

        Arguments - A(Dot_1), B(Dot_2)

        Returns - Distance (float)
    '''
    return DistanceBetweenCoordinates(A.get_center(), B.get_center())


def SegmentLength(AB):
    '''
        Calculates the Length of a Segment

        Arguments - AB(Line)

        Returns - Length(float)
    '''
    a, b = AB.get_start_and_end()
    return DistanceBetweenCoordinates(a, b)


def SegmentEqualitySign1(AB, sign_size=0.2, color=WHITE):
    '''
        Equality sign with 1 small line in the middle of the segment

        Arguments - AB(Line)

        Optional - sign_size=0.2, Color=WHITE

        Returns - sign Mobject
    '''
    length_AB = SegmentLength(AB)
    sign = AB.copy()
    sign = sign.scale(sign_size / length_AB)
    sign = sign.set_color(color)
    sign = sign.rotate(PI / 2)

    return sign


def SegmentEqualitySign2(AB, sign_size=0.2, color=WHITE):
    '''
        Equality sign with 2 small lines for a segment

        Arguments - AB(Line)

        Optional - sign_size=0.2, Color=WHITE

        Returns - sign VGroup
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


def SegmentEqualitySign3(AB, sign_size=0.2, color=WHITE):
    '''
        Equality sign with 2 small lines for a segment

        Arguments - AB(Line)

        Optional - sign_size=0.2, color=WHITE

        Returns - sign VGroup
    '''
    a, b = AB.get_start_and_end()
    length_AB = np.sqrt(sum((np.array(a) - np.array(b))**2))
    unit_vector = AB.get_unit_vector()
    sign = AB.copy()
    sign = sign.scale(sign_size / length_AB)
    sign = sign.set_color(color)
    sign = sign.rotate(PI / 2)
    sign_1 = sign.copy().shift((unit_vector[0] * RIGHT + unit_vector[1] * UP) * 0.1)
    sign_2 = sign.copy().shift((-unit_vector[0] * RIGHT - unit_vector[1] * UP) * 0.1)
    sign = VGroup(sign_1, sign, sign_2)

    return sign


def CommonSegmentSign(AB, color=WHITE):
    '''
        Sign of common segment (\sim - S)
    '''
    sign = MathTex(r'\sim', font_size=70, color=color)
    sign.move_to(AB.get_midpoint())
    sin = AB.get_unit_vector()[1]
    cos = AB.get_unit_vector()[0]
    if cos > 0:
        sign.rotate(np.arcsin(sin))
    else:
        sign.rotate(PI - np.arcsin(sin))
    return sign


def FilledAngle(line_1, line_2, radius=0.4, quadrant=(1, 1), other_angle=False, color=WHITE, 
    stroke_width=0, stroke_color=WHITE, fill_opacity=1
):
    '''
        Returns angle sign filled with some color

        Arguments - same as Angle

        It also can ad stroke to the filled angle sign
    '''
    angle = Angle(line_1, line_2, radius=radius, quadrant=quadrant, other_angle=other_angle)

    intersection_point = line_intersection(line_1.get_start_and_end(), line_2.get_start_and_end())

    angle_points = angle.points
    side_1_points = Line(intersection_point, angle_points[0]).points
    side_2_points = Line(angle_points[-1], intersection_point).points

    points = np.concatenate([side_1_points, angle_points, side_2_points])

    filled_angle = VMobject().set_points_as_corners(points)
    filled_angle.set_stroke(color=stroke_color, width=stroke_width).set_fill(color=color, opacity=fill_opacity)

    return filled_angle


def Angle2(line_1, line_2, radius=0.4, quadrant=(1, 1), other_angle=False, stroke_width=4, color=WHITE):
    '''
        VGroup of 2 circular arcs representing an angle of two lines

        Arguments - same as Angle() # Expect of **kwargs

        Returns - Vgroup()
    '''
    a_1 = Angle(line_1, line_2, radius=radius, quadrant=quadrant, other_angle=other_angle, color=color, stroke_width=stroke_width)
    a_2 = Angle(line_1, line_2, radius=radius + 0.1, quadrant=quadrant, other_angle=other_angle, color=color, stroke_width=stroke_width)

    return VGroup(a_1, a_2)


def Angle3(line_1, line_2, radius=0.4, quadrant=(1, 1), other_angle=False, stroke_width=4, color=WHITE):
    '''
        VGroup of 3 circular arcs representing an angle of two lines

        Arguments - same as Angle() # Expect of **kwargs

        Returns - Vgroup()
    '''
    a_1 = Angle(line_1, line_2, radius=radius, quadrant=quadrant, other_angle=other_angle, color=color, stroke_width=stroke_width)
    a_2 = Angle(line_1, line_2, radius=radius + 0.1, quadrant=quadrant, other_angle=other_angle, color=color, stroke_width=stroke_width)
    a_3 = Angle(line_1, line_2, radius=radius + 0.2, quadrant=quadrant, other_angle=other_angle, color=color, stroke_width=stroke_width)

    return VGroup(a_1, a_2, a_3)


def MathtexSegmentsEquality(labels, font_size=30, color=WHITE):
    '''
        Writes 2 segments equality (AB=XY) in MathTex as a VGroup of 5 mobjects

        Argument - labels(list of 4 labels)

        Returns - MathTex('AB=CD')
    '''
    label_1_1, label_1_2, label_2_1, label_2_2 = labels

    segments_equality = MathTex(r'' + label_1_1, r'' + label_1_2, r'=', r'' + label_2_1, r'' + label_2_2, 
        font_size=font_size, color=color)

    return segments_equality


def MathtexCommonSegment(labels, font_size=30, color=WHITE):
    '''
        Writes segment is common (AB-ն ընդհանուր է) in MathTex as a VGroup of 3 Mobjects

        Arguments - labels (list of 2 labels)

        Returns - VGroup() from 3 MathTex mobjects ('A''B' '-ն ընդհանուր է') # 'AB is common'
    '''
    label_1, label_2 = labels
    
    AB = MathTex(r'' + label_1, r'' + label_2, font_size=font_size, color=color)

    is_common = MathTex(r'\textrm{-ն ընդհանուր է}', tex_template=armenian_tex_template, 
        font_size=font_size, color=color).next_to(AB, RIGHT, buff=0).shift(DOWN*0.04)

    segment_common = VGroup(*AB, is_common)
    
    return segment_common


def MathTexAnglesEquality(abc, xyz, font_size=30, color=WHITE):
    '''
        Angle <ABC=<XYZ
    ''' 
    return MathTex(r'\angle ' + abc, r'=', r'\angle ' + xyz, font_size=font_size, color=color)


def MathTexTrianglesEquality(abc, xyz, color=WHITE, font_size=30):
    '''
        MathTex Mobject 'ABC=XYZ'

        Arguments - abc('ABC'), xyz('XYZ')

        Returns - MathTex('ABC=XYZ)
    '''
    return VGroup(MathTex(r'\triangle ' + abc, r'=', r'\triangle ' + xyz, font_size=font_size, color=color))


def Rightarrow(font_size=45, color=WHITE):
    return MathTex(r'\Rightarrow', font_size=font_size, color=color)


def ConcludeFromStatementsSystem(statements, conclusion, position=RIGHT, rightarrow_size=45, individual_letters=True):
    '''
        Arranges statements under each other, puts Brace from the left, '=>' and the conclusion
        
        Arguments - statements (some sort of group of statements), conclusion
        
        Optional arguments - individual_letters (if True, returning VGroup will consists from submobjects of statements submobjects
        (usefull for animating triangles equality))

        Returns - VGroup of (statements, brace, =>, conclusion) - ' { statements => conclusion '
    '''
    statements = VGroup(*statements).arrange(DOWN, aligned_edge=LEFT)

    brace = Brace(statements, direction=[-1, 0, 0])

    rightarrow = Rightarrow(font_size=rightarrow_size, color=conclusion.get_color())
    rightarrow.next_to(statements, RIGHT)

    if position.any == RIGHT.any():
        conclusion.next_to(rightarrow, RIGHT)
    elif position.any() == DOWN.any():
        conclusion.next_to(brace, RIGHT).shift(DOWN*1.25)

    conclude_from_system = VGroup()

    if individual_letters:
        for i in range(len(statements)):
            conclude_from_system.add(*statements[i])

        conclude_from_system.add(brace, rightarrow, *conclusion)
    
    else:
        conclude_from_system.add(*statements, brace, rightarrow, conclusion)
    
    return conclude_from_system


def ConcludeFromSAS(statements, conclusion, position=RIGHT, rightarrow_size=45, individual_letters=True):
    '''
        Arranges statements under each other, puts Brace from the left, '=>', \triangle^{(1)} and the conclusion
        
        Arguments - statements (some sort of group of statements), conclusion
        
        Optional arguments - individual_letters (if True, returning VGroup will consists from submobjects of statements submobjects
        (usefull for animating triangles equality))

        Returns - VGroup of (statements, brace, =>, \triangle^{(1)} conclusion) - ' { statements => conclusion '
    '''
    conclude = ConcludeFromStatementsSystem(statements, conclusion, position, rightarrow_size, individual_letters)

    conclude_from_sas = VGroup(*conclude[:-1])
    sas = MathTex(r'\triangle ^ {(1)}', font_size=30)
    sas.next_to(conclude_from_sas[-1], UP, buff=0.15).shift(0.15*RIGHT)
    conclude_from_sas.add(sas)
    conclude_from_sas.add(conclude[-1])

    return conclude_from_sas


def ConcludeFromASA(statements, conclusion, position=RIGHT, rightarrow_size=45, individual_letters=True):
    '''
        Arranges statements under each other, puts Brace from the left, '=>', \triangle^{(2)} and the conclusion
        
        Arguments - statements (some sort of group of statements), conclusion
        
        Optional arguments - individual_letters (if True, returning VGroup will consists from submobjects of statements submobjects
        (usefull for animating triangles equality))

        Returns - VGroup of (statements, brace, =>, \triangle^{(2)} conclusion) - ' { statements => conclusion '
    '''
    conclude = ConcludeFromStatementsSystem(statements, conclusion, position, rightarrow_size, individual_letters)

    conclude_from_asa = VGroup(*conclude[:-1])
    asa = MathTex(r'\triangle ^ {(2)}', font_size=30)
    asa.next_to(conclude_from_asa[-1], UP, buff=0.15).shift(0.15*RIGHT)
    conclude_from_asa.add(asa)
    conclude_from_asa.add(conclude[-1])

    return conclude_from_asa


def ConcludeFromSSS(statements, conclusion, position=RIGHT, rightarrow_size=45, individual_letters=True):
    '''
        Arranges statements under each other, puts Brace from the left, '=>', \triangle^{(3)} and the conclusion
        
        Arguments - statements (some sort of group of statements), conclusion
        
        Optional arguments - individual_letters (if True, returning VGroup will consists from submobjects of statements submobjects
        (usefull for animating triangles equality))

        Returns - VGroup of (statements, brace, =>, \triangle^{(3)} conclusion) - ' { statements => conclusion '
    '''
    conclude = ConcludeFromStatementsSystem(statements, conclusion, position, rightarrow_size, individual_letters)

    conclude_from_sss = VGroup(*conclude[:-1])
    sss = MathTex(r'\triangle ^ {(3)}', font_size=30)
    sss.next_to(conclude_from_sss[-1], UP, buff=0.15).shift(0.15*RIGHT)
    conclude_from_sss.add(sss)
    conclude_from_sss.add(conclude[-1])

    return conclude_from_sss


def TransformSegmentLabelsIntoStatement(segment_dots_labels, statement, transform_segment=True, run_time=1):
    '''
        Animations for Transforming segment into a statement AB

        Arguments - segment_dots_labels(AB, A, B, label_A, label_B), statement ('A', 'B')

        Optional argument - transform_segment, run_time

        Returns list of 2 or 3 animations
    '''
    AB = segment_dots_labels[0].copy()
    A, B = segment_dots_labels[1].copy(), segment_dots_labels[2].copy()
    label_A, label_B = segment_dots_labels[3].copy(), segment_dots_labels[4].copy()
    
    AB_transformed = Dot((statement[0].get_center() + statement[1].get_center())/2,
        color=AB.get_color(), radius=0)
    
    transformation_labels = (
        ReplacementTransform(label_A, statement[0], rate_func=linear, run_time=run_time),
        ReplacementTransform(label_B, statement[1], rate_func=linear, run_time=run_time))

    transformation_segment = Transform(VGroup(AB, A, B), AB_transformed, run_time=run_time, rate_func=linear)

    if transform_segment == False:
        animations = [*transformation_labels]
    else:
        animations = [*transformation_labels, transformation_segment]

    return animations





# Functions that play some animations and return something



def CircleFromSpinningRadius(self, 
        radius=1, center=ORIGIN, starting_point_angle=0, 
        equality_sign=0, equality_sign_color=WHITE,
        radius_color=WHITE, circle_color=GREEN, direction=1, center_color=WHITE,
        create_center=True, create_radius=True, create_point=True, create_equality_sign=True,
        r_sign=MathTex(''), r_sign_angle=-30, run_time=4
):
    '''
        This function Creates a Circle using it's radius like a Compass Drawing tool (կարկին)

        Arguments - radius, center, point from which to start (angle in DEGREES), colors and run time

        Optional - starting_point_angle=0, radius_color(line color), circle_color, run_time=4

        Returns the Circle and the Center
    '''

    Center = always_redraw(lambda: Dot(center, color=center_color))
    circle = Circle(radius=radius, color=circle_color).move_to(center)

    moving_point_angle = ValueTracker(starting_point_angle)

    moving_point = always_redraw(lambda: 
        Dot(circle.point_at_angle((moving_point_angle.get_value() % 360) * DEGREES), color=circle_color))

    radius_line = always_redraw(lambda: 
        Line(center, circle.point_at_angle((moving_point_angle.get_value() % 360) * DEGREES), color=radius_color))

    if direction == 1:
        arc = always_redraw(lambda: 
            Arc(
                start_angle=starting_point_angle * DEGREES + 0.001, 
                angle=(moving_point_angle.get_value() - starting_point_angle) * DEGREES, 
                arc_center=center, radius=radius, color=circle_color))

    else:
        arc = always_redraw(lambda:
            Arc(
                start_angle=starting_point_angle * DEGREES + 0.001, 
                angle=(moving_point_angle.get_value() - starting_point_angle)*DEGREES,
                arc_center=center, radius=radius, color=circle_color))

    if equality_sign == 1:
        equality_sign_OR = always_redraw(lambda: SegmentEqualitySign1(radius_line, color=equality_sign_color))
    if equality_sign == 2:
        equality_sign_OR = always_redraw(lambda: SegmentEqualitySign2(radius_line, color=equality_sign_color))
    if equality_sign == 3:
        equality_sign_OR = always_redraw(lambda: SegmentEqualitySign3(radius_line, color=equality_sign_color))

    if len(r_sign) > 0:
        
        sign_r = always_redraw(lambda:
            r_sign.copy().next_to(
                (Center.get_center() + circle.point_at_angle(
                    ((moving_point_angle.get_value() + r_sign_angle)  % 360) * DEGREES)) / 2, buff=0))



    if create_center:
        self.play(Create(Center))
    else:
        self.add(Center)
    
    if create_radius:
        self.play(Create(radius_line))
    else:
        self.add(radius_line)
    self.add(Center)
    
    if equality_sign != 0:
        if create_equality_sign == True:
            self.play(Create(equality_sign_OR))
        else:
            self.add(equality_sign_OR)
    
    if create_point:
        self.play(Create(moving_point))
    else:
        self.add(moving_point_angle)
    
    if len(r_sign) > 0:
        self.play(Create(sign_r))

    self.wait(0.5)

    self.add(arc)

    if direction == 1:
        self.play(
            moving_point_angle.animate(run_time=run_time, rate_func=linear).set_value(starting_point_angle + 360))
    else:
        self.play(
            moving_point_angle.animate(run_time=run_time, rate_func=linear).set_value(starting_point_angle - 360))

    self.remove(arc)
    self.add(circle)


    if equality_sign != 0:
        if len(r_sign) > 0:
            self.play(
                Uncreate(moving_point), 
                Uncreate(radius_line), 
                Uncreate(equality_sign_OR),
                Uncreate(sign_r)
            )
        else:
            self.play(
                Uncreate(moving_point), 
                Uncreate(radius_line), 
                Uncreate(equality_sign_OR),
            )
    else:
        if len(r_sign) > 0:
            self.play(
                Uncreate(moving_point), 
                Uncreate(radius_line),
                Uncreate(sign_r)
            )
        else:
            self.play(
                Uncreate(moving_point), 
                Uncreate(radius_line),
            )

    return circle, Center






# Functions that only play some animations



def PlaySegmentWiggling(self, 
    segment_dots_labels, wiggle_endpoints=True, color=0, scale_factor=1.3, run_time=1.3
):
        '''
            Wiggles segment AB together with A and B (optional), and scales in and out Labels of A and B
            
            Arguments - self, (AB, A, B, label_A, label_B)

            Optional - wiggle_endpoints(True or False), color(default is the same as AB), scale_factor(label), run_time
        '''
        AB, A, B, label_A, label_B = segment_dots_labels
        a, b = A.copy(), B.copy()

        if color == 0:
            ab = AB.copy()
        else:
            ab = AB.copy().set_color(color=color)
        
        if wiggle_endpoints == True:

            self.play(
                Wiggle(VGroup(ab, a, b), rate_func=linear),
                label_A.animate(rate_func=there_and_back).scale(scale_factor), 
                label_B.animate(rate_func=there_and_back).scale(scale_factor),
                run_time=run_time
            )
        
        else:

            self.play(
                Wiggle(ab, rate_func=linear),
                label_A.animate(rate_func=there_and_back).scale(scale_factor), 
                label_B.animate(rate_func=there_and_back).scale(scale_factor),
                run_time=run_time
            )
        
        self.remove(a, b, ab)



def PlayTwoSegmentsWiggling(self, 
    segment_dots_labels_1, segment_dots_labels_2, wiggle_endpoints=True, 
    simultaneously=True, color=0, scale_factor=1.3, run_time=1.3
):
        '''
            SegmentWiggling for AB and XY
            
            Arguments - self, AB, XY, (A, B, X, Y), (label_A, label_B, label_X, label_Y)

            Optional - wiggle_endpoints, simultaneously(True or False), color(same as AB), scale_factor(label), 
            run_time (for each wiggling)
        '''

        A, B = segment_dots_labels_1[1].copy(), segment_dots_labels_1[2].copy()
        X, Y = segment_dots_labels_2[1].copy(), segment_dots_labels_2[2].copy()

        label_A, label_B = segment_dots_labels_1[3], segment_dots_labels_1[4]
        label_X, label_Y = segment_dots_labels_2[3], segment_dots_labels_2[4]

        if color == 0:
            ab, xy = segment_dots_labels_1[0].copy(), segment_dots_labels_2[0].copy()
        else:
            ab, xy = segment_dots_labels_1[0].copy().set_color(color=color), segment_dots_labels_2[0].copy().set_color(color=color)


        if not simultaneously:
        
            PlaySegmentWiggling(self, segment_dots_labels_1, wiggle_endpoints=wiggle_endpoints, 
                color=color, scale_factor=scale_factor, run_time=run_time)
            self.wait(0.2)
            PlaySegmentWiggling(self, segment_dots_labels_2, wiggle_endpoints=wiggle_endpoints, 
                color=color, scale_factor=scale_factor, run_time=run_time)
        
        else:  
            if wiggle_endpoints:
                
                self.play(
                    Wiggle(VGroup(ab, A, B), rate_func=linear),
                    label_A.animate(rate_func=there_and_back).scale(scale_factor), 
                    label_B.animate(rate_func=there_and_back).scale(scale_factor),
                    Wiggle(VGroup(xy, X, Y), rate_func=linear),
                    label_X.animate(rate_func=there_and_back).scale(scale_factor), 
                    label_Y.animate(rate_func=there_and_back).scale(scale_factor),
                    run_time=run_time
                )

            else:

                self.play(
                    Wiggle(ab, rate_func=linear),
                    label_A.animate(rate_func=there_and_back).scale(scale_factor), 
                    label_B.animate(rate_func=there_and_back).scale(scale_factor),
                    Wiggle(xy, rate_func=linear),
                    label_X.animate(rate_func=there_and_back).scale(scale_factor), 
                    label_Y.animate(rate_func=there_and_back).scale(scale_factor),
                    run_time=run_time
                )
            
        self.remove(A, B, ab, X, Y, xy)



def PlaySegmentThickening(self, 
    segment_dots_labels, thicken_endpoints=True, color=0, scale_factor=1.3, run_time=1.3
):
        '''
            Thickens segment AB together with A and B (optional), and scales in and out Labels of A and B
            
            Arguments - self, (AB, A, B, label_A, label_B)

            Optional - thicken_endpoints(True or False), color(default is the same as AB), scale_factor(label), run_time
        '''
        AB, A, B, label_A, label_B = segment_dots_labels
        if color == 0:
            color = AB.get_color()

        if thicken_endpoints:

            self.play(
                AB.animate(rate_func=there_and_back).set_stroke(color=color, width=8),
                A.animate(rate_func=there_and_back).scale(1.5),
                B.animate(rate_func=there_and_back).scale(1.5),
                label_A.animate(rate_func=there_and_back).scale(scale_factor), 
                label_B.animate(rate_func=there_and_back).scale(scale_factor),
                run_time=run_time
            )
        
        else:

            self.play(
                AB.animate(rate_func=there_and_back).set_stroke(color=color, width=8),
                label_A.animate(rate_func=there_and_back).scale(scale_factor), 
                label_B.animate(rate_func=there_and_back).scale(scale_factor),
                run_time=run_time
            )



def PlayTwoSegmentsThickening(self, 
    segment_dots_labels_1, segment_dots_labels_2, thicken_endpoints=True, 
    simultaneously=True, color=0, scale_factor=1.3, run_time=1.3
):
        '''
            blabla
        '''
        AB, A, B, label_A, label_B = segment_dots_labels_1
        XY, X, Y, label_X, label_Y = segment_dots_labels_2

        if color == 0:
            ab_color = AB.get_color()
            xy_color = XY.get_color()
        else:
            ab_color = color
            xy_color = color
        
        if not simultaneously:
            PlaySegmentThickening(self, segment_dots_labels_1, thicken_endpoints=thicken_endpoints, 
                scale_factor=scale_factor, color=ab_color, run_time=run_time/2)
            self.wait(0.2)
            PlaySegmentThickening(self, segment_dots_labels_2, thicken_endpoints=thicken_endpoints, 
                scale_factor=scale_factor, color=xy_color, run_time=run_time/2)
        
        else: 
            if thicken_endpoints:
                self.play(
                    AB.animate(rate_func=there_and_back).set_stroke(color=ab_color, width=8),
                    A.animate(rate_func=there_and_back).scale(1.5),
                    B.animate(rate_func=there_and_back).scale(1.5),
                    label_A.animate(rate_func=there_and_back).scale(scale_factor), 
                    label_B.animate(rate_func=there_and_back).scale(scale_factor),
                    XY.animate(rate_func=there_and_back).set_stroke(color=xy_color, width=8),
                    X.animate(rate_func=there_and_back).scale(1.5),
                    Y.animate(rate_func=there_and_back).scale(1.5),
                    label_X.animate(rate_func=there_and_back).scale(scale_factor), 
                    label_Y.animate(rate_func=there_and_back).scale(scale_factor),
                    run_time=run_time
                )

            else:
                self.play(
                    AB.animate(rate_func=there_and_back).set_stroke(color=ab_color, width=8),
                    A.animate(rate_func=there_and_back).scale(1.5),
                    B.animate(rate_func=there_and_back).scale(1.5),
                    XY.animate(rate_func=there_and_back).set_stroke(color=xy_color, width=8),
                    X.animate(rate_func=there_and_back).scale(1.5),
                    Y.animate(rate_func=there_and_back).scale(1.5),
                    run_time=run_time
                )



def PlayAnglesWiggling(self,
    angle_1, angle_2=False, run_time=2
):
    if angle_2:
        self.play(
            Wiggle(angle_1, scale_value=1.3, rotation_angle=0.05*TAU),
            Wiggle(angle_2, scale_value=1.3, rotation_angle=0.05*TAU),
            run_time=run_time
        )
    
    else:
        self.play(Wiggle(angle_1, scale_value=1.3, rotation_angle=0.05*TAU), run_time=run_time)
    



def PlayTransformSegmentsLabelsIntoEquality(self, 
    segment_dots_labels_1, segment_dots_labels_2, equality, 
    transform_segments=True, transform_simultaneously=True, run_time=1.5
):
    '''
        ReplacementTransforms segments into equality AB=XY

        Arguments - self, segment_dots_labels_1, segment_dots_labels_2, equality MathTex('A','B','=','X','Y')

        Optional argument - transform_segments, transform_simultaneously, run_time
    '''
    transformation_AB = TransformSegmentLabelsIntoStatement(segment_dots_labels_1, equality[0:2],
        transform_segment=transform_segments, run_time=run_time)

    write_equal = Write(equality[2])
    
    transformation_XY = TransformSegmentLabelsIntoStatement(segment_dots_labels_2, equality[3:5], 
        transform_segment=transform_segments, run_time=run_time)

    if not transform_simultaneously: 

        self.play(*transformation_AB)
        self.play(write_equal)
        self.play(*transformation_XY)
    
    else:

        self.play(*transformation_AB, *transformation_XY)
        self.play(write_equal)



def PlayTransformCommonSegmentLabelsIntoStatement(self, 
    segment_dots_labels, statement, transform_segment=True, run_time=1.5
):

    transformation_AB = TransformSegmentLabelsIntoStatement(segment_dots_labels, statement[0:2], 
        transform_segment=transform_segment, run_time=run_time)
    
    write_common = Write(statement[2])

    animations = [*transformation_AB, write_common]

    if transform_segment:
        self.play(animations[0], animations[1], animations[2])
        self.play(animations[3])
    
    else:
        self.play(animations[0], animations[1])
        self.play(animations[2])



def PlayTwoSegmentsEqualityWiggling(self, 
    pair, equality, color=0, wiggle_simultaneously=True, 
    wiggle_endpoints=True, transform_simultaneously=True, transform_segments=True, run_time=2.5
):
        '''
            Wiggles 2 segments and transforms into AB=XY

            Arguments - pair((AB, A, B, label_A, label_B), (XY, X, Y, label_X, label_Y)) input for TwoSegmentsWiggling;
            equality(MathTex from 5 Mobjects  AB=XY)
        '''
        PlayTwoSegmentsWiggling(self, *pair, color=color,
                simultaneously=wiggle_simultaneously, wiggle_endpoints=wiggle_endpoints, run_time=run_time/2)
        
        PlayTransformSegmentsLabelsIntoEquality(self, pair[0], pair[1], equality=equality,
            transform_simultaneously=transform_simultaneously, transform_segments=transform_segments, run_time=run_time/2
        )



def PlaySegmentIsCommonWiggling(self, 
    segment_dots_labels, statement, sign=0, color=0, wiggle_endpoints=True, transform_segment=True, run_time=2.5
):

    PlaySegmentWiggling(self, 
        segment_dots_labels, wiggle_endpoints=wiggle_endpoints, color=color, run_time=run_time/2
    )

    if sign != 0:
        self.play(Create(sign))

    PlayTransformCommonSegmentLabelsIntoStatement(self,
        segment_dots_labels, statement=statement, transform_segment=transform_segment, run_time=run_time/2
    )
    


def PlayTwoSegmentsEqualityThickening(self, 
    pair, equality, color=0, thicken_simultaneously=True, 
    thicken_endpoints=True, transform_simultaneously=True, transform_segments=True, run_time=2.5
):
        '''
            Makes 2 segments thicker than thinner and transforms into AB=XY

            Arguments - pair((AB, A, B, label_A, label_B), (XY, X, Y, label_X, label_Y))
            equality(MathTex from 5 Mobjects  AB=XY)
        '''
        PlayTwoSegmentsThickening(self, *pair, color=color, 
            simultaneously=thicken_simultaneously, thicken_endpoints=thicken_endpoints, run_time=run_time/2)
        
        PlayTransformSegmentsLabelsIntoEquality(self, pair[0], pair[1], equality=equality,
            transform_simultaneously=transform_simultaneously, transform_segments=transform_segments, run_time=run_time/2
        )



def PlaySegmentIsCommonThickening(self, 
    segment_dots_labels, statement, color=0, thicken_endpoints=True, transform_segment=True, run_time=2.5
):
    
    PlaySegmentThickening(self, 
        segment_dots_labels, thicken_endpoints=thicken_endpoints, color=color, run_time=run_time/2
    )

    PlayTransformCommonSegmentLabelsIntoStatement(self,
        segment_dots_labels, statement=statement, transform_segment=transform_segment, run_time=run_time/2
    )



def PlayTwoAnglesEqualityWiggling(self, 
    angle_sign_1, angle_sign_2, equality, color=0, 
    transform_simultaneously=True, wiggle_simultaneously=True, run_time=4
):
    '''
    '''
    if color == 0:
        color_1 = angle_sign_1.get_color()
        color_2 = angle_sign_2.get_color()
    else:
        color_1 = color
        color_2 = color

    copy_angle_1 = angle_sign_1.copy().set_color(color_1)
    copy_angle_2 = angle_sign_2.copy().set_color(color_2)

    wiggling = [
            Wiggle(copy_angle_1, rotation_angle=0.08*TAU, scale_value=1.3, run_time=run_time*0.625),
            Wiggle(copy_angle_2, rotation_angle=0.08*TAU, scale_value=1.3, run_time=run_time*0.625)
    ]

    transformations = [
        ReplacementTransform(angle_sign_1.copy(), equality[0]),
        Write(equality[1]),
        ReplacementTransform(angle_sign_2.copy(), equality[2])
    ]

    if wiggle_simultaneously:
        self.play(*wiggling, run_time=run_time/2)
    else:
        self.play(wiggling[0], run_time=run_time/4)
        self.play(wiggling[1], run_time=run_time/4)
    
    self.remove(copy_angle_1, copy_angle_2)
    
    if transform_simultaneously:
        self.play(transformations[0], transformations[2], run_time=run_time*0.375)
        self.play(transformations[1])
    else:
        self.play(transformations[0], run_time=run_time*0.1875)
        self.play(transformations[1])
        self.play(transformations[2], run_time=run_time*0.1875)



def PlayTwoAnglesEqualityThickening(self, 
    angle_sign_1, angle_sign_2, equality, color=0, 
    transform_simultaneously=True, thicken_simultaneously=True, run_time=3
):
    '''
    '''
    if color == 0:
        color_1 = angle_sign_1.get_color()
        color_2 = angle_sign_2.get_color()
    else:
        color_1 = color
        color_2 = color
    
    thickening = [
        angle_sign_1.animate(rate_func=there_and_back).set_stroke(color=color_1, width=8),
        angle_sign_2.animate(rate_func=there_and_back).set_stroke(color=color_2, width=8)
    ]

    transformations = [
        ReplacementTransform(angle_sign_1.copy(), equality[0]),
        Write(equality[1]),
        ReplacementTransform(angle_sign_2.copy(), equality[2])
    ]
    
    if thicken_simultaneously:
        self.play(*thickening, run_time=run_time/2)
    else:
        self.play(thickening[0], run_time=run_time/4)
        self.play(thickening[1], run_time=run_time/4)

    if transform_simultaneously:
        self.play(transformations[0], transformations[2], run_time=run_time/2)
        self.play(transformations[1])
    else:
        self.play(transformations[0], run_time=run_time/4)
        self.play(transformations[1])
        self.play(transformations[2], run_time=run_time/4)



def PlayBraceConclude(self, 
    conclude_from_system, conclusion_run_time=2
):
    '''
        From ConcludeFromSAS (or ASA or SSS) animates drawing Brace, rightarrow and conclusion

        Arguments - conclude_from_system(last 3 elements must be brace, rightarrow and conclusion respectively)
    '''
    self.play(Write(conclude_from_system[-3]))
    self.wait(0.2)
    self.play(Write(conclude_from_system[-2]))
    self.wait(0.2)
    self.play(Write(conclude_from_system[-1]), run_time=conclusion_run_time)



def PlayConcludeTriangleCongruence(self,
    conclude_from_statements, rightarrow_run_time=2, conclusion_run_time=2
):
    '''
        From ConcludeFromStatementsSystem animates drawing Brace, rightarrow, \triangle^{()} and conclusion

        Arguments - conclude_from_system(last 4 elements must be brace, rightarrow, \triangle^{()} and conclusion respectively)
    '''
    self.play(Write(conclude_from_statements[-4]))
    self.wait(0.2)
    self.play(Write(conclude_from_statements[-3]), Write(conclude_from_statements[-2]), run_time=rightarrow_run_time)
    self.wait(0.2)
    self.play(Write(conclude_from_statements[-1]), run_time=conclusion_run_time)





class TrianglesCongruence(Scene):


    def SSS( 
        vertices_ABC, sides_ABC, mob_labels_ABC, labels_ABC, 
        vertices_XYZ, sides_XYZ, mob_labels_XYZ, labels_XYZ, 
        brace_tip=[0, 0, 0], common=0,
        return_extras=False
    ):
            '''
                Equality of two triangles by their 3 sides in system - { sides_equalities => triangle_equality

                if there is a common side, that will be last,
                others are in order

                Arguments - vertices_ABC(A, B, C), sides_ABC (AB, BC, AC(order matters)), 
                mob_labels_ABC(mobjects, preferably from LabelPoint()), labels_ABC('A', 'B', 'C'), 
                same things for second triangle(XYZ), 
                brace_tip(left middle point of system of equalities), 
                common(if triangles have a common side - side of the first triangle(BC))

                Returns - VGroup of mobjects (same as ConcludeFromSystem)

                IF return everything=True then returns system and some extra things for PlaySSS functions
            '''
        # Read points lables,    
            A, B, C = vertices_ABC
            AB, BC, CA = sides_ABC
            label_a, label_b, label_c = labels_ABC
            label_A, label_B, label_C = mob_labels_ABC
            X, Y, Z = vertices_XYZ
            XY, YZ, ZX = sides_XYZ
            label_x, label_y, label_z = labels_XYZ
            label_X, label_Y, label_Z = mob_labels_XYZ

            abc = label_a + label_b + label_c
            xyz = label_x + label_y + label_z

            fs = label_A.font_size

        # pairs (equal sides)
            pair_AB_XY = ((AB, A, B, label_A, label_B), (XY, X, Y, label_X, label_Y))
            pair_BC_YZ = ((BC, B, C, label_B, label_C), (YZ, Y, Z, label_Y, label_Z))
            pair_CA_ZX = ((CA, C, A, label_C, label_A), (ZX, Z, X, label_Z, label_X))
            pairs = [pair_AB_XY, pair_BC_YZ, pair_CA_ZX]

        # labels pairs
            abxy_labels = (label_a, label_b, label_x, label_y)
            bcyz_labels = (label_b, label_c, label_y, label_z)
            cazx_labels = (label_c, label_a, label_z, label_x)
            labels_pairs = [abxy_labels, bcyz_labels, cazx_labels]

        # singles (for common side)
            ABAB = (AB, A, B, label_A, label_B)
            BCBC = (BC, B, C, label_B, label_C)
            CACA = (CA, C, A, label_C, label_A)
            singles = [ABAB, BCBC, CACA]

        # labels singles
            ab_labels = (label_a, label_b)
            bc_labels = (label_b, label_c)
            ca_labels = (label_c, label_a)
            labels_singles = [ab_labels, bc_labels, ca_labels]

        # MathTex equalities
            ab_xy = MathtexSegmentsEquality(labels_pairs[0], font_size=fs)
            bc_yz = MathtexSegmentsEquality(labels_pairs[1], font_size=fs)
            ca_zx = MathtexSegmentsEquality(labels_pairs[2], font_size=fs)
            
            ab_common = MathtexCommonSegment(labels_singles[0], font_size=fs)
            bc_common = MathtexCommonSegment(labels_singles[1], font_size=fs)
            ca_common = MathtexCommonSegment(labels_singles[2], font_size=fs)

        # Equality system
            
            if common == 0:
                equalities = VGroup(ab_xy, bc_yz, ca_zx)
                common_index = 0

            if common == AB:
                equalities = VGroup(bc_yz, ca_zx, ab_common)
                common_index = 1

            if common == BC:
                equalities = VGroup(ab_xy, ca_zx, bc_common)
                common_index = 2
                
            if common == CA:
                equalities = VGroup(ab_xy, bc_yz, ca_common)
                common_index = 13
            
            triangle_equality = MathTexTrianglesEquality(abc, xyz, font_size=fs)

            conclude_from_system = ConcludeFromStatementsSystem(equalities, triangle_equality, individual_letters=True)
            conclude_from_system.next_to(brace_tip, RIGHT, buff=0)

        # return
            if return_extras:
                return conclude_from_system, (pairs, singles, equalities, common_index)
            else:
                return conclude_from_system




    def PlaySSSWiggling(self, 
        conclude_from_system, extras,
        wiggle_endpoints=[True, True, True], wiggle_simultaneously=[True, True, True],
        transform_simultaneously=[True, True, True], 
        colors=[0, 0, 0], run_times=[3, 3, 3], wait_time=[1, 1, 1]
    ):
            '''
                Shows and writes equality of two triangles by their 3 sides by wiggling them,
                if there is a common side, that will be shown last,
                others are animated in order

                Arguments - vertices_ABC(A, B, C), sides_ABC (AB, BC, AC(order matters)), mob_labels_ABC(mobjects, preferably from LabelPoint()), 
                labels_ABC('A', 'B', 'C'), same things for second triangle(XYZ), brace_tip(left middle point of system of equalities), 
                common(if triangles have a common side - side of the first triangle(BC)), 
                wiggle_endpoints(list - True or False for each side), 
                wiggle_simultaneously(2 equal sides(list - True or False for each side)), 
                color(change color of the side while wiggling(list - 0 or color for each side)), 
                run_time(animations of sides(list)), wait_time(pause between animations of sides, or final brace(list))

                Returns - VGroup of mobjects (same as ConcludeFromSystem)
            '''
        # INITS

            (pairs, singles, equalities, common_index) = extras

            if common_index == 0:
                sequence = pairs

            if common_index == 1:
                sequence = [pairs[1], pairs[2], singles[0]]
                colors = [colors[1], colors[2], colors[0]]
                wiggle_endpoints = [wiggle_endpoints[1], wiggle_endpoints[2], wiggle_endpoints[0]]
                wiggle_simultaneously = [wiggle_simultaneously[1], wiggle_simultaneously[2], wiggle_simultaneously[0]]
                transform_simultaneously = [transform_simultaneously[1], transform_simultaneously[2], transform_simultaneously[0]]

            if common_index == 2:
                sequence = [pairs[0], pairs[2], singles[1]]
                colors = [colors[0], colors[2], colors[1]]
                wiggle_endpoints = [wiggle_endpoints[0], wiggle_endpoints[2], wiggle_endpoints[1]]
                wiggle_simultaneously = [wiggle_simultaneously[0], wiggle_simultaneously[2], wiggle_simultaneously[1]]
                transform_simultaneously = [transform_simultaneously[0], transform_simultaneously[2], transform_simultaneously[1]]
                
            if common_index == 3:
                sequence = [pairs[0], pairs[1], singles[2]]

        # Animations

            for i in range(2):
                PlayTwoSegmentsEqualityWiggling(self, 
                    sequence[i], equalities[i], color=colors[i], 
                    wiggle_simultaneously=wiggle_simultaneously[0], wiggle_endpoints=wiggle_endpoints[i], 
                    transform_simultaneously=transform_simultaneously[i], run_time=run_times[i]
                )
                self.wait(wait_time[i])
            
            if common_index == 0:
                PlayTwoSegmentsEqualityWiggling(self, 
                    sequence[2], equalities[2], color=colors[2], 
                    wiggle_simultaneously=wiggle_simultaneously[2], wiggle_endpoints=wiggle_endpoints[2], 
                    transform_simultaneously=transform_simultaneously[2], run_time=run_times[2]
                )

            else:
                PlaySegmentIsCommonWiggling(self, 
                    sequence[2], equalities[2], color=colors[2], 
                    wiggle_endpoints=wiggle_endpoints[2], run_time=run_times[2]
                )
                self.wait(wait_time[2])

            PlayBraceConclude(self, conclude_from_system)




    def PlaySSSThickening(self, 
        conclude_from_system, extras,
        thicken_endpoints=[True, True, True], thicken_simultaneously=[True, True, True], 
        transform_simultaneously=[True, True, True], 
        colors=[0, 0, 0], run_times=[3, 3, 3], wait_time=[1, 1, 1]
    ):
            '''
                Shows and writes equality of two triangles by their 3 sides by thickening them,
                if there is a common side, that will be shown last,
                others are animated in order
            '''
        # INITS

            (pairs, singles, equalities, common_index) = extras


            if common_index == 0:
                sequence = pairs

            if common_index == 1:
                sequence = [pairs[1], pairs[2], singles[0]]
                colors = [colors[1], colors[2], colors[0]]
                thicken_endpoints = [thicken_endpoints[1], thicken_endpoints[2], thicken_endpoints[0]]
                thicken_simultaneously = [thicken_simultaneously[1], thicken_simultaneously[2], thicken_simultaneously[0]]
                transform_simultaneously = [transform_simultaneously[1], transform_simultaneously[2], transform_simultaneously[0]]

            if common_index == 2:
                sequence = [pairs[0], pairs[2], singles[1]]
                colors = [colors[0], colors[2], colors[1]]
                thicken_endpoints = [thicken_endpoints[0], thicken_endpoints[2], thicken_endpoints[1]]
                thicken_simultaneously = [thicken_simultaneously[0], thicken_simultaneously[2], thicken_simultaneously[1]]
                transform_simultaneously = [transform_simultaneously[0], transform_simultaneously[2], transform_simultaneously[1]]
                
            if common_index == 3:
                sequence = [pairs[0], pairs[1], singles[2]]

        # Animations

            for i in range(2):
                PlayTwoSegmentsEqualityThickening(self, 
                    sequence[i], equalities[i], color=colors[i], 
                    thicken_simultaneously=thicken_simultaneously[0], thicken_endpoints=thicken_endpoints[i], 
                    transform_simultaneously=transform_simultaneously[i], run_time=run_times[i]
                )
                self.wait(wait_time[i])
            
            if common_index == 0:
                PlayTwoSegmentsEqualityThickening(self, 
                    sequence[2], equalities[2], color=colors[2], 
                    thicken_simultaneously=thicken_simultaneously[2], thicken_endpoints=thicken_endpoints[2], 
                    transform_simultaneously=transform_simultaneously[2], run_time=run_times[2]
                )

            else:
                PlaySegmentIsCommonThickening(self, 
                    sequence[2], equalities[2], color=colors[2], 
                    thicken_endpoints=thicken_endpoints[2], run_time=run_times[2]
                )
                self.wait(wait_time[2])

            PlayBraceConclude(self, conclude_from_system)







class test(Scene):
    def construct(self):

    # init ABC XYZ points, segments, labels, MathTex equalities
        a = [-5, 0.5, 0]
        b = [-4, 2.5, 0]
        c = [-1, 0.5, 0]
        x = [-5, -2.5, 0]
        y = [-4, -0.5, 0]
        z = [-1, -2.5, 0]

        A = Dot(a)
        B = Dot(b)
        C = Dot(c)
        vertices_1 = [A, B, C]
        X = Dot(x)
        Y = Dot(y)
        Z = Dot(z)
        vertices_2 = [X, Y, Z]

        AB = always_redraw(lambda: Line(A.get_center(), B.get_center()))
        BC = always_redraw(lambda: Line(B.get_center(), C.get_center(), color=BLUE))
        CA = always_redraw(lambda: Line(C.get_center(), A.get_center()))
        sides_1 = [AB, BC, CA]
        XY = always_redraw(lambda: Line(X.get_center(), Y.get_center()))
        YZ = always_redraw(lambda: Line(Y.get_center(), Z.get_center(), color=GREEN))
        ZX = always_redraw(lambda: Line(Z.get_center(), X.get_center()))
        sides_2 = [XY, YZ, ZX]

        label_a = 'A'
        label_b = 'B'
        label_c = 'C'
        label_A = always_redraw(lambda: LabelPoint(A, label_a))
        label_B = always_redraw(lambda: LabelPoint(B, label_b, UP*0.75))
        label_C = always_redraw(lambda: LabelPoint(C, label_c, DR*0.5))
        labels_1 = [label_a, label_b, label_c]
        mob_labels_1  = [label_A, label_B, label_C]


        label_x = 'X_1'
        label_y = 'Y_1'
        label_z = 'Z_1'
        label_X = always_redraw(lambda: LabelPoint(X, label_x))
        label_Y = always_redraw(lambda: LabelPoint(Y, label_y, UP*0.75))
        label_Z = always_redraw(lambda: LabelPoint(Z, label_z, DR*0.5))
        labels_2 = [label_x, label_y, label_z]
        mob_labels_2 = [label_X, label_Y, label_Z]

        abc = label_a + label_b + label_c
        xyz = label_x + label_y + label_z

        triangle_ABC = [vertices_1, sides_1, mob_labels_1, labels_1]
        triangle_XYZ = [vertices_2, sides_2, mob_labels_2, labels_2]

        equality_AB_XY = MathtexSegmentsEquality((label_a, label_b, label_x, label_y))
        equality_BC_YZ = MathtexSegmentsEquality((label_b, label_c, label_y, label_z))
        equality_CA_ZX = MathtexSegmentsEquality((label_c, label_a, label_z, label_x))

        segment_AB = (AB, A, B, label_A, label_B)
        segment_BC = (BC, B, C, label_B, label_C)
        segment_CA = (CA, C, A, label_C, label_A)

        segment_XY = (XY, X, Y, label_X, label_Y)
        segment_YZ = (YZ, Y, Z, label_Y, label_Z)
        segment_ZX = (ZX, Z, X, label_Z, label_X)

        angle_CAB = Angle(CA, AB, quadrant=(-1, 1))
        angle_ABC = Angle2(AB, BC, quadrant=(-1, 1))
        angle_BCA = Angle3(BC, CA, quadrant=(-1, 1))
        angles_ABC = VGroup(angle_CAB, angle_ABC, angle_BCA)

        angle_ZXY = Angle(ZX, XY, quadrant=(-1, 1))
        angle_XYZ = Angle2(XY, YZ, quadrant=(-1, 1))
        angle_YZX = Angle3(YZ, ZX, quadrant=(-1, 1))
        angles_XYZ = VGroup(angle_ZXY, angle_XYZ, angle_YZX)

    # animations

        self.add(*triangle_ABC[1], *triangle_ABC[0], *triangle_ABC[2])
        self.add(*triangle_XYZ[1], *triangle_XYZ[0], *triangle_XYZ[2])
        self.add(angles_ABC, angles_XYZ)

        triangles_equality, extras = TrianglesCongruence.SSS(
            *triangle_ABC, *triangle_XYZ, common=BC, brace_tip=[1, 1, 0], return_extras=True)

        common_sign_BC = CommonSegmentSign(BC)
        common_sign_AB = CommonSegmentSign(AB)
        common_sign_CA = CommonSegmentSign(CA)
        self.add(common_sign_CA, common_sign_AB, common_sign_BC)
        




class test_(Scene):
    def construct(self):

    # init ABC isoscale triangle CA=CB and H midpoint of AB
        a = [2, 0, 0]
        b = [4, 0, 0]
        c = [3, 3, 0]
        h = [3, 0, 0]

        label_a = 'A'
        label_b = 'B'
        label_c = 'C'
        label_h = 'H'

        A = Dot(a)
        B = Dot(b)
        C = Dot(c)
        H = Dot(h)

        label_A = LabelPoint(A, label_a)
        label_B = LabelPoint(B, label_b, DR*0.5)
        label_C = LabelPoint(C, label_c, UL*0.5)
        label_H = LabelPoint(H, label_h, DR*0.5)


        AB = Line(a, b)
        HB = Line(h, b)
        HA = Line(h, a)
        AC = Line(a, c)
        BC = Line(b, c)
        CH = Line(c, h)

        labels_ACH = [label_a, label_c, label_h]
        vertices_ACH = [A, C, H]
        mob_labels_ACH = [label_A, label_C, label_H]
        sides_ACH = [AC, CH, HA]
        triangle_ACH = [vertices_ACH, sides_ACH, mob_labels_ACH, labels_ACH]

        labels_BCH = [label_b, label_c, label_h]
        vertices_BCH = [B, C, H]
        mob_labels_BCH = [label_B, label_C, label_H]
        sides_BCH = [BC, CH, HB]
        triangle_BCH = [vertices_BCH, sides_BCH, mob_labels_BCH, labels_BCH]

        angle_CHA = RightAngle(CH, HA, quadrant=(-1, 1), length=0.3)
        angle_CHB = RightAngle(CH, HB, quadrant=(-1, 1), length=0.4)

        segment_HA = VGroup(HA, H, A, label_H, label_A)
        segment_HB = VGroup(HB, H, B, label_H, label_B)
        segment_CH = VGroup(CH, C, H, label_C, label_H)


    # init MathTex 
        HA_HB = MathtexSegmentsEquality([label_h, label_a, label_h, label_b])
        ch_is_common = MathtexCommonSegment([label_c, label_h])
        angles_CHA_CHB = MathTexAnglesEquality(label_c+label_h+label_a, label_c+label_h+label_b)
        triangles_equality_ACH_BCH = MathTexTrianglesEquality(label_a+label_c+label_h, label_b+label_c+label_h)

        ACH_BCH_equality = ConcludeFromStatementsSystem([HA_HB, ch_is_common, angles_CHA_CHB], triangles_equality_ACH_BCH)
        ACH_BCH_equality.shift(4*LEFT)

    # animations
        self.add(*triangle_ACH[1], *triangle_ACH[0], *triangle_ACH[2])
        self.add(*triangle_BCH[1], *triangle_BCH[0], *triangle_BCH[2])
        self.add(angle_CHA, angle_CHB)

        self.wait(1)
        PlayTwoSegmentsEqualityWiggling(self, (segment_HA, segment_HB), HA_HB, color=ORANGE)
        PlaySegmentIsCommonThickening(self, segment_CH, ch_is_common)
        PlayTwoAnglesEqualityWiggling(self, angle_CHA, angle_CHB, angles_CHA_CHB, color=RED,
            wiggle_simultaneously=True, transform_simultaneously=True)
        PlayBraceConclude(self, ACH_BCH_equality)
        self.wait(0.5)





        # SSS
        # ACH_BCH_equality = TrianglesCongruence.SSS(*triangle_ACH, *triangle_BCH, brace_tip=[-6, 0, 0])
        # self.play(Write(ACH_BCH_equality, run_time=5))

