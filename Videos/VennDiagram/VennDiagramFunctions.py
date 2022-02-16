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
    This function takes 2 centers and 2 radiuses
    Optional arguments are colors of sets and fill opacity

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


class VennCirclesModifications(Scene):
    def construct(self):

        def Modify2CirclesVenn(c_1, r_1, crc_1, c_2, r_2, crc_2, set_1, set_2, intersect, 
        new_c_1=np.array([0.001, 0.001, 0.001]), new_r_1=0.001, new_c_2=np.array([0.001, 0.001, 0.001]), new_r_2=0.001, 
        color_1='#12C10D', color_2='#FF2000', color_intersect=YELLOW, fill_opacity=0.3, run_time=1.5, framerate=15):
            '''
            Modify2CirclesVenn takes centers, radiuses and bodies of 2 existing circles, their differences and intersection
            Optional arguments are - new centers, new radiuses, colors of sets, fill opacity of the colors and time of transformation
            
            Old circles are transformed into new circles, if you don't pass any new parameter for a circle, it doesn't change

            Returns new centers, radiuses, circles, differences and intersection
            '''
            if np.all(new_c_1 == np.array([0.001, 0.001, 0.001])):
                new_c_1 = c_1
            if new_r_1 == 0.001:
                new_r_1 = r_1
            if np.all(new_c_2 == np.array([0.001, 0.001, 0.001])):
                new_c_2 = c_2
            if new_r_2 == 0.001:
                new_r_2 = r_2
            if framerate == 15:
                delay_time = 0.07
            if framerate == 30:
                delay_time = 0.04
            if framerate == 60:
                delay_time = 0.02

            number_of_steps = int(run_time/delay_time)

            for i in range(number_of_steps):

                self.remove(crc_1, crc_2, set_1, set_2, intersect)
                
                temp_c_1 = c_1 + i * (new_c_1 - c_1)/number_of_steps
                temp_r_1 = r_1 + i * (new_r_1 - r_1)/number_of_steps
                temp_c_2 = c_2 + i * (new_c_2 - c_2)/number_of_steps
                temp_r_2 = r_2 + i * (new_r_2 - r_2)/number_of_steps

                crc_1 = Circle(radius=temp_r_1, color=WHITE).move_to(temp_c_1)
                crc_2 = Circle(radius=temp_r_2, color=WHITE).move_to(temp_c_2)

                intersect = Intersection(crc_1, crc_2, color=color_intersect, fill_opacity=fill_opacity)
                set_1 = Difference(crc_1, intersect, color=color_1, fill_opacity=fill_opacity)
                set_2 = Difference(crc_2, intersect, color=color_2, fill_opacity=fill_opacity)

                self.add(crc_1, crc_2, set_1, set_2, intersect)

                self.wait(delay_time)

            return new_c_1, new_r_1, crc_1, new_c_2, new_r_2, crc_2, set_1, set_2, intersect
            # (c_1, r_1, crc_1, c_2, r_2, crc_2, set_1, set_2, intersect)


        def Modify3CirclesVenn(c_1, r_1, crc_1, c_2, r_2, crc_2, c_3, r_3, crc_3, set_1, set_2, set_3, 
                intersect_1_2, intersect_1_3, intersect_2_3, intersect,
                new_c_1=np.array([0.001, 0.001, 0.001]), new_r_1=0.001, 
                new_c_2=np.array([0.001, 0.001, 0.001]), new_r_2=0.001, 
                new_c_3=np.array([0.001, 0.001, 0.001]), new_r_3=0.001, 
                color_1='#12C10D', color_2='#FF2000', color_3=YELLOW, 
                color_1_2=ORANGE, color_1_3=BLUE, color_2_3=PINK, color_intersect=WHITE,
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

