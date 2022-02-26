from manim import *
import numpy as np

class Problem_12515(Scene):
    def construct(self):
        ground_1_y = 1
        ground_2_y = -2
        ground_1 = Line([-8, ground_1_y, 0], [8, ground_1_y, 0])
        ground_2 = Line([-8, ground_2_y, 0], [8, ground_2_y, 0])

        ball_radius = 0.3
        balls_distance = 0.7 + 2 * ball_radius
        arrow_size = 40

        upper_left_balls_x = np.arange(-6, -6 + 5*balls_distance, balls_distance)
        upper_left_coordinates = np.array([*[[x, ground_1_y+ball_radius, 0] for x in upper_left_balls_x]])
        upper_right_coordinates = np.array([*[abs(x) for x in upper_left_coordinates]])[::-1]

        upper_left_balls = VGroup(
            *[
                VGroup(
                    Circle(ball_radius, WHITE).set_fill(GREEN, opacity=0.7),
                    MathTex(r'\rightarrow', font_size=arrow_size).set_stroke(WHITE, 4)
                ).move_to(coord)
                for coord in upper_left_coordinates
            ]
        )

        upper_right_balls = VGroup(
            *[
                VGroup(
                    Circle(ball_radius, WHITE).set_fill(ORANGE, opacity=0.7),
                    MathTex(r'\leftarrow', font_size=arrow_size).set_stroke(WHITE, 4)
                ).move_to(coord)
                for coord in upper_right_coordinates
            ]
        )


        self.add(ground_1, ground_2, upper_left_balls, upper_right_balls)
        self.wait(1)
        self.play(
            upper_left_balls[-1].animate(rate_func=linear).move_to([-ball_radius, ground_1_y+ball_radius, 0]),
            upper_right_balls[0].animate(rate_func=linear).move_to([ball_radius, ground_1_y+ball_radius, 0]),
            run_time=2
        )
        self.play(
            Rotating(upper_right_balls[0][1], radians=-PI, rate_func=linear, about_point=upper_right_balls[0].get_center()),
            upper_right_balls[0][0].animate(rate_func=linear).set_fill(GREEN),
            Rotating(upper_left_balls[-1][1], radians=PI, rate_func=linear, about_point=upper_left_balls[-1].get_center()),
            upper_left_balls[-1][0].animate(rate_func=linear).set_fill(ORANGE),
            run_time=2
        )
        self.play(
            upper_left_balls[-1].animate(rate_func=linear).move_to(upper_left_coordinates[-1]),
            upper_right_balls[0].animate(rate_func=linear).move_to(upper_right_coordinates[0]),
            run_time=2
        )
        self.wait(1)
        # self.play(upper_right_balls[2].animate(run_time=1, rate_func=linear).set_opacity(0.3))
        self.wait(1)
