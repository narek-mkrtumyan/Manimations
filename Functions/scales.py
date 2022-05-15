from .qarakusiscene import *
from typing import List


class ScalesWithItems(VGroup):
    def __init__(
        self,
        left_mobs_list_of_str : List[str], right_mobs_list_of_str : List[str], 
        weight_scale_factor=0.75, fruit_scale_factor=1, scales_scale_factor=1, scales_plate_stretch_factor=1
    ):
        VGroup.__init__(self)

        self.weight_scale_factor = weight_scale_factor
        self.fruit_scale_factor = fruit_scale_factor
        self.scales_plate_stretch_factor = scales_plate_stretch_factor

        self.scales = Scales(5, scales_plate_stretch_factor).scale(scales_scale_factor)
        
        self.left_mobs = self.convert_list_of_items_to_list_of_mobjects(left_mobs_list_of_str)
        self.left_mobs = VGroup(*self.left_mobs).arrange(aligned_edge=DOWN).next_to(self.scales.left_plate, UP, buff=DEFAULT_SCALES_BUFF)

        self.right_mobs = self.convert_list_of_items_to_list_of_mobjects(right_mobs_list_of_str)
        self.right_mobs = VGroup(*self.right_mobs).arrange(aligned_edge=DOWN).next_to(self.scales.right_plate, UP, buff=DEFAULT_SCALES_BUFF)

        self.add(self.scales, self.left_mobs, self.right_mobs)

    def convert_list_of_items_to_list_of_mobjects(self, items):
        """Function takes as input list of strings and converts it to list 
        of mobjects

        Note:
            Options for input are` ['apple', 'weight_{n}']
    
        Args:
            items (list of strings): items to convert to mobjects

        Returns:
            mobjs (list of mobjects)

        Examples:
            convert_list_of_items_to_list_of_mobjects(['apple', 'apple', 'weight_'])
        """

        mobjs = []
        for i in items:
            if i.lower() == "red_apple":
                mobjs.append(Apple(RED).scale(self.fruit_scale_factor))
            elif i.lower() == "green_apple":
                mobjs.append(Apple(GREEN).scale(self.fruit_scale_factor))
            elif i.lower() == "mushroom":
                mobjs.append(Mushroom().scale(self.fruit_scale_factor))
            elif i.lower().startswith('weight'):
                weight_weight = int(i.split('_')[1])
                mobjs.append(Weight(weight_weight, scale_factor=self.weight_scale_factor))
            else:
                raise ValueError("Pass a valid fruit name or \'weight_value\'")
        return mobjs






class ScalesScene(QarakusiScene):

    @staticmethod
    def get_indexes_for_removing(mylist):
        return list(j - i for i, j in enumerate(mylist))

    def add_scales_items(self, scales_with_items : ScalesWithItems, display_option=FadeIn, unit_creation_runtime : float=0.75):
        """Function plays the animation of creating items and initializes 
        `self.left_mobs` and `self.right_mobs` attributes 

        Note:
            self.left_mobs and self.right_mobs are VGroups

        Args:
            left_mobs (list of strings): see list of allowed options is docstring of function above 
            right_mobs (list of strings):
            left_mobs_shift (np.array): where to position left plate default` LEFT * 4
            right_mobs_shift (np.array): where to position right plate default` RIGHT * 3
            display_option (str): one of ['Create', "FadeIn"] default is FadeIn
            unit_creation_runtime (float): creation time for each item default` 0.75

        Returns:
            None
        """

        for i in scales_with_items.left_mobs:
            self.play(display_option(i), run_time=unit_creation_runtime)

        for i in scales_with_items.right_mobs:
            self.play(display_option(i), run_time=unit_creation_runtime)

    
    def remove_objects_from_both_sides(self, scales_with_items : ScalesWithItems, left_mobs_indexes, right_mobs_indexes):
        
        left_mobs = VGroup(*[scales_with_items.left_mobs[i] for i in left_mobs_indexes])
        right_mobs = VGroup(*[scales_with_items.right_mobs[i] for i in right_mobs_indexes])
        to_fade_out = VGroup(*left_mobs, *right_mobs)
        self.play(to_fade_out.animate.shift(UP))
        self.play(FadeOut(to_fade_out))
        self.remove(to_fade_out)

        for i in self.get_indexes_for_removing(left_mobs_indexes):
            scales_with_items.left_mobs.remove(scales_with_items.left_mobs[i])

        for i in self.get_indexes_for_removing(right_mobs_indexes):
            scales_with_items.right_mobs.remove(scales_with_items.right_mobs[i])
                        


    def split_weight(self, scales_with_items : ScalesWithItems, side : str, weight_index : int, new_weights : List[int]):
        """Function splits given weight into new ones with given weights

        Args:
            weight_index (int): index in its side list
            new_weights (list of int): weights of smaller weights 
            side (string): either 'left' or 'right' 

        Note:
            also updates `self.left_mobs` or `self.right_mobs` attributes

        Raises:
            Exception: if sum of new_weights isn't equal to weights weight

        """

        if side == 'right':
            weight : Weight = scales_with_items.right_mobs[weight_index]

            print(weight.scale_factor)

            if weight.weight_value != sum(new_weights):
                raise Exception(f"You can't split {weight.weight_value} weight into weights with weights {new_weights}")
            
            new_weights_vgroup = VGroup(*[Weight(w, scale_factor=weight.scale_factor) for w in new_weights])
            new_weights_vgroup.arrange(buff=0.1, aligned_edge=DOWN).move_to(weight.get_center()).align_to(weight, DOWN)

            temporary_mobs = scales_with_items.right_mobs.copy()
            temporary_mobs.remove(temporary_mobs[weight_index])

            self.play(Transform(scales_with_items.right_mobs[weight_index], new_weights_vgroup, remover=True))

            self.remove(scales_with_items.right_mobs)
            scales_with_items.right_mobs = VGroup(*new_weights_vgroup, *temporary_mobs)
            self.add(scales_with_items.right_mobs)

        
        elif side == 'left':
            weight : Weight = scales_with_items.left_mobs[weight_index]

            print(weight.scale_factor)

            if weight.weight_value != sum(new_weights):
                raise Exception(f"You can't split {weight.weight_value} weight into weights with weights {new_weights}")
            
            new_weights_vgroup = VGroup(*[Weight(w, scale_factor=weight.scale_factor) for w in new_weights])
            new_weights_vgroup.arrange(buff=0.1, aligned_edge=DOWN).move_to(weight.get_center()).align_to(weight, DOWN)

            temporary_mobs = scales_with_items.left_mobs.copy()
            temporary_mobs.remove(temporary_mobs[weight_index])

            self.play(Transform(scales_with_items.left_mobs[weight_index], new_weights_vgroup, remover=True))

            self.remove(scales_with_items.left_mobs)
            scales_with_items.left_mobs = VGroup(*new_weights_vgroup, *temporary_mobs)
            self.add(scales_with_items.left_mobs)




    def combine_weights(self, scales_with_items : ScalesWithItems, side, kettlebells_indexes : List[int], new_place : str = 'center'):

        if side.lower().startswith('le'):
            kettlebells = list(scales_with_items.left_mobs[i] for i in kettlebells_indexes)
        else:
            kettlebells = list(scales_with_items.right_mobs[i] for i in kettlebells_indexes)

        big_kettlebell_weight = sum([i.weight_value for i in kettlebells])

        if new_place == 'center':
            big_kettlebell_position = VGroup(*kettlebells).get_center()
        if new_place == 'left':
            big_kettlebell_position = kettlebells[0].get_center()
        if new_place == 'right':
            big_kettlebell_position = kettlebells[-1].get_center()

        big_kettlebell = Weight(big_kettlebell_weight, scale_factor=kettlebells[0].scale_factor)
        big_kettlebell.move_to(big_kettlebell_position).align_to(kettlebells[0], DOWN)

        self.play(ReplacementTransform(VGroup(*kettlebells), big_kettlebell))

        if side.lower().startswith('le'):
            scales_with_items.left_mobs.remove(*kettlebells)
            scales_with_items.left_mobs.add(big_kettlebell)
        if side.lower().startswith('ri'):
            scales_with_items.right_mobs.remove(*kettlebells)
            scales_with_items.right_mobs.add(big_kettlebell)


    def reorder_scales_objects(self, scales_side_mobs : VGroup()):
        weights = VGroup()
        fruits = VGroup()
        for mob in scales_side_mobs:
            if type(mob) == Weight:
                weights.add(mob)
            else:
                fruits.add(mob)
        
        new_order_mobs = VGroup(*fruits.copy(), *weights.copy())
        new_order_mobs.arrange(aligned_edge=DOWN).move_to(scales_side_mobs.get_center())
        new_order_places = [mob.get_center() for mob in new_order_mobs]
        
        self.play(weights.animate.shift(UP))
        self.play(
            *[fruits[i].animate.move_to(new_order_places[i]) for i in range(len(fruits))],
            *[weights[j].animate.move_to(new_order_places[j + len(fruits)] + UP) for j in range(len(weights))]
        )
        self.play(weights.animate.shift(DOWN))

        for mob in scales_side_mobs:
            scales_side_mobs.remove(mob)

        scales_side_mobs.add(*fruits, *weights)



