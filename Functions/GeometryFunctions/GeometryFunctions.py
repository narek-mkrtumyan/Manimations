from manim import *
import numpy as np


armenian_tex_template = TexTemplate()
armenian_tex_template.add_to_preamble(r"\usepackage{armtex}")



# Functions that return something


def LabelPoint(point, label, position=DL*0.5, font_size=30):
    '''
    Adds label to a point

    Arguments - point(Dot), label(string)

    Optional - Position relative to the point=DL, font_size=25

    Returns - the Text mobject of label
    '''
    label_point = MathTex(r'' + label, font_size=font_size, color=point.get_color())
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
    a, b = AB.get_start_and_end()
    length_AB = np.sqrt(sum((np.array(a) - np.array(b))**2))
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


def FilledAngle(line_1, line_2, radius=0.4, quadrant=(1, 1), other_angle=False, stroke_width=0, stroke_color=WHITE, 
    color=WHITE, fill_opacity=1):
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
        font_size=font_size, color=color).next_to(AB, RIGHT, buff=0)

    segment_common = VGroup(*AB, is_common)
    
    return segment_common


def MathTexTrianglesEquality(abc, xyz, color=WHITE, font_size=30):
    '''
    MathTex Mobject 'ABC=XYZ'

    Arguments - abc('ABC'), xyz('XYZ')

    Returns - MathTex('ABC=XYZ)
    '''
    return MathTex(r'\triangle ' + abc + r'\ =\ ' + r'\triangle ' + xyz, font_size=font_size, color=color)


def ConcludeFromStatementSystem(statements, conclusion, font_size=30, individual_letters=False):
    '''
    Arranges statements under each other, puts Brace from the left, '=>' and the conclusion
    
    Arguments - statements (some sort of group of statements), conclusion
    
    Optional arguments - individual_letters (if True, returning VGroup will consists from submobjects of statements submobjects
    (usefull for animating triangles equality))

    Returns - VGroup of (statements, brace, =>, conclusion) - ' { statements => conclusion '
    '''
    statements = VGroup(*statements).arrange(DOWN, aligned_edge=LEFT)

    brace = Brace(statements, direction=[-1, 0, 0])

    rightarrow = MathTex(r'' + '\Rightarrow', font_size=font_size, color=conclusion.get_color())
    rightarrow.next_to(statements, RIGHT)

    conclusion.next_to(rightarrow, RIGHT)

    conclude_from_system = VGroup()

    if individual_letters:
        for i in range(len(statements)):
            conclude_from_system.add(*statements[i])

        conclude_from_system.add(brace, rightarrow, *conclusion)
    
    else:
        conclude_from_system.add(*statements, brace, rightarrow, conclusion)
    
    return conclude_from_system


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
        animation = [*transformation_labels]
    else:
        animation = [*transformation_labels, transformation_segment]

    return animation


def TransformSegmentsLabelsIntoEquality(segment_dots_labels_1, segment_dots_labels_2, equality, transform_segments=True, run_time=1.5):         
    '''
    Animations for Transforming segments into equality AB=XY

    Arguments - segment_dots_labels_1, segment_dots_labels_2, equality('A''B''=''X''Y')

    Optional argument - transform_segments, run_time

    Returns list of 5 or 7 animations
    '''
    transformation_AB = TransformSegmentLabelsIntoStatement(segment_dots_labels_1, equality[0:2],
        transform_segment=transform_segments, run_time=run_time)

    write_equal = Write(equality[2])
    
    transformation_XY = TransformSegmentLabelsIntoStatement(segment_dots_labels_2, equality[3:5], 
        transform_segment=transform_segments, run_time=run_time)

    animation = [*transformation_AB, write_equal, *transformation_XY]

    return animation


def TransformCommonSegmentLabelsIntoStatement(segment_dots_labels, statement, transform_segment=True, run_time=1.5):
    '''
    Animations for Transforming segment into a statement 'AB-ն ընդհանուր է' ('AB is common')

    Arguments - segment_dots_labels, statement

    Optional argument - transform_segment, run_time

    Returns list of 3 or 4 animations
    '''
    transformation_AB = TransformSegmentLabelsIntoStatement(segment_dots_labels, statement[0:2], 
        transform_segment=transform_segment, run_time=run_time)
    
    write_common = Write(statement[2])

    animation = [*transformation_AB, write_common]

    return animation





# Functions that play some animations and return something



def CircleFromSpinningRadius(self, radius=1, center=[0, 0, 0], starting_point_angle=0, 
        radius_color=WHITE, circle_color=GREEN, run_time=4):
    '''
    This function Creates a Circle using it's radius like a Compass Drawing tool (կարկին)

    Arguments - radius, center, point from which to start (angle in DEGREES), colors and run time

    Optional - starting_point_angle=0, radius_color(line color), circle_color, run_time=4

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






# Functions that only play some animations



def PlaySegmentWiggling(self, segment_dots_labels, wiggle_endpoints=True, color=0, scale_factor=1.2, run_time=1.3):
        '''
        Wiggles segment AB together with A and B (optional), and scales in and out Labels of A and B
        
        Arguments - self, AB, A, B, label_A, label_B

        Optional - wiggle_endpoints(True or False), color(default is the same as AB), scale_factor(label), run_time
        '''
        AB, A, B, label_A, label_B = segment_dots_labels
        a, b = A.copy(), B.copy()

        if color == 0:
            ab = AB.copy()
        else:
            ab = AB.copy().set_color(color=color)
        
        if wiggle_endpoints == True:

            self.play(Wiggle(VGroup(ab, a, b), rate_func=linear),
                    label_A.animate(rate_func=there_and_back).scale(scale_factor), 
                        label_B.animate(rate_func=there_and_back).scale(scale_factor),
                            run_time=run_time)
        
        else:

            self.play(Wiggle(ab, rate_func=linear),
                    label_A.animate(rate_func=there_and_back).scale(scale_factor), 
                        label_B.animate(rate_func=there_and_back).scale(scale_factor),
                            run_time=run_time)
        
        self.remove(a, b, ab)



def PlayTwoSegmentsWiggling(self, segment_dots_labels_1, segment_dots_labels_2, wiggle_endpoints=True, simultaneously=False, color=0,
        run_time=1.3):
        '''
        SegmentWiggling for AB and XY
        
        Arguments - self, AB, XY, (A, B, X, Y), (label_A, label_B, label_X, label_Y)

        Optional - wiggle_endpoints, simultaneously(True or False), color(same as AB), scale_factor(label), 
        run_time (for each wiggling)
        '''
        scale_factor = 1.2

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
                
                self.play(Wiggle(VGroup(ab, A, B), rate_func=linear),
                    label_A.animate(rate_func=there_and_back).scale(scale_factor), 
                        label_B.animate(rate_func=there_and_back).scale(scale_factor),
                    Wiggle(VGroup(xy, X, Y), rate_func=linear),
                        label_X.animate(rate_func=there_and_back).scale(scale_factor), 
                            label_Y.animate(rate_func=there_and_back).scale(scale_factor),
                                        run_time=run_time)

            else:

                self.play(Wiggle(ab, rate_func=linear),
                        label_A.animate(rate_func=there_and_back).scale(scale_factor), 
                            label_B.animate(rate_func=there_and_back).scale(scale_factor),
                        Wiggle(xy, rate_func=linear),
                            label_X.animate(rate_func=there_and_back).scale(scale_factor), 
                                label_Y.animate(rate_func=there_and_back).scale(scale_factor),
                                            run_time=run_time)
            
        self.remove(A, B, ab, X, Y, xy)



def PlayTransformSegmentsLabelsIntoEquality(self, animations, transform_segments=True, transform_simultaneously=False):

    if not transform_simultaneously: 

        if transform_segments:
            self.play(animations[0], animations[1], animations[2])
            self.play(animations[3])
            self.play(animations[4], animations[5], animations[6])

        else:
            self.play(animations[0], animations[1])
            self.play(animations[2])
            self.play(animations[3], animations[4])
    
    else:

        self.play(*animations)



def PlayTransformCommonSegmentLabelsIntoStatement(self, animations, transform_segment=True):

    if transform_segment:
        self.play(animations[0], animations[1], animations[2])
        self.play(animations[3])
    
    else:
        self.play(animations[0], animations[1])
        self.play(animations[2])



def PlayTwoSegmentsEqualityWiggling(self, pair, equality, run_time=2.5, color=WHITE, wiggle_simultaneously=True, 
    wiggle_endpoints=True, transform_simultaneously=False, transform_segments=True):
    '''
    Wiggles 2 segments and transforms into AB=CD

    Arguments - pair((AB, A, B, label_A, label_B), (CD, C, D, label_C, label_D)) input for TwoSegmentsWiggling;
    equality(MathTex from 5 Mobjects  AB=CD)
    '''
    
    PlayTwoSegmentsWiggling(self, *pair, color=color,
            simultaneously=wiggle_simultaneously, wiggle_endpoints=wiggle_endpoints, run_time=run_time/2)
    
    PlayTransformSegmentsLabelsIntoEquality(self, 
        TransformSegmentsLabelsIntoEquality(
            pair[0], pair[1], equality=equality,
            transform_segments=transform_segments, run_time=run_time/2),
            transform_simultaneously=transform_simultaneously, transform_segments=transform_segments)



def PlaySegmentCommonWiggling(self, segment_dots_labels, statement, run_time=2.5, color=WHITE, wiggle_endpoints=True, transform_segment=True):

    PlaySegmentWiggling(self, segment_dots_labels, wiggle_endpoints=wiggle_endpoints, color=color, run_time=run_time/2)

    PlayTransformCommonSegmentLabelsIntoStatement(self, 
        TransformCommonSegmentLabelsIntoStatement(
            segment_dots_labels, statement=statement, transform_segment=transform_segment, run_time=run_time/2))



def PlayBraceConclude(self, conclude_from_system):
    '''
    From ConcludeFromStatementsSystem animates drawing Brace, rightarrow and conclusion

    Parameters - conclude_from_system(last three elements must be brace, rightarrow and conclusion respectively)
    '''
    self.play(Write(conclude_from_system[-3]))
    self.play(Write(conclude_from_system[-2]))
    self.play(Write(conclude_from_system[-1]))







class TrianglesCongruence(Scene):


    def SSSWiggling(self, vertices_ABC, sides_ABC, mob_labels_ABC, labels_ABC, 
        vertices_XYZ, sides_XYZ, mob_labels_XYZ, labels_XYZ, brace_tip=[0, 0, 0],
            common=0, wiggle_endpoints=[True, True, True], wiggle_simultaneously=[True, True, True],
                transform_simultaneously=[False, False, False], colors=[0, 0, 0],
                    run_times=[2.5, 2.5, 2.5], wait_time=[1, 1, 1]):
            '''
            Shows and writes equality of two triangles by their 3 sides,
            if there is a common side, that will be shown last,
            others are animated in order

            Arguments - vertices_ABC(A, B, C), sides_ABC (AB, BC, AC(order matters)), mob_labels_ABC(mobjects, preferably from LabelPoint()), 
            labels_ABC('A', 'B', 'C'), same things for second triangle(XYZ), brace_tip(left middle point of system of equalities), 
            common(if triangles have a common side), 
            wiggle_endpoints(list - True or False for each side), 
            wiggle_simultaneously(2 equal sides(list - True or False for each side)), 
            color(change color of the side while wiggling(list - 0 or color for each side)), 
            run_time(animations of sides(list)), wait_time(pause between animations of sides, or final brace(list))

            Returns - VGroup of mobjects (same as ConcludeFromSystem)
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
                sequence = pairs

            if common == AB:
                equalities = VGroup(bc_yz, ca_zx, ab_common)
                sequence = [pairs[1], pairs[2], singles[0]]
                colors = [colors[1], colors[2], colors[0]]
                wiggle_endpoints = [wiggle_endpoints[1], wiggle_endpoints[2], wiggle_endpoints[0]]
                wiggle_simultaneously = [wiggle_simultaneously[1], wiggle_simultaneously[2], wiggle_simultaneously[0]]
                transform_simultaneously = [transform_simultaneously[1], transform_simultaneously[2], transform_simultaneously[3]]

            if common == BC:
                equalities = VGroup(ab_xy, ca_zx, bc_common)
                sequence = [pairs[0], pairs[2], singles[1]]
                colors = [colors[0], colors[2], colors[1]]
                wiggle_endpoints = [wiggle_endpoints[0], wiggle_endpoints[2], wiggle_endpoints[1]]
                wiggle_simultaneously = [wiggle_simultaneously[0], wiggle_simultaneously[2], wiggle_simultaneously[1]]
                transform_simultaneously = [transform_simultaneously[0], transform_simultaneously[2], transform_simultaneously[1]]
                
            if common == CA:
                equalities = VGroup(ab_xy, bc_yz, ca_common)
                sequence = [pairs[0], pairs[1], singles[2]]
            
            triangle_equality = MathTexTrianglesEquality(abc, xyz, font_size=fs)

            conclude_from_system = ConcludeFromStatementSystem(equalities, triangle_equality, font_size=fs, individual_letters=True)
            conclude_from_system.next_to(brace_tip, RIGHT, buff=0)

        # Animations

            if common == 0:
                PlayTwoSegmentsEqualityWiggling(self, sequence[0], equalities[0], color=colors[0], 
                    wiggle_simultaneously=wiggle_simultaneously[0], wiggle_endpoints=wiggle_endpoints[0], 
                        transform_simultaneously=transform_simultaneously[0], run_time=run_times[0])

                self.wait(wait_time[0])

                PlayTwoSegmentsEqualityWiggling(self, sequence[1], equalities[1], color=colors[1], 
                    wiggle_simultaneously=wiggle_simultaneously[1], wiggle_endpoints=wiggle_endpoints[1], 
                        transform_simultaneously=transform_simultaneously[1], run_time=run_times[1])

                self.wait(wait_time[1])

                PlayTwoSegmentsEqualityWiggling(self, sequence[2], equalities[2], color=colors[2], 
                    wiggle_simultaneously=wiggle_simultaneously[2], wiggle_endpoints=wiggle_endpoints[2], 
                        transform_simultaneously=transform_simultaneously[2], run_time=run_times[2])
                        
                self.wait(wait_time[2])

                PlayBraceConclude(self, conclude_from_system)

            else:
                PlayTwoSegmentsEqualityWiggling(self, sequence[0], equalities[0], color=colors[0], 
                    wiggle_simultaneously=wiggle_simultaneously[0], wiggle_endpoints=wiggle_endpoints[0], 
                        transform_simultaneously=transform_simultaneously[0], run_time=run_times[0])

                self.wait(wait_time[0])

                PlayTwoSegmentsEqualityWiggling(self, sequence[1], equalities[1], color=colors[1], 
                    wiggle_simultaneously=wiggle_simultaneously[1], wiggle_endpoints=wiggle_endpoints[1], 
                        transform_simultaneously=transform_simultaneously[1], run_time=run_times[1])

                self.wait(wait_time[1])

                PlaySegmentCommonWiggling(self, sequence[2], equalities[2], color=colors[2], 
                    wiggle_endpoints=wiggle_endpoints[2], run_time=run_times[2])

                self.wait(wait_time[2])

                PlayBraceConclude(self, conclude_from_system)
        
        # return
            return conclude_from_system




class test(Scene):
    def construct(self):

        C = Dot([-1, 1, 0])
        CA = always_redraw(lambda: Line(C.get_center(), [0, -1, 0]))
        self.add(C, CA)
        self.wait(0.5)
        self.play(C.animate().move_to([3, 1, 0]))
        self.wait(0.5)
        
