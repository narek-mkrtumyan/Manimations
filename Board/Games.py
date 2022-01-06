from manim import *
from Table import Board

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

class a3h8(Scene):
	CONFIG = {
	'lose_color' : RED
	}
	def construct(self):
		lose_color = RED
		board = Board()
		self.add(board)
		self.play(
			board.animate.color_cell([6,7], lose_color),
			board.animate.color_cell([7,6], lose_color)
			)
		self.wait()

		queen = SVGMobject('queen.svg')
		queen.color = WHITE
		queen.width = board.cells[0][0].width
		queen.move_to(board.cells[7][6])
		self.play(Create(queen))
		self.wait()