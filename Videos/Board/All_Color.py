import sys

from numpy import dtype
sys.path.append('../../')
from Functions.QarakusiFunctions import *

def write_random_knights():
	table = np.random.choice(2, 64)
	table.shape = (8,8)
	np.savetxt("random_knights.csv", table, delimiter=",")
	print(table)


ORANGE = '#FF6700'
GREEN = '#68BB59'
arm_and_left = TexTemplate()
arm_and_left.add_to_preamble('''\\usepackage{armtex}
\\usepackage[a4paper, total={6in, 8in}]{geometry}''')
MANY_COLORS = [WHITE, GREEN, ORANGE, RED, BLUE, YELLOW, PURPLE, 'FF0000', PINK, GREY]
arm_and_ams = TexTemplate()
arm_and_ams.add_to_preamble('''\\usepackage{armtex}
\\usepackage{amsmath}''')
class All_Color(Scene):
	def given(self):
		#number = MathTex('12542')
		self.text = Tex('$n$', '$\\times$', '$n$', ' տախտակի յուրաքանչյուր վանդակ ներկված է ', '$n-1$', ' գույներից որևէ մեկով։',' Եթե ', 'տողում', ' կամ ', 'սյունում ', '\\raggedright կան վանդակներ, որոնք նույն գույնի են, ապա կարող ենք տվյալ տողը կամ սյունը ներկել այդ գույնով։', ' Ապացուցել, որ կարող ենք աղյուսակը դարձնել միագույն։',
		tex_template=arm_and_left, font_size=25)
		#task = Task(number, text)
		self.text.to_edge(UP).shift(0.3*RIGHT)
		self.number = Tex('Խնդիր 12542', tex_template=armenian_tex_template, font_size=25)
		self.number.to_corner(UL).set_color(GREEN).shift(0.25*LEFT)
		#self.add(self.text, self.number)
		self.add(self.number)
	def example(self):
		cboard = Board(size=1, rows=4, columns=4, stroke_width=1, color=WHITE, minus_stroke=True, minus_size=0.1)
		matrix = [
			[MANY_COLORS[0], MANY_COLORS[1], MANY_COLORS[0], MANY_COLORS[2]],
			[MANY_COLORS[2], MANY_COLORS[1], MANY_COLORS[2], MANY_COLORS[0]],
			[MANY_COLORS[0], MANY_COLORS[0], MANY_COLORS[1], MANY_COLORS[2]],
			[MANY_COLORS[1], MANY_COLORS[2], MANY_COLORS[0], MANY_COLORS[1]]
		]
		#self.board3.color_matrix(matrix)
		self.board3.shift(3*LEFT)
		cboard.shift(3*LEFT)

		self.play(Write(self.text[:6]), run_time=2)

		ndown = Tex('$n$').next_to(self.board3, DOWN)
		nleft = ndown.copy().next_to(self.board3, LEFT)

		self.play(
			TransformFromCopy(self.text[0], nleft),
			TransformFromCopy(self.text[2], ndown)
		)

		self.play(GrowFromCenter(cboard))
		#self.play(self.board3.animate.shift(3*LEFT))
		self.wait()

		white = Tex('Սպիտակ', tex_template=armenian_tex_template)
		white_cell = Square(side_length=0.9).set_fill(WHITE, opacity=1)
		whites = VGroup(white, white_cell).arrange(DOWN)
		whites.next_to(self.board3, 2*RIGHT)

		green = Tex('Կանաչ', tex_template=armenian_tex_template)
		green_cell = Square(side_length=0.9, color=GREEN).set_fill(GREEN, opacity=1)
		greens = VGroup(green, green_cell).arrange(DOWN)
		greens.next_to(whites, RIGHT)
		
		orange = Tex('Նարնջագույն', tex_template=armenian_tex_template)
		orange_cell = Square(side_length=0.9, color=ORANGE).set_fill(ORANGE, opacity=1)
		oranges = VGroup(orange, orange_cell).arrange(DOWN)
		oranges.next_to(greens, RIGHT)


		cells = VGroup(white_cell, green_cell, orange_cell)
		brace = Brace(cells)
		quantity = Tex('$n-1$').next_to(brace, DOWN)

		self.play(TransformFromCopy(self.text[4], quantity))

		self.play(Write(whites))
		self.play(Write(greens))
		self.play(Write(oranges))

		self.play(Create(brace))
		self.wait()

		def f(k):
			if k==0:
				return white_cell
			elif k==1:
				return green_cell
			else:
				return orange_cell
		for k in range(3):
			coords = []
			for i in range(4):
				for j in range(4):
					if matrix[i][j] == MANY_COLORS[k]:
						coords.append((i,j))
			for i,j in coords:
				self.board3.cells[i][j].set_fill(f(k).get_fill_color(), opacity=1)
			self.play(*[
				TransformFromCopy(f(k), self.board3.cells[i][j]) for i,j in coords
			])
		#self.remove(cboard)
		self.play(Write(self.text[6:11]), run_time=6)
		self.wait()

		self.board3.add_row_arrow(0)
		self.board3.row_arrows[0].shift(0.25*LEFT)
		self.wait(3)
		self.play(
			Create(self.board3.row_arrows[0], run_time=0.5),
			Circumscribe(self.board3.Rows[0], buff=0.05),
			Indicate(self.text[7])
		)
		self.wait()
		self.play(
			Circumscribe(self.board3.cells[0][0], buff=0.05),
			Circumscribe(self.board3.cells[0][2], buff=0.05)
		)

		self.wait(2)
		self.play(
			self.board3.animate.color_cell((0,1),WHITE, opacity=1).color_cell((0,3), WHITE, opacity=1),
		)
		self.wait(3)
		self.board3.add_col_arrow(3)
		self.board3.col_arrows[3].shift(0.25*DOWN)
		self.play(
			Create(self.board3.col_arrows[3], run_time=0.5),
			Circumscribe(self.board3.Cols[3], buff=0.05),
			Indicate(self.text[9])
		)
		self.wait()
		self.play(
			Circumscribe(self.board3.cells[0][3], buff=0.05),
			Circumscribe(self.board3.cells[1][3], buff=0.05)
		)
		self.wait(2)
		self.play(
			self.board3.animate.color_cell((2,3),WHITE, opacity=1).color_cell((3,3), WHITE, opacity=1),
		)
		self.wait()

		self.play(Write(self.text[11:]), run_time=3)
		self.play(
			FadeOut(self.board3.col_arrows[3]),
			FadeOut(self.board3.row_arrows[0])
		)

		fourleft = Tex('4').move_to(nleft)
		fourdown = fourleft.copy().move_to(ndown)
		three = Tex('3').move_to(quantity)

		self.wait(5)
		self.play(
			Transform(nleft,fourleft),
			Transform(ndown, fourdown)
		)

		self.play(Transform(quantity, three))
		self.wait()

		self.play(Circumscribe(self.board3.Rows[2],buff=0.05))
		self.play(self.board3.animate.color_cell((2,2), WHITE))
		self.play(Circumscribe(self.board3.Cols[2],buff=0.05))
		self.play(self.board3.animate.color_cell((1,2), WHITE))
		self.play(Circumscribe(self.board3.Rows[3],buff=0.05))
		self.play(self.board3.animate.color_cell((3,0), WHITE).color_cell((3,1), WHITE))
		self.play(Circumscribe(self.board3.Rows[1], buff=0.05))
		self.play(self.board3.animate.color_cell((1,0), WHITE).color_cell((1,1), WHITE))
		self.wait()

		all = Group(*self.mobjects)
		self.play(FadeOut(all))
		self.wait()

	def row(self):
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

		ndown = Tex('$n$').next_to(self.board5, DOWN)
		nleft = ndown.copy().next_to(self.board5, LEFT)

		self.wait()
		self.play(
			FadeIn(self.board5),
			FadeIn(ndown), FadeIn(nleft)
			)

		row = self.board5.cells[4]
		other_rows = self.board5.cells[:4]
		self.wait(2)
		self.play(ApplyWave(row))
		self.play(
			FadeOut(other_rows),
			FadeOut(ndown), FadeOut(nleft)
		)
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
		four = Tex('$n-1$').next_to(color_brace, DOWN)

		rabbit_brace = Brace(rabbits, sharpness=0.1)
		five = Tex('5').next_to(rabbit_brace, DOWN)
		five = Tex('$n$').next_to(rabbit_brace, DOWN)
		
		self.play(Create(color_brace), Write(four))
		self.play(Create(rabbit_brace), Write(five))
		self.wait()
		
		all = Group(*self.mobjects)

		self.play(all.animate.shift(2*LEFT))
		self.wait()

		Dir = Tex('$n$ ', '$>$', ' $n-1$',
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

		self.play(
			Circumscribe(rower[1]),
			Circumscribe(rower[4])
		)
		all = Group(*self.mobjects)
		self.play(FadeOut(all))
		self.wait()

	def color_rows(self, time):
		#self.add(self.board5)
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
		self.wait()
		self.play(FadeIn(self.board5))
		self.wait()
		self.text1 = Tex('Յուրաքանչյուր ', 'տողում', ' կան նույն գույնն ունեցող վանդակներ', tex_template=armenian_tex_template)
		self.text2 = Tex('Յուրաքանչյուր ', 'սյունում', ' կան նույն գույնն ունեցող վանդակներ', tex_template=armenian_tex_template)
		self.text3 = Tex('Արդեն կան նույն գույնն ունեցող տողեր',tex_template=armenian_tex_template)
		self.text1.to_edge(UP)
		self.text2.to_edge(UP)
		self.text3.next_to(self.text2, DOWN)
		self.play(Write(self.text1), run_time=3)
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
		self.wait(2.5)
		self.play(ReplacementTransform(self.text1, self.text2))
		self.wait(2.5)
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

		self.text = Tex('Մի վայրկյան․․․', tex_template=armenian_tex_template).next_to(self.board5, RIGHT)
		self.child = SVGMobject('pondering_child')
		v = VGroup(self.text, self.child).arrange(DOWN)
		v.next_to(self.board5, RIGHT)
		self.play(Write(self.text), FadeIn(self.child))
		self.play(Restore(self.board5))
	def col(self, time):
		self.play(Create(self.board5.col_arrows))

		easy = Tex('Ավելի լավ ձև կա', tex_template=armenian_tex_template)
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
		#cross = Cross(self.text2, color=RED)
		self.play(
			FadeOut(self.text),
			FadeOut(self.child),
			self.text2.animate.set_opacity(0.25)
			)
		self.play(Write(self.text3), run_time=2)

		self.wait(3)
		for i in range(5):
			if i != p and i != q:
				self.play(
					self.board5.cells[i].animate.set_fill(the_color, opacity=1), run_time=time
					)
		self.wait()

		self.play(FadeOut(self.board5.col_arrows))

		why = Tex('-Ինչո՞ւ', tex_template=armenian_tex_template)
		because = Tex('-Որովհետև արդեն կա $n$ հատ միագույն տող և $n-1$ հատ գույն', tex_template=armenian_tex_template)
		talk = VGroup(why, because).arrange(DOWN).align_on_border(LEFT)
		talk.next_to(self.text3, DOWN)
		self.play(FadeOut(self.text2), FadeOut(self.board5))
		self.play(Write(why), run_time=2)
		self.play(Write(because), run_time=3)
		self.wait()

		all = Group(*self.mobjects)
		self.play(FadeOut(all))
		self.wait()

	def proof(self):
		#self.row()
		self.color_rows(0.25)
		self.naive_col(0.25)
		self.col(0.25)

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
		sizes = [6,7,4,5,8]
		text = Tex(
			'''\\begin{enumerate}
			\item Բոլոր տողերում գտնենք\\\\ նույն գույնի վանդակներ\\\\ և այդ տողը դարձնենք\\\\ միագույն:
			\item Գտնենք նույն գույնով\\\\ ներկված տողեր և \\\\աղյուսակը դարձնենք\\\\ միագույն։
			\\end{enumerate}''',
			tex_template=arm_and_ams, font_size=35)
		text.to_edge(LEFT)
		self.wait(3)
		self.play(Write(text), run_time=5)
		for n in sizes:
			np_matrix = np.genfromtxt(f'{n}.csv', delimiter=',', dtype=int)
			matrix = []
			for k in range(n):
				row = []
				for j in range(n):
					row.append( MANY_COLORS[np_matrix.item(k,j)] )
				matrix.append( row)

			board = Board(size=5/n, rows=n, columns=n, stroke_width=0.15, minus_stroke=True)
			board.next_to(text, 6*RIGHT)
			self.add(board)
			board.color_matrix(matrix)
			self.algo(board, 0.25)
			self.play(FadeOut(board))
	def construct(self):
		self.board3 = Board(size=1, rows=4, columns=4, stroke_width=0.1, color=WHITE, minus_stroke=True, minus_size=0.1)
		self.board5 = Board(rows=5,columns=5, stroke_width=0.1, color=BLACK, minus_stroke=True, minus_size=0.1)

		#self.given()
		#self.example()
		#self.proof()
		self.final()


#slaqner Board u avelacnel animaciayum
#random table-ներ
#nor indicate