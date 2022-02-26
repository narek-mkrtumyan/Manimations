import sys
from venv import create

from numpy import dtype
sys.path.append('../../')
from Functions.QarakusiFunctions import *

class sync(Scene):
    def construct(self):
        board = Board(size=1.5, rows=3, columns=3)
        board.make_chess(white=BLUE_A, black=BLUE_E)
        
        start = Tex('Սկիզբ', tex_template=armenian_tex_template, font_size=30)
        start_dot = Dot().set_color(BLACK)
        start_dot.move_to(board.cells[2][0])
        start.next_to(start_dot, UP/2)
        end = Tex('Ավարտ', tex_template=armenian_tex_template, font_size=30)
        end_dot = Dot().set_color(BLACK)
        end_dot.move_to(board.cells[2][2])
        end.next_to(end_dot, UP/2)
        #self.add(board, start, start_dot, end, end_dot)
        self.wait()
        self.play(FadeIn(board))
        self.play(
            Write(start), Create(start_dot),
            Write(end), Create(end_dot))
        self.wait(20)
        vlines = VGroup(
            Line(board.cells[2][0].get_center(), board.cells[1][0].get_center(),stroke_width=5),
            Line(board.cells[1][0].get_center(), board.cells[0][0].get_center(),stroke_width=5), 
            Line(board.cells[0][2].get_center(), board.cells[1][2].get_center(),stroke_width=5), 
            Line(board.cells[1][1].get_center(), board.cells[2][1].get_center(),stroke_width=5)
        )
        hlines = VGroup(
            Line(board.cells[0][0].get_center(), board.cells[0][1].get_center(),stroke_width=5),
            Line(board.cells[0][1].get_center(), board.cells[0][2].get_center(),stroke_width=5), 
            Line(board.cells[1][2].get_center(), board.cells[1][1].get_center(),stroke_width=5), 
            Line(board.cells[2][1].get_center(), board.cells[2][2].get_center(),stroke_width=5),
            Line(board.cells[1][0].get_center(), board.cells[1][1].get_center(),stroke_width=5)
        )

        vlines.set_color(RED)
        hlines.set_color(RED)

        self.play(Create(vlines[0]), run_time=2)
        self.add(start_dot)
        self.wait(2)
        
        self.play(Create(hlines[4]), run_time=2)
        self.wait()
        self.play(Uncreate(hlines[4]), run_time=2)
        self.wait()

        self.play(Create(vlines[1]), run_time=2)
        self.wait(2)
        
        self.play(Create(hlines[0]), run_time=2)
        self.wait(2)
        self.play(Create(hlines[1]), run_time=2)
        self.play(Create(vlines[2]), run_time=2)
        self.wait(2)
        self.play(Create(hlines[2]), run_time=2)
        self.play(Create(vlines[3]), run_time=2)
        self.play(Create(hlines[3]), run_time=2)
        self.add(end_dot)
        self.wait()
