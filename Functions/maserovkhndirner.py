from .qarakusiscene import *



class SegmentEndmark(VMobject):
    def __init__(
        self, 
        length=DEFAULT_ENDMARK_LENGTH, 
        *args, **kwargs
    ):
        VMobject.__init__(self)
        endmark = Line([0, length/2, 0], [0, -length/2, 0])

        self.add(endmark)


class Segment(VGroup):
    def __init__(
        self,
        start=LEFT,
        end=RIGHT,
        color=WHITE,
        stroke_width=DEFAULT_STROKE_WIDTH,
        endmark_color=WHITE,
        text=False,
        text_position=DEFAULT_SEGMENT_TEXT_POSITION,
        opacity = 1
    ):

        VGroup.__init__(self)
        self.opacity = opacity

        self.text = text
        self.text_position = text_position

        self.line = Line(start, end, color=color, stroke_width=stroke_width)

        self.endmark_left = SegmentEndmark(length=stroke_width / 20, color=endmark_color)
        self.endmark_left.next_to(self.line, LEFT, buff=0)

        self.endmark_right = SegmentEndmark(length=stroke_width / 20, color=endmark_color)
        self.endmark_right.next_to(self.line, RIGHT, buff=0)

        self.add(self.line, self.endmark_left, self.endmark_right)

        self.set_text(text)


    def set_text(
        self,
        new_text,
        scene : Scene = False
    ):
        if scene:
            if self.text:
                scene.play(ReplacementTransform(self.text, new_text.next_to(self, self.text_position)))
            else:
                self.text = new_text.next_to(self, self.text_position)
                scene.play(Write(self.text))
        if new_text:
            self.remove(self.text)
            self.text = new_text.next_to(self, self.text_position)
            self.add(self.text)


    def add_text_updater(self):
        if self.text:
            self.remove(self.text)
            self.text.add_updater(lambda d: d.next_to(self, self.text_position))
            self.add(self.text)
            self.add(self.text)

    def add_line_updater(self):
        self.remove(self.line)
        self.line.add_updater(
            lambda d: d.become(
                Line(
                    self.endmark_left.get_center(),
                    self.endmark_right.get_center(),
                    color = self.line.get_color()
                ).set_opacity(self.opacity)#.set_z_index(endmark.get_z_index_reference_point() - 1)
            )
        )
        self.add(self.line)


    def remove_updater(self):
        self.remove(self.text)
        self.clear_updaters()
    

    def set_superopacity(self, opacity):
        self.opacity = opacity



class SimpleTwoPartsProblem(VGroup):
    def __init__(
        self,
        name_1,
        name_2,
        extra_length,
        total_length,
        wanted,
        first_segment_start_point=[1, 1.5, 0],
        sum_of_lengths_of_segments=5,
        extra_segment_color=DEFAULT_EXTRA_SEGMENT_COLOR,
        counting_color=DEFAULT_COUNTING_COLOR,
        name_font_size=DEFAULT_NAME_FONT_SIZE,
        segment_length_font_size=DEFAULT_SEGMENT_LENGTH_FONT_SIZE,
        total_length_font_size=DEFAULT_TOTAL_LENGTH_FONT_SIZE,
        equation_font_size=DEFAULT_EQUATION_FONT_SIZE
    ):
        VGroup.__init__(self)

        self.wanted = wanted
        self.counting_color = counting_color

        equal_length = int((total_length - extra_length) / 2)
        scale_factor_of_segments = sum_of_lengths_of_segments / total_length
        
        equal_segment_length = equal_length * scale_factor_of_segments
        extra_segment_length = extra_length * scale_factor_of_segments

        class Drawing(VGroup):
            def __init__(self):
                VGroup.__init__(self)

                self.first_segment = Segment(
                        first_segment_start_point, 
                        np.array(first_segment_start_point) + np.array([equal_segment_length, 0, 0])
                    )

                self.second_segment = self.first_segment.copy().shift(1.5 * DOWN)

                self.extra_segment = Segment(
                    self.second_segment.endmark_right.get_center(),
                    self.second_segment.endmark_right.get_center() + np.array([extra_segment_length, 0, 0]),
                    color=extra_segment_color,
                    text=MathTex(f'{extra_length}', font_size=segment_length_font_size)
                )

                self.dashed_lines = VGroup(
                        DashedLine(self.first_segment.get_left(), self.second_segment.get_left()),
                        DashedLine(self.first_segment.get_right(), self.second_segment.get_right())
                    )
                
                self.second_segment_combined = Segment(
                            self.second_segment.endmark_left.get_center(),
                            self.extra_segment.endmark_right.get_center(),
                            text=MathTex(
                                f'{equal_length + extra_length}', 
                                font_size=segment_length_font_size
                            )
                        )

                self.first_name = Tex(name_1, tex_template=ARMTEX, font_size=name_font_size)
                self.first_name.next_to(self.first_segment, LEFT, buff=0.5)

                self.second_name = Tex(name_2, tex_template=ARMTEX, font_size=name_font_size)
                self.second_name.next_to(self.second_segment, LEFT, buff=0.5)

                self.brace = BraceLabel(
                    VGroup(self.first_segment, self.extra_segment), brace_direction=RIGHT, buff=1,
                    text=f'{total_length}', font_size=total_length_font_size
                )
                self.brace.brace.scale(1.2)

        class Solution(VGroup):
                def __init__(
                    self,
                    drawing : Drawing
                ):
                    VGroup.__init__(self)

                    self.total_minus_extra = MathTex(
                            '1)\ ', f'{total_length}', '-', f'{extra_length}', 
                            '=', f'{total_length - extra_length}', 
                            font_size=equation_font_size
                        )
                    self.total_minus_extra.next_to(drawing.second_segment, 5 * DOWN, aligned_edge=LEFT)
                    self.total_minus_extra[0].set_color(LIGHT_GRAY)

                    self.divide_by_two = MathTex(
                        '2)\ ', f'{total_length - extra_length}', ':', '2', 
                        '=', f'{equal_length}',
                        font_size=equation_font_size
                    )
                    self.divide_by_two.next_to(self.total_minus_extra, 1.5 * DOWN, aligned_edge=LEFT)
                    self.divide_by_two[3].set_color(counting_color)
                    self.divide_by_two[0].set_color(LIGHT_GRAY)

                    self.equal_length_plus_extra = MathTex(
                        '3)\ ', f'{equal_length}', '+', f'{extra_length}', 
                        '=', f'{equal_length + extra_length}',
                        font_size=equation_font_size
                    )
                    self.equal_length_plus_extra.next_to(self.divide_by_two, 1.5 * DOWN, aligned_edge=LEFT)
                    self.equal_length_plus_extra[0].set_color(LIGHT_GRAY)

                    self.count_one_part = MathTex(
                        '1', r'\textrm{ մաս}', 
                        font_size=equation_font_size, color=counting_color, tex_template=ARMTEX
                    )
                    self.count_one_part[0].move_to(self.divide_by_two[3].get_center())
                    self.count_one_part[1].next_to(self.count_one_part[0], RIGHT, buff=0.25)

                    self.first_segment_text = MathTex(f'{equal_length}', font_size=segment_length_font_size)
                    self.first_segment_text.next_to(drawing.first_segment, DEFAULT_SEGMENT_TEXT_POSITION)

                    self.second_segment_text = MathTex(f'{equal_length}', font_size=segment_length_font_size)
                    self.second_segment_text.next_to(drawing.second_segment, DEFAULT_SEGMENT_TEXT_POSITION)

                    self.first_rect = SurroundingRectangle(self.first_segment_text, GREEN, SMALL_BUFF + 0.05, 0.1)
                    self.second_rect = SurroundingRectangle(drawing.second_segment_combined.text, GREEN, SMALL_BUFF + 0.05, 0.1)

                    self.scissors = Scissors(drawing.second_segment.endmark_right.get_center())
        
        self.drawing = Drawing()
        self.solution = Solution(self.drawing)



