from manim import *

import sys
sys.path.append("../../")       # relative path to the root of the repository
from Functions.GeometryFunctions.GeometryFunctions import *    # or import specific function

fs = 40    # label font_size

class Problem1(Scene):
    def construct(self):
    #Draw segment orange segment AB and a point O, such that OA < OB. 
        pointA = Dot(point=2*LEFT, color=ORANGE)
        labelA = LabelPoint(pointA, 'A', font_size=fs)
        A = VGroup(pointA,labelA)

        pointB = Dot(point=2*RIGHT, color=ORANGE)
        labelB = LabelPoint(pointB, 'B', 0.5*DR, font_size=fs)
        B = VGroup(pointB,labelB)

        lineAB = Line(pointA, pointB, color=ORANGE)

        pointO = Dot(point=1.5*UP+LEFT, color=ORANGE)
        labelO = always_redraw(lambda: LabelPoint(pointO, 'O', UL*0.5, font_size=fs))
        O = VGroup(pointO,labelO)

        VGroup(A,B,O,lineAB).shift(DOWN)

        self.play(Write(A))
        self.play(Write(B))

        self.play(Write(lineAB))
        self.wait(0.5)

        self.play(Write(O))
        self.wait(0.5)

    #Draw a small circle with center O and radius smaller than OA.
        rOA = always_redraw(lambda: Line(pointA.get_center(), pointO.get_center()))
        rOB = always_redraw(lambda: Line(pointB.get_center(), pointO.get_center()))
        r = ValueTracker(1.0)

        circle = always_redraw(lambda : 
            Circle(radius=r.get_value(), arc_center=pointO.get_center(), color=WHITE)
        )

        self.play(Create(circle))
        self.wait(1)

    #Start to increase the radius of the circle, until in touches the point A.
        self.play(
            r.animate(run_time=3.0).set_value(np.linalg.norm(pointO.get_center()-pointA.get_center()))
        )
        self.wait(1)

    #At that moment blink the circle and the point A.
        self.play(FadeIn(circle))
        self.wait(1)

    #Then continue to increase the radius until it touches the point B.
        self.play(
            r.animate(run_time=3.0).set_value(np.linalg.norm(pointO.get_center()-pointB.get_center()))
        )
        self.wait(1)

    #At that moment blink the circle and the point B.
        self.play(FadeIn(circle))
        self.wait(1)

    #Stop changing the radius. 
    #Now move O, such that it touches B, O moves parallel to AB, closer to the bisector perpendicular of AB.
        r.add_updater(lambda x:
            x.set_value(np.linalg.norm(pointO.get_center()-pointB.get_center()))
        )

        self.play(
            pointO.animate(run_time=3.0).shift(0.75*RIGHT),
        )
        self.wait(1)

    #Continue it until the circle touches tbe point A as well. Stop animation.
        self.play(
            pointO.animate(run_time=3.0).shift(0.25*RIGHT),
        )
        self.wait(1)

    #Draw radiuses OA and OB, put sign of equal segments on them. 

        rOA = always_redraw(lambda: Line(pointA.get_center(), pointO.get_center()))
        rOB = always_redraw(lambda: Line(pointB.get_center(), pointO.get_center()))

        equality_sign_OA = always_redraw(lambda: SegmentEqualitySign1(rOA, color=ORANGE))
        equality_sign_OB = always_redraw(lambda: SegmentEqualitySign1(rOB, color=ORANGE))

        self.play(
            Create(rOA, run_time=2.0),
            Create(rOB, run_time=2.0)
        )
        self.wait(1)

        self.play(
            Create(equality_sign_OA),
            Create(equality_sign_OB)
        )
        self.wait(1)

    #Draw the midpoint of AB as M.
        pointM = Dot(lineAB.get_midpoint(), color=WHITE)
        labelM = LabelPoint(pointM, 'M', 0.5*DR, font_size=fs)
        M = VGroup(pointM,labelM)

        self.play(Write(M))
        self.wait(1)

    #Draw the bisector perpendicular of AB, it must pass through point O.
        perpend = Line(pointM,pointO, color=ORANGE).scale(4)

        self.play(Write(perpend))
        self.wait(1)

    #Highlight triangles AOM and BOM in different colors.
        triAOM = Polygon(pointA.get_center(),pointO.get_center(),pointM.get_center(), color=BLUE)
        triBOM = Polygon(pointB.get_center(),pointO.get_center(),pointM.get_center(), color=GREEN)

        self.play(Create(triAOM, run_time=2.0))
        self.wait(0.5)

        self.play(Create(triBOM, run_time=2.0))
        self.wait(1)

    #Remove highlights.
        self.play(
            Uncreate(triAOM),
            Uncreate(triBOM)
        )
        self.wait(1)

     #Now move point O over the bisector perpendicular, such that the circle changes it's radius and passes throught points A and B.
        lineOM = Line(pointO.get_center(),perpend.get_start()+1.5*UP)

        self.play(MoveAlongPath(pointO,lineOM, run_time=3.0))
        self.wait(1)

        lineMO = Line(perpend.get_start()+1.5*UP,perpend.get_end()+1.5*DOWN)

        self.play(MoveAlongPath(pointO,lineMO, run_time=3.0))
        self.wait(1)
