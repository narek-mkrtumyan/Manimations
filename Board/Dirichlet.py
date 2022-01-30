from manim import *
from Board import Board, T4

import numpy as np
import csv
import pandas as pd
from numpy import genfromtxt


class Knights(Scene):
	def first(self):
		pass
	def construct(self):
		rows = 8
		columns = 8
		self.board = Board(rows=rows, columns=columns, stroke_width=0.05)
		self.board.make_chess()

		self.play(Create(self.board))
		self.wait()