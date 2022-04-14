import sys
sys.path.append('../../')
from Functions.qarakusi import *

class problem_11037(Scene):
    def construct(self):

        numbers_and_signs = MathTex(r'a_1', r'<', r'a_2', r'<', r'a_3', r'<', r'a_4', r'<', r'a_5', r'<', 
                    r'a_6', r'<', r'a_7', r'<', r'a_8', r'<', r'a_9', r'<', r'a_{10}', 
                    font_size=50
                ).shift(3*UP)

        numbers = VGroup(*[numbers_and_signs[2*i] for i in range(10)])
        commas = VGroup(*[MathTex(',', font_size=50).move_to(numbers_and_signs[2*i+1].get_center()).shift(0.25*DOWN) for i in range(9)])

        rectangles = VGroup(*[SurroundingRectangle(numbers[i]) for i in range(len(numbers))])

        square_of_diff = VGroup(
                MathTex(r'(', r'a_1', r'-', r'a_2', r')', r'^2', font_size=50, color=GREEN),
                MathTex(r'(', r'a_1', r'-', r'a_3', r')', r'^2', font_size=50, color=GREEN),
                MathTex(r'\vdots', font_size=50, color=GREEN),
                MathTex(r'(', r'a_9', r'-', r'a_{10}', r')', r'^2', font_size=50, color=GREEN)
            ).arrange(DOWN).move_to([-4, 0, 0])

        diff_of_squares = VGroup(
                MathTex(r'|', r'a_1^2', r'-', r'a_2^2', r'|', font_size=50, color=ORANGE),
                MathTex(r'|', r'a_1^2', r'-', r'a_3^2', r'|', font_size=50, color=ORANGE),
                MathTex(r'|', r'\vdots', fr'|', font_size=50, color=ORANGE),
                MathTex(r'|', r'a_9^2', r'-', r'a_{10}^2', r'|', font_size=50, color=ORANGE),
            ).arrange(DOWN).move_to([4, 0, 0])

# Animations
        self.play(Write(numbers), Write(commas), rate_func=linear, run_time=3)

    # Write square of difference column
        self.play(Circumscribe(numbers[0], fade_out=True), Circumscribe(numbers[1], fade_out=True))
        self.play(ReplacementTransform(numbers[0].copy(), square_of_diff[0][1]), ReplacementTransform(numbers[1].copy(), square_of_diff[0][3]))
        self.play(Write(square_of_diff[0][0]), Write(square_of_diff[0][2]), Write(square_of_diff[0][4]), Write(square_of_diff[0][5]))

        self.play(Circumscribe(numbers[0], fade_out=True), Circumscribe(numbers[2], fade_out=True))
        self.play(ReplacementTransform(numbers[0].copy(), square_of_diff[1][1]), ReplacementTransform(numbers[2].copy(), square_of_diff[1][3]))
        self.play(Write(square_of_diff[1][0]), Write(square_of_diff[1][2]), Write(square_of_diff[1][4]), Write(square_of_diff[1][5]))

        self.play(Write(square_of_diff[2]))

        self.play(Circumscribe(numbers[8], fade_out=True), Circumscribe(numbers[9], fade_out=True))
        self.play(ReplacementTransform(numbers[8].copy(), square_of_diff[3][1]), ReplacementTransform(numbers[9].copy(), square_of_diff[3][3]))
        self.play(Write(square_of_diff[3][0]), Write(square_of_diff[3][2]), Write(square_of_diff[3][4]), Write(square_of_diff[3][5]))
    
    # # Write difference of squares column
    #     self.play(Circumscribe(numbers[0], fade_out=True), Circumscribe(numbers[1], fade_out=True))
    #     self.play(ReplacementTransform(numbers[0].copy(), diff_of_squares[0][0]), ReplacementTransform(numbers[1].copy(), diff_of_squares[0][2]))
    #     self.play(Write(diff_of_squares[0][1]))

    #     self.play(Circumscribe(numbers[0], fade_out=True), Circumscribe(numbers[2], fade_out=True))
    #     self.play(ReplacementTransform(numbers[0].copy(), diff_of_squares[1][0]), ReplacementTransform(numbers[2].copy(), diff_of_squares[1][2]))
    #     self.play(Write(diff_of_squares[1][1]))

    #     self.play(Write(diff_of_squares[2]))

    #     self.play(Circumscribe(numbers[8], fade_out=True), Circumscribe(numbers[9], fade_out=True))
    #     self.play(ReplacementTransform(numbers[8].copy(), diff_of_squares[3][0]), ReplacementTransform(numbers[9].copy(), diff_of_squares[3][2]))
    #     self.play(Write(diff_of_squares[3][1]))

        self.add(diff_of_squares)
        self.wait(1)
