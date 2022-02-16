from PIL.Image import new
from manim import *
import numpy as np

armenian = TexTemplate()
armenian.add_to_preamble(r"\usepackage{Armtex}")

color_1 = '#12C10D'
color_2 = '#FF2000'
color_3 = YELLOW


def DiagramFrom2Circles(c_1, r_1, c_2, r_2, color_1='#12C10D', color_2='#FF2000', color_intersect=YELLOW, fill_opacity=0.3, crc_colors=False):
    '''
    This fundtion takes 2 centers and 2 radiuses
    Optional arguments are colors of sets and fill opacity
    Default colors are - Green Red and Yellow(intersection)

    It generates circles, sets, and intersetion for a Venn Diagram
    It doesn't draw anything, you have to call this function inside Create or Add function, to draw the sets 

    Returns (c_1, r_1, crc_1, c_2, r_2, crc_2, set_1, set_2, intersect)
    Returned list is ready to pass to Modify2CirclesVenn function as a starting diagram
    '''

    if crc_colors == True:
        crc_1_color = color_1
        crc_2_color = color_2
    else:
        crc_1_color = WHITE
        crc_2_color = WHITE

    crc_1 = Circle(radius=r_1, color=crc_1_color).move_to(c_1)
    crc_2 = Circle(radius=r_2, color=crc_2_color).move_to(c_2)

    intersect = Intersection(crc_1, crc_2, color=color_intersect, fill_opacity=fill_opacity)

    set_1 = Difference(crc_1, intersect, color=color_1, fill_opacity=fill_opacity)
    set_2 = Difference(crc_2, intersect, color=color_2, fill_opacity=fill_opacity)

    return (c_1, r_1, crc_1, c_2, r_2, crc_2, set_1, set_2, intersect)



class Numbers_10_20(Scene):
    def construct(self):
        # Write numbers in the upper part of the screen

        headline_size = 50
        number_size = 50
        set_name_size = 35
        y_list = 3
        number_list = Tex('Թվեր - ', '$7$', ',\ ', '$32$', ',\ ', '$4$', ',\ ', '$14$', ',\ ', '$25$', ',\ ', '$1$', ',\ ', '$11$', ',\ ', '$21$',
         ',\ ', '$16$', ',\ ', '$26$', font_size=headline_size, tex_template=armenian).shift(UP*y_list)

        # Make circle
        # 1st circle is for  n < 20
        c_1 = np.array([-1.2, 0, 0])
        r_1 = 2
        # 2nd circle is for  n > 10
        c_2 = np.array([1.2, 0, 0])
        r_2 = 2

        diagram = DiagramFrom2Circles(c_1, r_1, c_2, r_2, crc_colors=True)
        (crc_1, crc_2, set_1, set_2, intersect) = (diagram[2], diagram[5], diagram[6], diagram[7], diagram[8])
        diagram = VGroup(crc_1, crc_2, set_1, set_2, intersect)

        # Write new numbers
        # First set
        name_1 = Text('20-ից փոքր', font_size=set_name_size, color=color_1).move_to(c_1 + np.array([-r_1 - 0.5, r_1, 0]))

        less_than_10 = VGroup()
        for (i, number) in [(0, '1'), (1, '4'), (2, '7')]:
            less_than_10.add(Tex(number, font_size=number_size, color=color_1).move_to(c_1).shift(LEFT, 3*UP/4).shift(DOWN*3*i/4))

        # Second set
        name_2 = Text('10-ից մեծ', font_size=set_name_size, color=color_2).move_to(c_2 + np.array([r_2 + 0.5, r_2, 0]))

        greater_than_20 = VGroup()
        for (i, number) in [(0, '26'), (1, '21'), (2, '25'), (3, '32')]:
            greater_than_20.add(Tex(number, font_size=number_size, color=color_2).move_to(c_2).shift(RIGHT, UP).shift(DOWN*3*i/4))

        # Intersection
        name_3 = Text('10 < Թիվ < 20', font_size=set_name_size, color=color_3).move_to([0, -3, 0])

        between_10_20 = VGroup()
        for (i, number) in [(0, '16'), (1, '11'), (2, '14')]:
            between_10_20.add(Tex(number, font_size=number_size, color=color_3).move_to((c_1 + c_2)/2).shift(3*UP/4).shift(DOWN*3*i/4))

        new_numbers = VGroup(less_than_10[2], greater_than_20[3], less_than_10[1], between_10_20[2], greater_than_20[2], less_than_10[0],
        between_10_20[1], greater_than_20[1], between_10_20[0], greater_than_20[0])

        # Final animations
        self.wait(0.5)

        self.play(Write(number_list))
        # Write sets' names and draw the circles
        self.play(Write(name_1))
        self.play(Create(crc_1))
        self.play(Write(name_2))
        self.play(Create(crc_2))

        # Fill sets with colors
        self.play(Create(set_1))
        self.wait(0.5)
        self.play(Create(set_2))
        self.wait(0.5)
        self.play(Create(intersect))
        self.wait(0.5)
        self.play(Write(name_3))

        # Indicate the numbers in order and send them to their places
        for i in range(len(new_numbers)):
            self.play(Transform(number_list[2*i + 1], new_numbers[i]))
            if i < len(new_numbers) - 1:
                self.remove(number_list[2*i + 2])
            self.wait(0.2)
        self.remove(number_list[0])

        self.wait(1)



class power_of_sets(Scene):
    def construct(self):

        # Write numbers in the upper part of the screen

        headline_size = 50
        number_size = 50
        set_name_size = 35
        set_power_size = 35
        y_list = 3
        number_list = Tex('Թվեր - ', '$7$', ',\ ', '$32$', ',\ ', '$4$', ',\ ', '$14$', ',\ ', '$25$', ',\ ', '$1$', ',\ ', '$11$', ',\ ', '$21$',
         ',\ ', '$16$', ',\ ', '$26$', font_size=headline_size, tex_template=armenian).shift(UP*y_list)

        # Make circle
        # 1st circle is for  n < 20
        c_1 = np.array([-1.2, 0, 0])
        r_1 = 2
        # 2nd circle is for  n > 10
        c_2 = np.array([1.2, 0, 0])
        r_2 = 2

        diagram = DiagramFrom2Circles(c_1, r_1, c_2, r_2, crc_colors=True)
        (crc_1, crc_2, set_1, set_2, intersect) = (diagram[2], diagram[5], diagram[6], diagram[7], diagram[8])
        diagram = VGroup(crc_1, crc_2, set_1, set_2, intersect)

        # Write new numbers
        # First set
        name_1 = Text('20-ից փոքր', font_size=set_name_size, color=color_1).move_to(c_1 + np.array([-r_1 - 0.5, r_1, 0]))
        less_than_10 = VGroup()
        for (i, number) in [(0, '1'), (1, '4'), (2, '7')]:
            less_than_10.add(Tex(f'${number}$', font_size=number_size, color=color_1).move_to(c_1).shift(LEFT, 3*UP/4).shift(DOWN*3*i/4))

        # Second set
        name_2 = Text('10-ից մեծ', font_size=set_name_size, color=color_2).move_to(c_2 + np.array([r_2 + 0.5, r_2, 0]))
        greater_than_20 = VGroup()
        for (i, number) in [(0, '26'), (1, '21'), (2, '25'), (3, '32')]:
            greater_than_20.add(Tex(f'${number}$', font_size=number_size, color=color_2).move_to(c_2).shift(RIGHT, UP).shift(DOWN*3*i/4))

        # Intersection
        name_3 = Text('10 < Թիվ < 20', font_size=set_name_size, color=color_3).move_to([0, -3, 0])
        between_10_20 = VGroup()
        for (i, number) in [(0, '16'), (1, '11'), (2, '14')]:
            between_10_20.add(Tex(f'${number}$', font_size=number_size, color=color_3).move_to((c_1 + c_2)/2).shift(3*UP/4).shift(DOWN*3*i/4))

        new_numbers = VGroup(less_than_10[2], greater_than_20[3], less_than_10[1], between_10_20[2], greater_than_20[2], less_than_10[0],
        between_10_20[1], greater_than_20[1], between_10_20[0], greater_than_20[0])

        power_set_1 = Text(f'{len(less_than_10)} հատ', font_size=set_power_size, color=color_1).move_to(c_1).shift(LEFT)
        power_set_2 = Text(f'{len(greater_than_20)} հատ', font_size=set_power_size, color=color_2).move_to(c_2).shift(RIGHT)
        power_intersect = Text(f'{len(between_10_20)} հատ', font_size=set_power_size, color=color_3).move_to((c_1 + c_2)/2)

        numbers = number_list

        # Final animations
        self.wait(0.5)

        self.play(Write(numbers))
        # Write sets' names and draw the circles
        self.play(Write(name_1))
        self.play(Create(crc_1))
        self.play(Write(name_2))
        self.play(Create(crc_2))

        # Fill sets with colors
        self.play(Create(set_1))
        self.wait(0.5)
        self.play(Create(set_2))
        self.wait(0.5)
        self.play(Create(intersect))
        self.wait(0.5)
        self.play(Write(name_3))

        # Indicate the numbers in order and send them to their places
        for i in range(len(new_numbers)):
            if i < len(new_numbers) - 1:
                self.play(Transform(numbers[i + 1], new_numbers[i]), FadeOut(numbers[i+2]))
                numbers.remove(numbers[i+2])
            else:
                self.play(Transform(numbers[i + 1], new_numbers[i]))
            self.wait(0.2)
        self.remove(numbers[0])
        numbers.remove(numbers[0])

        self.play(Transform(VGroup(numbers[0], numbers[2], numbers[5]), power_set_1))
        self.play(Transform(VGroup(numbers[3], numbers[6], numbers[8]), power_intersect))
        self.play(Transform(VGroup(numbers[1], numbers[4], numbers[7], numbers[9]), power_set_2))    

        self.wait(1)


