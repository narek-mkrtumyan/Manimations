"""
Feb 2022, Hayk Tarkhanyan
"""

from manim import *
import numpy as np
import sys

sys.path.append('../')

from Objects.Objects import *


armenian_tex_template = TexTemplate()
armenian_tex_template.add_to_preamble(r"\usepackage{armtex}")


class Scales(Scene):
    def construct(self):


        

        self.left_part_list_of_str = ['apple', 'apple', 'apple', 'kb_15_kg']
        self.right_part_list_of_str = ['apple', 'apple', 'kb_20_kg']

        # print(self.rename_list_to_use_in_dict(self.left_part_list_of_str))
        # self.left_part_apples = [0, 1, 2]
        # self.right_part_apples = [0, 1]

        self.add_objects(self.left_part_list_of_str, self.right_part_list_of_str, creation_runtime=0.4)


        # kettlebell = Weight(5)
        # self.play(Create(kettlebell))
        # print(self.right_part)
        # kettlebell = self.right_part[2]
        # print('left', self.left_part)
        print('right', self.right_part)

        self.split_kettlebell_into_several(2, [5, 15], part='right')
        self.wait()
        # print('left after split', self.left_part)
        print('right after split', self.right_part)

        # self.combine_kettlebells([2,3,4], 'right')
        # # print('left after combine', self.left_part)
        # print('right after combine', self.right_part)

        self.remove_objects_from_both_parts(left_part_indexes=[3], right_part_indexes=[3])
        self.wait()
        self.remove_objects_from_both_parts(left_part_indexes=[0,1], right_part_indexes=[0,1])
        # print('left after remove', self.left_part)
        # print('right after remove', self.right_part)
        # self.remove_objects_from_both_parts(left_part_indexes=[0,], right_part_indexes=[1])
        self.show_answer()
        # # print(new_kbs[0])
        # # print(self.left_part[3].kg)
        
        # print('look here', self.mobjects)

        # to_f = VGroup(self.mobjects[-1][1],  self.left_part[3].weight)


        # self.play(FadeOut(to_f))

        # self.remove_obj()



        # print(new_kbs)
        # self.combine_kettlebells(new_kbs)


    @staticmethod 
    def rename_list_to_use_in_dict(mylist):
        # https://stackoverflow.com/questions/30650474/python-rename-duplicates-in-list-with-progressive-numbers-without-sorting-list
        newlist = []
        for i, v in enumerate(mylist):
            totalcount = mylist.count(v)
            count = mylist[:i].count(v)
            newlist.append(f"{v}_{count + 1}" if totalcount > 1 else v)
        return newlist

    @staticmethod
    def get_indexes_for_removing(mylist):
        return list(j - i for i, j in enumerate(mylist))

    @staticmethod
    def convert_list_of_items_to_list_of_mobjects(items):
        """Function takes as input list of strings and converts it to list 
        of mobjects

        Note:
            Options for input are` ['apple', 'kb_{n}_kg'(from 1 to 20), ADD LATER 
    
        Args:
            items (list of strings): items to convert to mobjects

        Returns:
            mobjs (list of mobjects)

        Examples:
            convert_list_of_items_to_list_of_mobjects(['apple', 'apple', 'kb_2_kg'])
        """
        mobjs = []
        for i in items:
            if i == "apple":
                mobjs.append(SVGMobject(os.path.join('Objects', 'SVG_files', 'fruits', 'red_apple.svg')).scale(0.25))#.set_color(GREEN))
            if i == "mushroom":
                mobjs.append(SVGMobject(os.path.join('Objects', 'SVG_files', 'fruits', 'mushroom.svg')).scale(0.25))#.set_color(GREEN))
            if i.startswith('kb'):
                kb_weight = int(i.split('_')[1])
                mobjs.append(Weight(kb_weight).scale(0.6))
        return mobjs



    def add_objects(self, left_part, right_part, 
                    left_part_shift=LEFT*4, right_part_shift=RIGHT*3, 
                    display_option='FadeIn', creation_runtime=0.75):
        """Function plays the animation of creating items and initilizes 
        `self.left_part` and `self.right_part` attributes 

        Note:
            self.left_part and self.right_part are VGroups

        Args:
            left_part (list of strings): see list of allowed options is docstring of function above 
            right_part (list of strings):
            left_part_shift (np.array): where to position left plate default` LEFT * 4
            right_part_shift (np.array): where to position right plate default` RIGHT * 3
            display_option (str): one of ['Create', "FadeIn"] default is FadeIn
            creation_runtime (float): creation time for each item default` 0.75

        Returns:
            None
        """
        self.left_part = self.convert_list_of_items_to_list_of_mobjects(left_part)
        self.right_part = self.convert_list_of_items_to_list_of_mobjects(right_part)

        self.left_part = VGroup(*self.left_part).arrange().shift(left_part_shift) 
        self.right_part = VGroup(*self.right_part).arrange().shift(right_part_shift)

        # bad code, figure out a way to run a loop over both left part and right part, .copy or + or .add() methods didn't work, perhaps I'll never fix this though
        for i in self.left_part:
            if display_option.lower().startswith('cr'):
                self.play(Create(i), run_time=creation_runtime) 
            elif display_option.lower().startswith('fade'):
                self.play(FadeIn(i), run_time=creation_runtime) 

        for i in self.right_part:
            if display_option.lower().startswith('cr'):
                self.play(Create(i), run_time=creation_runtime) 
            elif display_option.lower().startswith('fade'):
                self.play(FadeIn(i), run_time=creation_runtime) 


        # big_kettlebell = self.combine_kettlebells([right_part[-2], right_part[-1]], play_animation=True)
        # # self.split_kettlebell_into_several(big_kettlebell, [3,3,4])
        # self.remove_obj()



    def remove_objects_from_both_parts(self, left_part_indexes, right_part_indexes):
        assert len(left_part_indexes) == len(right_part_indexes), f'when removing from both parts number of items should be equal, left part is {self.left_part} and right part is {self.right_part}'
        

        for i in range(len(left_part_indexes)):
            to_fade_out = VGroup(self.left_part[left_part_indexes[i]], self.right_part[right_part_indexes[i]])
            self.play(FadeOut(to_fade_out))
            
        for i in self.get_indexes_for_removing(left_part_indexes):
            self.left_part.remove(self.left_part[i])

        for i in self.get_indexes_for_removing(right_part_indexes):
            self.right_part.remove(self.right_part[i])
                        
        print('removes')
            
        # objs = [i for i, j in enumerate(self.left_part_list_of_str) if j == '']









    # @staticmethod
    # def kettlebell_weights_vgroup(kettlebells):
    #     return VGroup(*kettlebells)

    def split_kettlebell_into_several(self, kettlebell_index, new_weights, part='left'):
        """Function splits given kettlebell into new ones with given weights

        Args:
            kettlebell_index (int): index in its part list
            new_weights (list of int): weights of smaller kettlebells 
            part (string): either 'left' or 'right' 

        Note:
            also updates `self.left_part` or `self.right_part` attributes

        Raises:
            Exception: if sum of new_weights isn't equal to kettlebells weight


        """
        kettlebell : Weight = self.left_part[kettlebell_index] if part.lower().startswith('left') else self.right_part[kettlebell_index]

        if part.lower().startswith('le'):
            if kettlebell.kg != sum(new_weights):
                raise Exception(f"You can't split {kettlebell.kg} kettlebell into kettlebells with weights {new_weights}")
        else:
            if kettlebell.kg != sum(new_weights):
                raise Exception(f"You can't split {kettlebell.kg} kettlebell into kettlebells with weights {new_weights}")



        new_kettlebells = [Weight(w, kettlebell.scale_factor) for w in new_weights]
        new_weights_vgroup = VGroup(*new_kettlebells).arrange()

        new_weights_vgroup.move_to(kettlebell.weight.get_center() + np.array([0.3 * len(new_weights),0,0]))
        self.play(ReplacementTransform(kettlebell, new_weights_vgroup))

        if part.lower().startswith('le'):
            self.left_part.remove(kettlebell)
            self.left_part.add(*new_kettlebells)
        if part.lower().startswith('ri'):
            self.right_part.remove(kettlebell)
            self.right_part.add(*new_kettlebells)



    def combine_kettlebells(self, kettlebells_indexes, part='left'):
        kettlebells = list(self.left_part[i] for i in kettlebells_indexes) if part.lower().startswith('le') else list(self.right_part[i] for i in kettlebells_indexes)
        # kettlebells = VGroup(*[i.weight for i in self.left_part[kettlebells_indexes]]) if part.lower().startswith('le') else VGroup(*[i.weight for i in self.right_part[kettlebells_indexes]])0
        

        big_kettlebell_weight = sum([i.kg for i in kettlebells])

        # in centre
        # big_kettlebell_position = np.mean([i.weight.get_center() for i in kettlebells], axis=0)
        # next to previous
        big_kettlebell_position = kettlebells[0].weight.get_center()
        

        big_kettlebell = Weight(big_kettlebell_weight, kettlebells[0].scale_factor)

        big_kettlebell.move_to(big_kettlebell_position + np.array([0.1, 0, 0]))

        self.play(ReplacementTransform(VGroup(*kettlebells), big_kettlebell))

        if part.lower().startswith('le'):
            self.left_part.remove(*kettlebells)
            self.left_part.add(big_kettlebell)
        if part.lower().startswith('ri'):
            self.right_part.remove(*kettlebells)
            self.right_part.add(big_kettlebell)

    def show_answer(self):
        equal = MathTex('=').scale(4)
        
        self.play(Write(equal))

        self.play(self.left_part.animate.next_to(equal, LEFT))

        self.play(self.right_part.animate.next_to(equal, RIGHT))
        self.play(ReplacementTransform(self.right_part, Text(f"{self.right_part[0].kg} կգ").scale(1.6).next_to(equal, RIGHT)))
        
        # self.left_part.move_to(equal)
        # self.right_part.move_to(equal)



class Problem_11417(Scales):
    def construct(self):
        a = NumberPlane()
        self.add(a)

        scale_1 = SVGMobject(os.path.join('Objects', 'SVG_files', 'scales', 'scale_1.svg')).scale(1)#.set_color(WHITE)
        scale_1.shift(3.5*LEFT)
        
        scale_2 = SVGMobject(os.path.join('Objects', 'SVG_files', 'scales', 'scale_1.svg')).scale(1)#.set_color(WHITE)
        scale_2.shift(3.5*RIGHT)

        self.play(DrawBorderThenFill(VGroup(scale_1, scale_2
            )))
        


        self.left_part_list_of_str = ['mushroom', 'mushroom']
        self.right_part_list_of_str = ['kb_6_kg', 'apple', 'apple', 'apple']
        
        # self.add_objects(self.left_part_list_of_str, self.right_part_list_of_str, left_part_shift=2*LEFT+0.5*UP,  right_part_shift=RIGHT*2.5+0.5*UP, creation_runtime=0.4)
