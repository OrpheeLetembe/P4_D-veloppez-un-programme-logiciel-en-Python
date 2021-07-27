

from typing import List


from models.tournament import Tournament
from models.player import Player
from models.round import Match


class Controller:
    """class to accept user data, launch new tournaments, produce match results"""

    def __init__(self, view):
        """init the controller"""
        self.tournaments: List[Tournament] = []

        self.view = view

    def choice_main_menu(self):
        """

        :return:
        """
        while True:
            option_main_menu = self.view.show_main_menu(self)

            if option_main_menu == "1":
                tournament = self.add_tournament()
                self.tournaments.append(tournament)
                for i in range(1, tournament.number_of_players + 1):
                    player = self.get_player(i)
                    tournament.add_player(player)
                self.choice_secondary_menu(tournament)
            elif option_main_menu == "2":
                if not self.tournaments:
                    self.view.show_message(self, "The list of tournaments is empty")
                   # self.choice_main_menu()
                else:
                    self.view.show_tournament_list(self, self.tournaments)
            elif option_main_menu == "3":
                self.view.show_message(self, "Goodbye")
                break
            else:
                self.view.show_message(self, "Please make a selection from menu")
                #self.choice_main_menu()

    def choice_secondary_menu(self, tournament):
        """

        :param tournament:
        :return:
        """
        while True:
            option_secondary_menu = self.view.show_secondary_menu(self)

            if option_secondary_menu == "1":
                round = tournament.generate_round()
                if round is None:
                    self.view.show_message(self, "You have reached the last round of the tournament")
                else:
                    self.view.show_message(self, "____ {} ____".format(round.name))
                    self.add_result_match(round)
            elif option_secondary_menu == "2":
                self.update_ranking(tournament)
            elif option_secondary_menu == "3":
                print("option 3")
            elif option_secondary_menu == "4":
                comment = self.view.prompt_tournament_comment(self)
                tournament.add_comment(comment)
                print(tournament.description)
            elif option_secondary_menu == "5":
                self.choice_main_menu()
            else:
                self.view.show_message(self, "Please make a selection from menu")
                #self.choice_secondary_menu()

    def check_pace_entry(self):
        """ bal"""
        time_control = {"1": "Bullet", "2": "Blitz", "3": "Quick hit"}
        while True:
            pace = self.view.prompt_tournament_pace(self)
            if pace == "1":
                return time_control["1"]
            elif pace == "2":
                return time_control["2"]
            elif pace == "3":
                return time_control["3"]
            else:
                self.view.show_message(self, " {} is not part of the choice list".format(pace))

    def add_tournament(self):
        """

        :return:
        """
        name = self.view.prompt_tournament_name(self)
        location = self.view.prompt_tournament_location(self)
        date = self.view.prompt_tournament_date(self)
        pace = self.check_pace_entry()
        comment = self.view.prompt_tournament_comment(self)
        tournament = Tournament(name, location, date, pace, comment)
        print(tournament)
        self.view.show_players_title(self)
        return tournament

    def check_gender_entry(self):
        """

        :return:
        """
        while True:
            gender = self.view.prompt_player_gender(self)
            if gender == "M" or gender == "F":
                return gender
            else:
                self.view.show_message(self, "the gender of the player must be M or F")

    def check_ranking_entry(self):
        """

        :return:
        """
        while True:
            ranking = self.view.prompt_player_ranking(self)
            result = ranking.isdigit()
            if result:
                return int(ranking)
            else:
                self.view.show_message(self, "The player's ranking must be a positive number")

    def get_player(self, number_player):
        """

        :param number_player:
        :return:
        """
        self.view.show_player_number(number_player)
        last_name = self.view.prompt_player_last_name(self)
        first_name = self.view.prompt_player_first_name(self)
        birth = self.view.prompt_player_date_of_birth(self)
        gender = self.check_gender_entry()
        ranking = self.check_ranking_entry()
        player = Player(last_name, first_name, birth, gender, ranking)
        return player

    def add_result_match(self, round):
        """

        :param round:
        :return:
        """
        for k, match in enumerate(round.list_match[0]):
            match = list(match)
            player1 = match[0]
            player2 = match[1]

            self.view.show_opponent(self, k, player1.last_name, player2.last_name)

            winner = self.view.prompt_of_winner(self, player1.last_name, player2.last_name)

            if winner == "1":
                player1.win()
                player2.lose()
            elif winner == "2":
                player2.win()
                player1.lose()
            elif winner == "3":
                player1.draw()
                player2.draw()
            else:
                self.view.show_message(self, "Please enter 1, 2 or 3")

            match_score = Match([player1.last_name, player1.score], [player2.last_name, player2.score])
            round.add_match_score(match_score)
            round.save_end_date()

    def update_ranking(self, tournament):
        """

        :param tournament:
        :return:
        """

        self.view.show_message(self, "______Update ranking________")
        for player in tournament.list_players:
            self.view.show_update_kanking(self, player.last_name, player.ranking)
            self.view.show_message(self, "New ranking")
            player.ranking = self.check_ranking_entry()

    def run_tournament(self):
        """

        :return:
        """
        self.view.show_message(self, "__________ WELCOME __________")
        self.choice_main_menu()















