from manim import *

COLORS = [WHITE, GREEN, ORANGE, RED, BLUE, YELLOW]

DEFAULT_ENDMARK_LENGTH = 0.2
DEFAULT_COUNTING_COLOR = ORANGE

left_bound = Line([-3.5, 5, 0], [-3.5, -5, 0])
right_bound = Line([3.5, 5, 0], [3.5, -5, 0])
bounds = VGroup(left_bound, right_bound)

white_chess_figures_fill_color = WHITE
white_chess_figures_stroke_color = BLACK
black_chess_figures_fill_color = BLACK
black_chess_figures_stroke_color = WHITE
chess_figures_stroke_width = 2.5
chess_figures_scale_factor = 0.3


armenian_tex_template = TexTemplate()
armenian_tex_template.add_to_preamble(r"\usepackage{armtex}")

ARMTEX = TexTemplate()
ARMTEX.add_to_preamble(r"\usepackage{armtex}")

MONTHS_ARM = [
    'Հունվար',
    'Փետրվար',
    'Մարտ',
    'Ապրիլ',
    'Մայիս',
    'Հունիս',
    'Հուլիս',
    'Օգոստոս',
    'Սեպտեմբեր',
    'Հոկտեմբեր',
    'Նոյեմբեր',
    'Դեկտեմբեր'
]

MONTHS_LENGTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


WEEK_DAYS_ARM = ['Եկ', 'Եք', 'Չո', 'Հի', 'Ու', 'Շա', 'Կի']

