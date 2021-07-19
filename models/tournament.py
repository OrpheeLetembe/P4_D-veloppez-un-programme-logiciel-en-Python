

from typing import List
from operator import attrgetter

from models.player import Player
from models.round import Round
from models.round import Match


class Tournament:
	"""blabla"""

	def __init__(self, name, location, date, number_of_round=4):
		self.name = name
		self.location = location
		self.date = date
		self.number_of_round = number_of_round
		self.list_rounds = []
		self.players: List[Player] = []
		self.time_control = ""
		self.description = ""

	def __repr__(self):
		return repr((self.name, self.location, self.date))

	def add_player(self, player):
		self.players.append(player)

	@staticmethod
	def sort_by_ranking(list_player):
		return sorted(list_player, key=attrgetter("ranking"))

	@staticmethod
	def sort_by_score_(list_player):
		return sorted(list_player, key=attrgetter("score"), reverse=True)

	def generate_first_round(self):
		sort_list_player = self.sort_by_ranking(self.players)
		list_players_divided = int(len(sort_list_player)/2)
		list_player_part1 = sort_list_player[:list_players_divided]
		list_player_part2 = sort_list_player[list_players_divided:]
		return list(zip(list_player_part1, list_player_part2))

	def add_round(self, rounds):
		self.list_rounds.append(rounds)

	def generate_other_rounds(self):
		raise NotImplementedError


def main():
	tournament = Tournament("Tournoi 1", "Avignon", "14/01/2021")
	print(tournament)
	p1 = Player("letembe", "orphee", "13/04/1980", "m", 5)
	tournament.add_player(p1)
	p2 = Player("davion", "alex", "11/04/1980", "f", 4)
	tournament.add_player(p2)
	p3 = Player("martin", "toto", "11/04/1980", "M", 2)
	tournament.add_player(p3)
	p4 = Player("diallo", "papa", "11/04/1990", "M", 3)
	tournament.add_player(p4)
	p5 = Player("Able", "coucou", "13/04/1980", "f", 6)
	tournament.add_player(p5)
	p6 = Player("jacob", "jean", "11/04/1980", "m", 8)
	tournament.add_player(p6)
	p7 = Player("mamama", "andy", "11/04/1980", "M", 7)
	tournament.add_player(p7)
	p8 = Player("salif", "henry", "11/04/1990", "M", 1)
	tournament.add_player(p8)

	#vue
	print(tournament.number_of_round)

	round1 = Round("Round" + " " + str(Round.number_of_rounds))
	tournament.add_round(round1)
	list_of_match_round1 = tournament.generate_first_round()
	round1.add_match(list_of_match_round1)

	#print(tournament.players.index())


	for k, match in enumerate(list_of_match_round1):
		print("Match {}: {} VS {}".format(k + 1, match[0].last_name, match[1].last_name))

		winner = input("Winner : ")  # add control
		player1 = ""
		player2 = ""
		for player in match:
			if player.last_name == match[0].last_name:
				player1 = player
			elif player.last_name == match[1].last_name:
				player2 = player
		if winner == player1.last_name:
			player1.win()
			print(player1.last_name, player1.score)
		elif winner == player1.last_name:
			player2.win()
			print(player2.last_name, player2.score)
		elif winner == "draw":
			player1.draw()
			player2.draw()
			print(player1.score, player2.score)



if __name__ == "__main__":
	main()