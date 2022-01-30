from manim import *
import numpy as np
import sys
sys.path.append('../../../')
sys.path.append('../../')
sys.path.append('../')
from Functions.QarakusiFunctions import *

class Problem12525(Scene):
    def construct(self):

        coord_vertices = [
            np.array([-3, -2, 0]),
            np.array([0, np.sqrt(27)-2, 0]),
            np.array([3, -2, 0]),
        ]

        vertices = VGroup(*[Dot(coord) for coord in coord_vertices], color=WHITE)

        sides = VGroup(
            Line(coord_vertices[0], coord_vertices[1], color=WHITE),
            Line(coord_vertices[1], coord_vertices[2], color=WHITE),
            Line(coord_vertices[2], coord_vertices[0], color=WHITE)
        )

        lengths_are_3 = VGroup(
            MathTex(r'3', font_size=100).next_to(sides[0].get_midpoint(), UL*2),
            MathTex(r'3', font_size=100).next_to(sides[1].get_midpoint(), UR*2),
            MathTex(r'3', font_size=100).next_to(sides[2].get_midpoint(), DOWN*2)
        )

        unit_vectors = [*[side.get_unit_vector() for side in sides]]

        dividing_dots = VGroup(
            Dot(coord_vertices[0] + 2*unit_vectors[0], radius=2*DEFAULT_DOT_RADIUS),
            Dot(coord_vertices[0] + 4*unit_vectors[0], radius=2*DEFAULT_DOT_RADIUS),
            Dot(coord_vertices[1] + 2*unit_vectors[1], radius=2*DEFAULT_DOT_RADIUS),
            Dot(coord_vertices[1] + 4*unit_vectors[1], radius=2*DEFAULT_DOT_RADIUS),
            Dot(coord_vertices[2] + 2*unit_vectors[2], radius=2*DEFAULT_DOT_RADIUS),
            Dot(coord_vertices[2] + 4*unit_vectors[2], radius=2*DEFAULT_DOT_RADIUS),
        ).set_color(GREEN)

        center_dot = Dot([0, np.sqrt(3)-2, 0], color=GREEN)

        dividing_lines = VGroup(
            Line(dividing_dots[1].get_center(), dividing_dots[2].get_center()),
            Line(dividing_dots[0].get_center(), dividing_dots[3].get_center()),
            Line(dividing_dots[0].get_center(), dividing_dots[5].get_center()),
            Line(dividing_dots[1].get_center(), dividing_dots[4].get_center()),
            Line(dividing_dots[3].get_center(), dividing_dots[4].get_center()),
            Line(dividing_dots[2].get_center(), dividing_dots[5].get_center()),
        ).set_color(GREEN)

        lengths_are_1 = VGroup(
            VGroup(
                MathTex(r'1', font_size=75).move_to(lengths_are_3[0].get_center()).shift(DR*0.25),
                MathTex(r'1', font_size=75).move_to(lengths_are_3[0].get_center() + 2*unit_vectors[0]).shift(DR*0.25),
                MathTex(r'1', font_size=75).move_to(lengths_are_3[0].get_center() - 2*unit_vectors[0]).shift(DR*0.25),
            ),
            VGroup(
                MathTex(r'1', font_size=75).move_to(lengths_are_3[1].get_center()).shift(DL*0.2),
                MathTex(r'1', font_size=75).move_to(lengths_are_3[1].get_center() + 2*unit_vectors[1]).shift(DL*0.25),
                MathTex(r'1', font_size=75).move_to(lengths_are_3[1].get_center() - 2*unit_vectors[1]).shift(DL*0.25),
            ),
            VGroup(
                MathTex(r'1', font_size=75).move_to(lengths_are_3[2].get_center()).shift(UP*0.25),
                MathTex(r'1', font_size=75).move_to(lengths_are_3[2].get_center() + 2*unit_vectors[2]).shift(UP*0.25),
                MathTex(r'1', font_size=75).move_to(lengths_are_3[2].get_center() - 2*unit_vectors[2]).shift(UP*0.25),
            )
        )

        numbers_in_triangles = VGroup(
            MathTex(r'1', font_size=50).move_to(vertices[1].get_center()      - np.array([0, 2/np.sqrt(3), 0])),
            MathTex(r'2', font_size=50).move_to(dividing_dots[1].get_center() - np.array([0, 2/np.sqrt(3), 0])),
            MathTex(r'3', font_size=50).move_to(center_dot.get_center()       + np.array([0, 2/np.sqrt(3), 0])),
            MathTex(r'4', font_size=50).move_to(dividing_dots[2].get_center() - np.array([0, 2/np.sqrt(3), 0])),
            MathTex(r'5', font_size=50).move_to(dividing_dots[0].get_center() - np.array([0, 2/np.sqrt(3), 0])),
            MathTex(r'6', font_size=50).move_to(dividing_dots[5].get_center() + np.array([0, 2/np.sqrt(3), 0])),
            MathTex(r'7', font_size=50).move_to(center_dot.get_center()       - np.array([0, 2/np.sqrt(3), 0])),
            MathTex(r'8', font_size=50).move_to(dividing_dots[4].get_center() + np.array([0, 2/np.sqrt(3), 0])),
            MathTex(r'9', font_size=50).move_to(dividing_dots[3].get_center() - np.array([0, 2/np.sqrt(3), 0])),
        ).set_color(GREEN)
        
        coords_setup_1 = [
            np.array([-0.2, 2.5, 0]),
            np.array([0.2, 1.7, 0]),
            np.array([1, 1, 0]),
            np.array([-0.2, 0.5, 0]),
            np.array([-1.5, 0, 0]),
            np.array([0.9, -0.2, 0]),
            np.array([-1, -0.7, 0]),
            np.array([0.4, -1.1, 0]),
            np.array([2.5, -1.6, 0]),
            np.array([-2.2, -1.8, 0])
        ]

        dots_setup_1 = VGroup(*[Dot(coord) for coord in coords_setup_1]).set_color(ORANGE)

        
        coords_setup_2 = [
            np.array([0.2, 2.3, 0]),
            np.array([-0.2, 1.7, 0]),
            np.array([1.5, -0.3, 0]),
            np.array([-0.7, 1, 0]),
            np.array([-0.5, 0, 0]),
            np.array([0.9, -1, 0]),
            np.array([-1, -1.3, 0]),
            np.array([-0.6, -0.9, 0]),
            np.array([1.5, -1.6, 0]),
            np.array([-2.2, -1.3, 0])
        ]

        dots_setup_2 = VGroup(*[Dot(coord) for coord in coords_setup_2]).set_color(ORANGE)

        
        short_segment_1 = always_redraw(lambda: Line(dots_setup_1[1].get_center(), dots_setup_1[2].get_center(), color=ORANGE))
        short_segment_2 = always_redraw(lambda: Line(dots_setup_1[7].get_center(), dots_setup_1[6].get_center(), color=ORANGE))
        short_segment_3 = always_redraw(lambda: Line(dots_setup_1[5].get_center(), dots_setup_1[8].get_center(), color=ORANGE))

        self.add(vertices, sides)

        self.add(dots_setup_1)
        self.add(short_segment_1, short_segment_2, short_segment_3)
        self.wait()

        self.play(ReplacementTransform(dots_setup_1, dots_setup_2, run_time=3))

        # self.add(dividing_dots, dividing_lines, center_dot, lengths_are_3, lengths_are_1, numbers_in_triangles)




