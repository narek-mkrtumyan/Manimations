from os import remove
from PIL.Image import new
from manim import *
from manim.utils import tex_templates
import numpy as np
from numpy.lib.index_tricks import fill_diagonal

armenian = TexTemplate()
armenian.add_to_preamble(r"\usepackage{Armtex}")
tex = Tex('բլաբլա', tex_template=armenian)

color_1 = '#12C10D'
color_2 = '#FF2000'
color_3 = YELLOW      # This is also the color of intersect text if there are 2 circles

color_1_2 = ORANGE
color_1_3 = BLUE
color_2_3 = PINK

color_intersect = WHITE

fill_opacity = 0.3


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



class BananaLemon(Scene):
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

        # Import images and write names

        banana_x = -5
        banana = Text("Բանան", color=color_1, font_size=40).move_to([banana_x, 3.1, 0])
        banana_image_x = -3
        banana_image = ImageMobject("images/banana.jpg").scale(0.8).move_to([banana_image_x, 2.8, 0])

        lemon_x = 5
        lemon = Text("Լիմոն", color=color_2, font_size=40).move_to([lemon_x, 3.1, 0])
        lemon_image_x = 3
        lemon_image = ImageMobject("images/lemon.jpg").scale(0.4).move_to([3, 2.8, 0])

        # Write features for each fruit and common features in different VGroups

        features_banana = ["Դեղին", "Քաղցր", "Համեղ", "Երկար", "Միրգ"]
        features_lemon = ["Դեղին", "Թթու", "Կլոր", "Միրգ", "Անհարթ"]
        features_common = ["Դեղին", "Օգտակար", "Միրգ"]
        font_size = 30

        banana_features = VGroup()
        lemon_features = VGroup()
        common_features = VGroup()

        for i in range(len(features_banana)):
            banana_features.add(Text(features_banana[i], font_size=font_size, color=color_1).move_to([banana_image_x, 1-i, 0]))

        for i in range(len(features_lemon)):
            lemon_features.add(Text(features_lemon[i], font_size=font_size, color=color_2).move_to([lemon_image_x, 1-i, 0]))
        lemon_features[4].move_to([lemon_image_x, -2, 0])
        
        for i in range(len(features_common)):
            common_features.add(Text(features_common[i], font_size=font_size, color=color_3).move_to([0, -0.75*i, 0]))
        common_features[1].shift(0.2*RIGHT)

        # Create circles for Venn Diagram
        
        c_1 = np.array([-1.5, -0.8, 0])    # Center of the 1st circle
        r_1 = 2.8                          # Radius of the 1st circle
        c_2 = np.array([1.5, -0.8, 0])
        r_2 = 2.5

        diagram_features = [c_1, r_1, c_2, r_2]
        starting_diagram = DiagramFrom2Circles(*diagram_features)
        (c_1, r_1, crc_1, c_2, r_2, crc_2, set_1, set_2, intersect) = starting_diagram

        new_r_1 = 3
        new_r_2_1 = 2.7

        new_r_2_2 = 3


        # set the framerate 60 if rendering video in High quality, 30 - for Medium quality, and 15 for Low quality
        framerate = 60

        # Start animations

        self.wait(1)

        self.add(banana_image)
        self.play(Write(banana))
        self.wait(1)
        self.add(lemon_image)
        self.play(Write(lemon))
        self.wait(1)

        for i in range(5):
            self.play(Write(banana_features[i]))
            self.wait(0.3)
        for i in range(4):
            self.play(Write(lemon_features[i]))
            self.wait(0.3)

        self.play(Circumscribe(banana_features[0], fade_out=True, run_time=2), Circumscribe(lemon_features[0], fade_out=True, run_time=2))
        self.play(Transform(banana_features[0], common_features[0]), Transform(lemon_features[0], common_features[0]))
        self.wait(0.5)

        self.play(Circumscribe(banana_features[4], fade_out=True, run_time=2), Circumscribe(lemon_features[3], fade_out=True, run_time=2))
        self.play(Transform(banana_features[4], common_features[2]), Transform(lemon_features[3], common_features[2]))
        self.wait(1)

        self.play(Create(crc_1))
        self.wait(0.5)
        self.play(Create(crc_2))
        self.wait(0.5)

        self.play(Create(set_1), run_time=1.5)
        self.wait(0.5)
        self.play(Create(set_2), run_time=2)
        self.wait(1)

        self.play(Create(intersect), run_time=1.5)
        self.wait(1)

        self.play(Write(common_features[1]))

        starting_diagram = Modify2CirclesVenn(*starting_diagram, new_r_1=new_r_1, new_r_2=new_r_2_1, framerate=framerate)
        self.wait(1)

        self.play(Write(lemon_features[4]))
        starting_diagram = Modify2CirclesVenn(*starting_diagram, new_r_2=new_r_2_2, framerate=framerate)

        self.wait(1)



class FruitSweet(Scene):
    def construct(self):

        # Write names of the groups - fruit, sweet

        headline_size = 40
        name_size = 25
        set_power_size = 80

        y_headline = 3
        x_fruit = -5
        x_sweet = 5

        Fruit = Text('Միրգ', font_size=headline_size, color=color_1).move_to([x_fruit, y_headline, 0])
        Sweet = Text('Կոնֆետ', font_size=headline_size, color=color_2).move_to([x_sweet, y_headline, 0])
        Fruit_Sweet = Text('Միրգ և Կոնֆետ', font_size=headline_size-10, color=color_3).move_to([0, y_headline, 0])

        # Starting lists
        squad_fruit = ["Արշակ", "Աշխեն", "Լևոն", "Սմբատ", "Անահիտ", "Հովհաննես"]
        fruit_squad = VGroup()
        for i in range(len(squad_fruit)):
            fruit_squad.add(Text(squad_fruit[i], font_size=name_size, color=color_1).move_to([x_fruit, y_headline - 1, 0]).shift(DOWN*i*3/4))

        squad_sweet = ["Սոնա", "Կարեն", "Աշխեն", "Դավիթ", "Արամ", "Սմբատ", "Գայանե"]
        # sweet_squad = VGroup()
        # for i in range(len(squad_sweet)):
        #     sweet_squad.add(Text(squad_sweet[i], font_size=name_size, color=color_2).move_to([x_sweet, y_headline - 1, 0]).shift(DOWN*i*3/4))
        sweet_squad = []
        for name in squad_sweet:
            sweet_squad.append(Text(name, font_size=name_size, color=color_2))
        sweet_squad = VGroup(*sweet_squad).arrange(direction=DOWN, buff=0.4).move_to([x_sweet, 0, 0])
        
        names = VGroup(*fruit_squad, *sweet_squad)

        #Create diagram

        c_1 = np.array([-1.5, 0, 0])
        r_1 = 2.4
        c_2 = np.array([1.5, 0, 0])
        r_2 = 2.6

        diagram = DiagramFrom2Circles(c_1, r_1, c_2, r_2, crc_colors=True)
        (c_1, r_1, crc_1, c_2, r_2, crc_2, set_1, set_2, intersect) = diagram

        # New lists
        fruit_only = ["Արշակ", "Լևոն", "Անահիտ", "Հովհաննես"]
        only_fruit = VGroup()
        for i in range(len(fruit_only)):
            only_fruit.add(Text(fruit_only[i], font_size=name_size, color=color_1).move_to(c_1 + np.array([-0.75, 1, 0])).shift(DOWN*i*3/4))

        fruit_and_sweet = ["Աշխեն", "Սմբատ"]
        both = VGroup()
        for i in range(len(fruit_and_sweet)):
            both.add(Text(fruit_and_sweet[i], font_size=name_size, color=color_3).move_to([0, 1/2, 0]).shift(DOWN*i))
        
        sweet_only = ["Սոնա", "Կարեն", "Դավիթ", "Արամ", "Գայանե"]
        only_sweet = VGroup()
        for i in range(len(sweet_only)):
            only_sweet.add(Text(sweet_only[i], font_size=name_size, color=color_2).move_to(c_2 + np.array([0.75, 1.4, 0])).shift(DOWN*i*3/4))

        new_names = VGroup(only_fruit[0], both[0], only_fruit[1], both[1], only_fruit[2], only_fruit[3], *only_sweet)

        power_set_1 = Text(f'{len(only_fruit)}', font_size=set_power_size, color=color_1).move_to(c_1 + np.array([-1, 0, 0]))
        power_set_2 = Text(f'{len(only_sweet)}', font_size=set_power_size, color=color_2).move_to(c_2 + np.array([1, 0, 0]))
        power_intersect = Text(f'{len(both)}', font_size=set_power_size, color=color_3).move_to((c_1 + c_2)/2)

        union = Union(crc_1, crc_2, color=WHITE, fill_opacity=fill_opacity)
        set_fruit = Union(set_1, intersect, color=color_1, fill_opacity=fill_opacity)

        # Final animations
        self.wait(0.5)

        # Write Fruit, Sweet and names
        self.play(Write(Fruit))
        self.wait(0.5)
        self.play(Write(Sweet))
        self.wait(0.5)

        for name in fruit_squad:
            self.play(Write(name))
        self.wait(0.5)
        for name in sweet_squad:
            self.play(Write(name))

        # Transform names to the circles
        self.play(Transform(Fruit.copy(), crc_1))
        self.wait(0.5)
        self.play(Transform(Sweet.copy(), crc_2))
        self.wait(0.5)
        # Write Fruit_Sweet in the middle
        self.play(Write(Fruit_Sweet))
        self.wait(0.5)

        # Indicate the names and transfor to their new places
        for i in range(len(new_names)):
            if i == 1:
                self.play(Indicate(names[1]), Indicate(names[8]))
                self.play(Transform(names[1], new_names[i]), Transform(names[8], new_names[i]))
                self.remove(names[1], names[8])
                self.add(new_names[i])
                names.remove(names[8])
            elif i == 3:
                self.play(Indicate(names[3]), Indicate(names[10]))
                self.play(Transform(names[3], new_names[i]), Transform(names[10], new_names[i]))
                self.remove(names[3], names[10])
                self.add(new_names[i])
                names.remove(names[10])
            else:
                self.play(Indicate(names[i]))
                self.play(Transform(names[i], new_names[i]))
                self.remove(names[i])
                self.add(new_names[i])
        self.wait(0.5)

        # Fill sets with colors
        self.play(Indicate(Fruit, scale_factor=1.5, color=color_1, run_time=1.5))
        self.play(Create(set_1))
        self.wait(0.5)
        self.play(Indicate(Sweet, scale_factor=1.5, color=color_2, run_time=1.5))
        self.play(Create(set_2))
        self.wait(0.5)
        self.play(Indicate(Fruit_Sweet, scale_factor=1.5, color=color_3, run_time=1.5))
        self.play(Create(intersect))
        self.wait(0.5)

        # Transform names into the powers of each set
        self.play(Transform(VGroup(new_names[0], new_names[2], new_names[4], new_names[5]), power_set_1))
        self.wait(0.5)
        self.play(Transform(Group(new_names[6], new_names[7], new_names[8], new_names[9], new_names[10]), power_set_2))
        self.wait(0.5)
        self.play(Transform(VGroup(new_names[1], new_names[3]), power_intersect))
        self.wait(0.5)
        
        self.wait(1)



class MathSwimmingEnglish(Scene):
    def construct(self):
        
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

        font_size = 25
        headline_size = 40

        healdilne_y = 3.5
        
        Math_x = -5.5
        Swimming_x = -3.25
        English_x = -1

        # Write Math and math students
        Math = Text('Մաթեմ', color=color_1, font_size=headline_size).move_to([Math_x, healdilne_y, 0])

        students_math = ['Հայկ', 'Լիլիթ', 'Անի', 'Տիգրան', 'Էլեն', 'Գոռ', 'Տաթև']
        math_students = VGroup()
        for i in range(len(students_math)):
            math_students.add(Text(students_math[i], color=color_1, font_size=font_size).move_to([Math_x, healdilne_y-1-i/2, 0]))
        
        math_rectangle = Rectangle(height=4, width=1.5, color=color_1).move_to([Math_x, 1, 0])

        # Write Swimming and swimming students
        Swimming = Text('Լող', color=color_3, font_size=headline_size).move_to([Swimming_x, healdilne_y, 0])

        students_swimming = ['Անի', 'Գոռ', 'Տաթև', 'Նարե', 'Ռուբեն']
        swimming_students = VGroup()
        for i in range(len(students_swimming)):
            swimming_students.add(Text(students_swimming[i], color=color_3, font_size=font_size).move_to([Swimming_x, healdilne_y-1-i/2, 0]))
        
        swimming_rectangle = Rectangle(height=3, width=1.5, color=color_3).move_to([Swimming_x, 1.5, 0])
        
        # Write English and english students
        English = Text('Անգլերեն', color=color_2, font_size=headline_size).move_to([English_x, healdilne_y, 0])

        students_english = ['Հայկ', 'Լիլիթ', 'Անի', 'Արմեն', 'Հասմիկ', 'Նարե']
        english_students = VGroup()
        for i in range(len(students_english)):
            english_students.add(Text(students_english[i], color=color_2, font_size=font_size).move_to([English_x, healdilne_y-1-i/2, 0]))
        
        english_rectangle = Rectangle(height=3.5, width=1.5, color=color_2).move_to([English_x, 1.25, 0])

        # Write (Math and English) students
        students_math_eng = ['Հայկ', 'Լիլիթ']
        math_eng_students = VGroup()
        for i in range(len(students_math_eng)):
            math_eng_students.add(Text(students_math_eng[i], color=color_1_2, font_size=font_size).move_to([1, 1.8-i/2, 0]))

        # Write (Math and Swimming) students
        students_math_swim = ['Գոռ', 'Տաթև']
        math_swim_students = VGroup()
        for i in range(len(students_math_swim)):
            math_swim_students.add(Text(students_math_swim[i], color=color_1_3, font_size=font_size).move_to([0, -i/2, 0]))

        # Write (Math and English and Swimming) stundet
        student_math_eng_swim = 'Անի'
        math_eng_swim_student = Text(student_math_eng_swim, color=color_intersect, font_size=font_size).move_to([1, 0.3, 0])

        # Write (English and Swimming) student
        students_eng_swim = ['Անի', 'Նարե']
        eng_swim_students = VGroup()
        eng_swim_students.add(Text(students_eng_swim[0], color=color_2_3, font_size=font_size).move_to([1, 0.3, 0]))
        eng_swim_students.add(Text(students_eng_swim[1], color=color_2_3, font_size=font_size).move_to([2, -0.25, 0]))

        # Write new English students
        new_english_students = VGroup(english_students[0].copy().move_to([1, 1.8, 0]), english_students[1].copy().move_to([1, 1.3, 0]),
        english_students[2].copy().move_to([1, 0.3, 0]), english_students[3].copy().move_to([2.75, 1.75, 0]),
        english_students[4].copy().move_to([2.75, 1.25, 0]), english_students[5].copy().move_to([2, -0.25, 0]))

        # Write new Swimming students
        new_swimming_students = VGroup(eng_swim_students[0], swimming_students[1].copy().move_to([0, 0, 0]),
        swimming_students[2].copy().move_to([0, -0.5, 0]), eng_swim_students[1], swimming_students[4].copy().move_to([1, -1.75, 0]))

        # Write new Math students
        new_math_students = VGroup(math_eng_students[0], math_eng_students[1], math_eng_swim_student, 
        math_students[3].copy().move_to([-1, 1.75, 0]), math_students[4].copy().move_to([-1, 1.25, 0]), 
        math_swim_students[0], math_swim_students[1])



        # Draw the circles

        c_1 = np.array([-0.25, 1, 0])
        r_1 = 2

        c_2 = np.array([2, 1, 0])
        r_2 = 1.8

        c_3 = np.array([1, -0.75, 0])
        r_3 = 1.75

        diagram_features = [c_1, r_1, c_2, r_2, c_3, r_3]
        starting_diagram = DiagramFrom3Circles(*diagram_features, crc_colors=True)
        (c_1, r_1, crc_1, c_2, r_2, crc_2, c_3, r_3, crc_3, set_1, set_2, set_3, intersect_1_2, intersect_1_3, intersect_2_3, intersect) = starting_diagram



        # set the framerate 60 if rendering video in High quality, 30 - for Medium quality, and 15 for Low quality
        framerate = 60

        # Start animations

        # self.add(Math, Swimming, English, math_students, swimming_students, english_students)
        # self.add(english_rectangle, swimming_rectangle, math_rectangle)
        # self.add(new_english_students, new_math_students, new_swimming_students)
        # self.add(crc_1, crc_2, crc_3, set_1, set_2, set_3, intersect_1_2, intersect_1_3, intersect_2_3, intersect)

        self.wait(0.5)

        # Write Math, Swimming and English

        self.play(Write(Math))
        self.wait(0.5)
        self.play(Write(Swimming))
        self.wait(0.5)
        self.play(Write(English))
        self.wait(0.5)

        # Write students' names under each category

        self.play(Write(math_students), run_time=7)
        self.play(Create(math_rectangle))
        self.wait(0.5)

        self.play(Write(swimming_students), run_time=7)
        self.play(Create(swimming_rectangle))
        self.wait(0.5)

        self.play(Write(english_students), run_time=7)
        self.play(Create(english_rectangle))
        self.wait(0.5)

        # Create Cricles

        self.play(Transform(english_rectangle, crc_2), Transform(english_students, new_english_students),
        English.animate(run_time=3).shift(5*RIGHT), run_time=3)
        self.wait(0.5)

        self.play(Transform(swimming_rectangle, crc_3), Transform(swimming_students, new_swimming_students), 
        Transform(new_english_students[5], new_swimming_students[3]), Transform(new_english_students[2], new_swimming_students[0]), 
        Swimming.animate(rin_time=3).shift(4.5*RIGHT, 6.5*DOWN), run_time=3)
        self.wait(0.5)

        self.play(Transform(math_rectangle, crc_1), Transform(math_students, new_math_students), 
        Transform(new_swimming_students[0], new_math_students[2]), Transform(new_english_students[2], new_math_students[2]),
        Transform(new_english_students[0], new_math_students[0]), Transform(new_english_students[1], new_math_students[1]),
        Transform(new_swimming_students[1], new_math_students[5]), Transform(new_swimming_students[2], new_math_students[6]), 
        Math.animate(run_time=3).shift(4*RIGHT), run_time=3)
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



class VennDiagram(Scene):
    def construct(self):
        
        self.wait(0.5)
        BananaLemon.construct(self)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)
        FruitSweet.construct(self)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)
        MathSwimmingEnglish.construct(self)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)
        


class test(Scene):
    def construct(self):
        
        self.add(tex)
