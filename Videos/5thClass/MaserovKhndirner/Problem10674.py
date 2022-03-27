import sys
sys.path.append('../../../')
from Functions.qarakusi import *



class Problem10674(MaserovKhndirScene):
    def __init__(self):
        MaserovKhndirScene.__init__(self)

        self.task = Task(
                Tex('$\#10674$', font_size=DEFAULT_TASK_NUMBER_FONT_SIZE), 
                Tex(
                    'Գտնել երկու թիվ, որոնց գումարը $51$ է,',
                    'իսկ տարբերությունը՝ $13$։',
                    tex_template=ARMTEX, font_size=DEFAULT_TASK_NUMBER_FONT_SIZE
                )
            )
        self.name_1 = 'Առաջին'
        self.name_2 = 'Երկրորդ'
        self.extra_length = 13
        self.total_length = 51
        self.wanted = 'both'

        self.problem = SimpleTwoPartsProblem(
                self.name_1, 
                self.name_2,
                self.extra_length,
                self.total_length,
                self.wanted
            )
    
    def construct(self):

        self.play_task(self.task)
        self.PlayProblemProjecting(self.problem)
        self.PlaySolution(self.problem, indication=ApplyWave)
    
