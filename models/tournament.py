

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
		self.list_rounds: List[Round] = []
		self.list_players: List[Player] = []
		self.time_control = ""
		self.description = ""

	def __repr__(self):
		return repr((self.name, self.location, self.date))

	def get_next_round_number(self):
		return len(self.list_rounds) + 1

	def add_player(self, player):
		self.list_players.append(player)

	def sort_players_by_ranking(self):
		return sorted(self.list_players, key=attrgetter("ranking"))

	def sort_players_by_score_rank(self):
		return sorted(self.list_players, key=attrgetter("score", "ranking"), reverse=True)

	def generate_round(self, round_name=None):
		nb = self.get_next_round_number()
		if round_name is None:
			round_name = 'Round ' + str(nb)

		if nb == 1:
			return self.generate_first_round(round_name)
		else:
			return self.generate_other_rounds(round_name)

	def generate_first_round(self, round_name) -> Round:
		list_player_rank = self.sort_players_by_ranking()
		list_players_rank_divided = int(len(list_player_rank) / 2)
		list_player_rank_part1 = list_player_rank[:list_players_rank_divided]
		list_player_rank_part2 = list_player_rank[list_players_rank_divided:]
		round1 = Round(round_name)
		round1.add_match(list(zip(list_player_rank_part1, list_player_rank_part2)))
		self.add_round(round1)
		return round1


	def add_round(self, round):
		self.list_rounds.append(round)

	def generate_other_rounds(self, round_name):
		participants = self.sort_players_by_score_rank()
		#set_list_player_score_rank = set(list_player_score_rank)
		#print("participants : {}".format(participants))
		list_matchs = []
		while participants:
			player1 = participants[0]
			participants.remove(player1)
			player2 = self.get_opponent(player1, participants)
			participants.remove(player2)
			list_matchs.append({player1, player2})
		round = Round(round_name)
		round.add_match(list_matchs)
		self.add_round(round)
		# boucler sur les joueurs restants
		# selectionner un 2eme joueur avec lequel il n'a jamais joué
		# il faudra parcourir toutes les rounds et vérifier qu'il n'y a aucun match

		return round

	def get_opponent(self, player1, participants):
		for round in self.list_rounds:
			for match in round.list_match:
				if match == ({player1, participants[0]}):
					return participants[1]
				else:
					return participants[0]


		#Todo: parmis la liste des participants trouver le premier joueur qui n'a jamais joué avec player1
		return


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

	round = tournament.generate_round()
	print(round.name, round.list_match)
	for k, match in enumerate(round.list_match[0]):
		match = list(match)
		player1 = match[0]
		player2 = match[1]

		print("Match {}: {} VS {}".format(k + 1, player1.last_name, player2.last_name))

		winner = int(input("Winner (Enter 1 for {} , 2 for {} or 3 for draw) : ".format(player1.last_name, player2.last_name)))  # add control

		if winner == 1:
			player1.win()
			player2.lose()
			print(player1.last_name, player1.score)
		elif winner == 2:
			player2.win()
			player1.lose()
			print(player2.last_name, player2.score)
		elif winner == 3:
			player1.draw()
			player2.draw()
			print(player1.score, player2.score)


	round = tournament.generate_round()
	print(round.list_match)


if __name__ == "__main__":
	main()



