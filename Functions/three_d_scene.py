import manim
from manim import ThreeDScene as OriginalThreeDScene


class ThreeDScene(OriginalThreeDScene):
    def planate(self, obj):
        phi = self.camera.get_phi()
        theta = self.camera.get_theta()
        obj.rotate(phi, axis=manim.RIGHT)
        obj.rotate(90 * manim.DEGREES + theta, axis=manim.OUT)
        return obj
