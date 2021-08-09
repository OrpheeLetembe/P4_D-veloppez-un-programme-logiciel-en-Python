""" Tournament """

from typing import List
from operator import attrgetter

from models.player import Player
from models.round import Round


class Tournament:
    """
        A class to represent a tournament.
        ...
        Attributes
        ----------
        name    : str
            tournament name
        location : str
            tournament location
        date    : str
            date of the tournament
        number of round    : int
            number of rounds
        list_rounds   : list
            tournament round list
        list_players    : list
            list of tournament players
        number_of_players: int
            number of players for a tournament
        time_control   : str
            tournament pace
        description : str
            general remarks from the tournament
        Methods
        -------
        get_next_round_number():
            returns the size of the round list + 1
        add_player(player):
            add a player to the list of players
        add_comment(comment):
            Add a comment in the tournament description
        sort_players_by_ranking():
            returns the list of players sorted by ranking
        sort_players_by_score_rank():
            returns the list of players sorted by score and ranking
        sort_players_by_name():
            returns the list of players sorted by name
        generate_round(round_name=None):
            allows to generate the rounds
        generate_first_round(round_name):
            returns the first round of the tournament
        add_round(round):
            Adds a round to the tournament round list
        generate_other_rounds(round_name):
            returns the other rounds of the tournament
        get_opponent(player1, participants):
            allows to find the player 2 for each match from the second round
        match_exists(player1, player2):
            allows you to browse all the matches
        """

    def __init__(self, name, location, date, pace, comment, **kwargs):
        """
        Constructs all the necessary attributes for the tournament object.
        :param name: str
            tournament name
        :param location:  str
            tournament location
        :param date: str
            date of the tournament
        :param pace: str
            tournament pace
        :param comment: str
            general remarks from the tournament
        :param number_of_round: int
            number of rounds in the tournament (default is 4)
        """
        self.name = name
        self.location = location
        self.date = date
        self.number_of_round = 4
        self.list_rounds: List[Round] = []
        self.list_players: List[Player] = []
        self.number_of_players = 4
        self.time_control = pace
        self.description = comment

        if "list_rounds" in kwargs:
            self.list_rounds = kwargs["list_round"]

        if "list_players" in kwargs:
            self.list_players = kwargs["list_players"]

    def __repr__(self):
        return repr((self.name, self.location, self.date, self.time_control))

    def get_next_round_number(self):
        """ This function allows you to number the different rounds of a tournament.
        :return:  size of the round list + 1
        """
        return len(self.list_rounds) + 1

    def add_player(self, player):
        """ add a player to the list of players.
        :param player:
        :return: None
        """
        self.list_players.append(player)

    def add_comment(self, comment):
        """ Add a comment in the tournament description.
        :param comment: str
        :return: None
        """
        self.description += " " + comment

    def sort_players_by_ranking(self):
        """ This function allows to sort the list of players according to their ranking.
        :return: list of players sorted by ranking
        """
        return sorted(self.list_players, key=attrgetter("ranking"))

    def sort_players_by_score_rank(self):
        """ This function allows to sort the list of players according to their score.
        and their ranking
        :return: the list of players sorted by score and ranking
        """
        return sorted(self.list_players, key=attrgetter("score", "ranking"), reverse=True)

    def sort_player_by_name(self):
        """ This function allows to sort the list of players in alphabetical order.
        :return:the list of players sorted by name
        """
        return sorted(self.list_players, key=attrgetter("last_name"))

    def generate_round(self, round_name=None):
        """ This function allows to generate the different rounds.
        If the argument round_name isn't passed in, the return of the function
        get_next_round_number is used.
        :param round_name: str
        :return: the match list of the first round if the round_name = round 1 if not
            returns the match list of the other round
        """

        nb = self.get_next_round_number()
        if round_name is None:
            round_name = 'Round ' + str(nb)

        if nb == 1:
            return self.generate_first_round(round_name)
        elif nb > self.number_of_round:
            return None
        else:
            return self.generate_other_rounds(round_name)

    def generate_first_round(self, round_name) -> Round:
        """ This function divides the list of players sorted by ranking
        into two equal pat and matches the players according to their level.
        :param round_name: str
        :return:
            list of first round match
        """
        list_player_rank = self.sort_players_by_ranking()
        list_players_rank_divided = int(len(list_player_rank) / 2)
        list_player_rank_part1 = list_player_rank[:list_players_rank_divided]
        list_player_rank_part2 = list_player_rank[list_players_rank_divided:]
        round1 = Round(round_name)
        round1.add_match(list(zip(list_player_rank_part1, list_player_rank_part2)))
        self.add_round(round1)
        return round1

    def add_round(self, round):
        """ this function allows to add a round to the list of rounds of the tournament.
        :param round: match list
        :return: None
        """
        self.list_rounds.append(round)

    def generate_other_rounds(self, round_name):
        """ This function allows you to match players from other rounds.
        :param round_name: str
        :return: list of match of the other round
        """
        participants = self.sort_players_by_score_rank()
        list_matchs = []
        while participants:
            player1 = participants[0]
            participants.remove(player1)
            player2 = self.get_opponent(player1, participants)
            participants.remove(player2)
            list_matchs.append({player1, player2})
        other_round = Round(round_name)
        other_round.add_match(list_matchs)
        self.add_round(other_round)
        return other_round

    def get_opponent(self, player1, participants):
        """ This function allows to find the player 2 for each match from the second round.
        :param player1: object
        :param participants: the list of players sorted by score and ranking
        :return: player 2 of the match
        """
        for participant in participants:
            if not self.match_exists(player1, participant):
                return participant
        return participants[0]

    def match_exists(self, player1, player2):
        """ This it scans the list of matches from the previous rounds and determines
        if the first player in the list of players sorted by score and by rating has already
        played with the second player in the list.
        :param player1:
        :param player2:
        :return: bool
        """
        for r in self.list_rounds:
            for match in r.list_match:
                if match == ({player1, player2}):
                    return True
        return False

    def serialize(self):
        return {
            "name": self.name,
            "location": self.location,
            "date": self.date,
            "pace": self.time_control,
            "comment": self.description,
            "players": [x.serialize() for x in self.list_players],
            "rounds": [x for x in self.list_rounds]
        }

    def deserialize(self, serialize_tournament):

        name = serialize_tournament["name"]
        location = serialize_tournament["location"]
        date = serialize_tournament["date"]
        pace = serialize_tournament["pace"]
        comment = serialize_tournament["comment"]
        list_players = serialize_tournament["players"]
        list_rounds = serialize_tournament["rounds"]

        tournament = Tournament(name, location, date, pace, comment, list_players=list_players, list_rounds=list_rounds)
        return tournament


    # Function to test the module
    def scoring(self, round):
        for k, match in enumerate(round.list_match[0]):
            match = list(match)
            player1 = match[0]
            player2 = match[1]

            print("Match {}: {} VS {}".format(k + 1, player1.last_name, player2.last_name))

            winner = int(input("Winner (Enter 1 for {} , 2 for {} or 3 for draw) : ".format(player1.last_name,
                                                                                            player2.last_name)))
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


def main():
    # create tournament
    tournament = Tournament("Tournoi 1", "Avignon", "14/01/2021")
    # add players
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

    # Round 1
    round = tournament.generate_round()
    print(round.name, round.list_match)
    tournament.scoring(round)

    # Round 2
    round = tournament.generate_round()
    print(round.name, round.list_match)
    tournament.scoring(round)

    # Round 3
    round = tournament.generate_round()
    print(round.name, round.list_match)
    tournament.scoring(round)
    # Round 4
    round = tournament.generate_round()
    print(round.name, round.list_match)
    tournament.scoring(round)


if __name__ == "__main__":
    main()