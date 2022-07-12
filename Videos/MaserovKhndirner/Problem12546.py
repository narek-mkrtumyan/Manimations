import sys
sys.path.append("../../")
from Functions.qarakusi import *

class Problem12546(MaserovKhndirScene):
    def __init__(self):
        MaserovKhndirScene.__init__(self)

        self.task = Task(
                Tex('$\#12546$', font_size=DEFAULT_TASK_NUMBER_FONT_SIZE), 
                MathTex(
                    r'\textrm{Ռուբենն ունի } 10 \textrm{-ով ավել քիչ մատիտ, քան Լիլիթը։}',
                    r'\textrm{Քանի՞ մատիտ ունի Ռուբենը, եթե նրանք միասին ունեն } 24 \textrm{ հատ։}',
                    tex_template=ARMTEX, font_size=DEFAULT_TASK_NUMBER_FONT_SIZE
                )
            )
        self.name_1 = 'Ռուբեն'
        self.name_2 = 'Լիլիթ'
        self.extra_length = 10
        self.total_length = 24
        self.wanted = 'first'

        self.problem = SimpleTwoPartsProblem(
                self.task,
                self.name_1, 
                self.name_2,
                self.extra_length,
                self.total_length,
                self.wanted
            )
    
    def construct(self):
        
        self.play_task(self.task)
        self.PlayProblemCopying(self.problem)
        self.PlaySolution(self.problem)
