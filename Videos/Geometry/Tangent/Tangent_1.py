from manim import  *
import numpy as np

point_name_size = 25

o = np.array([0, 0, 0])
O = Dot(o)
O_ = Text('O', font_size=point_name_size).next_to(o, DOWN)
r = 2.5
R_ = Text('r', font_size=point_name_size)
crc = Circle(radius=r, color=GREEN).move_to(o)


class MoveSegment(Scene):
    def construct(self):
        
        alpha = ValueTracker(0)

        A = always_redraw(lambda: Dot([r * np.cos(alpha.get_value()), r * np.sin(alpha.get_value()), 0], color=ORANGE))
        B = always_redraw(lambda: Dot([-r * np.cos(alpha.get_value()), r * np.sin(alpha.get_value()), 0], color=ORANGE))

        segment = always_redraw(lambda: 
        Line(start=[r * np.cos(alpha.get_value()), r * np.sin(alpha.get_value()), 0], 
        end=[-r * np.cos(alpha.get_value()), r * np.sin(alpha.get_value()), 0], 
        color=ORANGE).scale(7 / (2 * r *np.cos(alpha.get_value()))))

        self.add(O, crc)
        self.add(A, B, segment)
        self.wait(0.5)
        self.play(alpha.animate.set_value(PI / 2), run_time=3, rate_func=linear)
        self.wait(0.5)
        self.remove(A, B, segment)


class IntersectionToTangent(Scene):
    def construct(self):

        self.add(O, crc)

        t = np.array([0, r, 0])
        T = Dot(t, color=ORANGE)

        alpha = ValueTracker(PI / 2)
        
        H = always_redraw(lambda: Dot([r * np.cos(alpha.get_value()), r * np.sin(alpha.get_value()), 0], color=ORANGE))
        segment = always_redraw(
            lambda: Line(start=t, end=[r * np.cos(alpha.get_value()), r * np.sin(alpha.get_value()), 0], color=ORANGE
            ).scale(7 / np.sqrt((t[0] - r * np.cos(alpha.get_value()))**2 + (t[1] - r * np.sin(alpha.get_value()))**2)))

        self.add(O, crc)
        self.add(segment, T, H)
        self.wait(0.5)
        self.play(alpha.animate.set_value(2.5 * PI), run_time=7, rate_func=linear)
        self.wait(0.5)

        self.remove(segment, T, H)


class RotateTangent(Scene):
    def construct(self):

        alpha = ValueTracker(PI / 2)
        
        H = always_redraw(lambda: Dot([r * np.cos(alpha.get_value()), r * np.sin(alpha.get_value()), 0], color=ORANGE))
        # h = H.get_center()
        tangent = always_redraw(
            lambda: TangentLine(crc, float("{:.2f}".format((alpha.get_value() - (int(alpha.get_value() / (2*PI))*(2*PI))) / (2*PI))), 
            length=7, color=ORANGE))

        self.add(O, crc)
        self.add(tangent, H)
        self.wait(0.5)
        self.play(alpha.animate.set_value(2.5 * PI), run_time=6, rate_func=linear)
        self.wait(0.5)
        

class ShortestWay(Scene):
    def construct(self):

        h = np.array([0, r, 0])
        H = Dot(h, color=ORANGE)
        H_ = Text('H', font_size=point_name_size).next_to(h, UP).shift(0.25*LEFT)
        OH = Line(start=o, end=h, color=ORANGE)
        R_OH = R_.copy().next_to(OH, LEFT)
        tangent = TangentLine(crc, 1/4, color=ORANGE, length=12)
        tangent_left = [-6, r, 0]
        tangent_right = [6, r, 0]

        right_angle = RightAngle(Line(h, tangent_left), Line(h, o), length=0.5)

        alpha_0 = PI / 4
        m = np.array([r / np.tan(alpha_0), r, 0])
        M_0 = Dot(m, color=ORANGE)
        M_0_ = Text('M', font_size=point_name_size).next_to(M_0, UP)
        OM_0 = Line(start=o, end=m, color=ORANGE)
        n = np.array([r * np.cos(alpha_0), r * np.sin(alpha_0), 0])
        N_0 = Dot(n, color=ORANGE)
        N_0_ = Text('N', font_size=point_name_size).next_to(N_0, RIGHT)
        ON_0 = Line(start=o, end=n, color=ORANGE)
        R_ON_0 = Text('r', font_size=point_name_size).next_to((o + n) / 2, LEFT)
        NM_0 = Line(start=n, end=m, color=PURE_RED)

        alpha = ValueTracker(PI / 4)
        m = [r / np.tan(alpha.get_value()), r, 0]
        M = always_redraw(lambda: Dot([r / np.tan(alpha.get_value()), r, 0], color=ORANGE))
        n = [r * np.cos(alpha.get_value()), r * np.sin(alpha.get_value()), 0]
        N = always_redraw(lambda: Dot([r * np.cos(alpha.get_value()), r * np.sin(alpha.get_value()), 0], color=ORANGE))
        ON = always_redraw(lambda: Line(start=o, end=[r * np.cos(alpha.get_value()), r * np.sin(alpha.get_value()), 0], color=ORANGE))

        R_ON = always_redraw(lambda: Text('r', font_size=point_name_size).
        next_to(Line(start=o, end=[r * np.cos(alpha.get_value()), r * np.sin(alpha.get_value()), 0]).get_midpoint(), LEFT))

        NM = always_redraw(lambda: Line(start=[r * np.cos(alpha.get_value()), r * np.sin(alpha.get_value()), 0], 
        end=[r / np.tan(alpha.get_value()), r, 0], color=PURE_RED))

        OMH = always_redraw(lambda: Angle(Line(start=[r / np.tan(alpha.get_value()), r, 0], end=o), 
        Line(start=[r / np.tan(alpha.get_value()), r, 0], end=tangent_left), radius=0.5, other_angle=True))


        self.wait(0.5)

        # self.add(O, O_, crc)
        # self.add(H, OH, O, R_OH)
        # self.add(tangent)
        # self.add(M_0, OM_0, O)
        # self.add(N_0)

        # # Animations
        # self.play(Create(O), Write(O_))
        # self.play(Create(crc))
        self.play(Create(tangent), Create(H))
        self.play(Create(OH))
        self.play(Write(H_))
        self.play(Write(R_OH))
        self.add(O)
        self.play(Create(OM_0))
        self.add(O)
        self.play(Create(M_0))
        self.play(Write(M_0_))
        self.wait(0.5)

        # Rotate OH to the ON
        self.play(Rotating(VGroup(OH, H).copy(), radians=-PI/4, about_point=o), Transform(R_OH.copy(), R_ON_0), run_time=1.5, rate_func=linear)
        self.add(O)
        self.play(Write(N_0_))

        # Create segment NM
        self.play(Create(NM_0))
        self.add(N_0, M_0)
        self.wait(1)

        # Rotate OM while keeping M on the tangent line
        self.add(ON, R_ON, N, M, NM, OMH)

        self.play(alpha.animate.set_value(PI / 2), run_time=2.6, rate_func=linear)
        self.remove(OMH)
        self.play(Create(right_angle))
        self.wait(1)

        self.add(OMH)
        self.play(alpha.animate.set_value(PI * 6 / 7), run_time=2.5, rate_func=linear)
        self.wait(1)

        self.play(alpha.animate.set_value(PI / 4), run_time=4, rate_func=linear)
        self.wait(1)

        # Rotate OM with it's full length
        self.play(Rotating(VGroup(ON_0, NM_0, N_0, M_0).copy(), radians=PI/4, about_point=o), Transform(R_ON_0.copy(), R_OH), run_time=1.5)
        self.add(O)

        self.wait(1)


class Angle_Right(Scene):
    def construct(self):
        
        h = np.array([0, r, 0])
        H = Dot(h, color=ORANGE)
        H_ = Text('H', font_size=point_name_size).next_to(h, UP).shift(0.25*LEFT)
        OH = Line(start=o, end=h, color=ORANGE)
        R_OH = R_.copy().next_to(OH, LEFT)
        tangent = TangentLine(crc, 1/4, color=ORANGE, length=12)
        tangent_left = [-6, r, 0]
        tangent_right = [6, r, 0]

        right_angle = RightAngle(Line(h, tangent_left), Line(h, o), length=0.5, color=ORANGE)

        alpha = ValueTracker(PI / 4)
        m = [r / np.tan(alpha.get_value()), r, 0]
        M = always_redraw(lambda: Dot([r / np.tan(alpha.get_value()), r, 0], color=ORANGE))
        n = [r * np.cos(alpha.get_value()), r * np.sin(alpha.get_value()), 0]
        N = always_redraw(lambda: Dot([r * np.cos(alpha.get_value()), r * np.sin(alpha.get_value()), 0], color=ORANGE))
        ON = always_redraw(lambda: Line(start=o, end=[r * np.cos(alpha.get_value()), r * np.sin(alpha.get_value()), 0], color=ORANGE))

        R_ON = always_redraw(lambda: Text('r', font_size=point_name_size).
        next_to(Line(start=o, end=[r * np.cos(alpha.get_value()), r * np.sin(alpha.get_value()), 0]).get_midpoint(), LEFT))

        NM = always_redraw(lambda: Line(start=[r * np.cos(alpha.get_value()), r * np.sin(alpha.get_value()), 0], 
        end=[r / np.tan(alpha.get_value()), r, 0], color=PURE_RED))

        OMH = always_redraw(lambda: Angle(Line(start=[r / np.tan(alpha.get_value()), r, 0], end=o), 
        Line(start=[r / np.tan(alpha.get_value()), r, 0], end=tangent_left), radius=0.5, other_angle=True))

        value_OMH = always_redraw(lambda: Integer(abs(Angle(Line(start=[r / np.tan(alpha.get_value()), r, 0], end=o), 
        Line(start=[r / np.tan(alpha.get_value()), r, 0], end=tangent_left), radius=0.5, other_angle=True).get_value(degrees=True)), 
        unit="^{\circ}", font_size=30).next_to(Angle(Line(start=[r / np.tan(alpha.get_value()), r, 0], end=o), 
        Line(start=[r / np.tan(alpha.get_value()), r, 0], end=tangent_left), radius=0.5, other_angle=True).get_midpoint(), DL*0.2))


        self.wait(0.5)

        self.add(O, O_, crc)
        self.add(H, OH, O, R_OH)
        self.add(tangent)

        # Rotate OM while keeping M on the tangent line
        self.add(ON, R_ON, N, M, NM, OMH, value_OMH)

        self.play(alpha.animate.set_value(PI / 2), run_time=2.6, rate_func=linear)
        self.wait(1)

        self.play(alpha.animate.set_value(PI * 6 / 7), run_time=2.5, rate_func=linear)
        self.wait(0.5)

        self.play(alpha.animate.set_value(PI / 2), run_time=4, rate_func=linear)
        self.remove(OMH)
        self.play(Create(right_angle))
        self.wait(0.5)

        self.add(OMH)
        self.play(alpha.animate.set_value(PI / 4), run_time=4, rate_func=linear)

        self.wait(1)


class Tangent(Scene):
    def construct(self):

        self.wait(0.5)
        MoveSegment.construct(self)
        IntersectionToTangent.construct(self)
        RotateTangent.construct(self)
        ShortestWay.construct(self)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)


class test(Scene):
    def construct(self):
        
        tangent = TangentLine(crc, alpha=0.8, length=10)

        self.add(crc, tangent)

