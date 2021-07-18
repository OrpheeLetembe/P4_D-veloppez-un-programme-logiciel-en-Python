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
		return repr((self.last_name, self.first_name, self.date_of_birth, self.gender, self.ranking))

	def win(self):
		self.score += 1

	def draw(self):
		self.score += 0


def main():

	list_of_players = []

	p1 = Player("letembe", "orphée", "13/04/1980", "m", 15)
	list_of_players.append(p1)
	p2 = Player("davion", "alex", "04/06/1982", "f", 10)
	list_of_players.append(p2)
	p3 = Player("letembe davion", "aurore", "10/05/2015", "f", 18)
	list_of_players.append(p3)
	p4 = Player("martin", "joseph", "13/05/1984", "m", 20)
	list_of_players.append(p4)
	p5 = Player("let", "orph", "13/04/1980", "m", 11)
	list_of_players.append(p5)
	p6 = Player("avion", "al", "04/06/1982", "f", 17)
	list_of_players.append(p6)
	p7 = Player("letemion", "aurore", "10/05/2015", "f", 21)
	list_of_players.append(p7)
	p8 = Player("tin", "seph", "13/05/1984", "m", 100)
	list_of_players.append(p8)

	for player in list_of_players:
		print("Player {} ".format(list_of_players.index(player) + 1))
		print(player)

	sort_list_player = sorted(list_of_players, key=attrgetter("ranking"))
	#print(sort_list_player)
	len_list_player = int(len(sort_list_player)/2)
	list_player1 = sort_list_player[:len_list_player]
	list_player2 = sort_list_player[len_list_player:]
	print(list_player1)
	print(list_player2)
	list_matchs = zip(list_player1, list_player2)
	for match in list_matchs:
		print(match)





if __name__ == "__main__":
	main()






