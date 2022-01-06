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

#TODO: understand set_fill
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

	def color_cell(self, coords, color, opacity=1):
		self.cells[coords[0]][coords[1]].set_fill(color, opacity=opacity)

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
		self.numbers = list()
		self.all_numbers = list()
		if isinstance(matrix_of_numbers, np.ndarray):
			assert self.rows == matrix_of_numbers.shape[0] and self.columns == matrix_of_numbers.shape[1], "Մատրիցի չափերը չեն համընկնում տախտակի չափերի հետ"
			for i in range(self.rows):
				k = list()
				l = list()
				for j in range(self.columns):
					k.append(matrix_of_numbers.item((i,j)))
					l.append(Integer(matrix_of_numbers.item((i,j))).move_to(self.cells[i][j].get_center()))
				self.numbers.append(l)
				self.all_numbers.append(k)
		else:
			assert self.rows == len(matrix_of_numbers) and self.columns == len(matrix_of_numbers[0]), "Մատրիցի չափերը չեն համընկնում տախտակի չափերի հետ"
			for i in range(self.rows):
				k=list()
				for j in range(self.columns):
					l.append(Integer(matrix_of_numbers.item((i,j))).move_to(self.cells[i][j].get_center()))
				self.numbers.append(l)
				self.all_numbers.append(k)
		self.numbers_ = matrix_to_VGroup(self.numbers)

	def add_trackers(self, matrix_of_numbers, dif):
		self.trackers = list()
		self.numbers = list()
		self.all_numbers = list()
		if isinstance(matrix_of_numbers, np.ndarray):
			assert self.rows == matrix_of_numbers.shape[0] and self.columns == matrix_of_numbers.shape[1], "Մատրիցի չափերը չեն համընկնում տախտակի չափերի հետ"
			for i in range(self.rows):
				k = list()
				l = list()
				for j in range(self.columns):
					tracker = ValueTracker(matrix_of_numbers.item((i,j)))
					k.append(tracker)
					l.append(matrix_of_numbers.item((i,j)))
					self.numbers.append(Integer(matrix_of_numbers.item((i,j))).move_to(self.cells[i][j].get_center()))
				self.trackers.append(k)
				self.all_numbers.append(l)
		else:
			assert self.rows == len(matrix_of_numbers) and self.columns == len(matrix_of_numbers[0]), "Մատրիցի չափերը չեն համընկնում տախտակի չափերի հետ"
			for i in range(self.rows):
				k = list()
				l = list()
				for j in range(self.columns):
					tracker = ValueTracker(matrix_of_numbers[i][j])
					k.append(tracker)
					l.append(matrix_of_numbers.item((i,j)))
					self.numbers.append(Integer(matrix_of_numbers[i][j]).move_to(self.cells[i][j].get_center()))
				self.trackers.append(k)
				self.all_numbers.append(l)
		self.numbers_ = VGroup(*self.numbers)

	def track(self, dif):
		#for i in range(self.rows):
		#	for j in range(self.columns):
		def number_updater(mobject):
			mobject.set_value(self.trackers[0][0].get_value())
			#mobject = Tex(self.trackers[i][j].get_value())
		for number in self.numbers:
			number.add_updater(number_updater)

		for i in range(self.rows):
			for j in range(self.columns):
				def cell_updater(mobject):
					mobject.set_fill(YELLOW, opacity=self.trackers[i][j].get_value()/dif)
				for row in self.cells:
					for cell in row:
						cell.add_updater(cell_updater)

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
