from manim import *

import sys
sys.path.append("../../")       # relative path to the root of the repository
from Functions.GeometryFunctions.GeometryFunctions import *    # or import specific function

class Problem4(Scene):
    def construct(self):

    # Draw a green circle with diameters AB (orange) and center O(orange).
        circle = Circle(radius=2.0, color=GREEN)

        pointA = Dot(color=ORANGE).shift(2*LEFT)
        labelA = Text("A", color=ORANGE, font_size=30).next_to(pointA,DL,buff=SMALL_BUFF)
        A = VGroup(pointA,labelA)

        pointB = Dot(color=ORANGE).shift(2*RIGHT)
        labelB = Text("B", color=ORANGE, font_size=30).next_to(pointB,DR,buff=SMALL_BUFF)
        B = VGroup(pointB,labelB)

        lineAB = Line(pointA.get_center(),pointB.get_center(), color=ORANGE)

        pointO = Dot(color=ORANGE)
        labelO = Text("O", color=ORANGE, font_size=30).next_to(pointO,DOWN,buff=SMALL_BUFF)
        O = VGroup(pointO,labelO)

        self.play(Create(circle, run_time=3.0))
        self.wait()

        self.play(
            Write(O)
        )
        self.wait()

        self.play(Create(lineAB, run_time=3.0))
        self.wait()

        self.play(
            Write(A),
            Write(B)
        )
        self.wait(1)

    # Draw a point C on the circle (close to A) and connect it to A and B. Draw blue AC and white BC.
        pointC = Dot(color=ORANGE).move_to(circle.point_at_angle(5*PI/6))
        labelC = Text("C", color=ORANGE, font_size=30).next_to(pointC,UL,buff=SMALL_BUFF)
        labelC.add_updater(lambda x: 
            x.next_to(pointC,UL,buff=SMALL_BUFF)
        )
        C= VGroup(pointC,labelC)

        self.play(Write(C))
        self.wait(1)

        color_frac = ValueTracker(0)

        AC =  Line(color=BLUE).add_updater(lambda z:
            z.become(Line(pointA.get_center(),pointC.get_center(), 
                color=rgb_to_hex(hex_to_rgb(BLUE)*(1-color_frac.get_value()) + hex_to_rgb(YELLOW)*color_frac.get_value())))
        )

        BC =  Line(color=WHITE).add_updater(lambda z:
            z.become(Line(pointB.get_center(),pointC.get_center(), 
                color=rgb_to_hex(hex_to_rgb(WHITE)*(1-color_frac.get_value()) + hex_to_rgb(YELLOW)*color_frac.get_value())))
        )

        self.play(
            Create(AC, run_time=3.0),
            Create(BC, run_time=3.0)
        )
        self.add(A, B, C)
        self.wait(1)

    # Move point C among the circle and simultaneously make CA and CB Yellow 
        arc = ArcBetweenPoints(circle.point_at_angle(PI/2), circle.point_at_angle(5*PI/6), radius=2.0).flip().rotate(PI/3)

        self.play(
            MoveAlongPath(pointC, arc, rate_func=linear),
            color_frac.animate(rate_func=linear).set_value(1), 
            run_time=6
        )
        self.wait(1)

        AC.clear_updaters()
        BC.clear_updaters()

    # When C arrives to the center of the AB, stop and make chords AC and BC thicker and return to normal size
        self.play(
            AC.animate(run_time=2.0, rate_func=there_and_back).set_stroke_width(8),
            BC.animate(run_time=2.0, rate_func=there_and_back).set_stroke_width(8)
        )
        self.wait(1)

    # Draw sign of equal sizes on AC and BC.
        equality_sign_AC = SegmentEqualitySign1(AC, color=YELLOW)
        equality_sign_BC = SegmentEqualitySign1(BC, color=YELLOW)

        self.play(
            Create(equality_sign_AC),
            Create(equality_sign_BC)
        )
        self.wait(1)

        #Connect O and C.
        OC = Line(pointO.get_center(),pointC.get_center())

        self.play(
            Create(OC, run_time=3.0)
        )
        self.add(O, C)
        self.wait(1)

    # Blink 2 times the segments Ac and CB.
        self.play(
            FadeIn(AC),
            FadeIn(BC),
        )
        self.play(
            FadeIn(AC),
            FadeIn(BC),
        )
        self.wait(1)

    # Draw a sign of equal segments for AO and OB.
        AO = Line(pointA,pointO)
        OB = Line(pointO,pointB)

        equality_sign_AO = SegmentEqualitySign2(AO, color=ORANGE)
        equality_sign_BO = SegmentEqualitySign2(OB, color=ORANGE)

        self.play(
            Create(equality_sign_AO),
            Create(equality_sign_BO)
        )

    # Blink 2 times the segments OC.
        self.play(FadeIn(OC))
        self.play(FadeIn(OC))
        self.wait(1)

    # Draw the following text below the circle 
    # "АC=CB => ABC եռանկյունը հավասարասրուն է և CO միջնագիծը կլինի նաև բարձրություն, ուստի< АОC = 90^o"
    
        t1 = MathTex(r'AC=CB\ \Rightarrow\ \textrm{եռանկյունը հավասարասրուն է և}\ CO',
            font_size=32, tex_template=armenian_tex_template).next_to(circle,DOWN,buff=0.5)
        
        t2 = MathTex(r'\textrm{միջնագիծը կլինի նաև բարձրություն, ուստի}\ \angle AOC =', '90^{\circ}',
            font_size=32, tex_template=armenian_tex_template).next_to(t1,DOWN)

        self.play(Write(t1))
        self.play(Write(t2))
        self.wait(1)

    # Draw a blue rectangle around the number 90^o..
        box = SurroundingRectangle(t2[-1], color=BLUE, buff=SMALL_BUFF)

        self.play(Create(box))
        self.wait(1)

    # Draw a sign of 90 degrees to the angle COA.
        angle = RightAngle(AO,OC, length=0.3, quadrant=(-1,1))

        self.play(Create(angle))
        self.wait(1)

    # Move the copy of number 90 from the text <AOC=90^o to the angle AOC.
        anglelabel = MathTex(r"90^{\circ}", font_size=32).next_to(angle,UL, buff=SMALL_BUFF)

        self.play(
            ReplacementTransform(t2[-1].copy(),anglelabel, run_time=3.0)
        )
        self.wait()
