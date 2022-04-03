import sys
sys.path.append('../../../')
from Functions.qarakusi import *

class linear_algebra_chapter_0_thumbnail(Scene):
    def construct(self):

        white_line_1 = Line([-7, -2, 0], [7, 2, 0], stroke_width=6)
        white_line_2 = Line([-7, 3, 0], [7, -3, 0], stroke_width=6)

        white_lines = VGroup(white_line_1, white_line_2)

        blue_line_1 = Line([-14, -4, 0], [14, 4, 0], stroke_width=6)
        blue_line_2 = Line([-14, 6, 0], [14, -6, 0], stroke_width=6)

        blue_lines = VGroup(
            blue_line_1.copy().set_color(BLUE).shift(UP * 2),
            blue_line_1.copy().set_color(BLUE).shift(UP * 4),
            blue_line_1.copy().set_color(BLUE).shift(UP * 6),

            blue_line_1.copy().set_color(BLUE).shift(DOWN * 2),
            blue_line_1.copy().set_color(BLUE).shift(DOWN * 4),
            blue_line_1.copy().set_color(BLUE).shift(DOWN * 6),


            blue_line_2.copy().set_color(BLUE).shift(UP * 2),
            blue_line_2.copy().set_color(BLUE).shift(UP * 4),
            blue_line_2.copy().set_color(BLUE).shift(UP * 6),

            blue_line_2.copy().set_color(BLUE).shift(DOWN * 2),
            blue_line_2.copy().set_color(BLUE).shift(DOWN * 4),
            blue_line_2.copy().set_color(BLUE).shift(DOWN * 6),
        )


        green_arrow = Arrow(
            start=ORIGIN - np.array([14/5, 4/5, 0]) * 0.085,
            end=np.array([14/5, 4/5, 0]) * 1.1,
            color=GREEN, stroke_width=9,
        )
        green_arrow.tip.scale(1.25)
        
        red_arrow = Arrow(
            start=ORIGIN - np.array([14/5, -6/5, 0]) * 0.085,
            end=np.array([14/5, -6/5, 0]) * 1.1,
            color=RED, stroke_width=9,
        )
        red_arrow.tip.scale(1.25)

        arrows = VGroup(green_arrow, red_arrow)

        text = MathTex(
            r'\textrm{Գծային}\ ', 
            r'\textrm{հանրահաշվի}\ ', 
            r'\textrm{հիմունքներ}\ ',
            tex_template=armenian_tex_template, font_size=120
        ).arrange(DOWN, buff=1)

        background_rects = VGroup(
            BackgroundRectangle(text[0], color=BLACK, fill_opacity=0.5),
            BackgroundRectangle(text[1], color=BLACK, fill_opacity=0.5),
            BackgroundRectangle(text[2], color=BLACK, fill_opacity=0.5)
        )

        # white_lines.set_opacity(0.6)
        # blue_lines.set_opacity(0.6)
        # arrows.set_opacity(0.8)


        VGroup(white_lines, blue_lines).set_opacity(0.7)


        self.add(white_lines, blue_lines, arrows)

        self.add(background_rects, text)


