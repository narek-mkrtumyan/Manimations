from ctypes import alignment
from turtle import down
from manim import *
import sys
sys.path.append('../../')
from Functions.QarakusiFunctions import *

arm_and_left = TexTemplate()
arm_and_left.add_to_preamble('''\\usepackage{armtex}
\\usepackage[a4paper, total={6in, 8in}]{geometry}''')

class Third(Scene):
    def given(self):
        problem_number = Tex('Խնդիր 3', tex_template=armenian_tex_template, font_size=28)
        problem_number.to_corner(UL).set_color(GREEN).shift(0.25*LEFT)
        self.problem = Tex('''\\raggedright Մաթեմիայում կա 20 քաղաք, որոնք իրար են միացված ավտոմոբիլային ճանապարհներով։ Բարեփոխումների շրջանակում 
                            Մաթեմիայի թագավորը հանձնարարում է ցանկացած երկու քաղաքների միջև ապահովել 
                            կա՛մ ''', 'օդային (ինքնաթիռով)', ' կա՛մ', ' երկաթուղային (գնացքով) ',
                            '''տրանսպորտային կապ, ընդ որում երկու քաղաքների միջև չի միաժամանակ կարող լինել
                            երկաթուղային և օդային կապ։ Մաթեմիայի թագավորը վախենում է ինքնաթիռով թռիչքներից,
                            ուստի տրանսպորտի նախարարը ցանկանում է այնպես կազմակերպել երթևեկությունը,
                            որ թագավորը ցանկացած քաղաքից ցանկացած այլ քաղաք կարողանա հասնել գնացքի
                            միջոցով։ Առավելագույնը ''', 'քանի՞ ', '''օդային երթուղի պետք է թույլատրել Մաթեմիայում, որպեսզի
                            ավիաընկերությունների կողմից օդային թռիչքների կազմակերպումից անկախ թագավորը
                            կարողանա այցելել բոլոր քաղաքները:''',
tex_template=arm_and_left,font_size=25)
        self.problem.to_edge(UP)
        self.add(problem_number)
        self.add(self.problem)
        
        self.play(Create(self.G))

        city = Text('Քաղաքներ')
        city.move_to(self.G[1].get_center()+3*RIGHT)
        self.play(Write(city))
        arr = Arrow(city, self.G[1])
        self.play(Create(arr))

        decimal = Integer(1, unit=None)
        decimal.next_to(city, RIGHT)
        tracker = ValueTracker(value=1)
        decimal.add_updater(lambda d: d.set_value(tracker.get_value()))
        self.play(Write(decimal))
        self.play(self.G[1].animate.set_color(PURE_RED))
        k=2
        for i in self.G:
            self.play(Rotate(self.G, angle=-PI/10), run_time=0.25)
            tracker.set_value(k)
            if k!=20:
                k+=1
        self.play(
            FadeOut(city), FadeOut(arr), FadeOut(decimal),
            self.G[1].animate.set_color(WHITE)
            )
        train = VGroup(
            Line(start=np.array([- 2., 0., 0.]), end=np.array([2., 0., 0.]), color=self.black),
            Text('Երկաթուղային', color=self.black, font_size=40))
        train.arrange(DOWN)
        plane = VGroup(
            Line(start=np.array([- 2., 0., 0.]), end=np.array([2., 0., 0.]), color=self.white), 
            Text('Օդային', color=self.white, font_size=40))

        plane.arrange(DOWN)
        settings = VGroup(train, plane).arrange(DOWN, buff=1)
        settings.move_to(self.G.get_center()+6*RIGHT)
        self.play(Write(settings[0]))
        self.play(
            self.problem[3].animate.set_color(self.black),
            Wiggle(settings[0]), Wiggle(self.problem[3]))
        self.play(Write(settings[1]))
        self.play(
            self.problem[1].animate.set_color(self.white),
            Wiggle(settings[0]), Wiggle(self.problem[1]))
        self.wait()

        self.G.add_edges(*[(1,10), (4,17)], edge_config={ (1,10) : {'color' : self.black}, (4,17): self.white })
        self.remove(self.G.edges[(1,10)], self.G.edges[(4,17)])
        self.play(TransformFromCopy(train[0], self.G.edges[(1,10)]))
        self.play(TransformFromCopy(plane[0], self.G.edges[(4,17)]))
        self.add(self.G)
        self.play(FadeOut(self.G.edges[(1,10)]), FadeOut(self.G.edges[(4,17)]))
        self.wait()

    def solution(self):
        n = 'n'
        ten = 10
        problem_number = Tex('Խնդիր 3', tex_template=armenian_tex_template, font_size=28)
        problem_number.to_corner(UL).set_color(GREEN).shift(0.25*LEFT)
        self.problem = Tex('''\\raggedright Մաթեմիայում կա 20 քաղաք, որոնք իրար են միացված ավտոմոբիլային ճանապարհներով։ Բարեփոխումների շրջանակում 
                            Մաթեմիայի թագավորը հանձնարարում է ցանկացած երկու քաղաքների միջև ապահովել 
                            կա՛մ ''', 'օդային (ինքնաթիռով)', ' կա՛մ', ' երկաթուղային (գնացքով) ',
                            '''տրանսպորտային կապ, ընդ որում երկու քաղաքների միջև չի միաժամանակ կարող լինել
                            երկաթուղային և օդային կապ։ Մաթեմիայի թագավորը վախենում է ինքնաթիռով թռիչքներից,
                            ուստի տրանսպորտի նախարարը ցանկանում է այնպես կազմակերպել երթևեկությունը,
                            որ թագավորը ցանկացած քաղաքից ցանկացած այլ քաղաք կարողանա հասնել գնացքի
                            միջոցով։ Առավելագույնը ''', 'քանի՞ ', '''օդային երթուղի պետք է թույլատրել Մաթեմիայում, որպեսզի
                            ավիաընկերությունների կողմից օդային թռիչքների կազմակերպումից անկախ թագավորը
                            կարողանա այցելել բոլոր քաղաքները:''',
tex_template=arm_and_left,font_size=25)
        self.problem.to_edge(UP)

        #self.add(self.problem)
        self.add(self.G)

        self.play(
            self.problem[5].animate.set_color(RED),
            Wiggle(self.problem[5]))
        whites = VGroup(*[Line(UP, DOWN, color=self.white) for i in range(10)]).arrange(RIGHT)
        quantity = VGroup(Brace(whites), Tex(f"{n}")).arrange(DOWN)
        quantity.next_to(whites, DOWN)
        first = VGroup(whites, quantity)
        first.move_to(self.G.get_center()+6*RIGHT)
        self.play(Create(whites))
        self.play(Write(quantity[0]))
        self.play(TransformFromCopy(self.problem[5], quantity[1]))
        self.wait()

        white_edges = [
            (1,7), (4,5), (10,15), (10,2), (20,9),
            (6,17), (12, 3), (11, 16), (5, 18), (8,9)
        ]
        self.G.add_edges(*white_edges)
        for i,j in white_edges:
            self.G.edges[(i,j)].set_color(self.white)
        self.remove(*[self.G.edges[(i,j)] for i,j in white_edges])

        self.play(*[
            Transform(whites[i], self.G.edges[white_edges[i]]) for i in range(10)
        ])
        self.add(self.G)
        self.wait()

        black_edges = []
        for i in range(1,21):
            for j in range(i,21):
                if not ( (i,j) in white_edges or (j,i) in white_edges ):
                    black_edges.append((i,j))
        self.G.add_edges(*black_edges)
        for i,j in black_edges:
            self.G.edges[(i,j)].set_color(self.black)
        self.remove(*[self.G.edges[(i,j)] for i,j in black_edges])        
        self.play(*[
            Create(self.G.edges[pair]) for pair in black_edges
        ], run_time=2)
        self.wait()

        

    def construct(self):
        self.white = BLUE
        self.black = ORANGE
        
        vertices = range(1,21)
        #edges = [(i,j) for i in range(1,21) for j in range(i, 21)]
        edges = []
        #for i in range(1,21):
        #    for j in range(i, 21):
        #        edges.append((i,j))
        self.G = Graph(vertices, edges, layout='circular').scale(0.75)
        self.G.shift(4*LEFT+2*DOWN)

        #self.given()
        self.solution()