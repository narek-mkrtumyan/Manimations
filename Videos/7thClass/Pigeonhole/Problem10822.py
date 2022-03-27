import sys
sys.path.append('../../../')
from Functions.qarakusi import *

class Problem10822(Scene):
    def construct(self):
        
        board = Board().scale(0.7)

        groups_of_four = [[[], [], [], []], [[], [], [], []], [[], [], [], []], [[], [], [], []]]

        for i in range(8):
            for j in range(8):
                groups_of_four[int(i/2)][int(j/2)].append(board.cells[i][j])
        
        # print(type(groups_of_four[0][0]))

        # groups_of_four = matrix_to_VGroup(groups_of_four)

        # print(groups_of_four)

        for i in range(len(groups_of_four)):
            for j in range(len(groups_of_four[i])):
                groups_of_four[i][j] = VGroup(*groups_of_four[i][j])
            groups_of_four[i] = VGroup(*groups_of_four[i])
        groups_of_four_ = VGroup()
        for i in range(len(groups_of_four)-1, -1, -1):
            for j in range(len(groups_of_four[i])):
                groups_of_four_.add(groups_of_four[i][j])
        

        knight = ChessFigures().white_knight

        self.play(board.animate.make_chess())
        
        self.play(groups_of_four_.animate.arrange_in_grid(4, 4, buff=0.5))

        self.add(knight)
        self.wait()



        # self.play(FadeOut(groups_of_four[0][1]))
        # self.wait()





class test(Scene):
    def construct(self):

        board = Board()
        self.play(board.animate.make_chess())



        white_pawns = VGroup(*[ChessFigures().white_pawn.move_to(board.cells[1][i].get_center()) for i in range(8)])
        black_pawns = VGroup(*[ChessFigures().black_pawn.move_to(board.cells[6][i].get_center()) for i in range(8)])

        white_knights = VGroup(
            ChessFigures().white_knight.move_to(board.cells[0][1]),
            ChessFigures().white_knight.move_to(board.cells[0][6])
        )

        black_knights = VGroup(
            ChessFigures().black_knight.move_to(board.cells[7][1]),
            ChessFigures().black_knight.move_to(board.cells[7][6])
        )

        white_bishops = VGroup(
            ChessFigures().white_bishop.move_to(board.cells[0][2]),
            ChessFigures().white_bishop.move_to(board.cells[0][5])
        )

        black_bishops = VGroup(
            ChessFigures().black_bishop.move_to(board.cells[7][2]),
            ChessFigures().black_bishop.move_to(board.cells[7][5])
        )

        white_rooks = VGroup(
            ChessFigures().white_rook.move_to(board.cells[0][0]),
            ChessFigures().white_rook.move_to(board.cells[0][7])
        )

        black_rooks = VGroup(
            ChessFigures().black_rook.move_to(board.cells[7][0]),
            ChessFigures().black_rook.move_to(board.cells[7][7])
        )

        white_queen = ChessFigures().white_queen.move_to(board.cells[0][3])

        black_queen = ChessFigures().black_queen.move_to(board.cells[7][3])

        white_king = ChessFigures().white_king.move_to(board.cells[0][4])

        black_king = ChessFigures().black_king.move_to(board.cells[7][4])

        self.add(white_pawns)
        self.add(black_pawns)

        self.add(white_knights)
        self.add(black_knights)

        self.add(white_bishops)
        self.add(black_bishops)

        self.add(white_rooks)
        self.add(black_rooks)

        self.add(white_queen)
        self.add(black_queen)

        self.add(white_king)
        self.add(black_king)


        

        


