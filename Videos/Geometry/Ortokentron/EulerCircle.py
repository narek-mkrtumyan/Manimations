import sys
sys.path.append('../../../')
from Functions.QarakusiFunctions import *

class EulerCircle(Scene):
    def construct(self):
        all_dots = VGroup()

        A = Dot([-2.25, -2.5, 0]).set_stroke(BLACK, 2)
        B = Dot([0, 2, 0]).set_stroke(BLACK, 2)
        C = Dot([4.5, -2.5, 0]).set_stroke(BLACK, 2)

        VGroup(A, B, C).shift(UP * 1.2)

        label_A = always_redraw(lambda: LabelPoint(A, 'A'))
        label_B = always_redraw(lambda: LabelPoint(B, 'B', position=UP))
        label_C = always_redraw(lambda: LabelPoint(C, 'C', position=DR))

        all_dots.add(A, B, C)

        AB = always_redraw(lambda: Line(A.get_center(), B.get_center()))
        AC = always_redraw(lambda: Line(A.get_center(), C.get_center()))
        BC = always_redraw(lambda: Line(B.get_center(), C.get_center()))

        M_A = always_redraw(lambda: Dot(BC.get_center(), color=GREEN).set_stroke(BLACK, 2))
        M_B = always_redraw(lambda: Dot(AC.get_center(), color=GREEN).set_stroke(BLACK, 2))
        M_C = always_redraw(lambda: Dot(AB.get_center(), color=GREEN).set_stroke(BLACK, 2))

        all_dots.add(M_A, M_B, M_C)

        label_M_A = always_redraw(lambda: LabelPoint(M_A, 'M_A', position=UR))
        label_M_B = always_redraw(lambda: LabelPoint(M_B, 'M_B', position=DOWN))
        label_M_C = always_redraw(lambda: LabelPoint(M_C, 'M_C', position=UL))

        H_A = always_redraw(lambda: Dot(BC.get_projection(A.get_center()), color=BLUE).set_stroke(BLACK, 2))
        H_B = always_redraw(lambda: Dot(AC.get_projection(B.get_center()), color=BLUE).set_stroke(BLACK, 2))
        H_C = always_redraw(lambda: Dot(AB.get_projection(C.get_center()), color=BLUE).set_stroke(BLACK, 2))
        all_dots.add(H_A, H_B, H_C)

        AH_A = always_redraw(lambda: Line(A.get_center(), H_A.get_center(), color=BLUE))
        BH_B = always_redraw(lambda: Line(B.get_center(), H_B.get_center(), color=BLUE))
        CH_C = always_redraw(lambda: Line(C.get_center(), H_C.get_center(), color=BLUE))

        H = always_redraw(lambda: 
                Dot(line_intersection(AH_A.get_start_and_end(), BH_B.get_start_and_end()), color=BLUE)
            )
        H.add_updater(lambda f: H.become(H.set_stroke(BLACK, 2)))
        label_H = always_redraw(lambda: LabelPoint(H, 'H', RIGHT))
        all_dots.add(H)

        label_H_A = always_redraw(lambda: LabelPoint(H_A, 'H_A', position=UR))
        label_H_B = always_redraw(lambda: LabelPoint(H_B, 'H_B', position=DOWN))
        label_H_C = always_redraw(lambda: LabelPoint(H_C, 'H_C', position=UL))

        O = always_redraw(lambda: 
                Dot(
                    line_intersection(
                        perpendicular_bisector(AC.get_start_and_end()), 
                        perpendicular_bisector(BC.get_start_and_end())
                    )
                ).set_stroke(BLACK, 2)
            )
        label_O = always_redraw(lambda: LabelPoint(O, 'O', DL*0.5))
        all_dots.add(O)
        
        circumscribed_circle_ABC = always_redraw(lambda: Circle(DistanceBetweenPoints(O, A), color=WHITE).move_to(O.get_center()))

        euler_line = always_redraw(lambda: Line(H.get_center(), O.get_center(), color=ORANGE))

        G = always_redraw(lambda: Dot(euler_line.get_center(), color=ORANGE).set_stroke(BLACK, 2))
        label_G = always_redraw(lambda: LabelPoint(G, 'G'))
        all_dots.add(G)

        euler_circle = always_redraw(lambda: Circle(radius=DistanceBetweenPoints(G, H_B), color=ORANGE).move_to(G.get_center()))

        # all_dots.set_stroke(BLACK, 2)




        self.add(A, B, C, label_A, label_B, label_C)
        self.add(AB, AC, BC)
        self.add(M_A, M_B, M_C, label_M_A, label_M_B, label_M_C)
        self.add(H_A, H_B, H_C, label_H_A, label_H_B, label_H_B, label_H_C)
        self.add(AH_A, BH_B, CH_C)
        self.add(H, label_H)

        self.add(O, G, H, euler_line, label_G, label_H, label_O, euler_circle)

        self.add(circumscribed_circle_ABC)

        self.add(all_dots)

        self.wait()
        self.play(B.animate.shift(2 * RIGHT), run_time=2)
        self.wait()
        # self.play(B.animate.shift(2 * RIGHT), run_time=3)
        # self.wait(5)
