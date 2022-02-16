from os import wait
from manim import *
import numpy as np

import sys
sys.path.append("../../")       # relative path to the root of the repository
from Functions.GeometryFunctions.GeometryFunctions import *

class Problem5(Scene):
    def construct(self):

    # Draw a points A and B (WHITE) and a circle with the center O, such that the 
    # radius is bigger than AB/2.
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

        temp_circle, temp_O = CircleFromSpinningRadius(self, radius=1.5, center=pointO.get_center(),
            starting_point_angle=180, circle_color=GREEN, radius_color=ORANGE, center_color=GREEN, 
            create_center=False, create_radius=False)
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
        self.wait(1)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects])




class Կառուցում(Scene):
    def construct(self):

# Inits for small circle
    # A, B, template small radius on top left corner
        a = np.array([-1, -1, 0])
        b = np.array([1, -1, 0])
        A = Dot(a)
        B = Dot(b)
        label_A = LabelPoint(A, 'A', DOWN*0.75)
        label_B = LabelPoint(B, 'B', DOWN*0.75)
        AB = Line(a, b)

        small_radius_value = 0.6
        small_template_radius = Line([-6, 2.5, 0], [-6 + small_radius_value, 2.5, 0], 
                                color=ORANGE)
        label_radius = MathTex(r'R', font_size=30).next_to(small_template_radius, 2.5*UP)

        copy_small_template_radius = small_template_radius.copy()

    # O, small circle
        O = Dot([-3, 1, 0], color=GREEN)

        small_circle = always_redraw(lambda:
                Circle(radius=small_radius_value, color=GREEN).move_to(O.get_center())
            )
        small_radius = Line(a, a - np.array([small_radius_value, 0, 0]), color=ORANGE)
        small_diameter = Line(a, a + np.array([2*small_radius_value, 0, 0]), 
                            color=ORANGE, stroke_width=DEFAULT_STROKE_WIDTH*2
                        )
    
    # Blue circle that passes through A and B
        blue_center = Dot([0, 0, 0], color=BLUE)
        blue_circle = Circle(radius=np.sqrt(2), color=BLUE).move_to(blue_center.get_center())

    # R < AB/2 => impossible
        R_smaller_AB_half_impossible = MathTex(
            r'R\ <\ \frac{AB}{2} \textrm{դեպքում կառուցել հնարավոր չէ}',
            tex_template=armenian_tex_template, font_size=30)
        R_smaller_AB_half_impossible.move_to([0, 3.25, 0])

        red_rect = SurroundingRectangle(R_smaller_AB_half_impossible, color=RED)

# Animations for small circle (0,39)
    # Create R, A, B
        self.wait(0.5)
        self.play(Create(small_template_radius), Create(label_radius))
        self.wait(0.5)
        self.play(Create(A), Create(label_A), Create(B), Create(label_B))
        self.wait(0.5)

    # Create O, small circle
        self.play(Create(O))
        self.wait(0.5)

        self.play(
            copy_small_template_radius.animate(rate_func=linear)
            .next_to(O.get_center(), LEFT, buff=0)
            )
        self.remove(copy_small_template_radius)
        temporary_circle, temporary_o = CircleFromSpinningRadius(self, 
                radius=small_radius_value, center=O.get_center(), starting_point_angle=180, 
                circle_color=GREEN, radius_color=ORANGE, center_color=GREEN, 
                create_center=False, create_radius=False, run_time=2
                )
        self.remove(temporary_circle, temporary_o)
        self.add(small_circle)
        self.wait(0.5)

    # Move small circle to A
        self.play(
            O.animate(rate_func=linear, run_time=2.5)
            .move_to(a - np.array([small_radius_value, 0, 0]))
        )
        self.wait(0.5)

    # Show that it has the R radius, passes through A and doesn't pass through B
        self.play(FadeIn(small_radius))
        self.wait(0.2)
        self.play(FadeOut(small_radius))
        self.wait(0.2)
        self.play(A.animate(rate_func=there_and_back, run_time=2).scale(2))
        self.wait(0.2)
        self.play(B.animate(rate_func=there_and_back, run_time=2).scale(2))
        self.wait(1)

    # Rotate the small circle around A
        self.play(
            Rotating(O, radians=-PI*4/3, about_point=a, run_time=4.0)
        )
        self.wait(0.5)
        self.play(
            Rotating(O, radians=PI/3, about_point=a, run_time=1.5)
        )
        self.wait(2)

    # Add some circle that passes through A and B
    # Show and write that if diameter is smaller than AB, it's impossible
        self.play(FadeIn(blue_center), FadeIn(blue_circle))
        self.wait(0.5)

        self.play(Create(AB))
        self.wait(1)

        self.play(Create(small_diameter))
        self.wait(1)

        self.play(FadeOut(blue_center), FadeOut(blue_circle))
        self.wait(0.5)

        self.play(Write(R_smaller_AB_half_impossible, run_time=4))
        self.wait(0.2)

        self.play(Create(red_rect))
        self.wait(0.5)

    # Remove small circle O and AB
        self.remove(small_diameter, O, small_circle, AB)
        self.wait(1)


# Inits for big circle
    # Big radius, new O, big circle
        big_radius_value = 1.5
        big_template_radius = Line([-6, 2.5, 0], [-6 + big_radius_value, 2.5, 0], 
                                color=ORANGE)
        equality_sign_radius = SegmentEqualitySign1(big_template_radius)
        copy_big_template_radius = big_template_radius.copy()

        O = Dot([-3, 1, 0], color=GREEN)
    
    # R > AB/2
        R_bigger_AB_half = MathTex(r'\ >\ \frac{AB}{2}', font_size=30)
        R_bigger_AB_half.next_to(label_radius)

        green_rect = SurroundingRectangle(VGroup(label_radius, R_bigger_AB_half))
   
    # Big circle
        big_circle = always_redraw(lambda:
                Circle(radius=big_radius_value, color=GREEN).move_to(O.get_center())
            )

# Animations for big circle (39,54)
    # Draw big radius
        self.play(Create(big_template_radius))
        self.play(Write(R_bigger_AB_half))
        self.remove(small_template_radius)
        self.wait(1)

    # Draw big circle
        self.play(Create(O))
        self.wait(0.5)

        self.play(
            copy_big_template_radius.animate(rate_func=linear)
            .next_to(O.get_center(), LEFT, buff=0)
            )
        self.remove(copy_big_template_radius)
        temporary_circle, temporary_o = CircleFromSpinningRadius(self, 
                radius=big_radius_value, center=O.get_center(), starting_point_angle=180, 
                circle_color=GREEN, radius_color=ORANGE, center_color=GREEN, 
                create_center=False, create_radius=False, run_time=2
                )
        self.remove(temporary_circle, temporary_o)
        self.add(big_circle)
        self.wait(0.5)

    # Move big circle to A
        self.play(
            O.animate(rate_func=linear, run_time=2.5)
            .move_to(a - np.array([big_radius_value, 0, 0]))
        )
        self.wait(0.2)
        self.play(A.animate(rate_func=there_and_back, run_time=1.5))
        self.wait(0.5)

    # Rotate big circle until it passes through B
        self.play(
            Rotating(O, radians=np.arccos(2/3)-PI, about_point=a, run_time=4.0)
        )
        self.wait(0.2)
        self.play(B.animate(rate_func=there_and_back, run_time=1.5))
        self.wait(2)


# Inits for big circle, triangles AMO, BMO
    # Label big O
        label_O = LabelPoint(O, 'O', UL*0.5, color=WHITE)
    
    # OA, OB, and equality sign
        OA = always_redraw(lambda: Line(O.get_center(), a, color=ORANGE))
        OB = always_redraw(lambda: Line(O.get_center(), b, color=ORANGE))

        equality_signs_OA_OB = VGroup(
                SegmentEqualitySign1(OA),
                SegmentEqualitySign1(OB)
            )
    
    # M, OM, AM, MB, equality_sign_AM_MB fill_AMO fill_BMO
        M = Dot(AB.get_midpoint())
        label_M = LabelPoint(M, 'M')

        OM = Line(O.get_center(), M.get_center(), color=GREEN)
        AM = Line(A.get_center(), M.get_center())
        MB = Line(M.get_center(), B.get_center())

        equality_signs_AM_MB = VGroup(
                SegmentEqualitySign2(AM),
                SegmentEqualitySign2(MB)
            )

        fill_AMO = Polygon(A.get_center(), M.get_center(), O.get_center())
        fill_AMO.set_stroke(width=0).set_fill(BLUE, 0.5)

        fill_BMO = Polygon(B.get_center(), M.get_center(), O.get_center())
        fill_BMO.set_stroke(width=0).set_fill(YELLOW, 0.5)

    # Triangles AMO BMO equality
        AO_BO_equality = MathtexSegmentsEquality(('A', 'O', 'B', 'O'))

        OM_is_common = MathtexCommonSegment(('O', 'M'))
        OM_common_sign = CommonSegmentSign(OM)

        AM_MB_equality = MathtexSegmentsEquality(('A', 'M', 'M', 'B'))

        triangles_AMO_BMO_equality = MathTexTrianglesEquality('AMO', 'BMO')

        conclude_from_sss = ConcludeFromSSS(
                (AO_BO_equality, OM_is_common, AM_MB_equality),
                triangles_AMO_BMO_equality, DOWN
            )
        conclude_from_sss.next_to([-6.5, 0, 0], RIGHT, buff=0)
        
    # Angles AMO BMO equal 90
        angle_AMO = Angle(AM, OM, quadrant=(-1, -1), other_angle=True, 
            radius=0.25, color=BLUE)
        angle_BMO = Angle(MB, OM, quadrant=(1, -1), radius=0.35, color=YELLOW)

        rightarrow = Rightarrow().next_to(triangles_AMO_BMO_equality, RIGHT)

        AMO_BMO_90 = MathTex(r'\angle AMO', r'=', r'\angle BMO\ ', r'=\ 90^{\circ}', font_size=30)
        AMO_BMO_90.next_to(triangles_AMO_BMO_equality, 2*DOWN, aligned_edge=LEFT)

        right_angle_AMO = RightAngle(AM, OM, quadrant=(-1, -1), other_angle=True, 
            length=0.25, color=BLUE)
        right_angle_BMO = RightAngle(MB, OM, quadrant=(1, -1), length=0.35, color=YELLOW)

    # Perpendicular bisector of AB
        pb = Line(M.get_center()+np.array([0, 2, 0]), M.get_center()+np.array([0, -2, 0]),
            color=GREEN)
        right_angle = RightAngle(AM, pb, quadrant=(-1, -1), other_angle=True, 
            length=0.25, color=GREEN)

    # O belongs to perpendicular bisector of AB
        O_belongs_pb_AB = MathTex(r'O\textrm{-ն գտնվում է}\ AB\textrm{-ի միջնուղղահայացի վրա}',
            tex_template=armenian_tex_template, font_size=30)
        O_belongs_pb_AB.next_to([-7, -3.25, 0], RIGHT, buff=0)

# Animations for big circle, triangles AMO, BMO (54,117)
    # Write O, join A and B
        self.play(Write(label_O))
        self.wait(0.5)

        self.play(Create(AB))
        self.wait(0.5)
    
    # Create OA OB and equality signs
        self.play(Create(OA))
        self.add(A)
        self.play(Create(OB))
        self.add(B)
        self.wait(0.5)

        self.play(Create(equality_signs_OA_OB))
        self.wait(0.2)

        self.play(Wiggle(big_template_radius))
        self.play(Create(equality_sign_radius))
        self.wait(0.5)
    
    # Create M, OM, fill_AMO, fill_BMO
        self.play(Create(M), Create(label_M))
        self.play(Create(equality_signs_AM_MB))
        self.play(Create(OM))
        self.add(M)
        self.wait(1)
        self.play(FadeIn(fill_AMO))
        self.play(FadeIn(fill_BMO))
        self.wait(0.5)

    # Show triangles AMO BMO equality
        PlayTwoSegmentsEqualityWiggling(self, 
            ((OA, O, A, label_A, label_O), (OB, B, O, label_B, label_O)), AO_BO_equality
        )
        self.wait(0.2)
        PlaySegmentIsCommonWiggling(self, 
            (OM, O, M, label_O, label_M), OM_is_common
        )
        self.wait(0.2)
        PlayTwoSegmentsEqualityWiggling(self, 
            ((AM, A, M, label_A, label_M), (MB, M, B, label_M, label_B)), AM_MB_equality
        )
        self.wait(0.2)
        PlayConcludeTriangleCongruence(self, conclude_from_sss)
        self.wait(1)
    
    # Show angles AMO and BMO equality
        self.play(Create(angle_AMO))
        self.play(Create(angle_BMO))
        self.wait(0.5)

        self.play(Write(rightarrow))
        PlayTwoAnglesEqualityWiggling(self, angle_AMO, angle_BMO, AMO_BMO_90[:3])
        self.wait(0.5)

        self.play(Write(AMO_BMO_90[-1]))
        self.wait(0.5)

        self.play(
            ReplacementTransform(angle_AMO, right_angle_AMO), 
            ReplacementTransform(angle_BMO, right_angle_BMO)
        )
        self.wait(0.5)

        PlaySegmentThickening(self, (OM, O, M, label_O, label_M), scale_factor=1.5)
        self.wait(0.5)

    # O belongs to pb of AB
        self.play(Write(O_belongs_pb_AB), run_time=2)
        self.wait(0.5)

        self.play(
            FadeOut(conclude_from_sss, rightarrow, AMO_BMO_90, 
            fill_BMO, fill_AMO, right_angle_AMO, right_angle_BMO, OM)
        )
        self.wait(0.5)

        self.play(Create(pb))
        self.play(Create(right_angle))
        self.wait(1)


# Inits for other circle and construction
    # Upper and lower circles
        o_up = O.get_center()
        o_down = np.array([o_up[0], 2*M.get_center()[1]-o_up[1], 0])

        circle_up = Circle(1.5, GREEN).move_to(o_up)
        circle_down = Circle(1.5, GREEN).move_to(o_down)

        circle = always_redraw(lambda: 
                Circle(SegmentLength(OA), color=GREEN).move_to(O.get_center())
            )

    # O_up and join A B
        O_up = Dot(o_up, color=GREEN)
        label_O_up = LabelPoint(O_up, 'O', RIGHT*0.75, color=WHITE)
        O_upA = Line(o_up, a, color=ORANGE)
        O_upB = Line(o_up, b, color=ORANGE)

    # O_down and join A B
        O_down = Dot(o_down, color=GREEN)
        label_O_down = LabelPoint(O_down, 'O_1', RIGHT*0.75, color=WHITE)

        O_downA = Line(o_down, a, color=ORANGE)
        O_downB = Line(o_down, b, color=ORANGE)

        equality_signs_O_downA_O_downB = VGroup(
            SegmentEqualitySign1(O_downA),
            SegmentEqualitySign1(O_downB)
        )

    # Copy_R_A copy_R_B
        copy_R_A_1 = VGroup(big_template_radius, equality_sign_radius).copy()
        copy_R_B_1 = VGroup(big_template_radius, equality_sign_radius).copy()
        copy_R_A_2 = VGroup(big_template_radius, equality_sign_radius).copy()
        copy_R_B_2 = VGroup(big_template_radius, equality_sign_radius).copy()
    
    # Small r=AB/2
        r = MathTex(r'r', font_size=30).next_to(AM, UP)

#Animations for finding other circle and construction (117,153)
    # Move O up, then down, wait at O, then move down until O_1
        self.remove(big_circle)
        self.add(circle)
        self.play(FadeOut(equality_signs_OA_OB, label_O, label_M))
        self.wait(0.25)
        self.play(O.animate(rate_func=linear, run_time=2).shift(UP*0.75))
        self.wait(1)

        self.play(O.animate(rate_func=linear, run_time=1.5).shift(DOWN*0.75))
        self.play(FadeIn(equality_signs_OA_OB))
        self.wait(0.5)
        self.play(FadeOut(equality_signs_OA_OB))
        self.wait(0.25)

        self.play(O.animate(rate_func=linear, run_time=4).move_to(M.get_center()))
        self.wait(1)

        self.play(O.animate(rate_func=linear, run_time=4).move_to(o_down))
        self.remove(circle, O, OA, OB, A, B)
        self.add(circle_down, O_down, O_downA, O_downB)
        self.wait(1)

    # Crate label O1 and equality signs
        self.play(Create(equality_signs_O_downA_O_downB))
        self.wait(1)
        self.play(Write(label_O_down))
        self.wait(1)

    # Bring O and upper  circle, fadeout lots of things
        self.play(
            Create(O_up), Create(O_upB), Create(O_upA),  Create(label_O_up),
            Create(equality_signs_OA_OB), Create(circle_up), FadeIn(A), FadeIn(B)
        )
        self.wait(1)

        self.play(
            FadeOut(
                O_belongs_pb_AB, circle_up, circle_down, equality_signs_AM_MB, 
                pb, right_angle, AM, MB, AB, M,
            )
        )
        self.wait(1)

    # Draw circles with centers A and B
        self.play(copy_R_A_1.animate(rate_func=linear, run_time=1).next_to(a, RIGHT, buff=0))
        self.remove(copy_R_A_1)
        circle_A, t_o = CircleFromSpinningRadius(self, radius=big_radius_value, center=a, 
                equality_sign=1, radius_color=ORANGE, circle_color=BLUE, 
                create_center=False, create_radius=False, create_equality_sign=False, run_time=3
            )
        self.remove(t_o)
        self.wait(1)

        self.play(copy_R_B_1.animate(rate_func=linear, run_time=1).next_to(b, LEFT, buff=0))
        self.remove(copy_R_B_1)
        circle_B, t_o = CircleFromSpinningRadius(self, radius=big_radius_value, center=b, 
                equality_sign=1, radius_color=ORANGE, circle_color=BLUE,
                create_center=False, create_radius=False, create_equality_sign=False, run_time=1.5,
                direction=-1, starting_point_angle=180
            )
        self.remove(t_o)
        self.wait(1)
        self.play(
            O_up.animate(rate_func=there_and_back, run_time=2.5).scale(2), 
            O_down.animate(rate_func=there_and_back, run_time=2.5).scale(2)
        )
        self.wait(1)

    # FadeOut everything
        self.play(
            FadeOut(
                A, B, label_A, label_B, circle_A, circle_B, 
                O_up, label_O_up, O_upA, O_upB, equality_signs_OA_OB,
                O_down, label_O_down, O_downA, O_downB, equality_signs_O_downA_O_downB
            )
        )
        self.wait(1)


# Final construction (153,...)
    # Create A and B and draw circles with centers A and B
        self.play(Create(A), Create(label_A))
        self.play( Create(B), Create(label_B))
        self.wait(0.5)

        self.play(copy_R_A_2.animate(rate_func=linear, run_time=1).next_to(a, RIGHT, buff=0))
        self.remove(copy_R_A_2)
        circle_A, t_o = CircleFromSpinningRadius(self, radius=big_radius_value, center=a, 
                equality_sign=1, radius_color=ORANGE, circle_color=BLUE, 
                create_center=False, create_radius=False, create_equality_sign=False, run_time=2.5
            )
        self.remove(t_o)
        self.wait(0.5)

        self.play(copy_R_B_2.animate(rate_func=linear, run_time=1).next_to(b, LEFT, buff=0))
        self.remove(copy_R_B_2)
        circle_B, t_o = CircleFromSpinningRadius(self, radius=big_radius_value, center=b, 
                equality_sign=1, radius_color=ORANGE, circle_color=BLUE,
                create_center=False, create_radius=False, create_equality_sign=False, run_time=1.5,
                direction=-1, starting_point_angle=180
            )
        self.remove(t_o)
        self.wait(1)
        self.play(
            O_up.animate(rate_func=there_and_back, run_time=2.5).scale(2), 
            O_down.animate(rate_func=there_and_back, run_time=2.5).scale(2)
        )
        self.wait(1)

        self.play(Create(green_rect))
        self.wait(1)
        self.play(Wiggle(red_rect, run_time=4))
        self.wait(1)

        self.play(FadeOut(circle_B, circle_A))
        self.wait(1)

        circle_up, t_o = CircleFromSpinningRadius(self, 
                big_radius_value, o_up, 180, equality_sign=1, radius_color=ORANGE, 
                center_color=GREEN, create_center=False, run_time=1.5
            )
        self.remove(t_o)
        circle_down, t_o = CircleFromSpinningRadius(self, 
                big_radius_value, o_down, 180, equality_sign=1, radius_color=ORANGE, 
                center_color=GREEN, create_center=False, run_time=1.5
            )
        self.remove(t_o)
        self.wait(1)

        self.play(FadeOut(circle_up, circle_down, O_up, O_down))
        self.wait(0.5)

    # R = AB/2
        self.play(Create(AB.set_color(ORANGE)))
        self.play(Create(M.set_color(GREEN)))
        
        self.play(Write(r))
        
        half_AB_crc_1, t_o = CircleFromSpinningRadius(self, 
                1, a, radius_color=ORANGE, center_color=GREEN, circle_color=BLUE, 
                create_center=False, create_radius=False, create_point=False, run_time=2
            )
        self.remove(t_o)

        half_AB_crc_2, t_o = CircleFromSpinningRadius(self, 
                1, b, radius_color=ORANGE, center_color=GREEN, circle_color=BLUE,
                create_center=False, create_radius=False, create_point=False, run_time=2
            )
        self.remove(t_o)
        self.wait(0.5)

        self.play(M.animate(rate_func=there_and_back, run_time=1.5).scale(2))
        self.wait(0.5)

        self.play(FadeOut(half_AB_crc_1, half_AB_crc_2))
        self.wait(0.5)

        last_circle, t_o = CircleFromSpinningRadius(self,
            1, M.get_center(), radius_color=ORANGE, center_color=GREEN, 
                create_center=False, create_radius=False, create_point=False, run_time=3
        )
        self.wait(1)

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)
