from manim import *
import numpy as np
import sys
sys.path.append('../')

from Objects.Objects import *
from Configs import *

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
        self.__line_color = color

        self.text = text
        self.position = position

        self.line = Line(start, end, color=color, stroke_width=stroke_width)

        self.endmark_left = SegmentEndmark(length=stroke_width / 20, color=endmark_color)
        self.endmark_left.next_to(self.line, LEFT, buff=0)

        self.endmark_right = SegmentEndmark(length=stroke_width / 20, color=endmark_color)
        self.endmark_right.next_to(self.line, RIGHT, buff=0)

        #self.line.add_updater(lambda d: d.become(Line(self.endmark_left.get_center(),
        #                                                                   self.endmark_right.get_center())))

        self.add(self.line, self.endmark_left, self.endmark_right)

        self.set_text(text)


    
    def set_text(self, new_text, scene=False):
        if scene:
            # self.remove(self.text)
            scene.play(ReplacementTransform(self.text, new_text.next_to(self.line.get_center(), self.position)))
        if new_text:
            self.remove(self.text)
            self.text = new_text.next_to(self.line.get_center(), self.position)
            self.add(self.text)

    def set_text_updater(self):
        self.remove(self.text)
        self.text.add_updater(lambda d: d.next_to(self.line.get_center(), self.position))
        self.add(self.text)
    
    


    def set_line_updater(self):
        self.remove(self.line)
        self.line.add_updater(lambda d: d.become(Line(self.endmark_left.get_center(),
                                                                           self.endmark_right.get_center(), color = self.__line_color)))
        self.add(self.line)

    def remove_updater(self):
        self.remove(self.text)
        self.clear_updaters()
        self.add(self.text)


    ### Մասերով խնդրի մասերը :D
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

        

