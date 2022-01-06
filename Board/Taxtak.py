from manim import *
import numpy as np
import csv
import pandas as pd
from numpy import genfromtxt

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
		chess = Board(rows=10, columns=10, stroke_width=1).shift(2*LEFT)
		self.play(Create(chess))
		self.wait()

		T4_1 = T4(stroke_width=1).shift(2*UP+3*RIGHT)
		T4_2 = T4(stroke_width=1).shift(2*DOWN+3*RIGHT)
		self.play(Create(T4_1))
		self.wait()
		self.play(chess.animate.make_chess())
		self.wait()
		self.play(T4_1.animate.color_cell(3, WHITE))
		self.wait()
		self.play(
			T4_1.animate.color_cell(0, WHITE),
			T4_1.animate.color_cell(2, WHITE)
			)
		self.wait()
		self.play(T4_1.animate.color_cell(1, DARK_BROWN))

		self.play(Create(T4_2))
		self.wait()
		self.play(T4_2.animate.color_cell(3, DARK_BROWN))
		self.wait()
		self.play(
			T4_2.animate.color_cell(0, DARK_BROWN),
			T4_2.animate.color_cell(2, DARK_BROWN)
			)
		self.wait()
		self.play(T4_2.animate.color_cell(1, WHITE))

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
	def step(self, i1, j1, i2, j2, pop, dif):
		change = Integer(pop).shift(5*RIGHT)
		self.play(Create(change))
		self.wait()
		self.play(Wiggle(self.board.numbers[0][0]), Wiggle(self.board.numbers[0][1]), Wiggle(change))
		change1=change.copy()
		change2=change.copy()
		self.play(
			FadeOut(self.board.numbers[i1][j1]),
			FadeOut(self.board.numbers[i2][j2]),
			change1.animate.move_to(self.board.cells[i1][j1]),
			change2.animate.move_to(self.board.cells[i2][j2]),
			FadeOut(change1),
			FadeOut(change2),
			FadeOut(change))

		self.board.all_numbers[i1][j1]+=pop
		self.board.all_numbers[i2][j2]+=pop

		self.board.numbers[i1][j1] = Integer(self.board.all_numbers[i1][j1]).move_to(self.board.cells[i1][j1])
		self.board.numbers[i2][j2] = Integer(self.board.all_numbers[i2][j2]).move_to(self.board.cells[i2][j2])
		self.play(
			Write(self.board.numbers[i1][j1]),
			Write(self.board.numbers[i2][j2])
			)
		if self.board.all_numbers[i1][j1]>=0:
			self.play(self.board.animate.color_cell([i1,j1], YELLOW, opacity=self.board.all_numbers[i1][j1]/dif))
		if self.board.all_numbers[i1][j1]<0:
			self.play(self.board.animate.color_cell([i1,j1], BLUE, opacity=-self.board.all_numbers[i1][j1]/dif))
		if self.board.all_numbers[i2][j2]>=0:
			self.play(self.board.animate.color_cell([i2,j2], YELLOW, opacity=self.board.all_numbers[i2][j2]/dif))
		if self.board.all_numbers[i2][j2]<0:
			self.play(self.board.animate.color_cell([i2,j2], BLUE, opacity=-self.board.all_numbers[i2][j2]/dif))
		self.wait()
	def construct(self):
		rows = 8
		columns = 8
		self.board = Board(size=0.9, rows=rows, columns=columns)
		self.play(Create(self.board))
		self.wait()

		low = -100
		high = 101
		dif = (high - 1 - low) / 2
		
		matrix = genfromtxt('random_table.csv', delimiter=',').astype(int)
		self.board.add_numbers(matrix)

		self.add(self.board.numbers_)
		self.wait()

		self.play(self.board.animate.colorful(dif))
		self.wait()
		#board.track(dif)

		change = -matrix.item(0,0)
		#self.play(Wiggle(self.board.cells[0][0]), Wiggle(self.board.cells[0][1]), Wiggle(change))
		self.step(0,0,0,1, change, dif)
		#board.update_color(dif)
		#board.trackers[0][0] += matrix.item(0,0)
		#board.trackers[0][1] += matrix.item(0,0)

		#self.play(
		#	change.copy().animate.move_to(board.cells[0][0]),
		#	change.copy().animate.move_to(board.cells[0][1]),
		#	FadeOut(change))
		#self.wait()

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
