from manim import *
import numpy as np

from Objects.Objects import *
from Configs import *




# Կամյական խնդրի ձևակերպում
class Task(VGroup):
    def __init__(
        self,
        number: MathTex,
        text: VGroup,
        **kwargs
    ):
        VGroup.__init__(self)

        self.number = number.set_color(YELLOW)
        self.text = text.arrange(DOWN, aligned_edge=LEFT)

        self.add(self.number, self.text.align_to(self.number, UP))
        self.arrange(RIGHT, aligned_edge=UP)




# doesn't work yet
class CounterInteger(VMobject): 
    def __init__(self, n=1, font_size=DEFAULT_EQUATION_FONT_SIZE, color=WHITE):
        VMobject.__init__(self)

        self.value = n
        self.font_size = font_size
        self.color = color

        self.count = Tex(f'{n}', font_size=font_size, color=color)

        self.add(self.count)

    
    def update_value(self, amount=1):
        self.value += amount
        coord = self.tex.get_center()
        self.remove(self.tex)
        self.tex = Tex(f'{self.value}', font_size=self.font_size, color=self.color)
        self.tex.move_to(coord)
        self.add(self.tex)


def CountNextFunction(
    count : CounterInteger,
    buff=MED_LARGE_BUFF,
    run_time=DEFAULT_WAIT_TIME,
    rate_func=smooth,
    style='up_down'
):
    new_count = CounterInteger(count.value + 1, count.font_size, count.color)
    new_count.move_to(count.get_center()).set_opacity(0)

    copy_count = count.copy()


    if style == 'up_down':

        anim_group = AnimationGroup(
            AnimationGroup(
                Transform(new_count.copy().shift(UP * buff), new_count.copy().set_opacity(1), remover=True),
                Transform(count.copy(), count.copy().shift(DOWN * buff).set_opacity(1), remover=True)
            ),
            Transform(count, new_count.set_opacity(1)),
            lag_ratio=1
        )

        count.update_value(1)

        anim_group = AnimationGroup(
            count.animate.shift(DOWN * buff).set_opacity(0),
            new_count.animate.shift(DOWN * buff).set_opacity(1),
            run_time = run_time, rate_func=rate_func
        )
        count = new_count

    return anim_group


# class CountNext(AnimationGroup):
#     def __init__(
#         self,
#         count : CounterInteger,
#         buff=MED_LARGE_BUFF,
#         run_time=DEFAULT_WAIT_TIME,
#         rate_func=smooth,
#         style='up_down'
#     ):
#         AnimationGroup.__init__(self)

#         new_count = CounterInteger(count.value + 1, count.font_size, count.color)
#         new_count.move_to(count.get_center()).set_opacity(0)

#         if style == 'up_down':
#             new_count.shift(UP * buff)
#             self = AnimationGroup(
#                 count.animate.shift(RIGHT * buff).set_opacity(0),
#                 new_count.animate.shift(RIGHT * buff).set_opacity(1),
#                 run_time = run_time, rate_func=rate_func
#             )






class QarakusiScene(Scene):

    def write_task(
        self,
        task : Task,
        run_time=7
    ):
        self.play(Write(task.number))
        self.play(Write(task.text, run_time=run_time))

    

    def move_task_up(
        self,
        task : Task
    ):
        [x_number_0, y_number_0, z_number_0] = task.number.get_center()
        [x_text_0, y_text_0, z_text_0] = task.text.get_center()
        y_up_number_0 = task.number.get_edge_center(UP)[1]
        y_up_text_0 = task.text.get_edge_center(UP)[1]
        [x_number_1, y_number_1, z_number_1] = [-6, 24/7, 0]
        [x_text_1, y_text_1, z_text_1] = [x_text_0, 24/7 + (y_up_number_0 - y_number_0) - (y_up_text_0 - y_text_0), z_text_0]
        def go_up(
            task : Task, 
            t
        ):
            pos_number = [x_number_0 * (1-t) + x_number_1 * t,
                          y_number_0 * (1-t) + y_number_1 * t,
                          z_number_0 * (1-t) + z_number_1 * t]
            task.number.move_to(pos_number).set_opacity(1-t/2)
            pos_text = [x_text_0 * (1-t) + x_text_1 * t,
                        y_text_0 * (1-t) + y_text_1 * t,
                        z_text_0 * (1-t) + z_text_1 * t]
            task.text.move_to(pos_text).set_opacity(1-t/3)

        self.play(UpdateFromAlphaFunc(task, go_up))

    def play_task(
        self,
        task : Task,
        run_time=8,
        pause_time=1
    ):
        self.write_task(task, run_time=run_time - 2)
        self.wait(pause_time)
        self.move_task_up(task)


    def play_count_next(
        self,
        count : CounterInteger,
        buff = MED_LARGE_BUFF,
        run_time = DEFAULT_WAIT_TIME,
        rate_func = smooth,
        style = 'up_down'  # can be added other styles later on
    ):
        new_count = CounterInteger(count.value + 1, count.font_size, count.color)
        new_count.move_to(count.get_center()).set_opacity(0)

        if style == 'up_down':
            new_count.shift(UP * buff)
            self.play(
                count.animate.shift(DOWN * buff).set_opacity(0),
                new_count.animate.shift(DOWN * buff).set_opacity(1),
                run_time = run_time, rate_func=rate_func
            )
            count.update_value(1)
            count.shift(UP * buff)
        
        if style == 'left_right':
            new_count.shift(LEFT * buff)
            self.play(
                count.animate.shift(RIGHT * buff).set_opacity(0),
                new_count.animate.shift(RIGHT * buff).set_opacity(1),
                run_time = run_time, rate_func=rate_func
            )
            count.update_value(1)
            count.shift(LEFT * buff)
        
        
        self.remove(new_count)
        self.add(count)
        





