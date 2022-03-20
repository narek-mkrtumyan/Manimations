from manim import *
import numpy as np
import csv

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
	"""Board
        
        Note:
            Also updates ``self.model`` variable
        Args:
			size (float): the side length of the cells
        
        Returns:
            SentenceTransformer
        
        Raises:
            NameError: raises if ``model_name`` is not from ``self.available_models`` list 
        Examples:
            >>> model = EmbeddingExtractor('nli-mpnet-base-v2', 'some_text')
            >>> print(model.load_model())
            SentenceTransformer(
                    (0): Transformer(
                    (auto_model): MPNetModel(
                        (embeddings): MPNetEmbeddings(
                        (word_embeddings): Embedding(30527, 768, padding_idx=1)
                        .....
        """
	def __init__(self, size=0.75, rows=8, columns=8, color=WHITE, midrows=0, midcolumns=0, stroke_width=0.2, minus_stroke=False, minus_size=0.2):
		k=VGroup()
		for i in range(rows):
			x = Square(color=color, stroke_width=stroke_width)
			x.width = size
			if minus_stroke:
				x.width = size-minus_size
			s = VGroup()
			for p in range(columns):
				d=x.copy()
				d.shift((p * (size + midrows)) * RIGHT)
				s += d
				s[p].shift((columns - 1) * (size + midrows) * 0.5 * LEFT)
			for j in range(columns):
				s[j].shift((i * (size + midcolumns) * UP))
				s[j].shift((rows - 1) * (size + midcolumns) * 0.5 * DOWN)
			k += s
		
		self.cells = k
		self.cells_ = self.cells
		
		VMobject.__init__(self)
		for i in range(rows):
			for j in range(columns):
				self.add(self.cells[i][j])
		
		self.rows = rows
		self.columns = columns
		self.size = size
		self.color = color
		self.row_arrows = VGroup(*[VMobject() for i in range(rows)])
		self.col_arrows = VGroup(*[VMobject() for i in range(columns)])
		#self.updated_numbers = VGroup()
		self.Rows = VGroup()
		self.Cols = VGroup()
		for i in range(rows):
			row = VGroup()
			for j in range(columns):
				row += self.cells[i][j]
			self.Rows += row
		for j in range(columns):
			col = VGroup()
			for i in range(rows):
				col += self.cells[i][j]
			self.Cols += col

	def color_cell(self, coords, color, opacity=1):
		self.cells[coords[0]][coords[1]].set_fill(color, opacity=opacity)

	def color_cells(self, coords, color, opacity=1):
		group = VGroup()
		for coord in coords:
			group += self.cells[coord[0]][coord[1]]
		group.set_color(color)

	def make_chess(self, white=WHITE, black=DARK_BROWN, opacity=1):
		"""Function set_fill as a chess board
        
        Note:
            Also updates ``self.model`` variable
        Args:
            white (str): color of the white cells
			black (str): color of the black cells
			opacity (float): opacity of the colored cells
        
        Returns:
            The board
        
        Examples:
            >>> model = EmbeddingExtractor('nli-mpnet-base-v2', 'some_text')
            >>> print(model.load_model())
            SentenceTransformer(
                    (0): Transformer(
                    (auto_model): MPNetModel(
                        (embeddings): MPNetEmbeddings(
                        (word_embeddings): Embedding(30527, 768, padding_idx=1)
                        .....
        """
		for i in range(self.rows):
			for j in range(self.columns):
				if (i+j)%2==0:
					self.cells[i][j].set_fill(black, opacity=opacity)
				else:
					self.cells[i][j].set_fill(white, opacity=opacity)
		return self
	
	def color4(self, color_0=ORANGE, color_1=PURE_GREEN, color_2=WHITE, color_3=GREY, opacity=1):
		for i in range(self.rows):
			for j in range(self.columns):
				if (i+j)%4==0:
					self.cells[i][j].set_fill(color_0, opacity=opacity)
				elif (i+j)%4==1:
					self.cells[i][j].set_fill(color_1, opacity=opacity)
				elif (i+j)%4==2:
					self.cells[i][j].set_fill(color_2, opacity=opacity)
				else:
					self.cells[i][j].set_fill(color_3, opacity=opacity)
		return self

	def color_matrix(self, matrix_of_colors):
		for i in range(len(matrix_of_colors)):
			for j in range(len(matrix_of_colors[i])):
				self.color_cell((i,j), matrix_of_colors[i][j])
		return self

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
	def add_row_arrow(self, coord: int, side='left'):
		"""Function creates an arrow to point a specific row
        
        Note:
            Also updates ``self.row_arrows`` variable
        Args:
			self (Board): the board
            coord (int): color of the white cells
			side (str): the position of the arrow

        Returns:
            The board
        """
		cell = self.cells[coord][0].get_center()
		if side=='left':
			cell = self.cells[coord][0].get_center()
			arr = Arrow(start=cell+2*LEFT,end=cell+0.25*LEFT, color=WHITE)
		else:
			cell = self.cells[coord][self.columns-1].get_center()
			arr = Arrow(start=cell-2*LEFT,end=cell-0.25*LEFT, color=WHITE)
		self.row_arrows[coord] = arr
		return self
	def add_col_arrow(self, coord: int, side='down'):
		"""Function creates an arrow to point a specific column
        
        Note:
            Also updates ``self.col_arrows`` variable
        Args:
			self (Board): the board
            coord (int): color of the white cells
			side (str): the position of the arrow

        Returns:
            The board
        """
		if side=='down':
			cell = self.cells[0][coord].get_center()
			arr = Arrow(start=cell+2*DOWN,end=cell+0.25*DOWN, color=WHITE)
		else:
			cell = self.cells[self.rows-1][coord].get_center()
			arr = Arrow(start=cell-2*DOWN,end=cell-0.25*DOWN, color=WHITE)
		self.col_arrows[coord] = arr
		return self
	def add_arrows(self, coords):
		return self

	def vertex(self):
		vertices = []
		board = Board(rows = self.rows+1, columns=self.columns+1)
		cells = board.cells
		for i in range(board.rows):
			p = []
			for j in range(board.columns):
				p.append(cells[i][j].get_center()+DL*board.size/2-cells[0][0].get_center()+self.cells[0][0].get_center())
			p.append
			vertices.append(p)
		self.vertices = vertices	
		return vertices
		
	def outline(self, vertex_list, color=ORANGE):
		line = VGroup()
		for i in range(len(vertex_list)-1):
			line += Line(vertex_list[i], vertex_list[i+1], color=color)
		return line

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