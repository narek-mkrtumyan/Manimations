from calendar import calendar
from hashlib import new
from re import M
from manim import *
import numpy as np
import sys
sys.path.append('../')
from Functions.GeometryFunctions import *
from Objects.Objects import *
from Configs import *
from Functions.Board import *

# Մասերով խնդիրների համար ֆունկցիաներ


class SegmentEndmark(VMobject):
    def __init__(self, length=DEFAULT_ENDMARK_LENGTH, *args, **kwargs):
        VMobject.__init__(self)
        endmark = Line([0, length/2, 0], [0, -length/2, 0])

        self.add(endmark)


class Segment(VGroup):
    def __init__(self, 
        start=LEFT, end=RIGHT, color=WHITE, stroke_width=DEFAULT_STROKE_WIDTH, endmark_color=WHITE,
        text=False, position=UP
    ):

        VGroup.__init__(self)

        self.text = text
        self.position = position

        self.line = Line(start, end, color=color, stroke_width=stroke_width)

        self.endmark_left = SegmentEndmark(length=stroke_width / 20, color=endmark_color)
        self.endmark_left.next_to(self.line, LEFT, buff=0)

        self.endmark_right = SegmentEndmark(length=stroke_width / 20, color=endmark_color)
        self.endmark_right.next_to(self.line, RIGHT, buff=0)


        self.add(self.line, self.endmark_left, self.endmark_right)

        self.set_text(text)


    
    def set_text(self, new_text, scene=False):
        if scene:
            # self.remove(self.text)
            scene.play(ReplacementTransform(self.text, new_text.next_to(self.line.get_center(), self.position)))
        self.text = new_text.next_to(self.line.get_center(), self.position)
        self.add(self.text)
        


        



def cut_with_scissors(self, cut_coordinate=ORIGIN):

    cut_coordinate = np.array(cut_coordinate) - np.array([0.2, 0.4, 0])

    open_scissors = OpenScissors()
    closed_scissors = ClosedScissors()
    closed_scissors.move_to(cut_coordinate)
    open_scissors.move_to(cut_coordinate - np.array([0, 0.5, 0]))

    self.play(FadeIn(open_scissors))
    self.wait(0.25)
    self.play(open_scissors.animate().move_to(cut_coordinate))
    self.wait(0.25)
    self.remove(open_scissors)
    self.add(closed_scissors)
    self.wait(0.5)
    self.remove(closed_scissors)
    self.add(open_scissors)
    self.wait(0.25)
    self.play(open_scissors.animate().move_to(cut_coordinate - np.array([0, 0.5, 0])))
    self.wait(0.25)
    self.play(FadeOut(open_scissors))



def MergeSegments(segments, color=WHITE, endmark_color=WHITE, stroke_width=DEFAULT_STROKE_WIDTH,
    sum_mathtexs=Dot(radius=0), sum_position=UP
):
    combined_segment = Segment(
            segments[0][0][0].get_start_and_end()[0], segments[-1][0][0].get_start_and_end()[1], 
            mathtex=sum_mathtexs, position=sum_position, color=color, 
            endmark_color=endmark_color, stroke_width=stroke_width
        )
    return combined_segment


def PlayMergeSegments(self, segments, combined_segment):

    self.add(combined_segment[0])
    self.play(FadeOut(*[seg[0] for seg in segments]))
    self.play(ReplacementTransform(VGroup(*[seg[1] for seg in segments]), combined_segment[1]))






def MultiplySegment(self, segment, factor=2, direction=RIGHT, 
    merge_segments=False, sum_mathtexs=False, sum_position=UP, run_time=3
):
    '''
        Expends given segment by copy pasting it in a sequence

        Arguments - self, segment(variable that returns the Segment() function), factor(scale factor), direction(where to expend)

        Optional - merge_segments(after expending remove marks on the segment and leave only big segment), 
            sum_mathtexs(what to write after merging), sum_position(where to write new mathtex), run_time(whole time)
    '''
    unit_run_time = run_time / (factor - 1)

    segments = VGroup(segment)
    
    if factor == 2:
        segment_right_half = segment.copy()
        self.play(segment_right_half.animate(rate_func=linear, run_time=unit_run_time/3).shift(DOWN))
        self.play(segment_right_half.animate(
            rate_func=linear, run_time=unit_run_time/3).shift(direction*SegmentLength(segment[0][0]))
        )
        self.play(segment_right_half.animate(rate_func=linear, run_time=unit_run_time/3).shift(UP))

        segments.add(segment_right_half)

    else:
        next_segment = MultiplySegment(self, segment, 2, direction, False, False, UP, unit_run_time)[1]
        segments.add(
            *MultiplySegment(self, next_segment, factor-1, direction, False, False, UP, run_time - unit_run_time)
        )
    
    if merge_segments:
        combined_segment = MergeSegments(segments, sum_mathtexs=sum_mathtexs, sum_position=sum_position)
        PlayMergeSegments(self, segments, combined_segment)
        segments = combined_segment

    return segments    


def MultiplySegmentRotating(self, segment, factor=2, direction=RIGHT, color=GREEN, 
    merge_segments=False, sum_mathtexs=False, sum_position=UP, run_time=3
):
    '''
            Expends given segment by copy pasting it in a sequence by rotating

            Arguments - self, segment(variable that returns the Segment() function), factor(scale factor),
                        direction(where to expend), color(rotating semi_segment color)

            Optional -  merge_segments(after expending remove marks on the segment and leave only big segment),
                        sum_mathtexs(what to write after merging), sum_position(where to write new mathtex), run_time(whole time)

            Features -  sum_position must have the same orientation as mathtex in the source segment !!!!!!!
                        The function can be optimized by removing the segment_list (type list) - leaving only segments (type VGroup)
     '''

    ssegment = segment.copy()
    unit_run_time = run_time / (factor - 1)
    segment_list = []
    segments = VGroup(segment)

    if direction[0] == -1:
        a = sum_position[1] / abs(sum_position[1])
        k = 2
        rotate_direction = 1 * a
    else:
        a = sum_position[1] / abs(sum_position[1])
        k = 1
        rotate_direction = -1 * a

    for i in range(factor-1):
        segment_list.append(ssegment.copy())
        end = int((i + k) % 2)
        semi_segment = VGroup(segment_list[i][0][0].set_color(color), segment_list[i][0][2-end])
        self.play(
            Rotating(
                semi_segment, about_point=segment_list[i][0][0].get_start_and_end()[end], 
                radians= -rotate_direction * PI, run_time=unit_run_time
            ),
            segment_list[i][1].animate(rate_func=linear, run_time=unit_run_time).shift(direction * SegmentLength(segment_list[i][0][0]))
        )
        self.add(semi_segment.set_color(WHITE))
        ssegment = segment_list[i]
        segments.add(ssegment)

    if merge_segments:
        combined_segment = MergeSegments(segments, sum_mathtexs=sum_mathtexs, sum_position=sum_position)
        PlayMergeSegments(self, segments, combined_segment)
        segments = combined_segment

    return segments    



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
    


    def shift_weekdays(self, scene):

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







class test(Scene):
    def construct(self):

        def play_number_counter(n=1, m=2, center=ORIGIN, color=WHITE):
            numbers = VGroup(*[MathTex(rf'{i}', color=color) for i in range(n, m+1)])
            numbers.move_to(center).set_opacity(0).shift(0.5*UP)
            numbers[0].shift(0.5*DOWN)

            self.play(numbers[0].animate().set_opacity(1))

            for i in range(len(numbers) - 1):
                self.play(
                numbers[i].animate().shift(0.5*DOWN).set_opacity(0),
                numbers[i+1].animate().shift(0.5*DOWN).set_opacity(1)
            )

            return numbers[-1]



        # calendar = CalendarMonth(month=4, first_weekday=3).scale(2)

        # self.add(calendar)
        # self.wait()

        # calendar.next_month(self)

        we = Weight(2)

        self.play(Create(we))

        print(we.weight_value)

        



        
