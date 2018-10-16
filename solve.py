"""Constraint Propagation approach to solve Sudoku puzzle

input: a string of numbers representing the 9x9 board from top left to 
bottom right (81 number of characters). 0 represents empty square.

output: a visual board that is filled according to Sudoku puzzle rules.

"""

def cross_product(A, B):
	return [a + b for a in A for b in B]

class Grid:
	"""A grid class that represents Sudoku puzzle

	Args:
		s: input string representing Sudoku board

	"""
	def __init__(self, s):
		assert(len(s) == 81)
		self.input = s
		self.board = {}
		self.digits = "123456789"
		self.rows = "ABCDEFGHI"
		self.columns = "123456789"
		self.squares = cross_product(self.rows, self.columns)
		for i in range(len(self.squares)):
			self.board[self.squares[i]] = s[i]
		self.unit_list = [cross_product(self.rows, c) for c in self.columns] + [cross_product(r, self.columns) for r in self.rows] + [cross_product(rs, cs) for rs in ["ABC", "DEF", "GHI"] for cs in ["123", "456", "789"]]
		assert(len(self.unit_list) == 27)
		self.units = dict((s, [u for u in self.unit_list if s in u]) for s in self.squares)
		self.peers = dict((s, set(sum(self.units[s], [])) - set([s])) for s in self.squares)



	
	def display(self):
		"""Visualize board as a 2-D grid
		"""
		width = 1 + max(len(self.board[s]) for s in self.squares)
		line = '+'.join(['-' * (width * 3)] * 3)
		for r in self.rows:
			print("".join(self.board[r + c].center(width) + ("|" if c in "36" else "") for c in self.columns))
			if r in "CF": print line
		print





