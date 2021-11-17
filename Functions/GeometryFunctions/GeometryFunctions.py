from manim import *
import numpy as np


armenian_tex_template = TexTemplate()
armenian_tex_template.add_to_preamble(r"\usepackage{armtex}")


def LabelPoint(point, label, position=DL*0.5, font_size=30):
    '''
    Adds label to a point

    Arguments - point(Dot), label(string)

    Optional - Position relative to the point=DL, font_size=25

    Returns - the Text mobject of label
    '''
    laebl_point = MathTex(r'' + label, font_size=font_size, color=point.get_color())
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


def SegmentsEqualitySign_2(AB, sign_size=0.2, color=WHITE):
    '''
    Equality sign with 2 small lines for a segment

    Arguments - AB(Line)

    Optional - sign_size=0.2, Color=WHITE

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


def mathtex_segments_equality(labels, font_size=30, color=WHITE):
    '''
    Writes 2 segments equality (AB=XY) in MathTex as a Group of 5 mobjects

    Argument - labels(list of 4 labels)
    '''
    label_1_1, label_1_2, label_2_1, label_2_2 = labels

    segments_equality = MathTex(r'' + label_1_1, r'' + label_1_2, r'=', r'' + label_2_1, r'' + label_2_2, 
        font_size=font_size, color=color)

    return segments_equality


def mathtex_common_segment(labels, font_size=30, color=WHITE):
    '''
    Writes segment is common (AB-ն ընդհանուր է) in MathTex as a Group of 3 Mobjects

    Arguments - labels (list of 2 labels)
    '''
    label_1, label_2 = labels
    
    segment_common = MathTex(r'' + label_1, r'' + label_2, r'\textrm{-ն ընդհանուր է}', 
        tex_template=armenian_tex_template, font_size=font_size, color=color)
    
    return segment_common




class CircleFunctions(Scene):

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

    

class SegmentFunctions(Scene):


    def SegmentWiggling(self, AB, A, B, label_A, label_B, wiggle_endpoints=True, color=0, scale_factor=1.2, run_time=1.3):
        '''
        Whiggles segment AB togeter with A and B (optional), and scales in and out Labels of A and B
        
        Arguments - self, AB, A, B, label_A, label_B

        Optional - wiggle_endpoints(Ture or False), color(default is the same as AB), scale_factor(label), run_time
        '''
        a, b = A.copy(), B.copy()

        if color == 0:
            ab = AB.copy()
        else:
            ab = AB.copy().set_color(color=color)
        
        if wiggle_endpoints == True:

            self.play(Wiggle(Group(ab, a, b), rate_func=linear),
                    label_A.animate(rate_func=there_and_back).scale(scale_factor), 
                        label_B.animate(rate_func=there_and_back).scale(scale_factor),
                            run_time=run_time)
        
        else:

            self.play(Wiggle(ab, rate_func=linear),
                    label_A.animate(rate_func=there_and_back).scale(scale_factor), 
                        label_B.animate(rate_func=there_and_back).scale(scale_factor),
                            run_time=run_time)
        
        self.remove(a, b, ab)



    def TwoSegmentsWiggling(self, AB, CD, endpoints, labels, wiggle_endpoints=True, simultaneously=False, color=0,
        run_time=1.3):
        '''
        SegmentWiggling for AB and CD
        
        Arguments - self, AB, CD, (A, B, C, D), (label_A, label_B, label_C, label_D)

        Optional - wiggle_endpoints, simultaneously(Ture or False), color(same as AB), scale_factor(label), run_time (for each wiggling)
        '''
        scale_factor = 1.2
        A, B, C, D = Group(*endpoints).copy()
        label_A, label_B, label_C, label_D = labels

        if color == 0:
            ab, cd = AB.copy(), CD.copy()
        else:
            ab, cd = AB.copy().set_color(color=color), CD.copy().set_color(color=color)


        if simultaneously == False:
        
            SegmentFunctions.SegmentWiggling(self, AB, A, B, label_A, label_B, wiggle_endpoints=wiggle_endpoints, 
                color=color, scale_factor=scale_factor, run_time=run_time)
            self.wait(0.2)
            SegmentFunctions.SegmentWiggling(self, CD, C, D, label_C, label_D, wiggle_endpoints=wiggle_endpoints, 
                color=color, scale_factor=scale_factor, run_time=run_time)
        
        else:
            
            if wiggle_endpoints == True:
                
                copy_A = A.copy()
                copy_B = B.copy()
                copy_C = C.copy()
                copy_D = D.copy()
                self.play(Wiggle(Group(ab, copy_A, copy_B), rate_func=linear),
                    label_A.animate(rate_func=there_and_back).scale(scale_factor), 
                        label_B.animate(rate_func=there_and_back).scale(scale_factor),
                    Wiggle(Group(cd, copy_C, copy_D), rate_func=linear),
                        label_C.animate(rate_func=there_and_back).scale(scale_factor), 
                            label_D.animate(rate_func=there_and_back).scale(scale_factor),
                                        run_time=run_time)

            else:

                self.play(Wiggle(ab, rate_func=linear),
                        label_A.animate(rate_func=there_and_back).scale(scale_factor), 
                            label_B.animate(rate_func=there_and_back).scale(scale_factor),
                        Wiggle(cd, rate_func=linear),
                            label_C.animate(rate_func=there_and_back).scale(scale_factor), 
                                label_D.animate(rate_func=there_and_back).scale(scale_factor),
                                            run_time=run_time)
            
            self.remove(A, B, ab, C, D, cd)



    def animate_segments_equality(self, pair, equality, run_time=2.5, color=WHITE, wiggle_simultaneously=True, 
        wiggle_endpoints=True, transform_simultaneously=False):
        '''
        Wiggles 2 segments and transforms into AB=CD

        Arguments - pair(AB, CD, (A, B, C, D), (label_A, label_B, label_C, label_D)) input for TwoSegmentsWiggling;
        equality(MathTex from 5 Mobjects  AB=CD)
        '''
        
        SegmentFunctions.TwoSegmentsWiggling(self, *pair, color=color,
                simultaneously=wiggle_simultaneously, wiggle_endpoints=wiggle_endpoints, run_time=run_time/2)
        
        labels = pair[3]
        label_S_1_1 = labels[0].copy()
        label_S_1_2 = labels[1].copy()
        label_S_2_1 = labels[2].copy()
        label_S_2_2 = labels[3].copy()

        if transform_simultaneously == False:
            self.play(label_S_1_1.animate(rate_func=linear).move_to(equality[0].get_center()),
                label_S_1_2.animate(rate_func=linear).move_to(equality[1].get_center()), run_time=run_time/4)
            self.play(Write(equality[2]))
            self.play(label_S_2_1.animate(rate_func=linear).move_to(equality[3].get_center()),
                label_S_2_2.animate(rate_func=linear).move_to(equality[4].get_center()), run_time=run_time/4)
        else:
            self.play(label_S_1_1.animate(rate_func=linear).move_to(equality[0].get_center()),
            label_S_1_2.animate(rate_func=linear).move_to(equality[1].get_center()),
            Write(equality[2]),
            label_S_2_1.animate(rate_func=linear).move_to(equality[3].get_center()),
            label_S_2_2.animate(rate_func=linear).move_to(equality[4].get_center()), run_time=run_time/2)

        self.remove(label_S_1_1, label_S_1_2, label_S_2_1, label_S_2_2)
        self.add(*[equality[i] for i in range(5)])



    def animate_segment_common(self, single, statment, run_time=2.5, wiggle_endpoints=True, color=WHITE):
        '''
        Wiggles a segments and transforms into - AB is common (AB-ն ընդհանուր է)

        Arguments - single(AB, A, B, label_A, label_B)
        Statment(AB-ն ընդհանուր է)
        '''
        SegmentFunctions.SegmentWiggling(self, *single, wiggle_endpoints=wiggle_endpoints, color=color, 
            run_time=run_time/2)

        copy_label_A = single[3].copy()
        copy_label_B = single[4].copy()

        self.play(
            copy_label_A.animate(rate_func=linear).move_to(statment[0].get_center()), 
            copy_label_B.animate(rate_func=linear).move_to(statment[1].get_center()), run_time=run_time/2)
        self.play(Write(statment[2]))

        self.remove(copy_label_A, copy_label_B)
        self.add(*[statment[i] for i in range(3)])


class TriangleFnctions(Scene):


    def TriangleEquality3Sides(self, vertices_ABC, sides_ABC, mob_labels_ABC, labels_ABC, 
        vertices_XYZ, sides_XYZ, mob_labels_XYZ, labels_XYZ, brace_tip=[0, 0, 0],
            common=0, wiggle_endpoints=[True, True, True], wiggle_simultaneously=[True, True, True],
                transform_simultaneously=[False, False, False], colors=[0, 0, 0],
                    run_times=[2.5, 2.5, 2.5], wait_time=[1, 1, 1]):
            '''
            Shows and writes equality of two triangles by their 3 sides

            Arguments - vertices_ABC(A, B, C), sides_ABC (AB, BC, AC(order matters)), mob_labels_ABC(mobjects, preferably from LabelPoint()), 
            labels_ABC('A', 'B', 'C'), same things for second triangle(XYZ), brace_tip(left middle point of system of equalities), 
            common(if triangles have a common side), 
            wiggle_endpoints(list - True or False for each side), 
            wiggle_simultaneously(2 equal sides(list - True or False for each side)), 
            color(change color of the side while wiggling(list - 0 or color for each side)), 
            run_time(animations of sides(list)), wait_time(pause between animations of sides, or final brace(list))
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
            ABXY = (AB, XY, (A, B, X, Y), (label_A, label_B, label_X, label_Y))
            BCYZ = (BC, YZ, (B, C, Y, Z), (label_B, label_C, label_Y, label_Z))
            CAZX = (CA, ZX, (C, A, Z, X), (label_C, label_A, label_Z, label_X))
            pairs = [ABXY, BCYZ, CAZX]

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
            ab_xy = mathtex_segments_equality(labels_pairs[0], font_size=fs)
            bc_yz = mathtex_segments_equality(labels_pairs[1], font_size=fs)
            ca_zx = mathtex_segments_equality(labels_pairs[2], font_size=fs)
            ab_common = mathtex_common_segment(labels_singles[0], font_size=fs)
            bc_common = mathtex_common_segment(labels_singles[1], font_size=fs)
            ca_common = mathtex_common_segment(labels_singles[2], font_size=fs)

        # Equality system
            
            if common == 0:
                equalities = Group(ab_xy, bc_yz, ca_zx)
                sequence = pairs

            if common == AB:
                equalities = Group(bc_yz, ca_zx, ab_common)
                sequence = [pairs[1], pairs[2], singles[0]]
                colors = [colors[1], colors[2], colors[0]]
                wiggle_endpoints = [wiggle_endpoints[1], wiggle_endpoints[2], wiggle_endpoints[0]]
                wiggle_simultaneously = [wiggle_simultaneously[1], wiggle_simultaneously[2], wiggle_simultaneously[0]]
                transform_simultaneously = [transform_simultaneously[1], transform_simultaneously[2], transform_simultaneously[3]]

            if common == BC:
                equalities = Group(ab_xy, ca_zx, bc_common)
                sequence = [pairs[0], pairs[2], singles[1]]
                colors = [colors[0], colors[2], colors[1]]
                wiggle_endpoints = [wiggle_endpoints[0], wiggle_endpoints[2], wiggle_endpoints[1]]
                wiggle_simultaneously = [wiggle_simultaneously[0], wiggle_simultaneously[2], wiggle_simultaneously[1]]
                transform_simultaneously = [transform_simultaneously[0], transform_simultaneously[2], transform_simultaneously[1]]
                
            if common == CA:
                equalities = Group(ab_xy, bc_yz, ca_common)
                sequence = [pairs[0], pairs[1], singles[2]]
            
            equalities.arrange_in_grid(cols=1, col_alignments='l', buff=0.25)

            brace = Brace(equalities, direction=[-1, 0, 0])

            conclude_equality = Group(MathTex(r'' + '\Rightarrow', font_size=fs).next_to(equalities, RIGHT, buff=0.2))
            conclude_equality.add(
                MathTex(r'\triangle ' + abc + r'\ =\ ' + r'\triangle ' + xyz, font_size=fs).next_to(conclude_equality[0], RIGHT))

            triangle_equality = Group(
                *equalities[0], *equalities[1], *equalities[2], brace, *conclude_equality).next_to(brace_tip, RIGHT, buff=0)

        # Animations
        
            def Brace_Conclude_Equality():
                self.play(Write(triangle_equality[-3]))
                self.play(Write(triangle_equality[-2]))
                self.play(Write(triangle_equality[-1]))
    

            if common == 0:
                SegmentFunctions.animate_segments_equality(self, sequence[0], equalities[0], color=colors[0], 
                    wiggle_simultaneously=wiggle_simultaneously[0], wiggle_endpoints=wiggle_endpoints[0], 
                        transform_simultaneously=transform_simultaneously[0], run_time=run_times[0])
                self.wait(wait_time[0])

                SegmentFunctions.animate_segments_equality(self, sequence[1], equalities[1], color=colors[1], 
                    wiggle_simultaneously=wiggle_simultaneously[1], wiggle_endpoints=wiggle_endpoints[1], 
                        transform_simultaneously=transform_simultaneously[1], run_time=run_times[1])
                self.wait(wait_time[1])

                SegmentFunctions.animate_segments_equality(self, sequence[2], equalities[2], color=colors[2], 
                    wiggle_simultaneously=wiggle_simultaneously[2], wiggle_endpoints=wiggle_endpoints[2], 
                        transform_simultaneously=transform_simultaneously[2], run_time=run_times[2])
                self.wait(wait_time[2])

                Brace_Conclude_Equality()

            else:
                SegmentFunctions.animate_segments_equality(self, sequence[0], equalities[0], color=colors[0], 
                    wiggle_simultaneously=wiggle_simultaneously[0], wiggle_endpoints=wiggle_endpoints[0], 
                        transform_simultaneously=transform_simultaneously[0], run_time=run_times[0])
                self.wait(wait_time[0])

                SegmentFunctions.animate_segments_equality(self, sequence[1], equalities[1], color=colors[1], 
                    wiggle_simultaneously=wiggle_simultaneously[1], wiggle_endpoints=wiggle_endpoints[1], 
                        transform_simultaneously=transform_simultaneously[1], run_time=run_times[1])
                self.wait(wait_time[1])

                SegmentFunctions.animate_segment_common(self, sequence[2], equalities[2], color=colors[2], wiggle_endpoints=wiggle_endpoints[2], 
                    run_time=run_times[2])
                self.wait(wait_time[2])

                Brace_Conclude_Equality()
        
        # return
            return triangle_equality



class test(Scene):
    def construct(self):
        self.wait()
        
