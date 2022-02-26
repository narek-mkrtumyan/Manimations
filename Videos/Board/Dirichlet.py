import sys

from numpy import dtype
sys.path.append('../../')
from Functions.QarakusiFunctions import *

class Knights(Scene):
	def example(self):
		matrix = np.genfromtxt('random_knights.csv', delimiter=',').astype(bool)
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
		self.pairing_all()
		self.orinak()

def write_random_knights():
	table = np.random.choice(2, 64)
	table.shape = (8,8)
	np.savetxt("random_knights.csv", table, delimiter=",")
	print(table)

ORANGE = '#FF6700'
GREEN = '#68BB59'

MANY_COLORS = [WHITE, GREEN, ORANGE, RED, BLUE, YELLOW, PURPLE, DARK_BROWN, PINK, GREY]

class All_Color(Scene):
	def given(self):
		pass
	def example(self):
		matrix = [
			[COLORS[0], COLORS[1], COLORS[0]],
			[COLORS[1], COLORS[1], COLORS[0]],
			[COLORS[0], COLORS[0], COLORS[1]]
		]
		self.board3.color_matrix(matrix)
		self.play(GrowFromCenter(self.board3))
		self.play(self.board3.animate.shift(3*LEFT))
		self.wait()
		white = Tex('Սպիտակ', tex_template=armenian_tex_template)
		white_cell = Square(side_length=1).set_fill(WHITE, opacity=1)
		whites = VGroup(white, white_cell).arrange(DOWN)
		whites.next_to(self.board3, RIGHT)
		self.play(Write(whites))
		self.wait()
		green = Tex('Կանաչ', tex_template=armenian_tex_template)
		green_cell = Square(side_length=1, color=GREEN).set_fill(GREEN, opacity=1)
		greens = VGroup(green, green_cell).arrange(DOWN)
		greens.next_to(whites, RIGHT)
		self.play(Write(greens))
		self.wait()
		
	def row(self):
		self.add(self.board5)
		#COLORS[4]=PURE_BLUE
		COLORS[1]='#68BB59'
		#COLORS[3]=PURE_RED
		COLORS[2]='#FF6700'
		COLORS[3]=WHITE
		matrix = [
			[COLORS[2], COLORS[1], COLORS[4], COLORS[3], COLORS[1]],
			[COLORS[4], COLORS[1], COLORS[4], COLORS[3], COLORS[4]],
			[COLORS[4], COLORS[2], COLORS[2], COLORS[1], COLORS[3]],
			[COLORS[1], COLORS[3], COLORS[3], COLORS[1], COLORS[4]],
			[COLORS[3], COLORS[2], COLORS[1], COLORS[4], COLORS[2]]
		]
		self.board5.color_matrix(matrix)
		self.board5.shift(3*LEFT)
		self.add(self.board5)
		row = self.board5.cells[4]
		other_rows = self.board5.cells[:4]
		self.wait()
		self.play(ApplyWave(row))
		self.play(FadeOut(other_rows))
		self.play(
			row.animate.move_to(DOWN).scale(2),
			)
		colors = VGroup(
			Text("Նարնջագույն").set_color(COLORS[2]),
			Text("Կանաչ").set_color(COLORS[1]),
			Text("Սպիտակ").set_color(COLORS[0]),
			Text("Կապույտ").set_color(COLORS[4])
		).arrange(RIGHT).scale(0.8)
		colors.to_edge(UP).shift(0.5*DOWN)
		self.play(Write(colors), run_time=2)
		self.wait()

		colors.save_state()
		row.save_state()
		colorner = colors.copy()
		rower = row.copy()

		r = Rabbit()
		rabbits = VGroup()
		for cell in row:
			rab = r.copy().set_color(cell.get_fill_color())
			rab.move_to(cell)
			rabbits += rab
			self.play(ReplacementTransform(cell, rab), run_time=0.2)
		c = Cage().scale(0.5)
		cages = VGroup(c.copy(), c.copy(), c.copy(), c.copy()).arrange(RIGHT, buff=1)
		cages.move_to(colors)
		for i in range(len(colors)):
			cages[i].set_color(colors[i].get_color())
			self.play(ReplacementTransform(colors[i], cages[i]), run_time=0.2)
		self.wait()
		
		color_brace = Brace(colors, sharpness=0.1)
		four = Tex('4').next_to(color_brace, DOWN)
		rabbit_brace = Brace(rabbits, sharpness=0.1)
		five = Tex('5').next_to(rabbit_brace, DOWN)
		self.play(Create(color_brace), Write(four))
		self.play(Create(rabbit_brace), Write(five))

		self.wait()
		
		all = Group(*self.mobjects)

		self.play(all.animate.shift(2*LEFT))
		self.wait()

		Dir = Tex('$5$ ', '$>$', ' $4$',
		'\\\\ Ըստ Դիրիխլեի սկզբունքի,', ' \\\\ կգտնվեն 2 նապաստակներ,\\\\ որոնք նույն վանդակում են',
		tex_template=armenian_tex_template, font_size=30).move_to(5*RIGHT)
		self.play(TransformFromCopy(five, Dir[0]))
		self.play(Write(Dir[1]), run_time=0.25)
		self.play(TransformFromCopy(four, Dir[2]))
		self.play(Write(Dir[3:]))
		self.wait()

		self.play(
			FadeOut(color_brace), FadeOut(four),
			FadeOut(rabbit_brace), FadeOut(five) 
		)

		for i in range(4):
			color = rabbits[i].get_fill_color()
			for j in range(4):
				if cages[j].get_fill_color() == color:
					self.play(rabbits[i].animate.move_to(cages[j]).set_opacity(0.5))
					self.add(cages[j])
		self.play(rabbits[4].animate.next_to(cages[0], DOWN))
		self.wait()

		self.play(FadeOut(rabbits), FadeOut(cages))
		colorner.shift(2*LEFT).scale(0.95)
		rower.shift(2*LEFT).scale(0.95)
		rower.shift(2.5*UP)
		
		self.play(FadeIn(colorner), FadeIn(rower))
		#self.play(Restore(colors), Restore(row))
		self.wait()
		
		d2 = Tex('կգտնվեն 2 վանդակներ, \\\\ որոնք նույն գույնն ունեն։',
		tex_template=armenian_tex_template, font_size=30)
		d2.next_to(Dir[-1], LEFT)
		self.play(Write(d2))
		Dirs = VGroup(Dir[-1],d2)
		self.play(
			Dirs.animate.shift(Dir[-1].get_center()-d2.get_center()),
			FadeOut(Dir[-1])
			)
		self.wait()


	def color_rows(self, time):
		self.add(self.board5)
		#COLORS[4]=PURE_BLUE
		COLORS[1]='#68BB59'
		#COLORS[3]=PURE_RED
		COLORS[2]='#FF6700'
		COLORS[3]=WHITE
		matrix = [
			[COLORS[4], COLORS[1], COLORS[4], COLORS[3], COLORS[4]],
			[COLORS[2], COLORS[1], COLORS[4], COLORS[3], COLORS[1]],
			[COLORS[3], COLORS[2], COLORS[1], COLORS[4], COLORS[2]],
			[COLORS[4], COLORS[2], COLORS[2], COLORS[1], COLORS[3]],
			[COLORS[1], COLORS[3], COLORS[3], COLORS[1], COLORS[4]],
		]
		self.board5.color_matrix(matrix)
		for i in range(4,-1,-1):
			# Here we find the repeated colors
			colors = list()
			for j in range(5):
				color = self.board5.cells[i][j].get_fill_color()
				if color in colors:
					q = j
					the_color = color
					break
				else:
					colors.append(self.board5.cells[i][j].get_fill_color())
			# the_color is the repeated color
			# q is the coord of the second repeated
			for j in range(q):
				if self.board5.cells[i][j].get_fill_color() == the_color:
					p = j
			# p is the coord of the first repeated
			self.board5.add_row_arrow(i)
			self.play(
				Create(self.board5.row_arrows[i], run_time=0.5))
			self.play(
				Circumscribe(self.board5.cells[i][p], buff=0.05),
				Circumscribe(self.board5.cells[i][q], buff=0.05)
				#Wiggle(self.board5.cells[i][q], scale_value=1.25, rotation_angle=0.05*TAU)
			)
			for j in range(5):
				if j != p and j != q:
					self.play(self.board5.animate.color_cell((i,j), the_color), run_time=time)
			self.play(FadeOut(self.board5.row_arrows[i]), run_time=0.5)
	def naive_col(self, time):
		self.board5.save_state()
		for i in range(5):
			# Here we find the repeated colors
			colors = list()
			for j in range(5):
				color = self.board5.cells[j][i].get_fill_color()
				if color in colors:
					q = j
					the_color = color
					break
				else:
					colors.append(self.board5.cells[j][i].get_fill_color())
			# the_color is the repeated color
			# q is the coord of the second repeated
			for j in range(q):
				if self.board5.cells[j][i].get_fill_color() == the_color:
					p = j
			# p is the coord of the first repeated
			self.board5.add_col_arrow(i)
			self.play(
				Create(self.board5.col_arrows[i], run_time=0.5))
			self.play(
				Circumscribe(self.board5.cells[p][i], buff=0.05),
				Circumscribe(self.board5.cells[q][i], buff=0.05)
				#Wiggle(self.board5.cells[i][q], scale_value=1.25, rotation_angle=0.05*TAU)
			)
			for j in range(5):
				if j != p and j != q:
					self.play(self.board5.animate.color_cell((j,i), the_color), run_time=time)
			self.play(FadeOut(self.board5.col_arrows[i]), run_time=0.5)

		text = Tex('Մի վայրկյան․․․', tex_template=armenian_tex_template).next_to(self.board5, RIGHT)
		child = SVGMobject('pondering_child')
		v = VGroup(text, child).arrange(DOWN)
		v.next_to(self.board5, RIGHT)
		self.play(Write(text), FadeIn(child))
		self.play(Restore(self.board5))
	def col(self, time):
		self.play(Create(self.board5.col_arrows))
		j = 0
		colors = list()
		for i in range(5):
			# Here we find the repeated colors
			color = self.board5.cells[i][j].get_fill_color()
			if color not in colors:
				colors.append(self.board5.cells[i][j].get_fill_color())
			else:
				q = i
				the_color = color
				break
		# the_color is the repeated color
		# q is the coord of the second repeated
		for i in range(q-1,-1,-1):
			if self.board5.cells[i][j].get_fill_color() == the_color:
				p = i
		# p is the coord of the first repeated
		self.play(
			ApplyWave(self.board5.cells[p]),
			ApplyWave(self.board5.cells[q])
		)
		for i in range(5):
			if i != p and i != q:
				self.play(
					self.board5.cells[i].animate.set_fill(the_color, opacity=1), run_time=time
					)
		self.wait()
	def proof(self):
		self.row()
		#self.color_rows(0.25)
		#self.naive_col(0.25)
		#self.col(0.25)

	def algo(self, board, time):
		time *= board.size
		n = board.rows
		for i in range(n-1,-1,-1):
			# Here we find the repeated colors
			colors = list()
			for j in range(n):
				color = board.cells[i][j].get_fill_color()
				if color in colors:
					q = j
					the_color = color
					break
				else:
					colors.append(board.cells[i][j].get_fill_color())
			# the_color is the repeated color
			# q is the coord of the second repeated
			for j in range(q):
				if board.cells[i][j].get_fill_color() == the_color:
					p = j
			# p is the coord of the first repeated
			#board.add_row_arrow(i)
			#self.play(
				#Create(board.row_arrows[i]),
				#Circumscribe(board.cells[i][p], buff=0.1),
				#Circumscribe(board.cells[i][q], buff=0.1),
				#Wiggle(board.cells[i][p], scale_value=1.15, rotation_angle=0.05*TAU),
				#Wiggle(board.cells[i][q], scale_value=1.15, rotation_angle=0.05*TAU),
			#	run_time = time
			#)
			for j in range(n):
				if j != p and j != q:
					board.color_cell((i,j), the_color)
					self.wait(time)
					#self.play(board.animate.color_cell((i,j), the_color), run_time = time)
		#self.play(FadeOut(board.row_arrows[i]))
		j = 0
		colors = list()
		for i in range(n):
			# Here we find the repeated colors
			color = board.cells[i][j].get_fill_color()
			if color not in colors:
				colors.append(board.cells[i][j].get_fill_color())
			else:
				q = i
				the_color = color
				break
		# the_color is the repeated color
		# q is the coord of the second repeated
		for i in range(q-1,-1,-1):
			if board.cells[i][j].get_fill_color() == the_color:
				p = i
		# p is the coord of the first repeated
		#self.play(
			#ApplyWave(board.cells[p]),
			#ApplyWave(board.cells[q]),
		#	run_time = time
		#)
		for i in range(n):
			if i != p and i != q:
				board.cells[i].set_fill(the_color, opacity=1)
				self.wait(time)
				#self.play(
				#	board.cells[i].animate.set_fill(the_color, opacity=1),
				#	run_time = time
				#	)
	def final(self):
		sizes = range(3,11)
		for n in range(9,10):
			np_matrix = np.genfromtxt(f'{n}.csv', delimiter=',', dtype=int)
			matrix = []
			for k in range(n):
				row = []
				for j in range(n):
					row.append( MANY_COLORS[np_matrix.item(k,j)] )
				matrix.append( row)

			board = Board(size=5/n, rows=n, columns=n, stroke_width=0.15, minus_stroke=True)
			self.add(board)
			board.color_matrix(matrix)
			self.algo(board, 0.25)
			self.play(FadeOut(board))
	def construct(self):
		self.board3 = Board(size=1, rows=4, columns=4, stroke_width=0.1, color=BLACK, minus_stroke=True)
		self.board5 = Board(rows=5,columns=5, stroke_width=0.1, color=BLACK, minus_stroke=True)

		#self.given()
		self.example()
		#self.proof()
		#self.final()


#slaqner Board u avelacnel animaciayum
#random table-ներ
#nor indicate