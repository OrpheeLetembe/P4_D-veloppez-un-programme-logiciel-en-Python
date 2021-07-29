

from typing import List
from datetime import datetime


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
            option_main_menu = self.view.show_main_menu()

            if option_main_menu == "1":
                self.generate_tournament()
            elif option_main_menu == "2":
                if not self.tournaments:
                    self.view.show_message("The list of tournaments is empty")
                else:
                    self.view.show_tournament_list(self.tournaments)
            elif option_main_menu == "3":
                self.view.show_message("__________ GOODBYE __________")
                break
            else:
                self.view.show_message("Please make a selection from menu")

    def choice_secondary_menu(self, tournament):
        """

        :param tournament:
        :return:
        """
        running = True
        while running:
            option_secondary_menu = self.view.show_secondary_menu()

            if option_secondary_menu == "1":
                round_match = tournament.generate_round()
                if round_match is None:
                    self.view.show_message("You have reached the last round of the tournament")
                else:
                    self.view.show_message("____ {} ____".format(round_match.name))
                    self.add_result_match(round_match)
            elif option_secondary_menu == "2":
                self.update_ranking(tournament)
            elif option_secondary_menu == "3":
                self.display_ranking(tournament)
            elif option_secondary_menu == "4":
                comment = self.view.prompt_tournament_comment()
                tournament.add_comment(comment)
            elif option_secondary_menu == "5":
                running = self.quit_tournament(tournament)
            elif option_secondary_menu == "6":
                self.choice_main_menu()
            else:
                self.view.show_message("Please make a selection from menu")

    def check_pace_entry(self):
        """ bal"""
        time_control = {"1": "Bullet", "2": "Blitz", "3": "Quick hit"}
        while True:
            pace = self.view.prompt_user_input("Time control (Enter 1 for bullet, 2 for blitz or 3 for quick hit")
            if pace == "1":
                return time_control["1"]
            elif pace == "2":
                return time_control["2"]
            elif pace == "3":
                return time_control["3"]
            else:
                self.view.show_message(" {} is not part of the choice list".format(pace))

    def check_date_entry(self, text):
        """

        :return:
        """
        while True:
            date = self.view.prompt_user_input(text)
            try:
                date_time = datetime.strptime(date, '%d/%m/%Y')
                if date_time:
                    return date
            except ValueError:
                self.view.show_message("Please enter a date in day/month/year format")

    def add_tournament(self):
        """

        :return:
        """
        self.view.show_message("______Tournament information______")
        name = self.view.prompt_user_input("Name")
        location = self.view.prompt_user_input("Location")
        date = self.check_date_entry("Date")
        pace = self.check_pace_entry()
        comment = self.view.prompt_user_input("Add a comment")
        tournament = Tournament(name, location, date, pace, comment)

        return tournament

    def check_gender_entry(self):
        """

        :return:
        """
        while True:
            gender = self.view.prompt_user_input("Gender")
            capitalize_gender = gender.capitalize()
            if capitalize_gender == "M" or capitalize_gender == "F":
                return capitalize_gender
            else:
                self.view.show_message("the gender of the player must be M or F")

    def check_ranking_entry(self):
        """

        :return:
        """
        while True:
            ranking = self.view.prompt_user_input("Ranking")
            result = ranking.isdigit()
            if result:
                return int(ranking)
            else:
                self.view.show_message("The player's ranking must be a positive number")

    def get_player(self, number_player):
        """

        :param number_player:
        :return:
        """
        self.view.show_player_number(number_player)
        last_name = self.view.prompt_user_input("Last name")
        first_name = self.view.prompt_user_input("First name")
        birth = self.check_date_entry("Date of birth")
        gender = self.check_gender_entry()
        ranking = self.check_ranking_entry()
        player = Player(last_name, first_name, birth, gender, ranking)
        return player

    def generate_tournament(self):
        tournament = self.add_tournament()
        self.tournaments.append(tournament)
        print(tournament.description)
        self.view.show_message("________ Player registration _______")
        for i in range(1, tournament.number_of_players + 1):
            player = self.get_player(i)
            tournament.add_player(player)
        self.choice_secondary_menu(tournament)

    def check_result_match_entry(self, player1, player2):
        while True:
            winner = self.view.prompt_of_winner(player1, player2)
            result = winner.isdigit()
            if result:
                winner = int(winner)
                if winner in range(1, 4):
                    return winner
                else:
                    self.view.show_message("Please enter 1, 2 or 3")
            else:
                self.view.show_message("Please enter a number between 1 and 3")

    def add_result_match(self, round):
        """

        :param round:
        :return:
        """
        for k, match in enumerate(round.list_match[0]):
            match = list(match)
            player1 = match[0]
            player2 = match[1]

            self.view.show_opponent(k, player1.last_name, player2.last_name)

            winner = self.check_result_match_entry(player1.last_name, player2.last_name)

            if winner == 1:
                player1.win()
                player2.lose()
            elif winner == 2:
                player2.win()
                player1.lose()
            else:
                player1.draw()
                player2.draw()
            #else:
                #self.view.show_message("Please enter 1, 2 or 3")

            match_score = Match([player1.last_name, player1.score], [player2.last_name, player2.score])
            print(match_score)
            round.add_match_score(match_score)
            round.save_end_date()

    def update_ranking(self, tournament):
        """

        :param tournament:
        :return:
        """

        self.view.show_message("______Update ranking________")
        for player in tournament.list_players:
            self.view.show_update_ranking(player.last_name, player.ranking)
            self.view.show_message("New ranking")
            player.ranking = self.check_ranking_entry()

    def display_ranking(self, tournament):
        list_player = tournament.sort_players_by_ranking()
        print()
        self.view.show_message("________ Ranking ________")
        self.view.show_player_ranking(list_player)

    def quit_tournament(self, tournament):
        number_round = tournament.get_next_round_number()
        if number_round != tournament.number_of_round:
            result = self.view.prompt_quit_tournament()
            return result
        else:
            return False

    def run_tournament(self):
        """

        :return:
        """
        self.view.show_message("__________ WELCOME __________")
        self.choice_main_menu()
