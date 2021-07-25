

class Player:
	"""
	A class to represent a player.
	...

	Attributes
	----------
	last_name : str
		player's last name
	first_name : str
		player's first name
	birth     : str
		player's date of birth
	gender    : str
		player's gender
	ranking   : int
		player's ranking
	score     : int
		player's score

	Methods
	-------
	Win():
		Adds one point to the player's score
	draw():
		Adds 0.5 to player's score
	lose():

	"""
	
	def __init__(self, last_name, first_name, birth, gender, ranking):
		"""
		Constructs all the necessary attributes for the player object.

		Parameters
		----------
		last_name  : str
			family name of the player
		first_name : str
			first name of the player
		birth      : str
			date of birth of the player
		gender     : str
			gender of the player
		ranking    : int
			ranking of the player

		"""
		self.last_name = last_name
		self.first_name = first_name
		self.date_of_birth = birth
		self.gender = gender
		self.ranking = ranking
		self.score = 0

	def __repr__(self):
		return repr((self.last_name, self.first_name, self.date_of_birth, self.gender, self.ranking, self.score))

	def win(self):
		"""Adds 1 to the player's score."""
		self.score += 1

	def draw(self):
		"""Adds 0.5 to the player's score."""
		self.score += 0.5

	def lose(self):
		self.score += 0


def main():
	pass


if __name__ == "__main__":
	main()






