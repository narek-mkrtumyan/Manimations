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

# Կամյական խնդրի ձևակերպում
class Task(VGroup):
    def __init__(self,
                 number: MathTex,
                 text: VGroup,
                 **kwargs):
        VGroup.__init__(self)

        self.number = number.set_color(YELLOW)
        self.text = text.arrange(DOWN, aligned_edge=LEFT)
        #self = VGroup(Task.number, Task.text).arrange(RIGHT, aligned_edge=UP)

        self.add(self.number, self.text)
        self.arrange(RIGHT, aligned_edge=UP)

    def up(self,
           scene: Scene):
        [x_number_0, y_number_0, z_number_0] = self.number.get_center()
        [x_text_0, y_text_0, z_text_0] = self.text.get_center()
        y_up_number_0 = self.number.get_edge_center(UP)[1]
        y_up_text_0 = self.text.get_edge_center(UP)[1]
        [x_number_1, y_number_1, z_number_1] = [-6, 24/7, 0]
        [x_text_1, y_text_1, z_text_1] = [x_text_0, 24/7 + (y_up_number_0 - y_number_0) - (y_up_text_0 - y_text_0), z_text_0]
        def go_up(self, t):
            pos_number = [x_number_0 * (1-t) + x_number_1 * t,
                          y_number_0 * (1-t) + y_number_1 * t,
                          z_number_0 * (1-t) + z_number_1 * t]
            self.number.move_to(pos_number).set_opacity(1-t/2)
            pos_text = [x_text_0 * (1-t) + x_text_1 * t,
                        y_text_0 * (1-t) + y_text_1 * t,
                        z_text_0 * (1-t) + z_text_1 * t]
            self.text.move_to(pos_text).set_opacity(1-t/3)

        scene.play(UpdateFromAlphaFunc(self, go_up))

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
            scene.play(ReplacementTransform(self.text, new_text.next_to(self.line.get_center(), self.position)))
        self.text = new_text.next_to(self.line.get_center(), self.position)
        self.add(self.text)


    ### Մասերով խնդր մասերը :D
class Diagram(VGroup):
    def __init__(self,
                 parts: List[List],
                 names: List[MathTex or DecimalNumber],
                 brace: bool = False,
                 total: MathTex or DecimalNumber = MathTex(r'.', font_size=1),
                 **kwargs):
        VGroup.__init__(self)
        assert len(parts) == len(names), "Length of 'parts' must match length of 'names'"

        players_number = len(parts)
        self.player = parts.copy()
        self.player_name = names.copy()
        self.list = parts
        for i in range(players_number):
            self.player[i] = [0 for _ in parts[i]]
            pointer = 0
            for j in range(len(parts[i])):

                if parts[i][j][0] % 100 == 0:
                    self.player[i][j] = Segment(start=[pointer, players_number/2 - i, 0],
                                                end= [pointer + parts[i][j][0]/1000, players_number/2 - i, 0],
                                                text= parts[i][j][1])
                else:
                    self.player[i][j] = Segment(start=[pointer, players_number/2 - i, 0],
                                                end= [pointer + parts[i][j][0]/1000, players_number/2 - i, 0],
                                                text= parts[i][j][1], color = ORANGE)
                pointer += parts[i][j][0]/1000
                self.add(self.player[i][j])
            self.player_name[i].move_to([-1, players_number/2 - i, 0], aligned_edge=RIGHT)
            self.add(self.player_name[i])

        #self.brace = brace
        if brace:
            self.brace = Brace(VGroup(*[ VGroup(*self.player[i]) for i in range(players_number)]),  RIGHT, buff=0.5)
            self.total = total.next_to(self.brace, RIGHT, buff=0.5)
            self.add(self.brace, self.total)
      

    def create_by_copying(self,
                          scene: Scene,
                          coping_list: List[List]):
        assert len(coping_list) == len(self.player), "Length of 'coping_list' must match length of 'self.player'"
        scene.play(AnimationGroup(*[Write(i) for i in self.player_name], lag_ratio=0.5))
        for i in range(len(self.player)):
            assert len(coping_list[i]) == len(self.player[i]), f"Length of 'coping_list[{i}]' must match length of 'self.player[{i}]'"
            for j in range(len(self.player[i])):
                if coping_list[i][j] == 0:
                    scene.play(Create(self.player[i][j].line),
                               Create(self.player[i][j].endmark_left),
                               Create(self.player[i][j].endmark_right), run_time = 0.7)
                    if self.player[i][j].text:
                        scene.play(Write(self.player[i][j].text), run_time = 0.5)
                else:
                    verifying = True
                    for k in range(i+1):
                        for l in range(len(self.player[k])):
                            if coping_list[i][j] == coping_list[k][l]:
                                scene.play(ReplacementTransform(self.player[k][l].copy(), self.player[i][j]))
                                verifying = False
                                break
                        if not verifying:
                            break

                    if verifying:
                        scene.play(Create(self.player[i][j].line),
                                   Create(self.player[i][j].endmark_left),
                                   Create(self.player[i][j].endmark_right), run_time = 0.7)
                        if self.player[i][j].text:
                            scene.play(Write(self.player[i][j].text), run_time = 0.5)
        if self.brace:
            scene.play(Create(self.brace))
            scene.play(Write(self.total))
    
    def create_by_order_and_steps(self,
                                  scene: Scene,
                                  order: List[int],
                                  steps: List[List[int]]):
        #
        #segments must be numbered for each "player", Segments with numbers 0 will not be copied. and the rest will be according to matching numbers
        #
        assert len(order) == len(self.player) and len(steps) == len(self.player), "Length of 'order' and 'steps' must match length of 'self.player'"
        interation_number = max([len(i) for i in steps])
        scene.play(AnimationGroup(*[Write(self.player_name[i]) for i in order], lag_ratio=0.5))
        for i in range(interation_number):
            for j in order:
                if i < len(steps[j]):
                    if i == 0:
                        ran = range(steps[j][i])
                    else:
                        ran = range(steps[j][i-1], steps[j][i])
                    for k in ran:
                        scene.play(Create(self.player[j][k].line),
                                   Create(self.player[j][k].endmark_left),
                                   Create(self.player[j][k].endmark_right), run_time = 0.7)
                        if self.player[j][k].text:
                            scene.play(Write(self.player[j][k].text), run_time = 0.5)
                    scene.wait()
        if self.brace:
            scene.play(Create(self.brace))
            scene.play(Write(self.total))
    def animate_superscale(self,
                           scene: Scene,
                           scale_ratio: float,
                           move_to_point: List[float] = [0, 0, 0]):
        self.generate_target()
        self.target.scale(scale_ratio)
        for name in self.target.player_name:
            name.shift((scale_ratio -1) * RIGHT).scale(1/scale_ratio)
        for player in self.target.player:
            for segment in player:
                if segment.text:
                    segment.text.scale(1/scale_ratio).next_to(segment.line.get_center(), segment.position)
                segment.endmark_left.scale(1/scale_ratio)  
                segment.endmark_right.scale(1/scale_ratio)
        self.target.move_to(move_to_point)
        scene.play(MoveToTarget(self))

    def show_equal_parts(self,
                         scene: Scene,
                         equal_list: List[int]):
        assert len(equal_list) == len(self.player), "Length of 'equal_parts' must match length of 'self.player'"
        for i in range(len(self.player)):
            assert len(equal_list[i]) == len(self.player[i]), f"Length of 'equal_parts[{i}]' must match length of 'self.player[{i}]'"
            for j in range(len(self.player[i])):
                if equal_list[i][j] != 0:
                    verifying = True
                    for k in range(i+1):
                        for l in range(len(self.player[k])):
                            if equal_list[i][j] == equal_list[k][l]:
                                if i != k:
                                    scene.play(ReplacementTransform(self.player[k][l].copy().set_color(YELLOW), self.player[i][j]))
                                    verifying = False
                                    break
                                else:
                                    segment_copy = self.player[k][l].copy().set_color(YELLOW)
                                    
                                    scene.play(segment_copy.animate.next_to(VGroup(segment_copy, self.player[i][j]), UP), run_time = 0.5, rate_func = rush_into)
                                    scene.play(ReplacementTransform(segment_copy, self.player[i][j]), run_time = 0.5, rate_func = rush_from)
                                    verifying = False
                                    break

                        if not verifying:
                            break

    def segment_perpendicular_projection(self,
                           scene: Scene,
                           project_from: List[int],
                           project_to: int,
                           add: bool = False,
                           subtract: bool = False,
                           replace: bool = False):
        p_left = [0, 0, 0]
        p_left[0] = self.player[project_from[0]][project_from[1]].endmark_left.get_center()[0]
        p_left[1] = self.player[project_to][0].endmark_left.get_center()[1]
        d_left = DashedLine(self.player[project_from[0]][project_from[1]].endmark_left.get_center(),
                            p_left)


        p_right = [0, 0, 0]
        p_right[0] = self.player[project_from[0]][project_from[1]].endmark_right.get_center()[0]
        p_right[1] = self.player[project_to][0].endmark_right.get_center()[1]
        d_right = DashedLine(self.player[project_from[0]][project_from[1]].endmark_right.get_center(),
                             p_right)
        new_line = Line(p_left, p_right, color=self.player[project_from[0]][project_from[1]].line.get_color())
        
        
        self.generate_target()
        self.target.set_opacity(0.35)
        #self.target.player[project_from[0]][project_from[1]].set_opacity(1)
        scene.play(MoveToTarget(self))
        scene.play(Create(d_left), Create(d_right), FadeIn(new_line, run_time = 1.5))
        scene.wait(2)
        if replace:
            verifying = False
            to_remove = VGroup()
            cut_segment_start_numbe: int
            cut_segment_end_numbe: int
            for i in range(len(self.player[project_to])):
                #if abs(p_left - segment.endmark_left.get_center()[0]) < 0.1:
                segment = self.player[project_to][i]

                if verifying:
                    to_remove.add(segment)
                    self.remove(segment)
                    #self.player[project_to].pop(i)
               
                if segment.endmark_right.get_center()[0] > p_left[0] - 0.1 and not verifying:
                   
                    to_remove.add(segment)
                    ##TODO
                    self.remove(segment)
                    cut_segment_start_number = i
                    
                    if abs(p_left[0] - segment.endmark_right.get_center()[0]) < 0.1:
                        color = segment.line.get_color()
                        text = segment.text
                    else:
                        color = ORANGE
                        text = False
                        #color=self.player[project_from[0]][project_from[1]].line.get_color()
                    left_segment = Segment(segment.endmark_left.get_center(), p_left, color=color, text=text)
                    self.player[project_to][i] = left_segment
                    self.add(self.player[project_to][i])
                    
                    

                    if i == len(self.player[project_to])-1:
                        new_segment = Segment(p_left, p_right, color=self.player[project_from[0]][project_from[1]].line.get_color())
                        self.player[project_to].append(new_segment)
                        self.add(self.player[project_to][i+1])
                        cut_segment_end_number = i
                        
                    else:
                        if segment.endmark_right.get_center()[0] > p_right[0] - 0.1:
                            new_segment = Segment(p_left, p_right, color=self.player[project_from[0]][project_from[1]].line.get_color())
                            self.player[project_to].insert(i+1, new_segment)
                            self.add(self.player[project_to][i+1])
                            right_segment = Segment(p_right, segment.endmark_left.get_center(), color=ORANGE)
                            self.player[project_to].insert(i+2, right_segment)
                            cut_segment_end_number = i
                            break                             

                    verifying = True


                if segment.endmark_right.get_center()[0] > p_right[0] + 0.1 and verifying:

                    to_remove.add(segment)
                    cut_segment_end_number = i
                    ##TODO
                    self.remove(segment)
                    
                    if abs(p_right[0] - segment.endmark_left.get_center()[0]) < 0.1:
                        color = segment.line.get_color()
                        text = segment.text
                    
                    else:
                        color = ORANGE
                        text = False
                        #color=self.player[project_from[0]][project_from[1]].line.get_color()
                    new_segment = Segment(p_left, p_right, color=self.player[project_from[0]][project_from[1]].line.get_color())
                    right_segment = Segment(p_right, segment.endmark_right.get_center(), color=color, text=text)
                    self.player[project_to][cut_segment_start_number + 1] = new_segment
                    self.add(self.player[project_to][cut_segment_start_number + 1])
                    if i == len(self.player[project_to]):
                        self.player[project_to].append(right_segment)
                        self.add(self.player[project_to][-1])

                    else:
                        self.player[project_to].insert(cut_segment_start_number + 2, right_segment)
                        self.add(self.player[project_to][cut_segment_start_number + 2])

                    break
            for i in range(cut_segment_start_number + 3, len(self.player[project_to])):
                self.player[project_to].pop(i)

        scene.play(Uncreate(d_left), Uncreate(d_right), FadeOut(new_line, run_time = 1.5), self.animate.set_opacity(1))        

    def update_segment_text(self,
                            segment_index: List[int],
                            text: MathTex or DecimalNumber):
        [i, j] = segment_index
        self.remove(self.player[i][j])
        self.player[i][j].set_text(text)
        self.add(self.player[i][j])
        


        



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







class test(Scene):
    def construct(self):

        def play_number_counter(n=1, m=2, center=ORIGIN, color=WHITE):
            numbers = VGroup(*[MathTex(rf'{i}', color=color) for i in range(n, m+1)])
            numbers.move_to(center).set_opacity(0).shift(0.5*UP)
            numbers[0].shift(0.5*DOWN)

            self.play(numbers[0].animate().set_opacity(1), rate_func=linear)

            for i in range(len(numbers) - 1):
                self.play(
                numbers[i].animate().shift(0.5*DOWN).set_opacity(0),
                numbers[i+1].animate().shift(0.5*DOWN).set_opacity(1)
            )

            return numbers[-1]

    




