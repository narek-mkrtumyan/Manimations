import numpy as np
import csv
from manim import *

MANY_COLORS = [WHITE, GREEN, ORANGE, RED, BLUE, YELLOW, PURPLE, DARK_BROWN, PINK, GREY]

sizes = range(3,11)
for i in sizes:
    matrix = np.random.randint(low=0,high=i-1, size=(i,i))
    np.savetxt(f"{i}.csv", matrix, delimiter=",")