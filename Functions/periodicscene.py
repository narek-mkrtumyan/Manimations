from manim import *
import numpy as np
import sys
from Functions.GeometryFunctions import DistanceBetweenCoordinates
sys.path.append('../')
from Objects.Objects import *
from Configs import *



class CircularVGroup(VGroup):
    def __init__(self, *vmobjects, radius=1.5, first_item_angle=90, surrounding_rectangle_color=YELLOW, **kwargs):
        super().__init__(*vmobjects, **kwargs)
        self.add(*vmobjects)
    
        self.number_of_items = len(self)
        self.radius = radius
        self.first_item_angle = first_item_angle

        self.unit_angle = 360 / self.number_of_items

        self.circle = Circle(self.radius)

        small_circle = self.circle.copy().scale(0.995)

        self.paths = VGroup()
        for i in range(self.number_of_items):
            item_angle = first_item_angle - i * self.unit_angle
            self[i].move_to(self.circle.point_at_angle((item_angle % 360) * DEGREES))
        

        self.rectangles = VGroup(*[SurroundingRectangle(mob, color=surrounding_rectangle_color) for mob in self])
        self.arcs = VGroup()
        self.arrows = VGroup()

        for i in range(self.number_of_items):
            points_big_arc = []
            points_small_arc = []

            for j in range(20):
                points_big_arc.append(
                    self.circle.point_at_angle(
                        ((first_item_angle - (i + 1) * self.unit_angle + j * self.unit_angle / 20) % 360) * DEGREES
                    )
                )
            for j in range(20):
                points_small_arc.append(
                    small_circle.point_at_angle(
                        ((first_item_angle - i * self.unit_angle - j * self.unit_angle / 20) % 360) * DEGREES
                    )
                )

            closing_points = Line(points_small_arc[0], points_big_arc[-1]).points
            opening_points = Line(points_small_arc[-1], points_big_arc[0]).points

            points = [
                *opening_points,
                *points_big_arc,
                *closing_points,
                *points_small_arc
            ]

            filled_arc = Difference(
                VMobject().set_points_smoothly(points).set_fill(WHITE, 1),
                Union(*[rect.copy().set_fill(opacity=1).set_stroke(WHITE) for rect in self.rectangles])
            ).set_fill(WHITE, 1)

            arc_start_and_end = [filled_arc.points[int(len(filled_arc.points)/2)], filled_arc.points[0]]


            arc = ArcBetweenPoints(arc_start_and_end[1], arc_start_and_end[0], radius=self.radius).reverse_direction()
            arrow = CurvedArrow(arc_start_and_end[0], arc_start_and_end[1], radius=-self.radius)

            if sum((arc.get_arc_center() - ORIGIN)**2) > 1:
                arc = ArcBetweenPoints(arc_start_and_end[0], arc_start_and_end[1], radius=self.radius).reverse_direction()
                arrow = CurvedArrow(arc_start_and_end[1], arc_start_and_end[0], radius=-self.radius)
            
            path = ArcBetweenPoints(
                self.circle.point_at_angle(((first_item_angle - i * self.unit_angle) % 360) * DEGREES),
                self.circle.point_at_angle(((first_item_angle - (i + 1) * self.unit_angle) % 360) * DEGREES),
                radius=self.radius
            ).reverse_direction()

            if sum((path.get_arc_center() - ORIGIN)**2) > 1:
                path = ArcBetweenPoints(
                    self.circle.point_at_angle(((first_item_angle - (i + 1) * self.unit_angle) % 360) * DEGREES),
                    self.circle.point_at_angle(((first_item_angle - i * self.unit_angle) % 360) * DEGREES),
                    radius=self.radius
                ).reverse_direction()

            self.arcs.add(arc)
            self.arrows.add(arrow)
            self.paths.add(path)
        
        self.vmobjects = VGroup(*self, *self.arcs, *self.arrows, *self.paths, *self.rectangles, self.circle)




        


class Week(VMobject):
    def __init__(
        self, 
        first_weekday=1, 
        full_width=2.45,
        weekend_color=RED
        ):
        VMobject.__init__(self)
        self.blocks = VGroup(
                *[Rectangle(height=full_width * 5 / 49, width=full_width/7, stroke_width=1) for i in range(7)]
            )
        self.blocks.arrange(buff=0)

        days = MathTex(*[r'\textrm{' + day + r'}' for day in WEEK_DAYS_ARM], font_size=20, tex_template=armenian_tex_template)
        days[-2:].set_color(weekend_color)

        self.days = VGroup(*days[first_weekday - 1:], *days[:first_weekday - 1])
        for i in range(7):
            self.days[i].move_to(self.blocks[i].get_center())

        self.add(self.blocks, self.days)


class CalendarMonth(VMobject):
    def __init__(
        self,
        style='normal', # 'line'
        year=2022, 
        month=1, 
        first_weekday=1, 
        weekend_color=RED, 
        extra_days_opacity=0.3, 
        background_color=YELLOW_E
    ):
        VMobject.__init__(self)

        self.year = year
        self.month =  month
        self.first_weekday = first_weekday
        self.extra_days_opacity = extra_days_opacity
        self.background_color = background_color
        self.weekend_color = weekend_color

        if year % 4 == 0 and month == 2:
            self.number_of_days = 28   
        else:
            self.number_of_days = MONTHS_LENGTHS[month - 1]

        if style == 'normal':
            outline_height = 2.9
            outline_width = 7 * WEEK_BLOCK_WIDTH
        
        if style == 'line':
            outline_height = 1.5
            outline_width = 2.45 / 7 * self.number_of_days

        self.outline = Rectangle(WHITE, outline_height, outline_width)
        
        self.background = VGroup()
        self.background.add(Rectangle(height=0.75, width=outline_width).set_stroke(width=0).set_fill(background_color, 0.5))
        self.background[0].next_to(ORIGIN + np.array([[0, outline_height / 2, 0]]), DOWN, buff=0)

        self.VMyear = MathTex(rf'{year}', font_size=25)
        self.VMyear.next_to(self.outline, UP).shift(0.55 * DOWN)

        self.VMmonth = MathTex(r'\textrm{' + MONTHS_ARM[month - 1] + r'}', font_size=25, tex_template=armenian_tex_template)
        self.VMmonth.next_to(self.VMyear, DOWN, buff=0.15)

        self.background.add(
            MathTex('<<', font_size=20).move_to(self.VMmonth.get_center()).shift(0.9 * LEFT),
            MathTex('>>', font_size=20).next_to(self.VMmonth.get_center()).shift(0.5 * RIGHT)
        )
        

        if style == 'normal':
            
            week = Week(full_width=outline_width, weekend_color=weekend_color).next_to(self.background, DOWN, buff=0)
            self.week_blocks = week.blocks
            self.week_days = week.days
            
            if year % 4 == 0 and month == 3:
                number_of_days_in_previous_month = 28
            elif month == 1:
                number_of_days_in_previous_month = 31
            else:
                number_of_days_in_previous_month = MONTHS_LENGTHS[month - 2]

            if first_weekday == 1:
                extra_days_from_start = np.array([])
            else:
                extra_days_from_start = np.arange(
                        number_of_days_in_previous_month - first_weekday + 2, number_of_days_in_previous_month + 1
                    )

            extra_days_till_end = np.arange(1, (7 - (len(extra_days_from_start) + self.number_of_days % 7)) % 7 + 1)

            days_list = np.arange(1, self.number_of_days + 1)

            full_list_of_days = np.concatenate([extra_days_from_start, days_list, extra_days_till_end])
            self.number_of_rows = int(len(full_list_of_days) / 7)

            self.full_days = VGroup(*[MathTex(fr'{int(day)}', font_size=19) for day in full_list_of_days])
            self.full_days.arrange_in_grid(cols=7, buff=0.17)
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

            self.add(
                self.outline,
                self.background,
                self.VMyear,
                self.VMmonth,
                self.week_days,
                self.week_blocks,
                self.days,
                self.extra_days
            )
        
        if style == 'line':
            
            self.week_blocks = VGroup(
                *[Rectangle(height=WEEK_BLOCK_HEIGHT, width=WEEK_BLOCK_WIDTH, stroke_width=1) for i in range(self.number_of_days)]
            )
            self.week_blocks.arrange(buff=0).next_to(self.background, DOWN, buff=0)

            self.week_days = VGroup()

            weekdays = MathTex(*[r'\textrm{' + day + r'}' for day in WEEK_DAYS_ARM * 6], font_size=20, tex_template=armenian_tex_template)
            for i in range(len(weekdays)):
                if (i + 1) % 7 == 0 or (i + 2) % 7 == 0:
                    weekdays[i].set_color(self.weekend_color)
            self.week_days = VGroup(*weekdays[first_weekday - 1 : first_weekday - 1 + self.number_of_days])
            
            self.days = VGroup(*[MathTex(fr'{int(i + 1)}', font_size=19) for i in range(self.number_of_days)])
            print(len(self.days), len(self.week_days))
            for i in range(len(self.days)):
                self.days[i].set_color(self.week_days[i].get_color())

            for i in range(self.number_of_days):
                self.week_days[i].move_to(self.week_blocks[i].get_center())
                self.days[i].next_to(self.week_blocks[i], DOWN, buff=0.15)


            self.add(
                self.outline,
                self.background,
                self.VMyear,
                self.VMmonth, 
                self.week_blocks,
                self.week_days,
                self.days
            )


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
        pass


def cyclic_shift(
    scene: Scene,
    vgroup: VGroup,
    steps = 1,
    direction = RIGHT,
    fade_in_and_out = True,
    rate_func = linear,
    run_time=1
):

    unit_distance = DistanceBetweenCoordinates(vgroup[0].get_center(), vgroup[1].get_center())
    unit_run_time = run_time / steps

    if steps == 1:
        new_vgroup = VGroup(
                vgroup[-1].copy(),
                *vgroup[:-1].copy()
            )
        
        for i in range(len(vgroup)):
            new_vgroup[i].move_to(vgroup[i].get_center())
        new_vgroup[0].shift(-unit_distance * direction).set_opacity(0)
        
        if fade_in_and_out:
            scene.play(
                *[
                    ReplacementTransform(vgroup[i], new_vgroup[i + 1], rate_func=rate_func, run_time=unit_run_time)
                    for i in range(len(vgroup) - 1)
                ],
                vgroup[-1].animate(rate_func=rate_func, run_time=unit_run_time).shift(unit_distance * direction).set_opacity(0),
                new_vgroup[0].animate(rate_func=rate_func, run_time=unit_run_time).shift(unit_distance * direction).set_opacity(1),
            )
        return  new_vgroup

    else:
        for i in range(steps):
            vgroup = cyclic_shift(scene, vgroup, 1, direction, fade_in_and_out, rate_func, unit_run_time)
        return vgroup
    



# class PeriodicScene(Scene):
#     def __init__(self, renderer=None, camera_class=..., always_update_mobjects=False, random_seed=None, skip_animations=False):
#         super().__init__(renderer, camera_class, always_update_mobjects, random_seed, skip_animations)
    
#     def indicate_





