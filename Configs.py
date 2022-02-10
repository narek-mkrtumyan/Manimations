from manim import *

COLORS = [WHITE, GREEN, ORANGE, RED, BLUE, YELLOW]

DEFAULT_ENDMARK_LENGTH = 0.2
DEFAULT_COUNTING_COLOR = ORANGE

left_bound = Line([-3.5, 5, 0], [-3.5, -5, 0])
right_bound = Line([3.5, 5, 0], [3.5, -5, 0])
bounds = VGroup(left_bound, right_bound)


armenian_tex_template = TexTemplate()
armenian_tex_template.add_to_preamble(r"\usepackage{armtex}")




