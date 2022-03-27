import sys

sys.path.append('../../../')
from Functions.qarakusi import *

class ConferenceTable(VMobject):
    def __init__(self, radius=2, number_of_people=8, hbuff=0.85, nbuff=0.35, labels='default', label_color=RED, numbers='default', number_color=WHITE, **kwargs):
        VMobject.__init__(self, **kwargs)

        self.circle_radius = radius
        self.circle = Circle(radius=radius, color=DARK_BROWN)
        self.number_of_people = number_of_people
        self.hbuff = hbuff
        self.nbuff = nbuff

        coords = self.__man_coords()
        man = Man(8)
        man.set_color(WHITE).scale(0.75)
        #man = ImageMobject('man_relax.png')
        #man.set_color(WHITE)
        self.profs = VGroup(*[man.copy().move_to(coord) for coord in coords])
        # assign labels to profs
        self.labels = VGroup()
        for i, prof in enumerate(self.profs):
            if labels == 'default':
                labels = range(1,self.number_of_people+1)
            self.labels += Tex(f'{labels[i]}', color=label_color).scale(0.9).move_to(prof).shift(0.2*UP)
        # flip profs
        n = self.number_of_people
        for i in range((n+1)//2, n):
            self.profs[i].flip()
        coords = self.__number_coords()
        self.numbers = VGroup()
        for i, coord in enumerate(coords):
            if numbers == 'default':
                numbers = range(1,self.number_of_people+1)
            self.numbers += Tex(f'{numbers[i]}').move_to(coord) 
        self.add(self.circle, self.profs, self.labels, self.numbers)

        self.the_table = VGroup(self.circle, self.numbers)
        self.the_profs = VGroup(self.profs, self.labels)
    def __man_coords(self):
        lst = np.zeros((self.number_of_people, 3))
        for i in range(self.number_of_people-1, -1, -1):
            coords = self.circle.get_center()
            coords += (np.sin(-i*TAU/self.number_of_people+PI/2)*UP + np.cos(-i*TAU/self.number_of_people+PI/2)*RIGHT) * (self.circle_radius + self.hbuff)
            lst[i] = coords
        return lst
    def __number_coords(self):
        lst = np.zeros((self.number_of_people, 3))
        for i in range(self.number_of_people-1, -1, -1):
            coords = self.circle.get_center()
            coords += (np.sin(-i*TAU/self.number_of_people+PI/2)*UP + np.cos(-i*TAU/self.number_of_people+PI/2)*RIGHT) * (self.circle_radius - self.nbuff)
            lst[i] = coords
        return lst
    def add_rotation_arrow(self, left=True, time=True):
        r = self.circle.width/2
        if left:
            side = LEFT
            if time:
                self.arrow = CurvedArrow(r*DOWN, r*UP).next_to(self.circle, side).flip()
            else:
                self.arrow = CurvedArrow(r*UP, r*DOWN).next_to(self.circle, side)
        else:
            side = RIGHT
            if time:
                self.arrow = CurvedArrow(r*UP, r*DOWN).next_to(self.circle, side).flip()
            else:
                self.arrow = CurvedArrow(r*DOWN, r*UP).next_to(self.circle, side)
        return self
        


class conference(Scene):
    def multirotate_table(self, table, time=False, many=2, run_time=1):
        n = table.number_of_people
        radius = table.circle_radius - table.nbuff
        if time:
            self.play(*[
                MoveAlongPath(
                    number,
                    ArcBetweenPoints(
                        start=number.get_center(), end=table.numbers[(i-many)%n].get_center(),
                        angle=2*PI*many/n)
                    ) for i, number in enumerate(table.numbers)
            ], run_time=run_time)
        else:
            self.play(*[
                MoveAlongPath(
                    number,
                    ArcBetweenPoints(
                        start=table.numbers[(i+many)%n].get_center(), end=number.get_center(),
                        angle=2*PI*many/n).reverse_direction()
                    )
                    for i, number in enumerate(table.numbers)
            ], run_time=run_time)
    def rotate_table(self, table, time=False, many=1, run_time=1):
        n = table.number_of_people
        radius = table.circle_radius - table.nbuff
        if time:
            for _ in range(many):
                self.play(*[
                    MoveAlongPath(
                        number,
                        ArcBetweenPoints(
                            start=number.get_center(), end=table.numbers[(i-1)%n].get_center(),
                            angle=2*PI/n)
                        ) for i, number in enumerate(table.numbers)
                ], run_time=run_time)
        else:
            for _ in range(many):
                self.play(*[
                    MoveAlongPath(
                        number,
                        ArcBetweenPoints(
                            start=table.numbers[(i+1)%n].get_center(), end=number.get_center(),
                            angle=2*PI/n).reverse_direction()
                        )
                        for i, number in enumerate(table.numbers)
                ], run_time=run_time)
    def problem(self):
        table = self.table
        self.rotate_table(table, time=True, many=2)
        self.wait()

        self.play(FadeOut(table.the_profs))

        self.play(table.the_table.animate.shift(3*LEFT))
        ctable = table.the_table.copy()
        timearrow = CurvedArrow(DOWN, UP).next_to(table.circle, LEFT).flip()
        self.play(ctable.animate.shift(3*RIGHT))
        ntimearrow = CurvedArrow(UP, DOWN).next_to(ctable[0], LEFT)
        self.play(Create(timearrow), Create(ntimearrow))
        self.wait()

        step1 = Tex('$k$').next_to(timearrow, LEFT)
        step2 = Tex('$n-k$').next_to(ntimearrow, LEFT)

        self.play(Write(step1), Write(step2))
        self.wait()

    def all_rotations(self):
        table = self.table
        table.scale(0.75)
        self.add(table.the_table)
        tables = VGroup(*[table.copy() for _ in range(8)]).arrange_in_grid(rows=2, cols=4)

        for i, table in enumerate(tables):
            table.add_rotation_arrow(left=False, time=True)
            self.play(Create(table.arrow))
            self.wait()
            tracker = ValueTracker(1)
            n = Integer(1).next_to(table.arrow, RIGHT)
            def updater(mobject):
                mobject.set_value(tracker.get_value())
            n.add_updater(updater)
            self.play(Write(n))
            for _ in range(i):
                self.rotate_table(table, run_time=0.75)
                tracker += 1
            self.wait()

        

    def construct(self):
        #number = Tex('Խնդիր', tex_template=armenian_tex_template, color=GREEN)
        #given = Tex('', tex_template=armenian_tex_template)
        n = 9
        labels = range(1,n+1)
        labels = [1,2,3,4,'.','.','.', '$n$']
        numbers = [1,2,3,4,'.','.','.', '$n$']
        #self.table = ConferenceTable(number_of_people=n, labels=labels, numbers=numbers)
        self.table = ConferenceTable(number_of_people=n)
        table = self.table
        table.scale(0.75)
        # self.play(Create(table.circle))
        # self.play(Write(table.numbers))
        # self.play(FadeIn(table.profs))
        # self.play(Write(table.labels))
        # self.wait()

        # self.problem()
        self.all_rotations()