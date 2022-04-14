import sys

sys.path.append('../../')
from Functions.qarakusi import *
from manim.mobject.geometry import ArrowTriangleTip, ArrowTriangleFilledTip, ArrowSquareFilledTip,\
                                ArrowCircleTip, ArrowCircleFilledTip
from Board import Board, T4

# --------- IMPORTS
from pathlib import Path
import os
# ---------- FLAGS
RESOLUTION = ""
FLAGS = f"-pql {RESOLUTION}"
SCENE = "a3h8"

if __name__ == '__main__':
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {FLAGS} {script_name} {SCENE}")

class MyCustomArrowTip(ArrowTip, RegularPolygon):
	def __init__(self, length=0.35, **kwargs):
		RegularPolygon.__init__(self, n=3, fill_opacity=1, **kwargs)
		self.width = length
		#self.stretch_to_fit_height(length)

class CustomTipExample(Scene):
	def construct(self):
		arr = Arrow(np.array([-1, -1, 0]), np.array([1, 1, 0]), tip_shape=MyCustomArrowTip)
		self.play(Create(arr))
		arr1 = Arrow(np.array([-3, -3, 0]), np.array([3, 3, 0]), tip_shape=MyCustomArrowTip).shift(2*RIGHT)
		self.play(Create(arr1))

class arrow(VMobject):
	def __init__(self, start, end, length=0.25):
		VMobject.__init__(self)
		v = end - start
		l = (v[0]**2+v[1]**2)**0.5
		v *= (l-length)/l
		end1 = start + v
		line = Line(start, end1)
		
		u = np.array([-v[1],v[0],0])
		lu = (u[0]**2+u[1]**2)**0.5
		u *= length/(3**0.5)
		u /= lu
		corner1 = end1 + u
		corner2 = end1 - u
		tip = Triangle([corner1, corner2, end])
		tip.set_fill(WHITE)
		self.add(line, tip)
class a3h8(Scene):
	#def __init__(self):
	#	Scene.__init__(self)
	CONFIG = {
	'lose_color' : RED
	}
	def moves(self, x,y):
		self.arrows = list()
		for i in range(self.columns-x):
			for j in range(self.rows-y):
				if i!=0 or j!=0:
					arr = Arrow(self.board.cells[x][y].get_center(), self.board.cells[x+i][y+j].get_center(),tip_shape=ArrowTriangleTip)
					arr.tip.length = 0.35
					self.arrows.append(arr)
		self.add(*self.arrows)
	def construct(self):
		self.lose_color = RED
		self.columns = 8
		self.rows = 8
		self.size = 0.75
		self.board = Board(columns=self.columns, rows=self.rows, size=self.size)
		self.add(self.board)
		self.play(
			self.board.animate.color_cell([6,7], self.lose_color).color_cell([7,6], self.lose_color)
			)
		self.wait()

		queen = SVGMobject('queen.svg')
		queen.color = WHITE
		queen.width = self.board.cells[0][0].width*0.75
		queen.move_to(self.board.cells[7][6])
		self.play(Create(queen))
		self.wait()


		#self.moves(4,5)
		x=5
		y=4
		self.arrows = list()
		for i in range(self.columns-x):
			for j in range(self.rows-y):
				if i!=0 or j!=0:
					#arr = Arrow(np.array(self.board.cells[x][y].get_center()), np.array(self.board.cells[x+i][y+j].get_center()),tip_shape=ArrowTriangleFilledTip)
					#arr.tip.set(length=0.35)
					arr = arrow(self.board.cells[x][y].get_center(),self.board.cells[x+i][y+j].get_center())
					self.add(arr)
		self.add(*self.arrows)
		self.wait()
print(Board.__doc__)
