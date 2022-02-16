from manim import *
import numpy as np

 
class Logo(Scene):
    def construct(self):
        
        # self.camera.background_color = WHITE

        logo = SVGMobject("white_only_logo.svg").scale(1.7).shift(0.7*UP)
        ysu = Text('ԵՊՀ', font_size=35).shift(2.9*UP)
        mmfsss = VGroup(*[Text('ՄԱԹԵՄԱՏԻԿԱՅԻ', font_size=30), Text('ԵՎ ՄԵԽԱՆԻԿԱՅԻ', font_size=30), 
        Text('ՖԱԿՈՒԼՏԵՏԻ', font_size=30), Text('ՈՒԳԸ', font_size=30)]).arrange(direction=DOWN, buff=0.2).shift(2.3*DOWN)

        # self.add(logo, ysu, mmfsss)

        self.wait(0.3)
        self.play(Write(ysu, run_time=1))
        self.play(Write(mmfsss, run_time=3), Write(logo, run_time=4.5))
        self.play(FadeOut(*[mob for mob in self.mobjects]), run_time=1)
        self.wait(0.2)
