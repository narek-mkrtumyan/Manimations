import sys

sys.path.append('../../')
from Functions.qarakusi import *
import csv
import pandas as pd
from numpy import genfromtxt


# --------- IMPORTS
from pathlib import Path
import os
# ---------- FLAGS
RESOLUTION = ""
FLAGS = f"-pql {RESOLUTION} -s"
SCENE = "Star"


if __name__ == '__main__':
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {FLAGS} {script_name} {SCENE}")

def matrix_to_VGroup(matrix):
	'''matrix-ի բոլոր տարրերով VGroup'''
	x=matrix[0][0]
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if(i!=0 or j!=0):
				x=VGroup(x, matrix[i][j])
	return x

def write_random_table(rows, columns, low, high, file_name):
	matrix = np.random.randint(low=low,high=high,size=(rows,columns))
	with open(file_name, 'w', encoding='UTF8', newline='') as f:
	    writer = csv.writer(f)
	    writer.writerows(matrix)


class tetramino(Scene):
	def construct(self):
		chess0 = Board(rows=10, columns=10, stroke_width=2).shift(3*LEFT)
		chess = Board(rows=10, columns=10, stroke_width=0.2).shift(3*LEFT)
		self.play(Create(chess0))
		self.add(chess)
		self.wait()

		T4_1 = T4(stroke_width=0.2).shift(2*UP+3*RIGHT)
		T4_2 = T4(stroke_width=0.2).shift(2*DOWN+3*RIGHT)

		T4_10 = T4(stroke_width=2).shift(2*UP+3*RIGHT)
		T4_20 = T4(stroke_width=2).shift(2*DOWN+3*RIGHT)
		self.play(Create(T4_10))
		self.add(T4_1)
		self.wait()

		self.play(FadeOut(chess0), chess.animate.make_chess())
		self.wait()

		self.play(T4_1.animate.color_cell(3, WHITE))
		self.wait()
		self.play(
			T4_1.animate.color_cell(0, WHITE).color_cell(2, WHITE)
			)
		self.wait()
		self.play(T4_1.animate.color_cell(1, DARK_BROWN), FadeOut(T4_10))
		#self.play(FadeOut(T4_10))

		self.play(Create(T4_20))
		self.add(T4_2)
		self.wait()
		self.play(T4_2.animate.color_cell(3, DARK_BROWN))
		self.wait()
		self.play(
			T4_2.animate.color_cell(0, DARK_BROWN).color_cell(2, DARK_BROWN)
			)
		self.wait()
		self.play(T4_2.animate.color_cell(1, WHITE), FadeOut(T4_20))

		myTemplate = TexTemplate()
		myTemplate.add_to_preamble(r"\usepackage{armtex}")
		text11 = Tex('3 սպիտակ', tex_template=myTemplate)
		text12 = Tex('1 սև', tex_template=myTemplate, color=DARK_BROWN)
		text22 = Tex('3 սև', tex_template=myTemplate, color=DARK_BROWN)
		text21 = Tex('1 սպիտակ',tex_template=myTemplate)
		text1 = VGroup(text11, text12)
		text1.arrange(DOWN)
		text2 = VGroup(text21, text22)
		text2.arrange(DOWN)
		text1.next_to(T4_1, RIGHT)
		text2.next_to(T4_2, RIGHT)
		self.play(Write(text2))
		self.play(Write(text1))
		self.wait()


class Knight(Scene):
	def construct(self):
		board = Board(size=1.5, rows=4, columns=4, stroke_width=2)
		board.remove(board.cells[0][0], board.cells[3][0], board.cells[0][3], board.cells[3][3])
		self.play(Create(board))
		self.wait()

		Knight = SVGMobject('Knight.svg')
		Knight.move_to(board.cells[3][1].get_center())
		Knight.width = 1

		self.play(board.cells[3][1].animate.set_fill(BLUE, opacity=1))
		self.play(Write((Knight)))
		self.wait()
		
		path = [[1,0], [2,2], [0,1], [1,3], [2,1], [0,2], [2,3], [1,1], [3,2], [2,0], [1,2], [3,1]]
		for k in range(len(path)):
			i = path[k][0]
			j = path[k][1]
			self.play(board.cells[i][j].animate.set_fill(RED, opacity=1))
			self.play(Knight.animate.move_to(board.cells[i][j].get_center()))
			if k>0:
				old_i = path[k-1][0]
				old_j = path[k-1][1]
				self.play(Write(Tex(k).move_to(board.cells[old_i][old_j].get_center())),
					board.cells[i][j].animate.set_fill(BLUE, opacity=1)
					)
			else:
				self.play(board.cells[i][j].animate.set_fill(BLUE, opacity=1))
			#self.play(Write(Tex(k+1).move_to(board.cells[i][j].get_center())))
		self.play(board.cells[3][1].animate.set_fill(RED, opacity=1))
		self.wait()
		#նշվում ա կարմիրով, ձին գալիս ա, դառնում ա կապույտ, ձին գնում ա, թիվ ա գրվում ու միգուցե միաժամանակ կապույտ ա դառնում

#myus idean ays Scene-um method greln a vor ani nerkumy
class sum(Scene):
	def do(self):
		low = -100
		high = 101
		self.dif = (high - 1 - low) / 2
	def hstep(self, i1, j1, i2, j2, change_value):
		cells = VGroup(self.board.cells[i1][j1], self.board.cells[i2][j2])
		self.play(Circumscribe(cells, color=RED))

		plus1 = Tex('$+$').next_to(self.board.cells[i1][j1], RIGHT)
		plus2 = Tex('$+$').next_to(self.board.cells[i2][j2], RIGHT)
		change1 = Integer(change_value).next_to(plus1, RIGHT)
		change2 = Integer(change_value).next_to(plus2, RIGHT)
		self.play(Write(change1), Write(change2))
		self.wait()
		
		self.play(
			Wiggle(self.board.numbers[i1][j1]),
			Wiggle(self.board.numbers[i2][j2]),
			Wiggle(change1), Wiggle(change2)
			)

		equal1 = Tex('$=$').next_to(change1, RIGHT)
		equal2 = Tex('$=$').next_to(change2, RIGHT)
		signs = VGroup(plus1, plus2, equal1, equal2)
		self.add(signs)
		self.wait(0.5)
		new1 = Integer(self.board.all_numbers[i1][j1]+change_value).next_to(equal1, RIGHT)
		new2 = Integer(self.board.all_numbers[i2][j2]+change_value).next_to(equal2, RIGHT)
		self.play(Write(new1), Write(new2))

		self.play(
			FadeOut(self.board.numbers[i1][j1]),
			FadeOut(self.board.numbers[i2][j2]),
			FadeOut(signs),
			FadeOut(change1), FadeOut(change2),
			new1.animate.move_to(self.board.cells[i1][j1]),
			new2.animate.move_to(self.board.cells[i2][j2])
			)

		self.board.all_numbers[i1][j1]+=change_value
		self.board.all_numbers[i2][j2]+=change_value

		self.board.numbers[i1][j1] = Integer(self.board.all_numbers[i1][j1]).move_to(self.board.cells[i1][j1])
		self.board.numbers[i2][j2] = Integer(self.board.all_numbers[i2][j2]).move_to(self.board.cells[i2][j2])
		self.add(self.board.numbers[i1][j1], self.board.numbers[i2][j2])
		self.remove(new1, new2)

		if self.board.all_numbers[i1][j1] >= 0:
			self.play(self.board.animate.color_cell([i1,j1], YELLOW, opacity=self.board.all_numbers[i1][j1]/self.dif))
		if self.board.all_numbers[i1][j1] < 0:
			self.play(self.board.animate.color_cell([i1,j1], BLUE, opacity=-self.board.all_numbers[i1][j1]/self.dif))
		if self.board.all_numbers[i2][j2] >= 0:
			self.play(self.board.animate.color_cell([i2,j2], YELLOW, opacity=self.board.all_numbers[i2][j2]/self.dif))
		if self.board.all_numbers[i2][j2] < 0:
			self.play(self.board.animate.color_cell([i2,j2], BLUE, opacity=-self.board.all_numbers[i2][j2]/self.dif))
		self.wait()


	def estep(self, i1, j1, i2, j2, change_value):
		cells = VGroup(self.board.cells[i1][j1], self.board.cells[i2][j2])
		self.play(Circumscribe(cells, color=RED),
			Wiggle(self.board.numbers[i1][j1]),
			Wiggle(self.board.numbers[i2][j2]))

		new1 = Integer(self.board.all_numbers[i1][j1]+change_value).move_to(self.board.cells[i1][j1])
		new2 = Integer(self.board.all_numbers[i2][j2]+change_value).move_to(self.board.cells[i2][j2])
		self.remove(self.board.numbers[i1][j1], self.board.numbers[i2][j2])
		self.add(new1, new2)

		self.board.all_numbers[i1][j1]+=change_value
		self.board.all_numbers[i2][j2]+=change_value

		self.board.numbers[i1][j1] = Integer(self.board.all_numbers[i1][j1]).move_to(self.board.cells[i1][j1])
		self.board.numbers[i2][j2] = Integer(self.board.all_numbers[i2][j2]).move_to(self.board.cells[i2][j2])
		self.add(self.board.numbers[i1][j1], self.board.numbers[i2][j2])
		self.remove(new1, new2)

		if self.board.all_numbers[i1][j1] >= 0:
			self.board.color_cell([i1,j1], YELLOW, opacity=self.board.all_numbers[i1][j1]/self.dif)
		if self.board.all_numbers[i1][j1] < 0:
			self.board.color_cell([i1,j1], BLUE, opacity=-self.board.all_numbers[i1][j1]/self.dif)
		if self.board.all_numbers[i2][j2] >= 0:
			self.board.color_cell([i2,j2], YELLOW, opacity=self.board.all_numbers[i2][j2]/self.dif)
		if self.board.all_numbers[i2][j2] < 0:
			self.board.color_cell([i2,j2], BLUE, opacity=-self.board.all_numbers[i2][j2]/self.dif)
	def construct(self):
		self.do()
		rows = 8
		columns = 8
		self.board = Board(size=0.95, rows=rows, columns=columns).shift(2*LEFT)
		self.play(Create(self.board))
		self.wait()
		
		matrix = genfromtxt('random_table.csv', delimiter=',').astype(int)
		self.board.add_numbers(matrix)

		self.add(self.board.numbers_)
		self.wait()

		self.play(self.board.animate.colorful(self.dif))
		self.wait()

		change = -matrix.item(0,7)
		self.hstep(0,7,1,7, change)
		change = -self.board.all_numbers[1][7]
		self.hstep(1,7,2,7, change)
		
		for i in range(2,7):
			change = -self.board.all_numbers[i][7]
			self.estep(i,7,i+1,7, change)
		self.wait()

class graph(Scene):
	def construct(self):
		vertices = [(1,1), (1,2), (2,1), (2,2)]
		edges = [ (vertices[0],vertices[1]),
		(vertices[1],vertices[3])
		]
		G = Graph(vertices, edges)
		self.add(G)
class Chessboard1(Table):
	def __init__(self, h_buff=0.3, v_buff=0.3, white=WHITE, black=DARK_BROWN):
		mat = list()
		for i in range(8):
			row = list()
			for j in range(8):
				row.append('T')
			mat.append(row)
		Table.__init__(self,mat,h_buff=h_buff,v_buff=v_buff,include_outer_lines=True)
		#self.set_color()
		entries = self.get_entries()
		entries.set_color(BLACK)

	def set_color(self, white=WHITE, black=DARK_BROWN):
		for i in range(8):
			for j in range(8):
				if (i+j)%2!=0:
					self.add(self.get_cell((i, j), color=black, fill_opacity=1))
				else:
					self.add(self.get_cell((i, j), color=white, fill_opacity=1))

	def remove_fields(self,l):
		for i, j in l:
			self.add(self.get_cell((i, j), color=BLACK, fill_opacity=1))
class table1(Scene):
	def construct(self):
		mat = list()
		for i in range(8):
			row = list()
			for j in range(8):
				row.append('T')
			mat.append(row)
		chess = Table(
			mat,
			h_buff=1.3,
			v_buff=1.3,
			include_outer_lines=True
			)
		entries = chess.get_entries()
		entries.set_color(BLACK)

		for i in range(8):
			for j in range(8):
				if (i+j)%2==0:
					chess.add(chess.get_cell((i, j), color=DARK_BROWN, fill_opacity=1))
				else:
					chess.add(chess.get_cell((i, j), color=WHITE, fill_opacity=1))
		#chess.add_highlighted_cell((0,0), color=WHITE)
		chess.scale(0.5)
		d = Dot(chess.get_cell((1,1)).get_center(), color=BLACK)
		self.play(Create(chess))
		self.add(d)
		self.wait()

class Star(Scene):
	def construct(self):
		star = Star(5, outer_radius=2, density=3, color=YELLOW)
		self.add(star)

#print(help(Circle))
#print(T4.__doc__)