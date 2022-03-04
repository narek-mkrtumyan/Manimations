from math import sqrt
import sys

sys.path.append("../../")
#from Functions.QarakusiFunctions import *
from manim import *
from Functions.Board import *
sys.path.insert(1, 'Objects/SVG_files/chess_figures')

class FourKnights(Scene):
	def construct(self):
		board = Board(size=1, rows=3, columns=3, stroke_width=2)
		#board.make_chess()
		black_knight = SVGMobject(r'C:\Users\Tigran\Documents\GitHub\Manimations\Objects\SVG_files\chess_figures\knight.svg')
		black_knight.width = 0.8
		white_knight = black_knight.copy().set_color(WHITE)
		vertices = range(1,10)
		edges = [(1,8), (1,6), (2,7), (2,9), (3,4), (3,8), (4,9), (6,7)]
		layout = dict()
		for i in 0,1,2:
			for j in 0,1,2:
				layout[3*i+j+1] = board.cells[i][j]
		G = Graph(vertices, edges, layout=layout,vertex_config={'color':RED}, edge_config={'stroke_color': GREEN})

		self.add(board)
		self.play(FadeIn(G))
		white_knight.move_to(board.cells[2][2])
		self.play(FadeIn(white_knight))

n=5
class ThreeColors(Scene):
	def construct(self):
		vertices = range(1,n+1)
		edges = list()
		for i in range(1,n):
			edges.append((i,(i+1)))
		edges.append((n,1))

		G = Graph(vertices,edges, layout="circular")

		edge_config={
			(-1,1) : {"stroke_color": ORANGE},
			(-2,1+n//3) : {"stroke_color": GREEN},
			(-3,1+(2*n)//3) : {"stroke_color": WHITE}
			}
		edge_config = dict()
		G.add_vertices(*[-1,-2,-3], positions={ -1 : [7,7,0], -2 : [-8,3,0], -3: [0,-5,0]})
		G.add_edges(*[(-1,1), (-2,1+n//3), (-3,1+(2*n)//3)], edge_config=edge_config)

		vedges = list(G.edges.values())
		edges = list(G.edges.keys())

		vedges[1].set_color(ORANGE)
		vedges[2].set_color(GREEN)

		self.play(Write(G))
		self.wait()
		#self.play(G.animate.change_layout("kamada_kawai"))

		array = np.genfromtxt('vertice_coords.csv', delimiter=',')
		b = np.zeros((n,3))
		b[:,:-1] = array
		print(b[0,:])
		#for i in range(1,n+1):
		#	G[i].move_to(b[i-1,:])
		
		self.play(
			*[G[i].animate.move_to(b[i-1,:]) for i in range(1,n+1)]
		)
		self.wait()
		

#arr = np.random.uniform(low=-3.5, high=3.5, size=(n,2))
#np.savetxt("vertex_coords.csv", arr, delimiter=",")
#print(arr)

'''
vertice_r = 0.3

def Vertice(center, radius, phi, color=WHITE):
	vertice=Circle(vertice_r,color,fill_opacity=0)
	vertice.move_to(center+radius/2*np.sin(phi)*UP+radius/2*np.cos(phi)*RIGHT)
	return vertice

def VName(center, radius, phi, color=WHITE, name=' '):
	text = Text(str(name)).scale(0.8)
	text.set_color(color)
	text.move_to(center+radius/2*np.sin(phi)*UP+radius/2*np.cos(phi)*RIGHT)
	return text

def edge(circle1,r1,circle2,r2):
	o1 = circle1.get_center()
	o2 = circle2.get_center()
	v = o2-o1
	x1 = o1+r1*v/((v[0]*v[0]+v[1]*v[1])**0.5)
	x2 = o2-r2*v/((v[0]*v[0]+v[1]*v[1])**0.5)
	return Line(x1,x2)

def graph(vertices,edges):
	v = list()
	names = list()
	e = list()
	n = len(vertices)
	for i in range(n):
		v.append(Vertice(ORIGIN, 3, PI-(i+1)/n*2*PI))
		names.append(VName(ORIGIN, 3, PI-(i+1)/n*2*PI, name=str(vertices[i])))
	m = len(edges)
	for i in range(m):
		e.append(edge(
				v[edges[i][0]-1],vertice_r,
				v[edges[i][1]-1],vertice_r
				))
	return v, names, e

class SSS_Graph(VMobject):
	def __init__(self,vertices,edges):
		self.vertices = vertices
		self.edges = edges
		self.Vertices = list()
		self.VNames = list()
		self.Edges = list()
		self.Vertices.append(Vertice(ORIGIN, 3, PI-1/6*2*PI))
		self.VNames.append(VName(ORIGIN, 3, PI-1/6*2*PI, name=str(self.vertices[0])))
		graph=VGroup(self.Vertices[0], self.VNames[0])
		
		for i in range(1,len(self.vertices)+1):
			self.Vertices.append(Vertice(ORIGIN, 3, PI-2*PI*i/6))
			self.VNames.append(VName(ORIGIN, 3, PI-2*PI*i/6))
			graph=VGroup(graph, self.Vertices[i], self.VNames[i])
		for i in range(len(self.edges)):
			edge = self.edges[i]
			self.Edges.append(Line(self.Vertices[edge[0]],self.Vertices[edge[1]]))
			graph = VGroup(graph,self.Edges[i])
		self.graph = graph


class Graf(VMobject):
	def __init__(self, vertices=[], edges=[]):
		self.vertices = vertices
		self.edges = edges

class EdgesHope(Scene):
	def construct(self):
		vertices = [1,2,3,4,5]
		edges = [(1,2), (4,3), (5,4),(1,3)]

		G = Graph(vertices, edges)

		self.play(Create(G))
		self.wait()
		self.play(G[1].animate.shift(2*RIGHT))

		Edges = list(G.edges.values())
		#self.play(FadeOut(Edges[1]))
		self.play(FadeOut(G[3]))
		self.wait()
'''