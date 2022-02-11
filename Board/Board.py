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

def knight_moves(i,j):
	old = [ [i+1,j+2], [i+2,j+1], [i+1,j-2], [i+2,j-1], [i-1,j+2], [i-2,j+1], [i-1,j-2], [i-2,j-1] ]
	new = list()
	for pair in old:
		m = pair[0]
		n= pair[1]
		if m<=7 and m>=0 and n<=7 and n>=0:
			new.append(pair)
	return new


class Board(VMobject):
	def __init__(self, size=0.75, rows=8, columns=8, color=WHITE, midrows=0, midcolumns=0, stroke_width=0.2):
		k=[]
		for i in range(rows):
			x=Square(color=color, stroke_width=stroke_width)
			x.width = size
			s=[]
			for p in range(columns):
				d=x.copy()
				d.shift((p * (size + midrows)) * RIGHT)
				s.append(d)
				s[p].shift((columns - 1) * (size + midrows) * 0.5 * LEFT)
			for j in range(columns):
				s[j].shift((i * (size + midcolumns) * UP))
				s[j].shift((rows - 1) * (size + midcolumns) * 0.5 * DOWN)
			k.append(s)
		self.cells = k
		self.cells_ = matrix_to_VGroup(k)
		VMobject.__init__(self)
		for i in range(rows):
			for j in range(columns):
				self.add(self.cells[i][j])
		self.rows = rows
		self.columns = columns
		self.size = size
		self.color = color
		#self.updated_numbers = VGroup()

	def color_cell(self, coords, color, opacity=1):
		self.cells[coords[0]][coords[1]].set_fill(color, opacity=opacity)

	def color_cells(self, coords, color, opacity=1):
		group = VGroup()
		for coord in coords:
			group += self.cells[coord[0]][coord[1]]
		group.set_color(color)

	def make_chess(self, white=WHITE, black=DARK_BROWN, opacity=1):
		for i in range(self.rows):
			for j in range(self.columns):
				if (i+j)%2==0:
					self.cells[i][j].set_fill(black, opacity=opacity)
				else:
					self.cells[i][j].set_fill(white, opacity=opacity)
	
	def color4(self):
		pass

	def add_numbers(self, matrix_of_numbers):
		self.numbers = VGroup()
		self.all_numbers = list()
		if isinstance(matrix_of_numbers, np.ndarray):
			assert self.rows == matrix_of_numbers.shape[0] and self.columns == matrix_of_numbers.shape[1], "Մատրիցի չափերը չեն համընկնում տախտակի չափերի հետ"
			for i in range(self.rows):
				k = list()
				l = VGroup()
				for j in range(self.columns):
					k.append(matrix_of_numbers.item((i,j)))
					if matrix_of_numbers.item((i,j)) is not None:
						l += Integer(matrix_of_numbers.item((i,j))).set_color(BLACK).move_to(self.cells[i][j].get_center())
				self.numbers += l
				self.all_numbers.append(k)
		else:
			assert self.rows == len(matrix_of_numbers) and self.columns == len(matrix_of_numbers[0]), "Մատրիցի չափերը չեն համընկնում տախտակի չափերի հետ"
			for i in range(self.rows):
				k=list()
				l = VGroup()
				for j in range(self.columns):
					k.append(matrix_of_numbers[i][j])
					if matrix_of_numbers[i][j] is not None:
						l += Integer(matrix_of_numbers[i][j]).set_color(BLACK).move_to(self.cells[i][j].get_center())
					else:
						l += Integer(0).move_to(8*RIGHT)
				self.numbers += l
				self.all_numbers.append(k)
		self.add(self.numbers)

	def update_numbers(self, matrix_of_numbers):
		self.updated_numbers = VGroup()
		group = VGroup()
		for i in range(self.rows):
			ggroup = VGroup()
			for j in range(self.columns):
				if matrix_of_numbers[i][j] is not None:
					self.all_numbers[i][j] = matrix_of_numbers[i][j]
					#self.numbers[i][j] = Integer(matrix_of_numbers[i][j]).set_color(BLACK).move_to(self.cells[i][j].get_center())
					#ggroup += self.numbers[i][j]
					num = Integer(matrix_of_numbers[i][j]).set_color(BLACK).move_to(self.cells[i][j].get_center())
					ggroup += num
				else:
					ggroup += Integer(0).move_to(8*RIGHT)
			group += ggroup
		#self.add(self.numbers)
		self.updated_numbers = group
		#self.add(self.updated_numbers)

	def colorful(self, dif):
		matrix = self.all_numbers
		for i in range(self.rows):
			for j in range(self.columns):
				if matrix[i][j]>0:
					self.color_cell([i,j], YELLOW, opacity=matrix[i][j]/dif)
				if matrix[i][j]<0:
					self.color_cell([i,j], BLUE, opacity=-matrix[i][j]/dif)

	def update_color(self, dif):
		def my_updater(mobject):
			#if self.all_numbers[i][j]>0:
			#	color = YELLOW
			#else:
			#	color = BLUE
			#mobject.set_fill(color, opacity=self.all_numbers[i][j]/dif)
			mobject.set_fill(YELLOW)
		for i in range(self.rows):
			for j in range(self.columns):
				self.cells[i][j].add_updater(my_updater)

class T4(VMobject):
	'''
	4 հատանոց T-աձև պատկեր
	'''
	def __init__(self, size=0.75, color=WHITE, stroke_width=0.2):
		k=[]
		T=4
		for position in [LEFT, T, RIGHT, DOWN]:
			if position is T:
				k.append(Square(color=color, stroke_width=stroke_width).set_width(size))
			else:
				k.append(Square(color=color, stroke_width=stroke_width).set_width(size).shift(size*position))
		self.cells = k
		self.cells_ = VGroup(*k)
		VMobject.__init__(self)
		self.add(self.cells_)
		self.size = size
		self.color = color

	def color_cell(self, coord, color, opacity=1):
		self.cells[coord].set_fill(color, opacity=opacity)

	def color_all(self, matrix_of_colors, opacity=1):
		for i in range(4):
			self.cells[i].set_fill(matrix_of_colors[i], opacity=opacity)
