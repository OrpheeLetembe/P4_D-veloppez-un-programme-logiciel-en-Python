"""
Class of players
"""
from operator import attrgetter


class Player:
	"""balabla"""
	
	def __init__(self, last_name, first_name, birth, gender, ranking):
		self.last_name = last_name
		self.first_name = first_name
		self.date_of_birth = birth
		self.gender = gender
		self.ranking = ranking
		self.score = 0

	def __repr__(self):
		return repr((self.last_name, self.first_name, self.date_of_birth, self.gender, self.ranking, self.score))

	def win(self):
		self.score += 1

	def draw(self):
		self.score += 0.5

	def lose(self):
		self.score += 0


def main():
	pass


if __name__ == "__main__":
	main()






