from PIL.Image import new
from manim import *
import numpy as np

armenian = TexTemplate()
armenian.add_to_preamble(r"\usepackage{Armtex}")

color_1 = '#12C10D'
color_2 = '#FF2000'
color_3 = YELLOW      # This is also the color of intersect text if there are 2 circles

color_1_2 = ORANGE
color_1_3 = BLUE
color_2_3 = PINK

color_intersect = WHITE


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



def DiagramFrom3Circles(c_1, r_1, c_2, r_2, c_3, r_3, color_1='#12C10D', color_2='#FF2000', color_3=YELLOW,
color_1_2=ORANGE, color_1_3=BLUE, color_2_3=PINK, color_intersect=WHITE, fill_opacity=0.3, crc_colors=False):
    '''
    This fundtion takes 3 centers and 3 radiuses
    Optional arguments are colors of sets and fill opacity

    It generates circles, sets, and intersetion for a Venn Diagram
    It doesn't draw anything, you have to call this function inside Create or Add function, to draw the sets 

    Returns (c_1, r_1, crc_1, c_2, r_2, crc_2, c_3, r_3, crc_3, set_1, set_2, set_3, intersect_1_2, intersect_1_3, intersect_2_3, intersect)
    Returned list is ready to pass to Modify3CirclesVenn function as a starting diagram
    '''

    if crc_colors == True:
        crc_1_color = color_1
        crc_2_color = color_2
        crc_3_color = color_3
    else:
        crc_1_color = WHITE
        crc_2_color = WHITE
        crc_3_color = WHITE

    crc_1 = Circle(radius=r_1, color=crc_1_color).move_to(c_1)
    crc_2 = Circle(radius=r_2, color=crc_2_color).move_to(c_2)
    crc_3 = Circle(radius=r_3, color=crc_3_color).move_to(c_3)

    intersect = Intersection(crc_1, crc_2, crc_3, color=color_intersect, fill_opacity=fill_opacity)

    intersect_1_2 = Difference(Intersection(crc_1, crc_2), intersect, color=color_1_2, fill_opacity=fill_opacity)
    intersect_1_3 = Difference(Intersection(crc_1, crc_3), intersect, color=color_1_3, fill_opacity=fill_opacity)
    intersect_2_3 = Difference(Intersection(crc_2, crc_3), intersect, color=color_2_3, fill_opacity=fill_opacity)

    set_1 = Difference(crc_1, Union(intersect_1_2, intersect_1_3, intersect), color=color_1, fill_opacity=fill_opacity)
    set_2 = Difference(crc_2, Union(intersect_1_2, intersect_2_3, intersect), color=color_2, fill_opacity=fill_opacity)
    set_3 = Difference(crc_3, Union(intersect_1_3, intersect_2_3, intersect), color=color_3, fill_opacity=fill_opacity)

    return (c_1, r_1, crc_1, c_2, r_2, crc_2, c_3, r_3, crc_3, set_1, set_2, set_3, intersect_1_2, intersect_1_3, intersect_2_3, intersect)



class Numbers(Scene):
    def construct(self):

        # Write numbers in the upper part of the screen

        headline_size = 50
        number_size = 40
        set_name_size = 35

        y_list = 3
        y_commas = y_list - 0.15
        x_list = -3
        x_commas = x_list + 0.3

        headline = Text('Թվեր - ', font_size=headline_size).move_to([x_list - 1.5, y_list, 0])
        list_numbers = ['7', '32', '4', '14', '25', '1', '11', '21', '16', '26']
        numbers = VGroup()
        commas = VGroup()
        for i in range(len(list_numbers)):
            numbers.add(Tex(list_numbers[i], font_size=number_size).move_to([x_list + i * 3/4, y_list, 0]))
            if i < len(list_numbers) - 1:
                commas.add(Tex(',', font_size=number_size).move_to([x_commas + i * 3/4, y_commas, 0]))

        # Make circles

        # 1st circle is for  n < 20
        c_1 = np.array([-1.2, 0, 0])
        r_1 = 2
        new_c_1 = np.array([-1.2, 1, 0])

        # 2nd circle is for  n > 10
        c_2 = np.array([1.2, 0, 0])
        r_2 = 2
        new_c_2 = np.array([1.2, 1, 0])

        # 3rd circle is for  n = 2k
        c_3 = np.array([0, -10, 0])
        r_3 = 0.5
        new_c_3 = np.array([0, -1.2, 0])
        new_r_3 = 0.5
        newest_r_3 = 2
        crc_3 = Circle(radius=r_3, color=color_3).move_to(c_3)

        first_diagram = DiagramFrom3Circles(c_1, r_1, c_2, r_2, c_3, r_3, crc_colors=True)
        (crc_1, crc_2, set_1, set_2, intersect_1_2) = (first_diagram[2],first_diagram[5],first_diagram[9],first_diagram[10],first_diagram[12])
        first_diagram = VGroup(crc_1, crc_2, set_1, set_2, intersect_1_2)

        starting_diagram = DiagramFrom3Circles(new_c_1, r_1, new_c_2, r_2, new_c_3, new_r_3, crc_colors=True)
        (new_crc_1, new_crc_2, new_crc_3, new_set_1, new_set_2, new_set_3,
        new_intersect_1_2, new_intersect_1_3, new_intersect_2_3, new_intersect) = (starting_diagram[2], starting_diagram[5], 
        starting_diagram[8], starting_diagram[9], starting_diagram[10], starting_diagram[11], 
        starting_diagram[12], starting_diagram[13], starting_diagram[14], starting_diagram[15])

        # Write new numbers

        # First set
        name_1 = Text('20-ից փոքր', font_size=set_name_size, color=color_1).move_to(c_1 + np.array([-r_1 - 0.5, r_1, 0]))

        less_than_10 = VGroup()
        for (i, number) in [(0, '1'), (1, '4'), (2, '7')]:
            less_than_10.add(Tex(number, font_size=number_size, color=color_1).move_to(c_1).shift(LEFT, UP/2).shift(DOWN*i/2))

        # Second set
        name_2 = Text('10-ից մեծ', font_size=set_name_size, color=color_2).move_to(c_2 + np.array([r_2 + 0.5, r_2, 0]))

        greater_than_20 = VGroup()
        for (i, number) in [(0, '26'), (1, '21'), (2, '25'), (3, '32')]:
            greater_than_20.add(Tex(number, font_size=number_size, color=color_2).move_to(c_2).shift(RIGHT, UP).shift(DOWN*i/2))
        
        # Intersection
        between_10_20 = VGroup()
        for (i, number) in [(0, '16'), (1, '11'), (2, '14')]:
            between_10_20.add(Tex(number, font_size=number_size, color=color_1_2).move_to((c_1 + c_2)/2).shift(UP/2).shift(DOWN*i/2))

        new_numbers = VGroup(less_than_10[2], greater_than_20[3], less_than_10[1], between_10_20[2], greater_than_20[2], less_than_10[0],
        between_10_20[1], greater_than_20[1], between_10_20[0], greater_than_20[0])

        # add mobjects on the screen for test

        self.add(headline)
        self.add(numbers, commas)
        self.wait(0.5)
        self.add(name_1, crc_1)
        self.add(name_2, crc_2)
        self.wait(0.5)
        self.remove(numbers, commas, headline)
        self.add(new_numbers)
        self.wait(0.5)
        self.add(set_1, set_2, intersect_1_2)
        self.add(VGroup(new_numbers, first_diagram, name_1, name_2).shift(UP))
        # self.add(crc_3)
        # self.remove(crc_3, first_diagram)
        # self.add(starting_diagram)


        # Final animations

        self.wait(0.5)
        
        # Wrte headline(Թվեր) and the numbers 
        # self.play(Write(headline))
        # self.wait(0.5)
        # for i in range(len(numbers)):
        #     self.play(Write(numbers[i]))
        #     if i < len(numbers) - 1:
        #         self.add(commas[i])
        # self.wait(0.5)

        # Write first two sets' names and draw the circles
        # self.play(Write(name_1))
        # self.play(Create(crc_1))
        # self.play(Write(name_2))
        # self.play(Create(crc_2))

        # Indicate the numbers in order and send them to their places
        # for i in range(len(numbers)):
        #     self.play(Indicate(numbers[i]))
        #     self.wait(0.2)
        #     if i < len(numbers) - 1:
        #         self.remove(commas[i])
        #     self.play(Transform(numbers[i], new_numbers[i]))
        #     self.wait(0.3)
        # self.remove(headline)
        # self.wait(0.5)

        # Fill sets with colors
        # self.play(Create(set_1))
        # self.play(Create(set_2))
        # self.play(Create(intersect_1_2))

        # self.play(VGroup(new_numbers, first_diagram, name_1, name_2).animate(run_time=1).shift(UP))
        # self.wait(0.5)

        self.remove(crc_1, crc_2, set_1, set_2, intersect_1_2)
        self.wait(0.5)
        self.add(new_crc_1, new_crc_2, new_crc_3)
        # self.add(new_set_1, new_set_2, new_intersect_1_2)


        self.wait(1)



class MathSwmEngIndividual(Scene):
    def construct(self):
        
        def Modify3CirclesVenn(c_1, r_1, crc_1, c_2, r_2, crc_2, c_3, r_3, crc_3, set_1, set_2, set_3, 
                intersect_1_2, intersect_1_3, intersect_2_3, intersect,
                new_c_1=np.array([0.001, 0.001, 0.001]), new_r_1=0.001, 
                new_c_2=np.array([0.001, 0.001, 0.001]), new_r_2=0.001, 
                new_c_3=np.array([0.001, 0.001, 0.001]), new_r_3=0.001, 
                color_1=GREEN, color_2=BLUE, color_3=RED, 
                color_1_2=ORANGE, color_1_3=YELLOW, color_2_3=PINK, color_intersect=WHITE,
                fill_opacity=0.3, run_time=1.5, framerate=15):
                    '''
                    Modify3CirclesVenn takes centers, radiuses and bodies of 3 existing circles, their differences and intersections.
                    Optional arguments are - new centers, new radiuses, colors of sets, fill opacity of the colors and time of transformation.
                    
                    Old circles are transformed into new circles if new parameters are given. 
                    If you don't pass any new parameter for a circle, it doesn't change.

                    Returns new centers, radiuses, circles, differences and intersections
                    '''
                    if np.all(new_c_1 == np.array([0.001, 0.001, 0.001])):
                        new_c_1 = c_1
                    if new_r_1 == 0.001:
                        new_r_1 = r_1
                    if np.all(new_c_2 == np.array([0.001, 0.001, 0.001])):
                        new_c_2 = c_2
                    if new_r_2 == 0.001:
                        new_r_2 = r_2
                    if np.all(new_c_3 == np.array([0.001, 0.001, 0.001])):
                        new_c_3 = c_3
                    if new_r_3 == 0.001:
                        new_r_3 = r_3
                    if framerate == 15:
                        delay_time = 0.07
                    if framerate == 30:
                        delay_time = 0.04
                    if framerate == 60:
                        delay_time = 0.02
                    
                    number_of_steps = int(run_time/delay_time)

                    for i in range(number_of_steps):

                        self.remove(crc_1, crc_2, crc_3, set_1, set_2, set_3, intersect_1_2, intersect_1_3, intersect_2_3, intersect)
                        
                        temp_c_1 = c_1 + i * (new_c_1 - c_1)/number_of_steps
                        temp_r_1 = r_1 + i * (new_r_1 - r_1)/number_of_steps
                        temp_c_2 = c_2 + i * (new_c_2 - c_2)/number_of_steps
                        temp_r_2 = r_2 + i * (new_r_2 - r_2)/number_of_steps
                        temp_c_3 = c_3 + i * (new_c_3 - c_3)/number_of_steps
                        temp_r_3 = r_3 + i * (new_r_3 - r_3)/number_of_steps

                        crc_1 = Circle(radius=temp_r_1, color=WHITE).move_to(temp_c_1)
                        crc_2 = Circle(radius=temp_r_2, color=WHITE).move_to(temp_c_2)
                        crc_3 = Circle(radius=temp_r_3, color=WHITE).move_to(temp_c_3)

                        intersect = Intersection(crc_1, crc_2, crc_3, color=color_intersect, fill_opacity=fill_opacity)

                        intersect_1_2 = Difference(Intersection(crc_1, crc_2), intersect, color=color_1_2, fill_opacity=fill_opacity)
                        intersect_1_3 = Difference(Intersection(crc_1, crc_3), intersect, color=color_1_3, fill_opacity=fill_opacity)
                        intersect_2_3 = Difference(Intersection(crc_2, crc_3), intersect, color=color_2_3, fill_opacity=fill_opacity)

                        set_1 = Difference(crc_1, Union(intersect_1_2, intersect_1_3, intersect), color=color_1, fill_opacity=fill_opacity)
                        set_2 = Difference(crc_2, Union(intersect_1_2, intersect_2_3, intersect), color=color_2, fill_opacity=fill_opacity)
                        set_3 = Difference(crc_3, Union(intersect_1_3, intersect_2_3, intersect), color=color_3, fill_opacity=fill_opacity)

                        self.add(crc_1, crc_2, crc_3, set_1, set_2, set_3, intersect_1_2, intersect_1_3, intersect_2_3, intersect)

                        self.wait(delay_time)

                    return new_c_1, new_r_1, crc_1, new_c_2, new_r_2, crc_2, new_c_3, new_r_3, crc_3, set_1, set_2, set_3, intersect_1_2, intersect_1_3, intersect_2_3, intersect
                    # (c_1, r_1, crc_1, c_2, r_2, crc_2, c_3, r_3, crc_3, set_1, set_2, set_3, intersect_1_2, intersect_1_3, intersect_2_3, intersect)

        font_size = 20
        headline_size = 30

        healdilne_y = 3.5
        
        Math_x = -6
        Swimming_x = -4.5
        English_x = -3

        # Write Math and math students

        Math = Text('Մաթեմ', color=color_1, font_size=headline_size).move_to([Math_x, healdilne_y, 0])

        students_math = ['Հայկ', 'Լիլիթ', 'Անի', 'Տիգրան', 'Էլեն', 'Գոռ', 'Տաթև']

        math_students = VGroup()
        for i in range(len(students_math)):
            math_students.add(Text(students_math[i], color=color_1, font_size=font_size).move_to([Math_x, healdilne_y-1-i/2, 0]))

        # Write Swimming and swimming students

        Swimming = Text('Լող', color=color_3, font_size=headline_size).move_to([Swimming_x, healdilne_y, 0])

        students_swimming = ['Անի', 'Գոռ', 'Տաթև', 'Նարե', 'Ռուբեն']

        swimming_students = VGroup()
        for i in range(len(students_swimming)):
            swimming_students.add(Text(students_swimming[i], color=color_3, font_size=font_size).move_to([Swimming_x, healdilne_y-1-i/2, 0]))
        
        # Write English and english students

        English = Text('Անգլերեն', color=color_2, font_size=headline_size).move_to([English_x, healdilne_y, 0])

        students_english = ['Հայկ', 'Անի', 'Լիլիթ', 'Արմեն', 'Հասմիկ', 'Նարե']

        english_students = VGroup()
        for i in range(len(students_english)):
            english_students.add(Text(students_english[i], color=color_2, font_size=font_size).move_to([English_x, healdilne_y-1-i/2, 0]))

        # Write (Math and English) students

        students_math_eng = ['Հայկ', 'Լիլիթ']

        math_eng_students = VGroup()
        for i in range(len(students_math_eng)):
            math_eng_students.add(Text(students_math_eng[i], color=color_1_2, font_size=font_size).move_to([2.5, 1.75-i/2, 0]))

        # Write (Math and Swimming) students

        students_math_swim = ['Գոռ', 'Տաթև']

        math_swim_students = VGroup()
        for i in range(len(students_math_swim)):
            math_swim_students.add(Text(students_math_swim[i], color=color_1_3, font_size=font_size).move_to([1.5, -i/2, 0]))

        # Write (Math and English and Swimming) stundet

        student_math_eng_swim = 'Անի'

        math_eng_swim_student = Text(student_math_eng_swim, color=color_intersect, font_size=font_size).move_to([2.5, 0.5, 0])

        # Write (English and Swimming) student

        students_eng_swim = ['Նարե']

        eng_swim_student = Text(students_eng_swim[0], color=color_2_3, font_size=font_size).move_to([3.5, -0.25, 0])



        # Draw the circles

        c_1 = np.array([1.25, 1, 0])
        r_1 = 2

        c_2 = np.array([3.5, 1, 0])
        r_2 = 1.8

        c_3 = np.array([2.5, -0.75, 0])
        r_3 = 1.75

        diagram_features = [c_1, r_1, c_2, r_2, c_3, r_3]
        starting_diagram = DiagramFrom3Circles(*diagram_features, crc_colors=True)
        (c_1, r_1, crc_1, c_2, r_2, crc_2, c_3, r_3, crc_3, set_1, set_2, set_3, intersect_1_2, intersect_1_3, intersect_2_3, intersect) = starting_diagram



        # set the framerate 60 if rendering video in High quality, 30 - for Medium quality, and 15 for Low quality
        framerate = 15

        # Start animations

        self.wait(0.5)

        # self.add(Math, Swimming, English, math_students, english_students, swimming_students)

        # Write Math, Swimming and English

        self.play(Write(Math))
        self.wait(0.5)
        self.play(Write(Swimming))
        self.wait(0.5)
        self.play(Write(English))
        self.wait(0.5)

        # Write students' names under each category

        self.play(Write(math_students), run_time=7)
        self.wait(0.5)
        self.play(Write(swimming_students), run_time=7)
        self.wait(0.5)
        self.play(Write(english_students), run_time=7)
        self.wait(0.1)

        # Create Cricles

        self.play(Transform(Math.copy(), crc_1), run_time=2)
        self.wait(0.5)
        self.play(Transform(English.copy(), crc_2))
        self.wait(0.5)
        self.play(Transform(Swimming.copy(), crc_3))
        self.wait(0.5)

        # Point out Math and English students and send to their place

        self.play(Circumscribe(math_students[0], fade_out=True, run_time=2), Circumscribe(english_students[0], fade_out=True, run_time=2))
        self.play(Transform(math_students[0], math_eng_students[0]), Transform(english_students[0], math_eng_students[0]))
        self.wait(0.5)
        self.play(Circumscribe(math_students[1], fade_out=True, run_time=2), Circumscribe(english_students[2], fade_out=True, run_time=2))
        self.play(Transform(math_students[1], math_eng_students[1]), Transform(english_students[2], math_eng_students[1]))
        self.wait(0.5)

        # Point out Math, English and Swimming student and send to their place

        self.play(Circumscribe(math_students[2], fade_out=True, run_time=2), Circumscribe(english_students[1], fade_out=True, run_time=2), 
        Circumscribe(swimming_students[0], fade_out=True, run_time=2))
        self.play(Transform(math_students[2], math_eng_swim_student), Transform(english_students[1], math_eng_swim_student), 
        Transform(swimming_students[0], math_eng_swim_student))
        self.wait(0.5)

        # Point out Math and Swimming students and send to their place

        self.play(Circumscribe(math_students[5], fade_out=True, run_time=2), Circumscribe(swimming_students[1], fade_out=True, run_time=2))
        self.play(Transform(math_students[5], math_swim_students[0]), Transform(swimming_students[1], math_swim_students[0]))
        self.wait(0.5)
        self.play(Circumscribe(math_students[6], fade_out=True, run_time=2), Circumscribe(swimming_students[2], fade_out=True, run_time=2))
        self.play(Transform(math_students[6], math_swim_students[1]), Transform(swimming_students[2], math_swim_students[1]))
        self.wait(0.5)

        # Point out English and Swimming students and send to their place

        self.play(Circumscribe(english_students[5], fade_out=True, run_time=2), Circumscribe(swimming_students[3], fade_out=True, run_time=2))
        self.play(Transform(english_students[5], eng_swim_student), Transform(swimming_students[3], eng_swim_student))
        self.wait(0.5)

        # Point out only Math students and send to their place

        self.play(Circumscribe(math_students[3], fade_out=True, run_time=2))
        self.play(math_students[3].animate(run_time=1).move_to([0.25, 1.75, 0]))
        self.wait(0.5)
        self.play(Circumscribe(math_students[4], fade_out=True, run_time=2))
        self.play(math_students[4].animate(run_time=1).move_to([0.25, 1.25, 0]))
        self.wait(0.5)

        # Point out only English students and send to their place

        self.play(Circumscribe(english_students[3], fade_out=True, run_time=2))
        self.play(english_students[3].animate(run_time=1).move_to([4.25, 1.75, 0]))
        self.wait(0.5)
        self.play(Circumscribe(english_students[4], fade_out=True, run_time=2))
        self.play(english_students[4].animate(run_time=1).move_to([4.25, 1.25, 0]))
        self.wait(0.5)

        # Point out only Swimming students and send to their place
        
        self.play(Circumscribe(swimming_students[4], fade_out=True, run_time=2))
        self.play(swimming_students[4].animate(run_time=1).move_to([2.5, -1.75, 0]))
        self.wait(0.5)

        # Color the sets

        self.play(Create(set_1))
        self.wait(0.3)
        self.play(Create(set_2))
        self.wait(0.3)
        self.play(Create(set_3))
        self.wait(0.3)
        self.play(Create(intersect_1_2))
        self.wait(0.3)
        self.play(Create(intersect_1_3))
        self.wait(0.3)
        self.play(Create(intersect_2_3))
        self.wait(0.3)
        self.play(Create(intersect))
        self.wait(0.3)

        self.wait(1)

