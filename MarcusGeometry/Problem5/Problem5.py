from manim import *

import sys
sys.path.append("../../")       # relative path to the root of the repository
from Functions.GeometryFunctions.GeometryFunctions import *

class Problem5(Scene):
    def construct(self):

    # Draw a points A and B (WHITE) and a circle with the center O, such that the radius is bigger than AB/2.
        r1 = ValueTracker(0.08)
        r2 = ValueTracker(0.08)
        pointA = always_redraw(lambda:
           Dot(radius=r1.get_value(), color=WHITE).shift(LEFT)
        )
        labelA = Text("A", color=WHITE, font_size=30).next_to(pointA, DOWN, buff=SMALL_BUFF)
        A = VGroup(pointA,labelA)

        pointB = always_redraw(lambda:
           Dot(radius=r2.get_value(), color=WHITE).shift(RIGHT)
        )
        labelB = Text("B", color=WHITE, font_size=30).next_to(pointB, DOWN, buff=SMALL_BUFF)
        B = VGroup(pointB,labelB)

        template_radius = Line([-6, 2.5, 0], [-4.5, 2.5, 0], color=ORANGE)
        template_radius_equality_sign = SegmentEqualitySign1(template_radius)
        radius_R = MathTex(r'R', font_size=30).next_to(template_radius, UP)

        pointO = Dot([-3, 1, 0], color=GREEN)
        labelO = Text("O", font_size=30)
        labelO.add_updater(lambda x:
            x.next_to(pointO, RIGHT, buff=SMALL_BUFF)
        )
        O = VGroup(pointO,labelO)

        circle1 = always_redraw(lambda : 
            Circle(radius=1.5, arc_center=pointO.get_center(), color=GREEN)
        )

        self.play(
            Create(template_radius),
            Create(radius_R)
        )

        self.play(
            Write(A),
            Write(B)
        )
        self.wait()
        self.play(
            Write(O)
        )
        self.wait()

        temp_radius_copy = template_radius.copy()
        self.play(temp_radius_copy.animate.next_to(pointO.get_center(), LEFT, buff=0))
        self.remove(temp_radius_copy)

        temp_circle, temp_O = CircleFromSpinningRadius(self, radius=1.5, center=pointO.get_center(), starting_point_angle=180, 
            circle_color=GREEN, radius_color=ORANGE, center_color=GREEN, create_center=False, create_radius=False)
        self.remove(temp_circle, temp_O)
        self.add(circle1)
        self.wait(1)

    # Move randomly the circle, until it meets the point A.
        self.play(
            pointO.animate(run_time=1.0, rate_func=linear).shift(0.5 * UP)
        )
        self.play(
            pointO.animate(run_time=1.5, rate_func=linear).shift(UP + RIGHT)
        )
        self.play(
            pointO.animate(run_time=2.0, rate_func=linear).shift(RIGHT + DOWN)
        )
        # self.play(                       # does the same in one motion
        #     pointO.animate(run_time=2.0, rate_func=linear).shift(2 * RIGHT + 0.5 * UP)
        # )
        self.wait(1)
    
    # When they meet, point A and the circle become thicker, then return back to normal size.
        self.play(
            r1.animate(rate_func=there_and_back, run_time=3.0).set_value(0.16),
            circle1.animate(run_time=3.0, rate_func=there_and_back).set_stroke_width(8)
        )
        self.wait(1)

    # Rotate the circle around the point A, such that meets the point B.
        self.play(
            Rotating(pointO, radians=-42*DEGREES, about_point=pointA.get_center(), run_time=3.0)
        )
        self.wait(1)

    # At that moment the point B and the circle become thicker, then return back to normal size. (CIRCLE 1).
        self.play(
            r2.animate(rate_func=there_and_back, run_time=3.0).set_value(0.16),
            circle1.animate(run_time=3.0, rate_func=there_and_back).set_stroke_width(8)
        )
        self.wait(1)

    # Draw segments OA and OB (ORANGE). 
        OA = always_redraw(lambda : 
           Line(pointA.get_center(),pointO.get_center(), color=ORANGE)
        )
        OB = always_redraw(lambda : 
           Line(pointB.get_center(),pointO.get_center(), color=ORANGE)
        )

        self.play(
            Create(OA, run_time=2.0),
            Create(OB, run_time=2.0)
        )
        self.wait(1)

    # Add sign of equal sizes on OA and OB.
        equality_sign_OA = always_redraw(lambda : 
            SegmentEqualitySign1(OA, color=ORANGE, sign_size=SegmentLength(OA) / 7.5)
        )
        equality_sign_OB = always_redraw(lambda : 
            SegmentEqualitySign1(OB, color=ORANGE, sign_size=SegmentLength(OB) / 7.5)
        )

        self.play(
            Create(equality_sign_OA),
            Create(equality_sign_OB)
        )
        self.wait(1)

    # Remove the circle, such that it remains isosceles triangle AOB.
        AB = Line(pointA.get_center(),pointB.get_center(), color=ORANGE)

        self.play(
            Create(AB, run_time=3.0)
        )
        self.wait(1)
        self.play(
            Uncreate(circle1)
        )
        self.wait(1)

    # Take the midpoint M of the segment AB and draw the line MO (thick green line).
        pointM = Dot().move_to(Line(pointA.get_center(),pointB.get_center()).get_midpoint())
        labelM = Text("M", font_size=30).next_to(pointM, DL, buff=SMALL_BUFF)
        M = VGroup(pointM,labelM)
        MO = Line(pointM.get_center(),pointO.get_center(), color=GREEN, stroke_width=2.5).scale(5.0)

        self.play(
            Write(M),
            Create(MO, run_time=3.0)
        )
        self.wait()

    # Add signs of equal segments for AM and BM
        equality_sign_AM = SegmentEqualitySign2(Line(pointA, pointM))
        equality_sign_BM = SegmentEqualitySign2(Line(pointB, pointM))

        self.play(
            Create(equality_sign_BM),
            Create(equality_sign_AM)
        )
        
    # Add the sign of 90 degree to the angles AMO and BMO.
        angle1 = RightAngle(MO,Line(pointM.get_center(),pointA.get_center()), length=0.2)
        angle2 = RightAngle(MO,Line(pointM.get_center(),pointB.get_center()), length=0.3)

        self.play(
            Create(angle1, run_time=2.0),
            Create(angle2, run_time=2.0)
        )
        self.wait(1)

    # Increase the radius of the circle, such that it passes points A and B, but O changes but keeps on green line.
        self.play(
            pointO.animate(run_time=3.0).shift(2*UP)
        )
        self.wait(2)

    # Stop a moment and start to decrease the radius, until M coincides with O.
        self.play(
            pointO.animate(run_time=3.0).move_to(pointM.get_center())
        )

        self.remove(equality_sign_OA, equality_sign_OB) # AM and AO are the same here
        self.wait(2)

    # Continue to move O, until the radius becomes the original one (but in another side of the line AB). (CIRCLE 2).
        self.add(equality_sign_OA, equality_sign_OB)
        self.play(
            pointO.animate(run_time=3.0).shift(1.11*DOWN)
        )
        self.wait(2)

        circle2 = Circle(radius=1.5, arc_center=pointO.get_center(), color=WHITE)

        self.play(
            Create(circle2)
        )
        self.wait()

    # Remove segments OA, OB, line AB and point O (it remain only points A, B and CIRCLE 2).
        self.play(
            Uncreate(OA),
            Uncreate(OB),
            Uncreate(AB),
            Uncreate(equality_sign_OA),
            Uncreate(equality_sign_OB),
            Uncreate(MO),
            Uncreate(M),
            Uncreate(angle1),
            Uncreate(angle2), 
            Uncreate(equality_sign_BM),
            Uncreate(equality_sign_AM)
        )
        self.remove(O)
        self.wait(1)

    # Add the original circle, that satisfied the condition (CIRCLE 1)
        circle3 = Circle(radius=1.5, color=WHITE).shift(1.11*UP)

        self.play(
            Create(circle3, run_time=3.0)
        )
        self.wait(1)

    # Draw OA and OB (ORANGE).
        OA1 = OA.copy().flip().shift(1.11*UP)
        OB1 = OB.copy().flip().shift(1.11*UP)

        self.play(
            Create(OA),
            Create(OA1),
            Create(OB),
            Create(OB1)
        )
        self.wait(1)

    # Draw a sign of equal sizes on radiuses of CIRCLE1 and CIRCLE 2 that connect to A and B.
        line3a = always_redraw(lambda : 
            SegmentEqualitySign1(OA1, color=ORANGE)
        )
        line4a = always_redraw(lambda : 
            SegmentEqualitySign1(OB1, color=ORANGE)
        )

        self.play(
            Create(equality_sign_OA),
            Create(equality_sign_OB),
            Create(line3a),
            Create(line4a)
        )
        self.wait(1)

    # Draw a circle with center A and radius OA (blue).
    # Draw a circle with center B and radius OB (blue).
        circleA = Circle(radius=1.5, arc_center=pointA.get_center(), color=BLUE)
        circleB = Circle(radius=1.5, arc_center=pointB.get_center(), color=BLUE)

        circleA, p = CircleFromSpinningRadius(self, radius=1.5, center=pointA.get_center(), 
                starting_point_angle=48.19, circle_color=BLUE, radius_color=ORANGE, 
                equality_sign=1, equality_sign_color=ORANGE, direction=-1, create_radius=False, center_color=BLUE)
        self.remove(p)
        self.wait(1)
        circleB, p = CircleFromSpinningRadius(self, radius=1.5, center=pointB.get_center(), 
                starting_point_angle=180-48.19, circle_color=BLUE, radius_color=ORANGE, 
                equality_sign=1, equality_sign_color=ORANGE, create_radius=False, center_color=BLUE)
        self.remove(p)

    # Delete CIRCLE 1 and CIRCLE 2.
        circle2a = circle2.copy()
        circle3a = circle3.copy()

        self.play(
            Uncreate(circle2),
            Uncreate(circle3)
        )
        self.wait()

    # Make intersection points of blue circles (O and another one) thinner and return to normal size.
        P = Dot(color=BLUE).move_to(pointO.get_center())

        Q = P.copy().shift(2.22*UP)

        self.play(
            Write(P),
            Write(Q)
        )
        self.wait(1)

    # Delete blue circles.
        self.play(
            Uncreate(circleA),
            Uncreate(circleB)
        )
        self.wait(1)

    # Draw CIRCLE 1
    # Draw CIRCLE 2.
        self.play(
            Create(circle2a, run_time=3.0),
            Create(circle3a, run_time=3.0)
        )
        self.wait(1)

    # Delete everything but points A and B.
        self.play(
            Uncreate(circle2a),
            Uncreate(circle3a),
            Uncreate(OA),
            Uncreate(OA1),
            Uncreate(OB),
            Uncreate(OB1),
            Uncreate(equality_sign_OB),
            Uncreate(line3a),
            Uncreate(equality_sign_OA),
            Uncreate(line4a),
            Uncreate(P),
            Uncreate(Q)
        )
        self.wait(1)

    # Draw a circle with radius < AB/2 with the center where the original point O was.
        circleO = Circle(radius=0.5, arc_center=pointO.get_center(), color=GREEN)

        circleO, p = CircleFromSpinningRadius(self, radius=0.5, center=pointO.get_center(),
            radius_color=GREEN, center_color=GREEN, circle_color=GREEN, r_sign=MathTex(r'r', font_size=25))
        
        self.remove(p)
        self.wait()

    # Write r < AB/2
        self.play(Write(MathTex(r'r < \frac{AB}{2}', font_size=40).to_edge(DOWN).shift(0.5*UP)))

    # Move the circle, until it meets point A.
        self.play(
            circleO.animate(run_time=3.0).move_to(Line(pointA.get_center(),pointM.get_center()).get_midpoint())
        )
        self.wait(1)

    # Rotate around A 360 degree with success to touch point B.
        self.play(
            Rotating(circleO, radians=2*PI, about_point=pointA.get_center(), run_time=3.0)
        )
        self.wait(1)

    # Move circle to the middle of segment AB.
        self.play(
            circleO.animate(run_time=3.0).move_to(ORIGIN)
        )
        self.wait(1)

    # Move it up, then move it down.
        self.play(
            circleO.animate(run_time=3.0, rate_func=there_and_back).shift(2*UP)
        )
        self.wait()
        