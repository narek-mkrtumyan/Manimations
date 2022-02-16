from manim import *
import numpy as np


def dist(a, b):
    return np.sqrt(sum((a-b)**2))


def BayesRectangles(sq_center, sq_size, prop_left, prop_ld, prop_rd, fill_opacity=1):

    ld_color = GREEN_E
    lu_color = DARK_GRAY
    rd_color = GREEN_B
    ru_color = GRAY

    a_1 = np.array([-sq_size/2, -sq_size/2, 0]) + sq_center
    a_2 = a_1 + np.array([0, sq_size, 0])
    a_3 = a_2 + np.array([sq_size, 0, 0])
    a_4 = a_1 + np.array([sq_size, 0, 0])

    bottom_point = always_redraw(lambda: Dot([a_1[0] + sq_size * prop_left.get_value(), a_1[1], 0], radius=0))
    upper_point = always_redraw(lambda: Dot([a_2[0] + sq_size * prop_left.get_value(), a_2[1], 0], radius=0))
    left_point = always_redraw(lambda: Dot([a_1[0], a_1[1] + sq_size * prop_ld.get_value(), 0], radius=0))
    right_point = always_redraw(lambda: Dot([a_4[0], a_4[1] + sq_size * prop_rd.get_value(), 0], radius=0))
    cl_point = always_redraw(lambda: Dot([a_1[0] + sq_size * prop_left.get_value(), a_1[1] + sq_size * prop_ld.get_value(), 0], radius=0))
    cr_point = always_redraw(lambda: Dot([a_1[0] + sq_size * prop_left.get_value(), a_4[1] + sq_size * prop_rd.get_value(), 0], radius=0))

    # FILL EACH RECTANGLE WITH A COLOR
    # RECTANGLE_LEFT_DOWN,  RECTANGLE_LEFT_UP,  RECTANGLE_RIGHT_DOWN,  RECTANGLE_RIGHT_UP

    rec_ld = always_redraw(lambda: Polygon(a_1, left_point.get_center(), cl_point.get_center(), bottom_point.get_center(), 
    color=WHITE, fill_opacity=fill_opacity).set_fill(ld_color))

    rec_lu = always_redraw(lambda: Polygon(left_point.get_center(), a_2, upper_point.get_center(), cl_point.get_center(),
    color=WHITE, fill_opacity=fill_opacity).set_fill(lu_color))

    rec_rd = always_redraw(lambda: Polygon(bottom_point.get_center(), cr_point.get_center(), right_point.get_center(), a_4,
    color=WHITE, fill_opacity=fill_opacity).set_fill(rd_color))

    rec_ru = always_redraw(lambda: Polygon(cr_point.get_center(), upper_point.get_center(), a_3, right_point.get_center(),
    color=WHITE, fill_opacity=fill_opacity).set_fill(ru_color))

    area_prop_dot = always_redraw(lambda: 
        Dot([prop_left.get_value() * prop_ld.get_value() / (1 - prop_left.get_value()) / prop_rd.get_value(), 0, 0], radius=0))

    dots = VGroup(bottom_point, upper_point, left_point, right_point, cl_point, cr_point)

    return rec_ld, rec_lu, rec_rd, rec_ru, dots, area_prop_dot


def BayesUnitRectangle(rect_center, rect_length, rect_width, area_prop_dot, fill_opacity=1):
    
            ld_color = GREEN_E
            rd_color = GREEN_B
            
            p_1 = np.array([-rect_length/2, -rect_width/2, 0]) + rect_center
            p_2 = p_1 + np.array([0, rect_width, 0])
            p_3 = p_2 + np.array([rect_length, 0, 0])
            p_4 = p_1 + np.array([rect_length, 0, 0])

            rect = Polygon(p_1, p_2, p_3, p_4,color=WHITE)

            d_1 = always_redraw(lambda: 
                Dot([p_1[0] + area_prop_dot.get_center()[0] / (area_prop_dot.get_center()[0] + 1) * rect_length, p_1[1], 0], radius=0))
            d_2 = always_redraw(lambda: 
                Dot([p_2[0] + area_prop_dot.get_center()[0] / (area_prop_dot.get_center()[0] + 1) * rect_length, p_2[1], 0], radius=0))
            
            rect_1 = always_redraw(lambda: Polygon(p_1, p_2, d_2.get_center(), d_1.get_center(), color=WHITE, fill_opacity=fill_opacity).set_fill(ld_color))
            rect_2 = always_redraw(lambda: Polygon(d_1.get_center(), d_2.get_center(), p_3, p_4, color=WHITE, fill_opacity=fill_opacity).set_fill(rd_color))

            dots = VGroup(d_1, d_2)
            
            return rect, rect_1, rect_2, dots



class Rectangles(Scene):
    def construct(self):

        sq_center = np.array([-3, 0, 0])
        sq_size = 4

        rect_center = np.array([2, 1, 0])
        rect_length = 3
        rect_width = 1

        zero_size_dots = VGroup()

        prop_left = ValueTracker(0.2)           # Proportion of the left group in the WHOLE group
        prop_ld = ValueTracker(0.7)             # Proportion of the bottom group in the LEFT group    LEFT_DOWN
        prop_rd = ValueTracker(0.3)             # Proportion of the bottom group in the RIGHT group   RIGHT_DOWN

        rec_ld, rec_lu, rec_rd, rec_ru, dots_1, area_prop_dot = BayesRectangles(sq_center, sq_size, prop_left, prop_ld, prop_rd)

        rect, rect_1, rect_2, dots_2 = BayesUnitRectangle(rect_center, rect_length, rect_width, area_prop_dot)

        # SOME COMPIES FOR TRANSFORMATIONS
        rec_ld_copy = rec_ld.copy()
        rec_rd_copy = rec_rd.copy()
        rect_1_copy = rect_1.copy()
        rect_2_copy = rect_2.copy()

        zero_size_dots.add(dots_1, area_prop_dot, dots_2)



        numerator = always_redraw(lambda: rect_1.copy().move_to(rect_center - np.array([0, 2, 0])).scale(0.3))
        denominator = VGroup(always_redraw(lambda: rect_1.copy().move_to(rect_center - np.array([0.8, 3, 0])).scale(0.3)), 
            Tex('+').move_to(rect_center - np.array([0, 3, 0])),
            always_redraw(lambda: rect_2.copy().move_to(rect_center - np.array([-0.8, 3, 0])).scale(0.3)))
        frac_line = Line(rect_center - np.array([1.2, 2.5, 0]), rect_center - np.array([-1.2, 2.5, 0]))

        self.add(zero_size_dots)
        self.add(rec_ld, rec_lu, rec_rd, rec_ru)
        self.wait(0.5)

        # CREATE UNIT RECTANGLE
        self.play(Create(rect))
        self.play(Transform(rec_ld_copy, rect_1))
        self.remove(rec_ld_copy)
        self.add(rect_1)
        self.play(Transform(rec_rd_copy, rect_2))
        self.remove(rec_rd_copy)
        self.add(rect_2)

        # CREATE FRACTION
        self.play(Transform(rect_1_copy.copy(), numerator))
        self.remove(rect_1_copy)
        self.add(numerator)
        self.play(Create(frac_line))
        self.play(Transform(rect_1_copy, denominator[0]))
        self.remove(rect_1_copy)
        self.add(denominator[0])
        self.play(Write(denominator[1]))
        self.play(Transform(rect_2_copy, denominator[2]))
        self.remove(rect_2_copy)
        self.add(denominator[2])

        # self.add(numerator, denominator, frac_line)

        self.wait(1)
        self.play(prop_left.animate().set_value(0.7), run_time=1.5, rate_func=linear)
        self.wait(0.5)
        self.play(prop_ld.animate().set_value(0.4), run_time=1.5, rate_func=linear)  
        self.wait(0.5)
        self.play(prop_rd.animate().set_value(0.8), run_time=1.5, rate_func=linear)  
        self.wait(1)      





class test(Scene):
    def construct(self):
        
        self.wait()
