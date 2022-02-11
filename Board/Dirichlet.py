from tkinter import W
from manim import *
from Board import Board, T4, knight_moves

import numpy as np
import csv
import pandas as pd
from numpy import genfromtxt


class Knights(Scene):
	def example(self):
		matrix = genfromtxt('random_knights.csv', delimiter=',').astype(bool)
		knight = SVGMobject('Knight.svg')
		knight.width = 0.6

		knights = VGroup()
		horses = []
		for i in range(self.rows):
			h = list()
			for j in range(self.columns):
				if matrix.item(i,j):
					horse = knight.copy().move_to(self.board.cells[i][j])
					h.append(horse)
					knights += horse
				else:
					h.append(1)
			horses.append(h)

		self.play(Create(knights))

		self.play(
			self.board.animate.color_cell((2,3), color=RED).color_cell((4,4), color=RED),
			Wiggle(horses[2][3]), Wiggle(horses[4][4])
			)
		self.play(
			self.board.animate.color_cell((2,3), color=WHITE).color_cell((4,4), color=DARK_BROWN)
			)

		pairs = [ 
		( (3,1), (5,2) ),
		( (4,6), (2,5) ),
		( (0,6), (1,4) ),
		( (7,7), (6,5) ),
		( (7,5), (5,4) )
		]
		bcoords = [(3,1),(4,6),(0,6), (7,7),(7,5)]
		wcoords = [(5,2),(2,5), (1,4), (6,5), (5,4)]
		#for pair in pairs:
		#	for first, second in pair:
		#		self.play(
		#			self.board.animate.color_cell(first, color=RED).color_cell(second, color=RED)
		#			)
		self.play(
			self.board.animate.color_cells(bcoords, color=RED).color_cells(wcoords, color=RED)
			)

		self.play(
			self.board.animate.color_cells(bcoords, color=DARK_BROWN).color_cells(wcoords, color=WHITE)
			)

		knights_out = VGroup()
		coords = [
		(3,1),(4,6), (0,6), (7,7),(7,5)
		]
		for coord in coords:
			knights_out += horses[coord[0]][coord[1]]
			knights -= horses[coord[0]][coord[1]]
		self.play(FadeOut(knights_out))

		self.play(FadeOut(knights))
		self.wait()

	def pair_idea(self):
		knight1 = SVGMobject('Knight.svg').move_to(self.board.cells[4][5])
		coords1 = knight_moves(4,5)
		knight1.width = 0.6
		self.play(
			self.board.animate.color_cell((4,5), color=BLUE)
			)
		self.play(Create(knight1))
		self.play(
			self.board.animate.color_cells(coords1, color=RED)
			)

		knight2 = knight1.copy().move_to(self.board.cells[6][4])
		coords2 = knight_moves(6,4)
		self.play(FadeIn(knight2))
		self.play(Wiggle(knight1), Wiggle(knight2))
		self.wait()
		self.play(
			FadeOut(knight1),
			self.board.animate.color_cells(coords1, color=DARK_BROWN)
		)

		self.play(
			self.board.animate.color_cells(coords2, color=RED)
		)

		self.play(FadeIn(knight1))
		self.play(Wiggle(knight1), Wiggle(knight2))
		self.wait()

		self.play(
			self.board.animate.color_cells(coords2, color=WHITE)
			)

		self.play(
			self.board.animate.color_cell((4,5), color=RED).color_cell((6,4), color=RED),
			FadeOut(knight1), FadeOut(knight2)
			)
	def vgroup(self, i1,j1,i2,j2):
		return VGroup(self.board.cells[i1][j1], self.board.cells[i2][j2])
	def pairing(self):
		arm = TexTemplate()
		arm.add_to_preamble(r"\usepackage{armtex}")

		vgroup1 = self.vgroup(4,5,6,4)
		
		self.play(
			self.board.animate.shift(3.5*LEFT)
			)
		
		pairs = VGroup()
		for i in range(1,9):
			tex = Tex('Զույգ ' + str(i), tex_template=arm)
			r = Rectangle(height=1.5+0.75, width=2*0.75, color=GREEN)
			pair = VGroup(tex, r).arrange(DOWN)
			pairs += pair

		pairs.arrange_in_grid(rows=2, cols=4, buff=0.3).shift(3.5*RIGHT)

		self.play(vgroup1.animate.move_to(pairs[0][1]))
		self.play(Create(pairs[0]))
		self.wait()

		self.play(
			Create(VGroup(pairs-pairs[0])),
			run_time=2
			)

		couples = VGroup(vgroup1)
		pair_coords = [
		[4,4,6,5],
		[4,7,6,6],
		[4,6,6,7],
		[5,5,7,4],
		[5,4,7,5],
		[5,7,7,6],
		[5,6,7,7]
		]
		i = 0

		for coords in pair_coords:
			i += 1
			i1 = coords[0]
			j1 = coords[1]
			i2 = coords[2]
			j2 = coords[3]
			
			vgroup = self.vgroup(i1,j1,i2,j2)
			couples += vgroup
			self.play(
				vgroup.animate.move_to(pairs[i][1])
				)
			if i==1:
				self.wait()

		pair_coords = [
			[0,0,0,0],
			[4,5,6,4],
			[4,4,6,5],
			[4,7,6,6],
			[4,6,6,7],
			[5,5,7,4],
			[5,4,7,5],
			[5,7,7,6],
			[5,6,7,7]
		]
		matrix_of_numbers = [[None for i in range(8)] for j in range(8)]

		for i in range(1,9):
			i1 = pair_coords[i][0]
			j1 = pair_coords[i][1]
			i2 = pair_coords[i][2]
			j2 = pair_coords[i][3]
			matrix_of_numbers[i1][j1] = i
			matrix_of_numbers[i2][j2] = i

		self.board.add_numbers(matrix_of_numbers)
		self.cboard.add_numbers(matrix_of_numbers)

		for i in range(1,9):
			i1 = pair_coords[i][0]
			j1 = pair_coords[i][1]
			i2 = pair_coords[i][2]
			j2 = pair_coords[i][3]
			self.play(
				Write(self.board.numbers[i1][j1]),
				Write(self.board.numbers[i2][j2]),
				run_time=0.8)
		self.wait()

		rect = Square(side_length=4*0.75, stroke_width=6)
		rect.shift(3.5*LEFT).shift(2*0.75*(UP+RIGHT))
		time_width = 1
		self.play(ShowPassingFlash(rect.set_color(GREEN), time_width=time_width))
		self.wait()
		rect.shift(4*0.75*(LEFT))
		self.play(ShowPassingFlash(rect.set_color(GREEN), time_width=time_width))
		rect.shift(4*0.75*(DOWN))
		self.play(ShowPassingFlash(rect.set_color(GREEN), time_width=time_width))
		rect.shift(4*0.75*(RIGHT))
		self.play(ShowPassingFlash(rect.set_color(GREEN), time_width=time_width))

		self.wait()
		self.play(Transform(self.board, self.cboard), FadeOut(pairs))
		self.wait()
	
	def numbering_all(self):
		pair_coords = [
			[0,0,0,0],
			[4,5,6,4],
			[4,4,6,5],
			[4,7,6,6],
			[4,6,6,7],
			[5,5,7,4],
			[5,4,7,5],
			[5,7,7,6],
			[5,6,7,7]
		]
		matrix_of_numbers = [[None for i in range(8)] for j in range(8)]

		for i in range(1,9):
			i1 = pair_coords[i][0]
			j1 = pair_coords[i][1]
			i2 = pair_coords[i][2]
			j2 = pair_coords[i][3]
			matrix_of_numbers[i1][j1] = i
			matrix_of_numbers[i2][j2] = i

		self.board.add_numbers(matrix_of_numbers)
		self.cboard.add_numbers(matrix_of_numbers)

		pair_coords = [
			[0,0,0,0],
			[4,1,6,0],
			[4,0,6,1],
			[4,3,6,2],
			[4,2,6,3],
			[5,1,7,0],
			[5,0,7,1],
			[5,3,7,2],
			[5,2,7,3],

			[0,1,2,0],
			[0,0,2,1],
			[0,3,2,2],
			[0,2,2,3],
			[1,1,3,0],
			[1,0,3,1],
			[1,3,3,2],
			[1,2,3,3],

			[0,5,2,4],
			[0,4,2,5],
			[0,7,2,6],
			[0,6,2,7],
			[1,5,3,4],
			[1,4,3,5],
			[1,7,3,6],
			[1,6,3,7]
		]
		matrix_of_numbers = [[None for i in range(8)] for j in range(8)]

		for i in range(9,33):
			i1 = pair_coords[i-8][0]
			j1 = pair_coords[i-8][1]
			i2 = pair_coords[i-8][2]
			j2 = pair_coords[i-8][3]
			matrix_of_numbers[i1][j1] = i
			matrix_of_numbers[i2][j2] = i
		
		self.wait()
		self.cboard.update_numbers(matrix_of_numbers)

		def col(i,j):
			if (i+j)%2==0:
				return DARK_BROWN
			else:
				return WHITE
		for i in range(9,33):
			i1 = pair_coords[i-8][0]
			j1 = pair_coords[i-8][1]
			i2 = pair_coords[i-8][2]
			j2 = pair_coords[i-8][3]
			self.play(
				self.cboard.cells[i1][j1].animate.set_color(RED),
				self.cboard.cells[i2][j2].animate.set_color(RED), run_time=0.25)
				
			self.play(
				Write(self.cboard.updated_numbers[i1][j1]),
				Write(self.cboard.updated_numbers[i2][j2]),
				self.cboard.cells[i1][j1].animate.set_color(col(i1,j1)),
				self.cboard.cells[i2][j2].animate.set_color(col(i2,j2)),
				run_time=0.25)

		self.wait()



	def cvgroup(self, i1,j1,i2,j2):
		return VGroup(self.cboard.cells[i1][j1], self.cboard.cells[i2][j2])

	def pairing_all(self):
		new_pairs = VGroup()
		new_without_old = VGroup()
		new_zuyger = list()
		new_rectangles = list()
		old_zuyger = list()
		arm = TexTemplate()
		arm.add_to_preamble(r"\usepackage{armtex}")
		for i in range(1,33):
			tex = Tex('Զույգ '+str(i), tex_template=arm).scale(0.5)
			r = Rectangle(height=0.5*(1.5+0.75), width=0.5*(2*0.75), color=GREEN)
			new_pair = VGroup(tex, r).arrange(DOWN/2)
			new_zuyger.append(new_pair)
			new_pairs += new_pair
			new_rectangles.append(r)
			if i<=8:
				old_zuyger.append(new_pair)
			else:
				new_without_old += new_pair

		vgroups = list()
		pair_coords = [
		[4,5,6,4],
		[4,4,6,5],
		[4,7,6,6],
		[4,6,6,7],
		[5,5,7,4],
		[5,4,7,5],
		[5,7,7,6],
		[5,6,7,7]
		]
		i=0
		for coords in pair_coords:
			i+=1
			i1 = coords[0]
			j1 = coords[1]
			i2 = coords[2]
			j2 = coords[3]
			vgroup = self.cvgroup(i1,j1,i2,j2)
			vgroups.append(vgroup)
		pair_coords = [
		[4,1,6,0],
		[4,0,6,1],
		[4,3,6,2],
		[4,2,6,3],
		[5,1,7,0],
		[5,0,7,1],
		[5,3,7,2],
		[5,2,7,3]
		]
		for coords in pair_coords:
			i+=1
			i1 = coords[0]
			j1 = coords[1]
			i2 = coords[2]
			j2 = coords[3]
			vgroup = self.cvgroup(i1,j1,i2,j2)
			vgroups.append(vgroup)
		pair_coords = [
		[0,1,2,0],
		[0,0,2,1],
		[0,3,2,2],
		[0,2,2,3],
		[1,1,3,0],
		[1,0,3,1],
		[1,3,3,2],
		[1,2,3,3]
		]
		for coords in pair_coords:
			i+=1
			i1 = coords[0]
			j1 = coords[1]
			i2 = coords[2]
			j2 = coords[3]
			vgroup = self.cvgroup(i1,j1,i2,j2)
			vgroups.append(vgroup)
		pair_coords = [
		[0,5,2,4],
		[0,4,2,5],
		[0,7,2,6],
		[0,6,2,7],
		[1,5,3,4],
		[1,4,3,5],
		[1,7,3,6],
		[1,6,3,7]
		]
		for coords in pair_coords:
			i+=1
			i1 = coords[0]
			j1 = coords[1]
			i2 = coords[2]
			j2 = coords[3]
			vgroup = self.cvgroup(i1,j1,i2,j2)
			vgroups.append(vgroup)

		new_pairs.arrange_in_grid(rows=4, cols=8, buff=0.3/2).shift(2.5*RIGHT)
		self.play(Create(new_pairs), run_time=4)
		self.wait()
		self.play(*[
			vgroups[i].animate.move_to(new_rectangles[i]) for i in range(8)]
				)
		self.play(*[
			vgroups[i].animate.move_to(new_rectangles[i]) for i in range(8,16)]
				)
		self.play(*[
			vgroups[i].animate.move_to(new_rectangles[i]) for i in range(16,24)]
				)
		self.play(*[
			vgroups[i].animate.move_to(new_rectangles[i]) for i in range(24,32)]
				)
		self.wait()

		tex = Tex('Կա 32 զույգ,\\\\ հետևաբար կարող ենք\\\\ դնել իրար չհարվածող\\\\ առավելագունը 32 ձի', tex_template=arm)
		tex.shift(4.5*LEFT)
		self.play(Write(tex))
		self.wait()
	def orinak(self):
		knight = SVGMobject('Knight.svg')
		knight.width=0.6

		knights = VGroup()

		self.play(
			self.board.animate.shift(2*LEFT))

		for i in range(8):
			for j in range(8):
				if (i+j)%2==0:
					knights += knight.copy().move_to(self.board.cells[i][j])

		self.play(Create(knights), run_time=3)
		Template = TexTemplate()
		Template.add_to_preamble(r"\usepackage{amssymb}")
		arm = TexTemplate()
		arm.add_to_preamble(r"\usepackage{armtex}")
		checkmark = Tex('\\checkmark', tex_template=Template,font_size=75)
		tex = Tex('32 իրար չհարվածող ձի', tex_template=arm)
		text = VGroup(tex, checkmark).arrange(DOWN)
		text.shift(4*RIGHT)
		self.play(Write(text))
		self.wait()
	def construct(self):
		self.rows = 8
		self.columns = 8
		self.board = Board(rows=self.rows, columns=self.columns, stroke_width=0.000)
		self.board.make_chess()

		self.cboard = self.board.copy()
		self.cboard.shift(3.5*LEFT)
		
		#self.play(Create(self.board))
		#self.wait()
		
		self.add(self.cboard)
		
		#self.example()
		#self.pair_idea()
		#self.pairing()
		self.numbering_all()
		#self.pairing_all()
		#self.orinak()
#table = np.random.choice(2, 64)
#table.shape = (8,8)
#np.savetxt("random_knights.csv", table, delimiter=",")
#print(table)

class Updater(Scene):
	def construct(self):
		dot1 = Dot().shift(LEFT)
		dot2 = Dot().shift(RIGHT)
		l = Line(dot1,dot2)
		def line_updater(mobject):
			mobject.put_start_and_end_on(dot1.get_center(), dot2.get_center())
		l.add_updater(line_updater)
		self.play(Create(l), Write(dot1), Write(dot2))
		self.wait()
		self.play(dot2.animate.shift(2*UP))
		self.wait()

class All_Color(Scene):
	def given(self):
		pass
	def example(self):
		pass
	def row(self):
		pass
	def color_rows(self):
		pass
	def col(self):
		pass
	def proof(self):
		pass
	def final(self):
		pass
	def construct(self):
		self.board3 = Board(rows=3, columns=3)
		self.board2 = Board()

		self.given()
		self.example()
		self.proof()
		self.final()