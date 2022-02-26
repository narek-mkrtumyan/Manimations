from manim import *
import numpy as np
import sys
sys.path.append('../')
from Objects.Objects import *
from Configs import *

class CalendarMonth(VMobject):
    def __init__(self, year=2022, month=1, first_weekday=1, weekend_color=RED, extra_days_opacity=0.3, background_color=YELLOW_E):
        VMobject.__init__(self)

        rectangle_height = 2.9
        rectangle_width = 2.35

        self.year = year
        self.month =  month
        self.first_weekday = first_weekday
        self.extra_days_opacity = extra_days_opacity
        self.background_color = background_color
        self.weekend_color = weekend_color

        self.outline = Rectangle(WHITE, rectangle_height, rectangle_width)
        
        self.background = VGroup()

        self.background.add(Rectangle(height=0.75, width=rectangle_width).set_stroke(width=0).set_fill(background_color, 0.5))
        self.background[0].next_to(ORIGIN + np.array([[0, rectangle_height / 2, 0]]), DOWN, buff=0)

        self.VMyear = MathTex(rf'{year}', font_size=25)
        self.VMyear.next_to(self.outline, UP).shift(0.55 * DOWN)

        self.VMmonth = MathTex(r'\textrm{' + months_arm[month - 1] + r'}', font_size=25, tex_template=armenian_tex_template)
        self.VMmonth.next_to(self.VMyear, DOWN, buff=0.15)

        self.background.add(
            MathTex('<<', font_size=20).move_to(self.VMmonth.get_center()).shift(0.9 * LEFT),
            MathTex('>>', font_size=20).next_to(self.VMmonth.get_center()).shift(0.5 * RIGHT)
        )

        self.week_blocks = VGroup(
                *[Rectangle(height=0.25, width=rectangle_width/7, stroke_width=1) for i in range(7)]
            )
        self.week_blocks.arrange(buff=0).next_to(self.background, DOWN, buff=0)

        self.week_days = MathTex(*[r'\textrm{' + day + r'}' for day in week_days_arm], font_size=20, tex_template=armenian_tex_template)
        for i in range(7):
            self.week_days[i].move_to(self.week_blocks[i].get_center())
        self.week_days[-2:].set_color(weekend_color)

        if year % 4 == 0 and month == 2:
            number_of_days_in_month = 28   
        else:
            number_of_days_in_month = months_lengths[month - 1]
        
        if year % 4 == 0 and month == 3:
            number_of_days_in_previous_month = 28
        elif month == 1:
            number_of_days_in_previous_month = 31
        else:
            number_of_days_in_previous_month = months_lengths[month - 2]

        if first_weekday == 1:
            extra_days_from_start = np.array([])
        else:
            extra_days_from_start = np.arange(
                    number_of_days_in_previous_month - first_weekday + 2, number_of_days_in_previous_month + 1
                )

        extra_days_till_end = np.arange(1, (7 - (len(extra_days_from_start) + number_of_days_in_month % 7)) % 7 + 1)

        days_list = np.arange(1, number_of_days_in_month + 1)


        full_list_of_days = np.concatenate([extra_days_from_start, days_list, extra_days_till_end])
        self.number_of_rows = int(len(full_list_of_days) / 7)

        self.full_days = VGroup(*[MathTex(fr'{int(day)}', font_size=19) for day in full_list_of_days])
        self.full_days.arrange_in_grid(cols=7, buff=0.15)
        self.full_days.next_to(self.week_blocks, DOWN, buff=0.15)

        self.extra_days = VGroup(
                *self.full_days[:len(extra_days_from_start)],
                *self.full_days[-len(extra_days_till_end):]
            )
        
        self.days = VGroup(*self.full_days[len(extra_days_from_start): -len(extra_days_till_end)])
        

        for i in range(len(full_list_of_days)):
            if i % 7 == 5  or  i % 7 == 6:
                self.full_days[i].set_color(weekend_color)
        
        self.extra_days.set_opacity(extra_days_opacity)

        self.add(self.outline, self.background, self.VMyear, self.VMmonth, self.week_days, self.week_blocks, self.days, self.extra_days)
    


    def shift_weekdays(self, scene, rate_functions):

        shift_amount = self.week_blocks[0].width * RIGHT

        if self.first_weekday != 7:
            new_calendar = CalendarMonth(
                    self.year, self.month, self.first_weekday + 1, 
                    self.weekend_color, self.extra_days_opacity, self.background_color
                ).scale(2)
            new_calendar.full_days.move_to(self.full_days.get_center())
            VGroup(*[new_calendar.full_days[7*i] for i in range(self.number_of_rows)]).set_opacity(0).shift(-shift_amount)

            scene.play(
                ReplacementTransform(
                    VGroup(*[self.full_days[7*i + 0] for i in range(self.number_of_rows)]),
                    VGroup(*[new_calendar.full_days[7*i + 1] for i in range(self.number_of_rows)])
                ),
                ReplacementTransform(
                    VGroup(*[self.full_days[7*i + 1] for i in range(self.number_of_rows)]),
                    VGroup(*[new_calendar.full_days[7*i + 2] for i in range(self.number_of_rows)])
                ),
                ReplacementTransform(
                    VGroup(*[self.full_days[7*i + 2] for i in range(self.number_of_rows)]),
                    VGroup(*[new_calendar.full_days[7*i + 3] for i in range(self.number_of_rows)])
                ),
                ReplacementTransform(
                    VGroup(*[self.full_days[7*i + 3] for i in range(self.number_of_rows)]),
                    VGroup(*[new_calendar.full_days[7*i + 4] for i in range(self.number_of_rows)])
                ),
                ReplacementTransform(
                    VGroup(*[self.full_days[7*i + 4] for i in range(self.number_of_rows)]),
                    VGroup(*[new_calendar.full_days[7*i + 5] for i in range(self.number_of_rows)])
                ),
                ReplacementTransform(
                    VGroup(*[self.full_days[7*i + 5] for i in range(self.number_of_rows)]),
                    VGroup(*[new_calendar.full_days[7*i + 6] for i in range(self.number_of_rows)])
                ),
                VGroup(*[self.full_days[7*i + 6] for i in range(self.number_of_rows)]).animate.shift(shift_amount).set_opacity(0),
                VGroup(*[new_calendar.full_days[7*i + 0] for i in range(1, self.number_of_rows)]).animate.shift(shift_amount).set_opacity(1),
                new_calendar.full_days[0].animate.shift(shift_amount).set_opacity(self.extra_days_opacity),
            )
            
            self.full_days = new_calendar.full_days
            self.extra_days = new_calendar.extra_days
            self.days = new_calendar.days
    
    
    def next_month(self, scene):

        print(len(self.extra_days))




class Week(VMobject):
    def __init__(self, full_width=2.35, weekend_color=RED):
        VMobject.__init__(self)
        self.blocks = VGroup(
                *[Rectangle(height=0.25, width=full_width/7, stroke_width=1) for i in range(7)]
            )
        self.blocks.arrange(buff=0)

        self.days = MathTex(*[r'\textrm{' + day + r'}' for day in week_days_arm], font_size=20, tex_template=armenian_tex_template)
        for i in range(7):
            self.days[i].move_to(self.blocks[i].get_center())
        self.days[-2:].set_color(weekend_color)

        self.add(self.blocks, self.days)





    




