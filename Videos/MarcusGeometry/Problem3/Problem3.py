from manim import *

class Problem3(Scene):
    def construct(self):

    # Draw a ORANGE line in the bottom of the screen and choose point A, B and C.
        point1 = Dot().move_to(2*DOWN+4*LEFT)
        point2 = Dot().move_to(2*DOWN+4*RIGHT)

        line = Line(point1,point2, color=ORANGE)

        pointA = Dot(point=2*DOWN+3*LEFT, color=ORANGE)
        labelA = Text("A", color=ORANGE, font_size=30).next_to(pointA, DOWN)
        A = VGroup(pointA,labelA)

        pointB = Dot(point=2*DOWN+LEFT, color=ORANGE)
        labelB = Text("B", color=ORANGE, font_size=30).next_to(pointB, DOWN)
        B = VGroup(pointB,labelB)

        pointC = Dot(point=2*DOWN+2*RIGHT, color=ORANGE)
        labelC = Text("C", color=ORANGE, font_size=30).next_to(pointC, DOWN)
        C = VGroup(pointC,labelC)

        self.play(
            Create(line, run_time=3.0)
        )
        self.wait()

        for i in [A,B,C]:
            self.play(
                Write(i)
            )
            self.wait()

    # Draw a random green circle and move it randomly until it touches point A.
        pointO = Dot(radius=0.0)

        r = ValueTracker(1.0)
        circle = always_redraw(lambda : 
            Circle(radius=r.get_value(), arc_center=pointO.get_center(), color=GREEN)
        )

        self.play(Create(circle, run_time=3.0))
        self.wait(1)
        
        self.play(
            pointO.animate(run_time=3.0).shift(DOWN+3*LEFT)
        )
        self.wait()

    # Rotate it (around point A) until touches the point B. 
        self.play(
            Rotating(pointO, radians=3*PI/2, about_point=pointA.get_center())
        )
        self.wait(0.5)

    # Increase the radius of the circle such that it touches A and B.
        lineAB = Line(pointA.get_center(),pointB.get_center())

        M = Dot(lineAB.get_midpoint())
        N = M.copy().shift(2*UP)

        linel1 = Line(M.get_center(),N.get_center(), color=BLUE)

        r.add_updater(lambda x:
            x.set_value(np.linalg.norm(pointO.get_center()-pointB.get_center()))
        )

        self.play(
            r.animate(run_time=6.0).set_value(np.linalg.norm(pointB.get_center()-pointO.get_center())),
            MoveAlongPath(pointO,linel1, run_time=6.0)
        )
        self.wait()

    # Decrease the radius of the circle such that it touches A and B.
        linel1_2 = Line(N.get_center(),M.get_center())

        self.play(
            r.animate(run_time=6.0).set_value(np.linalg.norm(pointB.get_center()-pointO.get_center())),
            MoveAlongPath(pointO,linel1_2, run_time=6.0)
        )
        self.wait()

    # Draw the blue bisector perpendicular of AB. 
        linel3 = linel1.copy().scale(2.0)

        self.play(
            Create(linel3, run_time=3.0)
        )
        self.wait()

    # Denote it by l_1.
        labell1 = MathTex(r"l_{1}", color=BLUE, font_size=30).next_to(linel3.get_end(),LEFT)

        self.play(
            Write(labell1)
        )
        self.wait()

    # Mention center of the circle O.
        O1 = always_redraw(lambda :
            Dot().move_to(pointO)
        )
        self.play(
            Create(O1)
        )
        self.wait(0.5)

    # Increase the radius of the circle such that it touches A and B. (O is on the bisector perpendicular)
        self.play(
            r.animate(run_time=6.0).set_value(np.linalg.norm(pointB.get_center()-pointO.get_center())),
            MoveAlongPath(pointO,linel1, run_time=6.0)
        )
        self.wait(0.5)

    # Decrease the radius of the circle such that it touches A and B. (O is on the bisector perpendicular)
        self.play(
            r.animate(run_time=6.0).set_value(np.linalg.norm(pointB.get_center()-pointO.get_center())),
            MoveAlongPath(pointO,linel1_2, run_time=6.0)
        )
        self.wait(0.5)

    # Change position of the circle such that it touces points B and C.
        self.remove(O1)
        self.wait(1)

        self.play(
            Rotating(pointO, radians=PI, about_point=pointB.get_center())
        )
        self.wait(0.5)

        self.play(
            r.animate(run_time=3.0).set_value(1.5),
            pointO.animate(run_time=3.0).shift(0.5*RIGHT)
        )
        self.wait(1)

    # Increase the radius of the circle such that it touches C and B.
        lineBC = Line(pointB.get_center(),pointC.get_center())

        P = Dot(lineBC.get_midpoint())
        Q = P.copy().shift(1.5*UP)

        linel2 = Line(P.get_center(),Q.get_center(), color=BLUE)

        self.play(
            r.animate(run_time=6.0).set_value(np.linalg.norm(pointB.get_center()-pointO.get_center())),
            MoveAlongPath(pointO,linel2, run_time=6.0)
        )
        self.wait(1)

    # Decrease the radius of the circle such that it touches C and B.
        linel2_2 = Line(Q.get_center(),P.get_center())

        self.play(
            r.animate(run_time=6.0).set_value(np.linalg.norm(pointB.get_center()-pointO.get_center())),
            MoveAlongPath(pointO,linel2_2, run_time=6.0)
        )
        self.wait()

    # Draw the blue bisector perpendicular of BC.
        linel4 = linel3.copy().shift(2.5*RIGHT)

        self.play(
            Create(linel4, run_time=3.0)
        )
        self.wait(1)

    # Denote it by l_2.
        labell2 = MathTex(r"l_{2}", color=BLUE, font_size=30).next_to(linel4.get_end(),RIGHT)

        self.play(
            Write(labell2)
        )
        self.wait(1)

    # Mention center of the circle O.
        self.play(
            Create(O1)
        )
        self.wait(1)

    # Increase the radius of the circle such that it touches C and B. (O is on the bisector perpendicular)
        self.play(
            r.animate(run_time=6.0).set_value(np.linalg.norm(pointB.get_center()-pointO.get_center())),
            MoveAlongPath(pointO,linel2, run_time=6.0)
        )
        self.wait()

    # Decrease the radius of the circle such that it touches C and B. (O is on the bisector perpendicular)
        self.play(
            r.animate(run_time=6.0).set_value(np.linalg.norm(pointB.get_center()-pointO.get_center())),
            MoveAlongPath(pointO,linel2_2, run_time=6.0)
        )
        self.wait(1)

    # Draw 90 degree angle between l_1 and the original line.
        angle1 = RightAngle(lineAB,linel1, length=0.25)

        self.play(Create(angle1))
        self.wait(1)

    # Draw 90 degree angle between l_2 and the original line.
        angle2 = RightAngle(lineAB,linel2, length=0.25)

        self.play(Create(angle2))
        self.wait(1)

    # Write 90 + 90 = 180 => l_1 || l_2.
        text = MathTex(r"90^{\circ}+90^{\circ}=180^{\circ}\Rightarrow l_{1}\parallel l_{2}", font_size=30).move_to(2*UP)

        self.play(Write(text))
        self.wait()
