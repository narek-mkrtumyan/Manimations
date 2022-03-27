import sys
sys.path.append('../../')
from Functions.qarakusi import *

class Problem12525(MovingCameraScene):
    def construct(self):

        problem_number = VGroup(MathTex(r'12525', color=ORANGE, font_size=60))
        problem_number.add(SurroundingRectangle(problem_number[0], color=GREEN))
        problem_number.move_to([-5, 3, 0])

        problem_test_parts = MathTex(
            r'3', r'\textrm{ կողմով եռանկյան մեջ նշված է }', r'10', r'\textrm{ կետ։}',
            r'\textrm{Ապացուցել, որ կարելի է ընտրել դրանցից}',
            r'2', r'\textrm{-ն այնպես, որ դրանցով կազմված}',
            r'\textrm{հատվածի երկարությունը մեծ չլինի }', r'1', r'\textrm{-ից։}',
            tex_template=armenian_tex_template, font_size=30
            )
        
        problem_test_parts[0].set_color(ORANGE)
        problem_test_parts[2].set_color(ORANGE)
        problem_test_parts[5].set_color(ORANGE)
        problem_test_parts[8].set_color(ORANGE)

        problem = VGroup(
            VGroup(*problem_test_parts[:4]),
            VGroup(*problem_test_parts[4]),
            VGroup(*problem_test_parts[5:7]),
            VGroup(*problem_test_parts[7:])
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).move_to([-3.5, 3, 0])

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
            Dot(coord_vertices[0] + 2*unit_vectors[0], radius=1.5*DEFAULT_DOT_RADIUS),
            Dot(coord_vertices[0] + 4*unit_vectors[0], radius=1.5*DEFAULT_DOT_RADIUS),
            Dot(coord_vertices[1] + 2*unit_vectors[1], radius=1.5*DEFAULT_DOT_RADIUS),
            Dot(coord_vertices[1] + 4*unit_vectors[1], radius=1.5*DEFAULT_DOT_RADIUS),
            Dot(coord_vertices[2] + 2*unit_vectors[2], radius=1.5*DEFAULT_DOT_RADIUS),
            Dot(coord_vertices[2] + 4*unit_vectors[2], radius=1.5*DEFAULT_DOT_RADIUS),
        ).set_color(GREEN)

        center_dot = Dot([0, np.sqrt(3)-2, 0], radius=1.5*DEFAULT_DOT_RADIUS, color=GREEN)

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
                MathTex(r'1', font_size=60).move_to(lengths_are_3[0].get_center() - 2*unit_vectors[0]).shift(RIGHT*0.25 + DOWN*0.4),
                MathTex(r'1', font_size=60).move_to(lengths_are_3[0].get_center()                    ).shift(RIGHT*0.25 + DOWN*0.4),
                MathTex(r'1', font_size=60).move_to(lengths_are_3[0].get_center() + 2*unit_vectors[0]).shift(RIGHT*0.25 + DOWN*0.4)
            ),
            VGroup(
                MathTex(r'1', font_size=60).move_to(lengths_are_3[1].get_center() - 2*unit_vectors[1]).shift(LEFT*0.25 + DOWN*0.4),
                MathTex(r'1', font_size=60).move_to(lengths_are_3[1].get_center()                    ).shift(LEFT*0.25 + DOWN*0.4),
                MathTex(r'1', font_size=60).move_to(lengths_are_3[1].get_center() + 2*unit_vectors[1]).shift(LEFT*0.25 + DOWN*0.4)
            ),
            VGroup(
                MathTex(r'1', font_size=60).move_to(lengths_are_3[2].get_center() - 2*unit_vectors[2]).shift(UP*0.25),
                MathTex(r'1', font_size=60).move_to(lengths_are_3[2].get_center()                    ).shift(UP*0.25),
                MathTex(r'1', font_size=60).move_to(lengths_are_3[2].get_center() + 2*unit_vectors[2]).shift(UP*0.25)
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


        coords_setup_3 = [
            np.array([0.2, 2.3, 0]),
            np.array([-0.2, -1.7, 0]),
            np.array([1.4, 0.1, 0]),
            np.array([-0.3, 1, 0]),
            np.array([-0.5, 0, 0]),
            np.array([0.9, -1, 0]),
            np.array([-1, -1.3, 0]),
            np.array([-0.6, -0.9, 0]),
            np.array([1.5, -1.6, 0]),
            np.array([-2.2, -1.3, 0])
        ]

        dots_setup_3 = VGroup(*[Dot(coord) for coord in coords_setup_3]).set_color(ORANGE)

        wanted_triangle_3 = Polygon(dividing_dots[0].get_center(), center_dot.get_center(), dividing_dots[-1].get_center(),stroke_width=0)
        wanted_triangle_3.set_fill(opacity=0.4, color=GREEN)
        wanted_segment_3 = Line(coords_setup_3[6], coords_setup_3[7], color=ORANGE)

        coords_setup_4 = [
            np.array([-0.2, 2.5, 0]),
            np.array([0.2, 1.7, 0]),
            np.array([1, 1, 0]),
            np.array([-0.2, 0.5, 0]),
            np.array([-1.5, 0, 0]),
            np.array([0.9, 0.4, 0]),
            np.array([-1, -0.7, 0]),
            np.array([0.1, -1.1, 0]),
            np.array([2.5, -1.6, 0]),
            np.array([-2.2, -1.8, 0])
        ]

        dots_setup_4 = VGroup(*[Dot(coord) for coord in coords_setup_4]).set_color(ORANGE)

        wanted_triangle_4_1 = Polygon(dividing_dots[1].get_center(), vertices[1].get_center(), dividing_dots[2].get_center(), stroke_width=0)
        wanted_triangle_4_1.set_fill(opacity=0.4, color=GREEN)
        wanted_segment_4_1 = Line(coords_setup_4[0], coords_setup_4[1], color=ORANGE)

        wanted_triangle_4_2 = Polygon(dividing_dots[2].get_center(), center_dot.get_center(), dividing_dots[3].get_center(), stroke_width=0)
        wanted_triangle_4_2.set_fill(opacity=0.4, color=GREEN)
        wanted_segment_4_2 = Line(coords_setup_4[2], coords_setup_4[5], color=ORANGE)

        short_segment_1 = always_redraw(lambda: Line(dots_setup_1[1].get_center(), dots_setup_1[2].get_center(), color=ORANGE))
        short_segment_2 = Line(dots_setup_2[7].get_center(), dots_setup_2[6].get_center(), color=ORANGE)
        short_segment_3 = Line(dots_setup_2[5].get_center(), dots_setup_2[8].get_center(), color=ORANGE)

        small_triangle_dots = VGroup( dividing_dots[1], vertices[1], dividing_dots[2] )

        small_triangle_sides = VGroup(
            Line(vertices[1].get_center(), dividing_dots[1].get_center()),
            Line(vertices[1].get_center(), dividing_dots[2].get_center()),
            dividing_lines[0],
        )

        small_triangle_sides_are_1 = VGroup(
            lengths_are_1[0][2].copy(),
            lengths_are_1[1][0].copy(),
            MathTex(r'1', font_size=60).next_to(dividing_lines[0].get_center(), DOWN)
        )

        dots_small_line = VGroup(
            Dot(small_triangle_dots[0].get_center(), color=ORANGE),
            Dot(small_triangle_dots[1].get_center(), color=ORANGE)
        )

        small_line = always_redraw(lambda: Line(dots_small_line[0].get_center(), dots_small_line[1].get_center(), color=ORANGE))
        length_small_line = always_redraw(lambda: 
                DecimalNumber(SegmentLength(small_line)/2, 1, font_size=25)
                .move_to(small_line.get_midpoint() - 0.25 * small_line.copy().rotate(PI/2).get_unit_vector())
            )

        ten_greater_9 = MathTex(r'10', r'>', r'9', font_size=100).move_to([5, 2, 0])
        ten_greater_9[0].set_color(ORANGE)
        ten_greater_9[2].set_color(GREEN)

        thumbnail_line = Line(coords_setup_1[4], coords_setup_1[6], color=ORANGE)
        thumbnail_text = MathTex(r'<1?', color=ORANGE, font_size=70).next_to(coords_setup_1[4], DR).shift(0.3*UR)


    # ANIMATIONS
        self.play(Create(vertices))
        self.play(Create(sides))
        self.play(Write(lengths_are_3))
        self.wait(0.5)

        self.play(Write(problem[0]))
        self.play(Create(dots_setup_1))
        self.play(Write(problem[1]))
        self.play(Write(problem[2]))
        self.play(Write(problem[3]))
        self.wait(0.5)

        self.play(Create(short_segment_1))
        self.wait(0.5)
        self.play(FadeOut(problem))
        self.wait(0.5)

    # # FOR THUMBNAIL 
    #     self.add(problem_number, thumbnail_text, thumbnail_line)
    #     self.remove(short_segment_1)
    #     self.wait()

        self.play(ReplacementTransform(dots_setup_1, dots_setup_2, run_time=3))
        self.wait(0.5)

        self.play(Uncreate(short_segment_1))
        self.wait(0.5)
        self.play(Create(short_segment_2))
        self.wait(0.5)
        self.play(Create(short_segment_3))
        self.wait(0.5)
        self.play(FadeOut(short_segment_2, short_segment_3))
        self.wait(0.5)

        self.play(FadeOut(dots_setup_2))
        self.wait(0.5)

        self.play(Create(dividing_dots[4:]))
        self.wait(0.5)
        self.play(ReplacementTransform(lengths_are_3[2], lengths_are_1[2]))
        self.wait(0.5)

        self.play(Create(dividing_dots[0:4]))
        self.wait(0.5)
        self.play(
            ReplacementTransform(lengths_are_3[0], lengths_are_1[0]),
            ReplacementTransform(lengths_are_3[1], lengths_are_1[1])
        )
        self.wait(0.5)

        self.play(Create(dividing_lines, rate_func=linear, run_time=3))
        self.wait(0.5)

        self.play(Create(center_dot))
        self.wait(0.5)
        self.add(dividing_dots[1], dividing_dots[2])
        self.play(Create(small_triangle_sides[:2]))
        self.wait(0.5)

        self.play(
            *[mob.animate().set_opacity(0.4) for mob in self.mobjects],
            VGroup(small_triangle_sides, small_triangle_dots, small_triangle_sides_are_1).animate().set_opacity(1)
        )
        self.wait()

        self.play(self.camera.frame.animate.scale(0.5).move_to(small_triangle_dots[1].get_center() - np.array([0, 1, 0])))
        self.wait(0.5)

        self.play(Create(dots_small_line))
        self.play(Create(small_line))
        self.wait(0.5)
        self.play(Write(length_small_line))
        self.wait(0.5)
        self.play(
            dots_small_line[0].animate().shift([0.6, 0.2, 0]),
            dots_small_line[1].animate().shift([0, -0.2, 0]),
            run_time=1.5
        )
        self.wait(0.5)
        self.play(
            dots_small_line[0].animate().shift([-0.1, 0.4, 0]),
            dots_small_line[1].animate().shift([0.5, -1.2, 0]),
            run_time=1.5
        )
        self.wait(0.5)
        self.play(
            dots_small_line[0].animate().shift([0.5, 0.8, 0]),
            dots_small_line[1].animate().shift([-0.2, -0.2, 0]),
            run_time=1.5
        )
        self.wait(0.5)
        self.play(
            dots_small_line[0].animate().shift([0, 0.1, 0]),
            dots_small_line[1].animate().shift([0.5, 0, 0]),
            run_time=1.5
        )
        self.wait(0.5)

        self.play(self.camera.frame.animate.scale(2).move_to(ORIGIN))
        self.wait(0.5)

        self.play(
            VGroup(vertices, sides, dividing_dots, dividing_lines, center_dot, lengths_are_1).animate().set_opacity(1),
            FadeOut(small_line, length_small_line, dots_small_line, small_triangle_sides_are_1[2])
        )
        self.wait(0.5)

        self.play(Create(numbers_in_triangles), run_time=4, rate_func=linear)
        self.wait(0.5)
        
        self.play(Write(ten_greater_9))
        self.wait(0.5)

        self.play(FadeOut(numbers_in_triangles))
        self.wait(0.5)

        self.play(FadeIn(dots_setup_3))
        self.wait(0.5)
        self.play(FadeIn(wanted_triangle_3))
        self.add(dots_setup_3[6], dots_setup_3[7])
        self.wait(0.5)
        self.play(Create(wanted_segment_3))
        self.wait(1)
        self.play(FadeOut(wanted_triangle_3, wanted_segment_3, dots_setup_3))
        self.wait(0.5)

        self.play(FadeIn(dots_setup_4))
        self.wait(0.5)
        self.play(FadeIn(wanted_triangle_4_1))
        self.add(dots_setup_4[0], dots_setup_4[1])
        self.wait(0.5)
        self.play(Create(wanted_segment_4_1))
        self.wait(1)
        self.play(FadeOut(wanted_triangle_4_1, wanted_segment_4_1))
        self.wait(0.5)

        self.play(FadeIn(wanted_triangle_4_2))
        self.add(dots_setup_4[2], dots_setup_4[5])
        self.wait(0.5)
        self.play(Create(wanted_segment_4_2))
        self.wait(1)
        self.play(FadeOut(wanted_triangle_4_2, wanted_segment_4_2))
        self.wait(0.5)

        self.play(FadeOut(*[mob for mob in self.mobjects]))





