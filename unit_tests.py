"""Unit tests for Sudoku solver
"""

from solve import Grid

def main():
	easy = "003020600900305001001806400008102900700000008006708200002609500800203009005010300"

	grid_easy = Grid(easy)
	grid_easy.display()
	u = grid_easy.units["A1"]
	print(u)
	assert(len(u) == 3)
	for i in u:
		assert(len(i) == 9)
	print("\n")
	print(grid_easy.peers["A1"])
	assert(len(grid_easy.peers["A1"]) == 20)




if __name__ == "__main__":
	main()