"""Backtracking approach to solve Sudoku puzzle

input: a string of numbers representing the 9x9 board from top left to 
bottom right (81 number of characters). 0 represents empty square.

output: a visual board that is correctly filled according to Sudoku puzzle rules.
"""

def cross_product(A, B):
	"""Return a list that is the cross product of A and B
	"""
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
		self.squares = cross_product(self.rows, self.columns) #squares (represented by) labels sorted by rows going from top to bottom and left to right
		for i in range(len(self.squares)):
			self.board[self.squares[i]] = s[i] #store square label to value mapping
		self.unit_list = ([cross_product(self.rows, c) for c in self.columns] +
						 [cross_product(r, self.columns) for r in self.rows] +
						 [cross_product(rs, cs) for rs in ["ABC", "DEF", "GHI"] for cs in ["123", "456", "789"]])
		assert(len(self.unit_list) == 27)
		self.units = dict((s, [u for u in self.unit_list if s in u]) for s in self.squares) #store a list of units that associate with each square
		self.peers = dict((s, set(sum(self.units[s], [])) - set([s])) for s in self.squares) #store a set of peers that associate with each sqaure



	
	def display(self):
		"""Visualize board as a 2-D grid
		"""
		width = 1 + max(len(self.board[s]) for s in self.squares)
		line = '+'.join(['-' * (width * 3)] * 3)
		for r in self.rows:
			print("".join(self.board[r + c].center(width) + ("|" if c in "36" else "") for c in self.columns))
			if r in "CF": print line
		print

	def find_unassigned(self):
		"""Find the next unassigned square in the board

		Returns:
			square label if found; -1 if all squares have filled
		"""
		for s in self.squares:
			if self.board[s] == "0":
				return s
		else:
			return -1

	def check_candidate(self, s, c):
		"""Check if a number is valid for a square position
		Args:
			s: label of the square
			c: the number to fill in

		Returns:
			True if the number is valid in that square; False if not
		"""
		for p in self.peers[s]:
			if self.board[p] == c:
				return False
		return True


	def solve(self):
		"""Solve the puzzle
		Returns:
			True if solved; False if not
		"""
		square_to_fill = self.find_unassigned()
		if square_to_fill == -1:
			return True
		for candidate in self.digits:
			if self.check_candidate(square_to_fill, candidate) == False:
				continue
			self.board[square_to_fill] = candidate
			if self.solve():
				return True
		self.board[square_to_fill] = "0"
		return False


	def check_valid(self):
		"""Check if a board is a valid and filled Sudoku board
		Returns:
			True if it is valid and filled; False if not
		"""
		for s in self.squares:
			val = self.board[s]
			for p in self.peers[s]:
				if self.board[p] == val:
					return False
		return True







