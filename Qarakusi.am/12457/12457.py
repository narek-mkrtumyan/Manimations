from manim import *
from manim.mobject import value_tracker
import numpy as np
from numpy.core.numeric import moveaxis

def ConstructPolygonLine(n, delta_x, delta_y, line_y, vertices):

    n_equals_n = Tex(f'N\ =\ ${n}$', font_size=60).move_to([-4.5, 3, 0])

    # THE LINE
    starting_point = -6.5
    ending_point = 6.5
    l_1 = np.array([starting_point, line_y, 0])
    l_2 = np.array([ending_point, line_y, 0])
    line = Line(l_1, l_2, color=ORANGE).scale(1.3)

    for i in range(len(vertices)):
        vertices[i] = vertices[i] + np.array([delta_x, delta_y, 0])

    polygon = Polygon(*vertices, color=GREEN)
    area = Polygon(*vertices, color=GREEN, fill_opacity=0.3)

    # INTERSECTION COORDINATES OF THE POLYGON AND THE LINE
    intersection_coordinates = []
    for i in range(len(vertices)):
        intersection_coordinates.append(line_intersection([l_1, l_2], [vertices[i], vertices[(i+n-1)%n]]))

    # INTERSECTION POINT ORANGE AND GREEN IN TURN
    intersection_points = VGroup()
    for i in range(len(intersection_coordinates)):
        if i % 2 == 0:
            intersection_points.add(Dot(intersection_coordinates[i], color=ORANGE))
        else:
            intersection_points.add(Dot(intersection_coordinates[i], color=GREEN))

    # INDICES OF THE INTERSECTION POINTS
    point_indices = Tex(*[f'${i+1}$' for i in range(n)], font_size=40)
    intersection_point_indices = VGroup()
    for i in range(len(intersection_coordinates)):
        if i % 2 == 0:
            intersection_point_indices.add(point_indices[i].set_color(ORANGE).next_to(intersection_points[i], DL * 0.6))
        else:
            intersection_point_indices.add(point_indices[i].set_color(GREEN).next_to(intersection_points[i], DR * 0.6))
    
    points = intersection_coordinates.copy()
    points.append(np.array([ending_point, line_y, 0]))
    points.append(np.array([starting_point, line_y, 0]))

    return n_equals_n, line, polygon, area, intersection_points, intersection_point_indices, points
    


class hexagon(Scene):
    def construct(self):
        
        n = 6
        n_equals_n = Tex(f'N\ =\ ${n}$', font_size=60).move_to([-4.5, 3, 0])
        
        delta_x = -1     # shift the hexagon left or right
        line_y = -1.5    # y coordinate of the main line

        # THE LINE
        starting_point = -6.5
        ending_point = 6.5
        l_1 = np.array([starting_point, line_y, 0])
        l_2 = np.array([ending_point, line_y, 0])
        line = Line(l_1, l_2, color=ORANGE).scale(1.3)

        # POLYGON VERTICES
        v_0 = np.array([-3.5 + delta_x, -1.3 + line_y, 0])
        v_1 = np.array([-1 + delta_x, 1.2 + line_y, 0])
        v_2 = np.array([0 + delta_x, -1.8 + line_y, 0])
        v_3 = np.array([1 + delta_x, 0.8 + line_y, 0])
        v_4 = np.array([3.5 + delta_x, -1.1 + line_y, 0])
        v_5 = np.array([-1 + delta_x, 3, 0])

        vertices = [v_0, v_1, v_2, v_3, v_4, v_5]

        hexagon = Polygon(*vertices, color=GREEN)
        area = Polygon(*vertices, color=GREEN, fill_opacity=0.3)

        # INTERSECTION COORDINATES OF THE POLYGON AND THE LINE
        intersection_coordinates = []
        for i in range(len(vertices)):
            intersection_coordinates.append(line_intersection([l_1, l_2], [vertices[i], vertices[(i+5)%6]]))

        # INTERSECTION POINT ORANGE AND GREEN IN TURN
        intersection_points = VGroup()
        for i in range(len(intersection_coordinates)):
            if i % 2 == 0:
                intersection_points.add(Dot(intersection_coordinates[i], color=ORANGE))
            else:
                intersection_points.add(Dot(intersection_coordinates[i], color=GREEN))

        # INDICES OF THE INTERSECTION POINTS
        point_indices = Tex(*[f'${i+1}$' for i in range(n)], font_size=40)
        intersection_point_indices = VGroup()
        for i in range(len(intersection_coordinates)):
            if i % 2 == 0:
                intersection_point_indices.add(point_indices[i].set_color(ORANGE).next_to(intersection_points[i], DL * 0.6))
            else:
                intersection_point_indices.add(point_indices[i].set_color(GREEN).next_to(intersection_points[i], DR * 0.6))
        intersection_point_indices[0].shift(0.1 * LEFT)
        intersection_point_indices[-1].shift(0.2 * RIGHT)

        x = ValueTracker(starting_point)
        dot_orange = always_redraw(lambda: Dot([x.get_value(), line_y, 0], color=ORANGE))
        dot_green = always_redraw(lambda: Dot([x.get_value(), line_y, 0], color=GREEN))

        moving_segments = []
        for i in range(len(intersection_coordinates)):
            if i % 2 == 0:
                moving_segments.append(always_redraw(lambda: Line(intersection_coordinates[i-1], [x.get_value(), line_y, 0], color=GREEN)))
        
        segments = []
        for i in range(len(intersection_coordinates)):
            if i % 2 == 0:
                segments.append(Line(intersection_coordinates[i], intersection_coordinates[i+1], color=GREEN))

        points = intersection_coordinates.copy()
        points.append(np.array([ending_point, line_y, 0]))
        points.append(np.array([starting_point, line_y, 0]))

        new_points_coordinates = [np.array([2 + i * 4/5, 2, 0]) for i in range(len(intersection_coordinates))]
        new_points = VGroup(*[Dot(new_points_coordinates[i], color=i%2*GREEN+(1-i%2)*ORANGE) for i in range(len(new_points_coordinates))])
        new_numbers = VGroup(*[Tex(f'${i+1}$', font_size=40, color=new_points[i].get_color()).move_to(new_points[i]) for i in range(len(new_points))])

        parentheses = VGroup()
        for i in range(len(new_numbers)):
            if i % 2 == 0:
                parentheses.add(Tex('(', font_size=60).move_to(new_points[i]).shift(0.2*LEFT))
            else:
                parentheses.add(Tex(')', font_size=60).move_to(new_points[i]).shift(0.2*RIGHT))
        
        n_is_even = Text('N-ը զույգ է', font_size=40).move_to([4, 0, 0])

        # self.wait(0.5)

        # self.add(line)
        # self.add(hexagon, area)
        # self.add(dot_orange)
        # self.add(intersection_point_indices, intersection_points)
        # self.wait(0.5)
        # self.add(n_equals_n)
        # self.add(parentheses)
        # self.add(new_points)
        # self.wait(0.5)
        # self.play(Transform(new_points, new_numbers))
        # self.wait(0.5)
        # self.play(Write(n_is_even))

        # self.wait(1)

        # Final animations
        self.wait(1)

        self.play(Create(hexagon), run_time=2)
        self.wait(0.5)
        self.play(Write(n_equals_n), run_time=1.5)
        self.wait(0.5)
        self.play(Create(line), run_time=1.5)
        self.wait(0.5)
        self.play(FadeIn(area))
        self.wait(0.5)
        self.play(Create(dot_orange))

        for i in range(len(points) - 1):
            run_time = (points[i][0] - points[i-1][0]) * 2 / 3
            self.remove(dot_orange, dot_green)
            if i % 2 == 0:
                self.add(dot_orange)
            else:
                self.add(dot_green)
                self.add(moving_segments[int(i/2)])
                self.play(x.animate.set_value(points[i][0]), rate_func=linear, run_time=run_time)
                self.remove(moving_segments[int(i/2)])
                self.add(segments[int(i/2)])
            self.play(x.animate.set_value(points[i][0]), rate_func=linear, run_time=run_time)
            if i < len(intersection_points):
                self.add(*[intersection_points[j] for j in range(i+1)])
                self.play(Write(intersection_point_indices[i]))
        
        self.wait(1)
        intersection_points_copy = intersection_points.copy()
        self.play(Transform(intersection_points_copy, new_points))
        self.remove(intersection_points_copy)
        self.add(new_points)
        self.wait(0.5)
        self.play(Create(parentheses))
        self.play(Transform(new_points, new_numbers))
        self.wait(0.5)
        self.play(Write(n_is_even))


        self.wait(1)



class octagon(Scene):
    def construct(self):

        n_equals_n = Tex('N\ =\ $8$', font_size=60).move_to([-4.5, 3, 0])

        delta_x = 0
        line_y = 0

        starting_point = -6.5
        ending_point = 6.5

        l_1 = np.array([starting_point, line_y, 0])
        l_2 = np.array([ending_point, line_y, 0])
        line = Line(l_1, l_2, color=ORANGE).scale(1.3)

        v_0 = np.array([-6 + delta_x, 1.2 + line_y, 0])
        v_1 = np.array([-2.2 + delta_x, -2 + line_y, 0])
        v_2 = np.array([-0.2 + delta_x, 1.2 + line_y, 0])
        v_3 = np.array([-2.5 + delta_x, -0.7 + line_y, 0])
        v_4 = np.array([-0.8 + delta_x, 3 + line_y, 0])
        v_5 = np.array([3 + delta_x, -0.5 + line_y, 0])
        v_6 = np.array([0.5 + delta_x, 0.6 + line_y, 0])
        v_7 = np.array([-2.5 + delta_x, -3.5 + line_y, 0])

        vertices = [v_0, v_1, v_2, v_3, v_4, v_5, v_6, v_7]

        octagon = Polygon(*vertices, color=GREEN)
        area = Polygon(*vertices, color=GREEN, fill_opacity=0.3)

        tic = []   # temporary_intersection_coordinates - with "wrong" order

        for i in range(len(vertices)):
            tic.append(line_intersection([l_1, l_2], [vertices[i], vertices[(i+7)%8]]))

        intersection_coordinates = [tic[0], tic[1], tic[4], tic[3], tic[2], tic[7], tic[6], tic[5]]

        tip = VGroup(*[Dot(tic[i]) for i in range(len(tic))])   # temporary_intersection_points - with "wrong" order

        intersection_points = VGroup()
        for i in range(len(intersection_coordinates)):
            if i % 2 == 0:
                intersection_points.add(Dot(intersection_coordinates[i], color=ORANGE))
            else:
                intersection_points.add(Dot(intersection_coordinates[i], color=GREEN))

        point_indices = Tex('$1$', '$2$', '$3$', '$4$', '$5$', '$6$', '$7$', '$8$', font_size=40)
        intersection_point_indices = VGroup()
        for i in range(len(intersection_coordinates)):
            if i % 2 == 0:
                intersection_point_indices.add(point_indices[i].set_color(ORANGE).next_to(intersection_points[i], DL * 0.5))
            else:
                intersection_point_indices.add(point_indices[i].set_color(GREEN).next_to(intersection_points[i], DR * 0.5))
        intersection_point_indices[1].shift(0.7*UP)
        intersection_point_indices[2].shift(0.7*UP)
        intersection_point_indices[3].shift(0.2*LEFT)
        intersection_point_indices[4].shift(0.5*RIGHT)
        intersection_point_indices[7].shift(0.7*UP)

        x = ValueTracker(starting_point)
        dot_orange = always_redraw(lambda: Dot([x.get_value(), line_y, 0], color=ORANGE))
        dot_green = always_redraw(lambda: Dot([x.get_value(), line_y, 0], color=GREEN))

        moving_segments = []
        for i in range(len(intersection_coordinates)):
            if i % 2 == 0:
                moving_segments.append(always_redraw(lambda: Line(intersection_coordinates[i-1], [x.get_value(), line_y, 0], color=GREEN)))
        
        segments = []
        for i in range(len(intersection_coordinates)):
            if i % 2 == 0:
                segments.append(Line(intersection_coordinates[i], intersection_coordinates[i+1], color=GREEN))

        points = intersection_coordinates.copy()
        points.append(np.array([ending_point, line_y, 0]))
        points.append(np.array([starting_point, line_y, 0]))

        new_points_coordinates = [np.array([1 + i * 4/5, 3, 0]) for i in range(len(intersection_coordinates))]
        new_points = VGroup(*[Dot(new_points_coordinates[i], color=i%2*GREEN+(1-i%2)*ORANGE) for i in range(len(new_points_coordinates))])
        new_numbers = VGroup(*[Tex(f'${i+1}$', font_size=40, color=new_points[i].get_color()).move_to(new_points[i]) for i in range(len(new_points))])
        intersection_points_copy = intersection_points.copy()

        parentheses = VGroup()
        for i in range(len(new_numbers)):
            if i % 2 == 0:
                parentheses.add(Tex('(', font_size=60).move_to(new_points[i]).shift(0.2*LEFT))
            else:
                parentheses.add(Tex(')', font_size=60).move_to(new_points[i]).shift(0.2*RIGHT))
        
        n_is_even = Text('N-ը զույգ է', font_size=40).move_to([3.5, -2, 0])


        # self.add(octagon, area, line)
        self.play(Create(octagon), run_time=2)
        self.wait(0.5)
        self.play(Write(n_equals_n), run_time=1.5)
        self.wait(0.5)
        self.play(Create(line), run_time=1.5)
        self.wait(0.5)
        self.play(FadeIn(area))
        self.wait(0.5)
        self.play(Create(dot_orange))
        
        self.wait(1)

        for i in range(len(points) - 1):
            run_time = (points[i][0] - points[i-1][0]) * 2 / 3
            self.remove(dot_orange, dot_green)
            if i % 2 == 0:
                self.add(dot_orange)
            else:
                self.add(dot_green)
                self.add(moving_segments[int(i/2)])
                self.play(x.animate.set_value(points[i][0]), rate_func=linear, run_time=run_time)
                self.remove(moving_segments[int(i/2)])
                self.add(segments[int(i/2)])
            self.play(x.animate.set_value(points[i][0]), rate_func=linear, run_time=run_time)
            if i < len(intersection_points):
                self.add(*[intersection_points[j] for j in range(i+1)])
                self.play(Write(intersection_point_indices[i]))
        
        self.wait(1)
        self.play(Transform(intersection_points_copy, new_points))
        self.remove(intersection_points_copy)
        self.add(new_points)
        self.wait(0.5)
        self.play(Create(parentheses))
        self.play(Transform(new_points, new_numbers))
        self.wait(0.5)
        self.play(Write(n_is_even))
        
        self.wait(1)



class nonagon(Scene):
    def construct(self):

        n_equals_n = Tex('N\ =\ $9$', font_size=60).move_to([-4.5, 3, 0])
    
        delta_x = 0
        line_y = 0

        starting_point = -6.5
        ending_point = 6.5

        l_1 = np.array([starting_point, line_y, 0])
        l_2 = np.array([ending_point, line_y, 0])
        line = Line(l_1, l_2, color=ORANGE).scale(1.3)

        v_0 = np.array([-6 + delta_x, 1.2 + line_y, 0])
        v_1 = np.array([-2.2 + delta_x, -2 + line_y, 0])
        v_2 = np.array([-0.2 + delta_x, 1.2 + line_y, 0])
        v_3 = np.array([-2.5 + delta_x, -0.7 + line_y, 0])
        v_4 = np.array([-3.2 + delta_x, 1 + line_y, 0])
        v_5 = np.array([-0.8 + delta_x, 3 + line_y, 0])
        v_6 = np.array([3 + delta_x, -0.5 + line_y, 0])
        v_7 = np.array([0.5 + delta_x, 0.6 + line_y, 0])
        v_8 = np.array([-2.5 + delta_x, -3.5 + line_y, 0])

        vertices = [v_0, v_1, v_2, v_3, v_4, v_5, v_6, v_7, v_8]

        nonagon = Polygon(*vertices, color=GREEN)
        area = Polygon(*vertices, color=GREEN, fill_opacity=0.3)

        tic = []   # temporary_intersection_coordinates - with "wrong" order

        for i in range(len(vertices)):
            if i != 5:
                tic.append(line_intersection([l_1, l_2], [vertices[i], vertices[(i+8)%9]]))

        intersection_coordinates = [tic[0], tic[1], tic[4], tic[3], tic[2], tic[7], tic[6], tic[5]]

        tip = VGroup(*[Dot(tic[i]) for i in range(len(tic))])   # temporary_intersection_points - with "wrong" order

        intersection_points = VGroup()
        for i in range(len(intersection_coordinates)):
            if i % 2 == 0:
                intersection_points.add(Dot(intersection_coordinates[i], color=ORANGE))
            else:
                intersection_points.add(Dot(intersection_coordinates[i], color=GREEN))
        
        point_indices = Tex('$1$', '$2$', '$3$', '$4$', '$5$', '$6$', '$7$', '$8$', font_size=40)
        intersection_point_indices = VGroup()
        for i in range(len(intersection_coordinates)):
            if i % 2 == 0:
                intersection_point_indices.add(point_indices[i].set_color(ORANGE).next_to(intersection_points[i], DL * 0.5))
            else:
                intersection_point_indices.add(point_indices[i].set_color(GREEN).next_to(intersection_points[i], DR * 0.5))
        intersection_point_indices[1].shift(0.7*UP)
        intersection_point_indices[2].shift(0.7*UP)
        intersection_point_indices[3].shift(0.2*LEFT)
        intersection_point_indices[4].shift(0.5*RIGHT)
        intersection_point_indices[7].shift(0.7*UP)

        x = ValueTracker(starting_point)
        dot_orange = always_redraw(lambda: Dot([x.get_value(), line_y, 0], color=ORANGE))
        dot_green = always_redraw(lambda: Dot([x.get_value(), line_y, 0], color=GREEN))

        moving_segments = []
        for i in range(len(intersection_coordinates)):
            if i % 2 == 0:
                moving_segments.append(always_redraw(lambda: Line(intersection_coordinates[i-1], [x.get_value(), line_y, 0], color=GREEN)))
        
        segments = []
        for i in range(len(intersection_coordinates)):
            if i % 2 == 0:
                segments.append(Line(intersection_coordinates[i], intersection_coordinates[i+1], color=GREEN))

        points = intersection_coordinates.copy()
        points.append(np.array([ending_point, line_y, 0]))
        points.append(np.array([starting_point, line_y, 0]))

        new_points_coordinates = [np.array([1 + i * 4/5, 3, 0]) for i in range(len(intersection_coordinates))]
        new_points = VGroup(*[Dot(new_points_coordinates[i], color=i%2*GREEN+(1-i%2)*ORANGE) for i in range(len(new_points_coordinates))])
        new_numbers = VGroup(*[Tex(f'${i+1}$', font_size=40, color=new_points[i].get_color()).move_to(new_points[i]) for i in range(len(new_points))])
        intersection_points_copy = intersection_points.copy()

        parentheses = VGroup()
        for i in range(len(new_numbers)):
            if i % 2 == 0:
                parentheses.add(Tex('(', font_size=60).move_to(new_points[i]).shift(0.2*LEFT))
            else:
                parentheses.add(Tex(')', font_size=60).move_to(new_points[i]).shift(0.2*RIGHT))
        
        n_is_even = Text('N-ը կենտ է', font_size=40).move_to([3.5, -2, 0])


        # self.add(nonagon, area, line)

        self.play(Create(nonagon), run_time=2)
        self.wait(0.5)
        self.play(Write(n_equals_n), run_time=1.5)
        self.wait(0.5)
        self.play(Create(line), run_time=1.5)
        self.wait(0.5)
        self.play(FadeIn(area))
        self.wait(0.5)
        self.play(Create(dot_orange))

        self.wait(1)

        for i in range(len(points) - 1):
            run_time = (points[i][0] - points[i-1][0]) * 2 / 3
            self.remove(dot_orange, dot_green)
            if i % 2 == 0:
                self.add(dot_orange)
            else:
                self.add(dot_green)
                self.add(moving_segments[int(i/2)])
                self.play(x.animate.set_value(points[i][0]), rate_func=linear, run_time=run_time)
                self.remove(moving_segments[int(i/2)])
                self.add(segments[int(i/2)])
            self.play(x.animate.set_value(points[i][0]), rate_func=linear, run_time=run_time)
            if i < len(intersection_points):
                self.add(*[intersection_points[j] for j in range(i+1)])
                self.play(Write(intersection_point_indices[i]))

        self.wait(1)
        self.play(Transform(intersection_points_copy, new_points))
        self.remove(intersection_points_copy)
        self.add(new_points)
        self.wait(0.5)
        self.play(Create(parentheses))
        self.play(Transform(new_points, new_numbers))
        self.wait(0.5)
        self.play(Write(n_is_even))
        self.wait(0.5)
        
        self.play(Indicate(Line(v_4, v_5, color=GREEN), color=PURE_RED, run_time=4, scale_factor=1))

        self.wait(1)



class problem_12457(Scene):
    def construct(self):
        
        self.wait(1)

        hexagon.construct(self)
        self.play(FadeOut(*[mob for mob in self.mobjects]))
        self.wait(0.3)
        octagon.construct(self)
        self.play(FadeOut(*[mob for mob in self.mobjects]))
        self.wait(0.3)
        nonagon.construct(self)
        self.play(FadeOut(*[mob for mob in self.mobjects]))

        self.wait(1)


class test(Scene):
    def construct(self):
        
        # HEXAGON VERTICES
        h_0 = np.array([-3.5, -1.3, 0])
        h_1 = np.array([-1, 1.2, 0])
        h_2 = np.array([0, -1.8, 0])
        h_3 = np.array([1, 0.8, 0])
        h_4 = np.array([3.5, -1.1, 0])
        h_5 = np.array([-1, 4.5, 0])

        hex_vertices = [h_0, h_1, h_2, h_3, h_4, h_5]

        (n_equals_6, line_hex, hexagon, area_hex, intersection_points_hex,
         intersection_point_indices_hex, points) = ConstructPolygonLine(6, -1, -1.5, -1.5, hex_vertices)

        # OCTAGON VERTICES
        o_0 = np.array([-6, 1.2, 0])
        o_1 = np.array([-2.2, -2, 0])
        o_2 = np.array([-0.2, 1.2, 0])
        o_3 = np.array([-2.5, -0.7, 0])
        o_4 = np.array([-0.8, 3, 0])
        o_5 = np.array([3, -0.5, 0])
        o_6 = np.array([0.5, 0.6, 0])
        o_7 = np.array([-2.5, -3.5, 0])

        octagon_vertices = [o_0, o_1, o_2, o_3, o_4, o_5, o_6, o_7]

        n_equals_8, line_oct, octaygon, area_oct, intersection_points_oct, intersection_point_indices_oct = ConstructPolygonLine(8, 0, 0, 0, octagon_vertices)
        center_1, center_2 = intersection_point_indices_oct[2].get_center(), intersection_point_indices_oct[4].get_center()
        center_3, center_4 = intersection_point_indices_oct[5].get_center(), intersection_point_indices_oct[7].get_center()
        intersection_point_indices_oct[4].move_to(center_1)
        intersection_point_indices_oct[2].move_to(center_2)
        intersection_point_indices_oct[7].move_to(center_3)
        intersection_point_indices_oct[5].move_to(center_4)


        # self.wait()
