from manim import *

# Հայերեն գրելու համար tex_template (նույն բանն են)
armenian_tex_template = TexTemplate()
armenian_tex_template.add_to_preamble(r'\usepackage{armtex}')
ARMTEX = TexTemplate()
ARMTEX.add_to_preamble(r'\usepackage{armtex}')


COLORS = [WHITE, GREEN, ORANGE, RED, BLUE, YELLOW]



# Մասերով խնդիրների հաստատուններ
DEFAULT_ENDMARK_LENGTH = 0.2
DEFAULT_SEGMENT_TEXT_POSITION = 0.75 * UP

DEFAULT_EXTRA_SEGMENT_COLOR = PURE_GREEN
DEFAULT_COUNTING_COLOR = ORANGE

DEFAULT_TASK_FONT_SIZE = 35
DEFAULT_TASK_NUMBER_FONT_SIZE = 40
DEFAULT_NAME_FONT_SIZE = 40
DEFAULT_SEGMENT_LENGTH_FONT_SIZE = 50
DEFAULT_TOTAL_LENGTH_FONT_SIZE = 70
DEFAULT_EQUATION_FONT_SIZE = 50

# Կշեռքով խնդիրների հաստատուններ
DEFAULT_SCALES_BUFF = 0

# Շախմատի ֆիգուրների հաստատուններ
white_chess_figures_fill_color = WHITE
white_chess_figures_stroke_color = BLACK
black_chess_figures_fill_color = BLACK
black_chess_figures_stroke_color = WHITE
chess_figures_stroke_width = 2.5
chess_figures_scale_factor = 0.3

# test_tex_template = TexTemplate() 
# test_tex_template.add_to_preamble(r'\\usepackage{fontspec}', r'\\setmainfont{Dejavu Serif}')

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


WEEK_DAYS_ARM = ['ԵԿ', 'ԵՔ', 'ՉՈ', 'ՀԻ', 'Ու', 'ՇԱ', 'ԿԻ']
WEEK_DAYS_ARM_LONG = ['ԵՐԿ', 'ԵՐՔ', 'ՉՐՔ', 'ՀՆԳ', 'ՈւՐԲ', 'ՇԲԹ', 'ԿԻՐ']

WEEK_BLOCK_WIDTH = 0.35
WEEK_BLOCK_HEIGHT = 0.25

