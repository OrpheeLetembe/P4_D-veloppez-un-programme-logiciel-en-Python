"""
Class of players
"""
from operator import attrgetter


class Player:
	"""balabla"""
	
	def __init__(self, last_name, first_name, birth, gender, rank):
		self.last_name = last_name
		self.first_name = first_name
		self.date_of_birth = birth
		self.gender = gender
		self.rank = rank

	def __repr__(self):
		return repr((self.last_name, self.first_name, self.date_of_birth, self.gender, self.rank))


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

	sort_list_player = sorted(list_of_players, key=attrgetter("rank"))
	print(sort_list_player)
	print("Round 1")
	print("Match 1 : {} VS {}".format(sort_list_player[0].last_name, sort_list_player[4].last_name))
	print("Match 2 : {} VS {}".format(sort_list_player[1].last_name, sort_list_player[5].last_name))
	print("Match 3 : {} VS {}".format(sort_list_player[2].last_name, sort_list_player[6].last_name))
	print("Match 4 : {} VS {}".format(sort_list_player[3].last_name, sort_list_player[7].last_name))


if __name__ == "__main__":
	main()






