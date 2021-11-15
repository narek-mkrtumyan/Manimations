from re import U
from typing import MutableSequence
from manim import *
import numpy as np

class segments(Scene):
    def construct(self):
        a_1 = np.array([-5, 2, 0])    # fisrt segment's starting coordinare
        b_1 = np.array([1, 2, 0])     # fisrt segment's ending coordinare
        a_2 = np.array([-5, -1, 0])   # sencond segment's starting coordinare
        b_2 = np.array([1, -1, 0])    # second segment's ending coordinare
        c_2 = np.array([3, -1, 0])    # extra part of the second segment is (c2, b2) 

        name_1 = Text("Հայկ").move_to([-4, 3, 0])
        name_2 = Text("Մանե").move_to([-4, 0, 0])

        cal1_14 = MathTex("14").move_to([3, 3, 0])                            # 14 - 2 = 12
        cal1_minus = MathTex("-").move_to([3.5, 3, 0])    
        cal1_2 = MathTex("2").move_to([3.9, 3, 0])    
        cal1_12 = MathTex("=12").move_to([4.7, 3, 0])  

        calculation_2 = MathTex("\\frac{12}{2}=").move_to([3.3, 1.5, 0])      # 12/2 = 6
        cal2_6 = MathTex("6").move_to([4.4, 1.5, 0])

        cal3_6 = MathTex("6").move_to([3, 0, 0])                              # 6 + 2 = 8
        cal3_plus = MathTex("+").move_to([3.4, 0, 0])
        cal3_2 = MathTex("2").move_to([3.8, 0, 0])
        cal3_equal = MathTex("=").move_to([4.2, 0, 0])
        cal3_8 = MathTex("8").move_to([4.7, 0, 0])

        startpoint_1 = Dot(a_1)
        endpoint_1 = Dot(b_1)
        segment_1 = Line(a_1, b_1).set_color(BLUE)
        # segment_1 = VGroup(startpoint_1, endpoint_1, line_1)

        startpoint_2 = Dot(a_2)
        endpoint_2 = Dot(b_2)
        segment_2 = Line(a_2, b_2).set_color(BLUE)
        # segment_2 = VGroup(startpoint_1, endpoint_2, line_2)
        extra_point = Dot(c_2)

        segment_difference = Line(b_2, c_2).set_color(RED)

        brace_difference = BraceBetweenPoints(b_2, c_2)
        brace_difference_text = brace_difference.get_text("2")

        brace_combined = BraceBetweenPoints(a_1 + np.array([0, 0.2, 0]), a_2 - np.array([0, 0.2, 0]))
        brace_combined_text = brace_combined.get_text("14")

        brace_1 = BraceBetweenPoints(a_1, b_1)
        brace_1_text = brace_1.get_text("6")
        brace_2 = BraceBetweenPoints(a_2, b_2)
        brace_2_text = brace_2.get_text("6")
        
        answer_1 = Text("-  6").move_to([-2.5, 3, 0])
        answer_2 = Text("-  8").move_to([-2.5, 0, 0])

        self.wait(0.5)

        self.play(Write(name_1))                            # write first name - Hayk

        self.play(Create(segment_1), Create(startpoint_1), Create(endpoint_1))  # draw Hayk's segment
        self.wait(0.5)

                                                                                # draw Mane's segment
        self.play(Transform(segment_1.copy(), segment_2),
        Transform(endpoint_1.copy(), endpoint_2), 
        Transform(startpoint_1.copy(), startpoint_2))
        self.wait(0.5)

        self.play(Create(segment_difference))               # add extra peace
        self.add(extra_point, endpoint_2)                   # add extra point on Mane's segment
        self.play(Create(brace_difference))                 # draw difference brace 
        self.play(Write(brace_difference_text))             # write 2
        self.wait(0.2)

        self.play(Write(name_2))                            # write second name - Mane
        self.wait(1)

        self.play(Create(brace_combined))                   # draw combined brace
        self.play(Write(brace_combined_text))               # write 14
        self.wait(1)

        self.play(Create(brace_1))                          # draw Hayk's brace
        self.play(Create(brace_2))                          # draw Mane's brace

        self.play(Transform(brace_combined_text.copy(), cal1_14))      # 14 - 2 = 12
        self.play(Write(cal1_minus))
        self.play(Transform(brace_difference_text.copy(), cal1_2))
        self.play(Write(cal1_12))
        self.wait(2)
        self.play(Write(calculation_2))                                # 12 / 2 = 6
        self.play(Write(cal2_6))
        self.wait(0.5)

        self.play(Transform(cal2_6.copy(), brace_1_text))              # write Hayk's 6
        self.play(Transform(cal2_6.copy(), brace_2_text))              # write Mane's 6
        self.wait(1.5)

        self.play(Transform(brace_2_text.copy(), cal3_6))              # 6 + 2 = 8
        self.play(Write(cal3_plus))
        self.play(Transform(brace_difference_text.copy(), cal3_2))
        self.play(Write(cal3_equal))
        self.play(Write(cal3_8))
        self.wait(1)

        self.play(Transform(brace_1_text.copy(), answer_1))            # write Haks's answer - 6
        self.play(Transform(cal3_8.copy(), answer_2))                  # write Mane's answer - 8
        self.wait(1)
