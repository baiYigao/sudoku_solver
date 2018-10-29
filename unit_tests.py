"""Unit tests for Sudoku solver
"""

from solve import Grid

def main():
	easy = "003020600900305001001806400008102900700000008006708200002609500800203009005010300"

	grid_easy = Grid(easy)
	print("Given board:")
	grid_easy.display()
	grid_easy.solve()
	print("Solved board:")
	grid_easy.display()
	check = grid_easy.check_valid()
	print("Is board valid? {}".format(check))




if __name__ == "__main__":
	main()