import numpy as np
import manim
from manim import VGroup
from manim import ThreeDAxes, Surface

from Functions.three_d_scene import ThreeDScene


class DiscreteCube(VGroup):
    def __init__(self, side_length, scale=1, surface_kwargs=None, **kwargs):
        if surface_kwargs is None:
            surface_kwargs = {}
        super().__init__(**kwargs)
        self.shifts = []
        # bottom
        self.add(
            Surface(
                lambda u, v: [u, scale - v, 0],
                u_range=[0, scale],
                v_range=[0, scale],
                resolution=side_length,
                **surface_kwargs
            )
        )
        self.shifts.append([0, 0, -1])
        # top
        self.add(
            Surface(
                lambda u, v: [u, v, scale],
                u_range=[0, scale],
                v_range=[0, scale],
                resolution=side_length,
                **surface_kwargs
            )
        )
        self.shifts.append([0, 0, 1])
        # left
        self.add(
            Surface(
                lambda u, v: [0, scale - v, u],
                u_range=[0, scale],
                v_range=[0, scale],
                resolution=side_length,
                **surface_kwargs
            )
        )
        self.shifts.append([-1, 0, 0])
        # right
        self.add(
            Surface(
                lambda u, v: [scale, v, u],
                u_range=[0, scale],
                v_range=[0, scale],
                resolution=side_length,
                **surface_kwargs
            )
        )
        self.shifts.append([1, 0, 0])
        # front
        self.add(
            Surface(
                lambda u, v: [scale - v, 0, u],
                u_range=[0, scale],
                v_range=[0, scale],
                resolution=side_length,
                **surface_kwargs
            )
        )
        self.shifts.append([0, -1, 0])
        # back
        self.add(
            Surface(
                lambda u, v: [u, scale, v],
                u_range=[0, scale],
                v_range=[0, scale],
                resolution=side_length,
                **surface_kwargs
            )
        )
        self.shifts.append([0, 1, 0])
    
    def break_into_pieces(self):
        return [side.animate.shift(shift) for side, shift in zip(self, self.shifts)]

    def get_side(self, vec):
        return max(self, key=lambda side: sum(v for point in side for v in point.points@vec))


class Problem11714(ThreeDScene):
    def rotate_direction(self, direction):
        return self.planate(manim.Vector(direction)).get_vector()

    def construct(self):
        def calculate_number_of_squares(side_length):
            theta = 45 * manim.DEGREES
            phi = 75 * manim.DEGREES

            self.set_camera_orientation(phi=phi, theta=theta)
            
            scale = 1.5
            cube = DiscreteCube(side_length, surface_kwargs={"checkerboard_colors":[manim.RED_D, manim.GREEN_D]}, scale=scale)
            cube2 = cube.copy()
            cube.move_to(manim.ORIGIN)

            self.add(cube)

            self.begin_ambient_camera_rotation(manim.DEGREES * 90)
            self.wait(2.5)
            self.stop_ambient_camera_rotation()
            self.wait(1)
            other_cube = cube.copy()
            self.add(other_cube)
            self.play(cube.animate.shift(self.rotate_direction(manim.RIGHT * 4)))
            self.play(other_cube.animate.shift(self.rotate_direction(manim.LEFT * 4)))
            self.play(other_cube.animate.set_color(manim.BLUE))
            self.wait(1)
            prompt = self.planate(
                manim.Text("Հաշվենք, թե քանի վանդակ ներկեցինք")
            ).shift(self.rotate_direction(manim.UP * 3.4))
            self.play(
                manim.Write(prompt)
            )
            self.wait(1)
            
            planation_animations = []
            out_side = self.planate(cube2.get_side(manim.OUT).copy())
            out = self.rotate_direction(manim.OUT)
            out_side.shift(-np.mean(out_side[0].points - cube.get_side(out)[0].points, axis=0))
            for from_, to_ in [(manim.RIGHT, manim.RIGHT),
                            (manim.LEFT, manim.LEFT),
                            (manim.UP, manim.UP),
                            (manim.DOWN, manim.DOWN),
                            (manim.IN, manim.LEFT * 2),
                            (manim.OUT, manim.OUT * 0)]:
                from_ = self.rotate_direction(from_)
                to_ = self.rotate_direction(to_ + manim.LEFT)
                side = cube.get_side(from_)
                planation_animations.append(manim.Transform(side, out_side.copy().shift(to_ * scale)))
            self.play(*planation_animations)
            self.wait(1)

            ind = 0
            for side in cube:
                for point in side:
                    ind += 1
                    num = self.planate(manim.Text(str(ind))).shift(np.mean(point.points, axis=0))
                    self.play(manim.Write(num, run_time=None if ind <= 8 else 0.2))
            self.wait(1)

        calculate_number_of_squares(2)
        self.clear()
        calculate_number_of_squares(6)
        prompt = self.planate(
            manim.Text("Ստացվեց 24 քառակուսի")
        ).shift(self.rotate_direction(manim.UP * 3.4))
