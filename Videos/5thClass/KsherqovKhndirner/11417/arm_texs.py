from manim import Tex, TexTemplate

ARMTEX = TexTemplate()
ARMTEX.add_to_preamble(r'\usepackage{armtex}')

Tex.set_default(tex_template=ARMTEX)

gram = Tex('գրամ')
sixty = Tex('- ', '60', font_size=60)

two_times_sixty = Tex('- ', r'2 $\cdot$ 60 = 120', font_size=60)
