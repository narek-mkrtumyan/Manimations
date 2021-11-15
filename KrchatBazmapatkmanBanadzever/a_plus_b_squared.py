from manim import *
import numpy as np

def ConstructSquare(a, b, center=[0, 0, 0], color_1=GREEN, color_2=ORANGE, color_3=DARK_BROWN, fill_opacity=0.6):
    '''
    Constructs quare with size a+b, devided into 4 parts - axa, axb, bxa, bxb
    Optional arguments - center(of the square), color_1(color of side a), color_2(color of the side b)
    Returns 9 points, 12 segments and 4 areas (from top to bottom, from left to right)
    '''
    fo = fill_opacity
    c = a + b

    top_left = Dot([center[0] - c/2, center[1] + c/2, 0])
    top_mid = Dot(top_left.get_center() + np.array([a, 0, 0]))
    top_right = Dot(top_left.get_center() + np.array([a + b, 0, 0]))

    bottom_left = Dot(top_left.get_center() + np.array([0, -c, 0]))
    bottom_mid = Dot(top_mid.get_center() + np.array([0, -c, 0]))
    bottom_right = Dot(top_right.get_center() + np.array([0, -c, 0]))

    mid_left = Dot(top_left.get_center() + np.array([0, -a, 0]))
    mid_mid = Dot(top_mid.get_center() + np.array([0, -a, 0]))
    mid_right = Dot(top_right.get_center() + np.array([0, -a, 0]))

    top_a = Line(top_left, top_right, color=color_1)
    top_b = Line(top_mid, top_right, color=color_2)

    left_a = Line(top_left, mid_left, color=color_1)
    left_b = Line(mid_left, bottom_left, color=color_2)

    bottom_a = Line(bottom_left, bottom_mid, color=color_1)
    bottom_b = Line(bottom_mid, bottom_right, color=color_2)

    right_a = Line(top_right, mid_right, color=color_1)
    right_b = Line(mid_right, bottom_right, color=color_2)

    mid_hor_a = Line(mid_left, mid_mid, color=color_1)
    mid_hor_b = Line(mid_mid, mid_right, color=color_2)

    mid_ver_a = Line(top_mid, mid_mid, color=color_1)
    mid_ver_b = Line(mid_mid, bottom_mid, color=color_2)

    square_a = Polygon(mid_left.get_center(), top_left.get_center(),
    top_mid.get_center(), mid_mid.get_center()).set_fill(color_1, opacity=fo).set_stroke(width=0)

    square_b = Polygon(bottom_mid.get_center(), mid_mid.get_center(),
    mid_right.get_center(), bottom_right.get_center()).set_fill(color_2, opacity=fo).set_stroke(width=0)

    rect_hor = Polygon(bottom_left.get_center(), mid_left.get_center(),
    mid_mid.get_center(), bottom_mid.get_center()).set_fill(color_3, opacity=fo).set_stroke(width=0)

    rect_ver = Polygon(mid_mid.get_center(), top_mid.get_center(),
    top_right.get_center(), mid_right.get_center()).set_fill(color_3, opacity=fo).set_stroke(width=0)

    points = VGroup(top_left, top_mid, top_right, mid_left, mid_mid, mid_right, bottom_left, bottom_mid, bottom_right)
    segments = VGroup(top_a, top_b, mid_hor_a, mid_hor_b, bottom_a, bottom_b, left_a, left_b, mid_ver_a, mid_ver_b, right_a, right_b)
    areas = VGroup(square_a, rect_ver, rect_hor, square_b)

    return points, segments, areas


class a_plus_b_squared(Scene):
    def construct(self):

        a = 2
        b = 1
        center = [0, 0, 0]

        points, segments, areas = ConstructSquare(a, b, center=center)
        (top_left, top_mid, top_right, mid_left, mid_mid, mid_right, bottom_left, bottom_mid, bottom_right) = points
        (top_a, top_b, mid_hor_a, mid_hor_b, bottom_a, bottom_b, left_a, left_b, mid_ver_a, mid_ver_b, right_a, right_b) = segments
        (square_a, rect_ver, rect_hor, square_b) = areas


        self.add(points, segments, areas)





class test(Scene):
    def construct(self):

        points, segments, areas = ConstructSquare(2, 1)

        self.add(segments, areas, points)

