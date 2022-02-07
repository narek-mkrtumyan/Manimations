from turtle import width
from manim import *
import numpy as np
import sys
from colour import Color
sys.path.append("../../../")
sys.path.append("../../")
sys.path.append("../")
from Functions.GeometryFunctions.GeometryFunctions import *



left_bound = Line([-3.5, 5, 0], [-3.5, -5, 0])
right_bound = Line([3.5, 5, 0], [3.5, -5, 0])
bounds = VGroup(left_bound, right_bound)

armenian_tex_template = TexTemplate()
armenian_tex_template.add_to_preamble(r"\usepackage{armtex}")

# ANIMAL SVGs or PNGs
# RABBIT = SVGMobject('/SVG_PNG_files/rabbit.svg').set_color(WHITE).scale(0.55)
# PIGEON = SVGMobject('/SVG_PNG_files/pigeon.svg').set_color(WHITE).scale(0.5)

# CAGE_SQUARE = SVGMobject('Functions/SVG_PNG_files/cage_square.svg').set_color(GOLD).scale(1.5)
# CAGE_BIRD = ImageMobject('../Functions/SVG_PNG_files/cage_bird.png').set_color(GOLD).scale(0.5)

# SMOOTH_THINKING_BUBBLE_LEFT_1 = ImageMobject('../Functions/SVG_PNG_files/smooth_thinking_bubble_left_1.png').set_color(WHITE).scale(0.5)
# SMOOTH_THINKING_BUBBLE_RIGHT_1 = ImageMobject('../Functions/SVG_PNG_files/smooth_thinking_bubble_right_1.png').set_color(WHITE).scale(0.5)

# SMOOTH_THINKING_BUBBLE_LEFT_2 = ImageMobject('../Functions/SVG_PNG_files/smooth_thinking_bubble_left_2.png').set_color(WHITE).scale(0.5)
# SMOOTH_THINKING_BUBBLE_RIGHT_2 = ImageMobject('../Functions/SVG_PNG_files/smooth_thinking_bubble_right_2.png').set_color(WHITE).scale(0.5)

# THINKING_BUBBLE_LEFT_1 = ImageMobject('../Functions/SVG_PNG_files/thinking_bubble_left_1.png').set_color(WHITE).scale(0.5)
# THINKING_BUBBLE_RIGHT_1 = ImageMobject('../Functions/SVG_PNG_files/thinking_bubble_right_1.png').set_color(WHITE).scale(0.5)

# THINKING_BUBBLE_LEFT_2 = ImageMobject('../Functions/SVG_PNG_files/thinking_bubble_left_2.png').set_color(WHITE).scale(0.6)
# THINKING_BUBBLE_RIGHT_2 = ImageMobject('../Functions/SVG_PNG_files/thinking_bubble_right_2.png').set_color(WHITE).scale(0.6)


# open_scissors = SVGMobject('../Functions/SVG_PNG_files/open_scissors.svg')
# open_scissors.set_color(WHITE).rotate(PI/10).scale(0.5)
# closed_scissors = ImageMobject('SVG_PNG_files/closed_scissors.png')
# closed_scissors.set_color(WHITE).scale(0.13).shift(0.1*DOWN).rotate(PI/5)



# Մասերով խնդիրների համար ֆունկցիաներ

DEFAULT_ENDMARK_LENGTH = 0.2
DEFAULT_COUNTING_COLOR = ORANGE


def Endmark(length=DEFAULT_ENDMARK_LENGTH, color=WHITE):
    return Line([0, length/2, 0], [0, -length/2, 0], color=color)


def Segment(start=[-1, 0, 0], end=[1, 0, 0], mathtex=False, position=UP,
    color=WHITE, endmark_color=WHITE, stroke_width=DEFAULT_STROKE_WIDTH):
    '''
        Returns a segment with endmarks and a label in the middle

        Arguments - start, end, mathtex(Mathtex('')), position(for mathtex), colors for line, endmarks, mathtex
    '''

    endmark_length = stroke_width / 20

    AB = Line(start, end, color=color, stroke_width=stroke_width)

    endmark_1 = AB.copy().set_color(endmark_color).scale(endmark_length / DistanceBetweenCoordinates(start, end))
    endmark_1.set_stroke(width=DEFAULT_STROKE_WIDTH)
    endmark_1.move_to(start).rotate(PI/2)

    endmark_2 = AB.copy().set_color(endmark_color).scale(endmark_length / DistanceBetweenCoordinates(start, end))
    endmark_2.set_stroke(width=DEFAULT_STROKE_WIDTH)
    endmark_2.move_to(end).rotate(PI/2)

    line = VGroup(AB, endmark_1, endmark_2)

    if mathtex:
        mathtex.next_to(line.get_center(), position * 2)
        return VGroup(line, mathtex)

    else:
        mathtex = MathTex('.', font_size=1)
        mathtex.next_to(line.get_center(), position * 2)
        return VGroup(line, mathtex)


def cut_with_scissors(self, open_scissors, closed_scissors, cut_coordinate=ORIGIN):
    '''
        At first, you have to init this variables - 

        open_scissors = SVGMobject('ROOT/Functions/SVG_PNG_files/open_scissors.svg')

        open_scissors.set_color(WHITE).rotate(PI/10).scale(0.5)

        closed_scissors = ImageMobject('ROOT/Functions/SVG_PNG_files/closed_scissors.png')
        
        closed_scissors.set_color(WHITE).scale(0.13).shift(0.1*DOWN).rotate(PI/5)
    '''
    cut_coordinate = np.array(cut_coordinate) - np.array([0.2, 0.4, 0])

    self.play(FadeIn(open_scissors.move_to(cut_coordinate - np.array([0, 0.5, 0]))))
    self.wait(0.25)
    self.play(open_scissors.animate().move_to(cut_coordinate))
    self.wait(0.25)
    self.remove(open_scissors)
    self.add(closed_scissors.move_to(cut_coordinate - np.array([0.1, 0.1, 0])))
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
        combined_segment = Segment(
                segment[0][0].get_start_and_end()[int((rotate_direction * a +1)/2)], 
                segment_list[-1][0][0].get_start_and_end()[int((factor + int((rotate_direction* a+1)/2) )% 2)],
                mathtex=sum_mathtexs, position=sum_position, color=segment[0][0].get_color()
            )
        self.add(combined_segment[0])
        self.play(FadeOut(*[seg[0] for seg in segment_list]), FadeOut(segment[0]))
        self.play(ReplacementTransform(VGroup(*[seg[1] for seg in segments]), combined_segment[1]))
        segments = combined_segment

    return segments




class Scissors:
    def __init__(self, cut_point):
        self.cut_point = cut_point
        scissor_1 = SVGMobject('../../../Functions/siz.svg').set_color(WHITE)
        scissor_2 = SVGMobject('../../../Functions/siz2.svg').set_color(WHITE)
        dot = Dot().scale(0.2)
        self.__p_end = [a + b for a, b in zip([0, -0.35, 0], cut_point)]
        VGroup(scissor_1, scissor_2).arrange(RIGHT, buff=0.1)
        scissor_1.shift(0.08 * DOWN + 0.6 * RIGHT)
        scissor_2.shift(0.08 * DOWN - 0.6 * RIGHT)
        scissors_with_dot = VGroup(scissor_1, scissor_2, dot).scale(0.5)
        point = scissors_with_dot[2].get_center()
        scissors_with_dot[0].rotate(angle=-0.02, about_point=point)
        scissors_with_dot[1].rotate(angle=0.02, about_point=point)
        scissors_with_dot.move_to(self.__p_end)
        scissors_with_dot.shift(DOWN)
        self.siz = scissors_with_dot


    def cut_in(self, screen):

        def cut_with_scissors(mobject, t):
            dt = 1/60
            dl= [0, 1/60, 0]
            if t < 1/2:
                angle = PI / 6 * dt
            else:
                angle = -PI / 6 * dt
            #p_end = [a+b for a, b in zip([0, -0.25, 0], mobject[3].get_center())]
            mobject.shift(dl)
            point = mobject[2].get_center()
            mobject[0].rotate(angle=angle, about_point=point)
            mobject[1].rotate(angle=-angle, about_point=point)
        screen.play(UpdateFromAlphaFunc(self.siz, cut_with_scissors, run_time=1, rate_func=linear))
        self.siz.move_to(self.__p_end)

    def cut_out(self, screen):
        def cut_with_scissors(mobject, t):
            dt = 1/60
            dl = [0, -1/60, 0]
            angle = PI / 6 * dt
            mobject.shift(dl)
            point = mobject[2].get_center()
            color = Color(hue=1, saturation=t/3, luminance=1-t)
            mobject.set_color(color)
            mobject[0].rotate(angle=angle, about_point=point)
            mobject[1].rotate(angle=-angle, about_point=point)
        screen.play(UpdateFromAlphaFunc(self.siz, cut_with_scissors, run_time=1, rate_func=linear))
        screen.remove(self.siz)







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
            

        last_number = play_number_counter(1, 5)

