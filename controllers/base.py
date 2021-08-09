from tinydb import TinyDB, Query

from typing import List
from datetime import datetime


from models.tournament import Tournament
from models.player import Player
from models.round import Match


class Controller:
    """class to accept user data, launch new tournaments, produce match results"""

    def __init__(self, view):
        """init the controller"""
        self.db = TinyDB("db.json")
        self.tournaments: List[Tournament] = []

        self.view = view

        self.list_players = []

    def choice_main_menu(self):
        """ This function display the main menu"""
        main_menu = True
        while main_menu:
            option_main_menu = self.view.show_main_menu()

            if option_main_menu == "1":
                self.generate_tournament()
            elif option_main_menu == "2":
                tournament = self.continue_tournament()
                self.choice_secondary_menu(tournament)
            elif option_main_menu == "3":
                db = self.db
                list_tournaments = db.table("tournament").all()
                if not list_tournaments:
                    self.view.show_message("The list of tournaments is empty")
                else:
                    self.get_all_tournaments()
            elif option_main_menu == "4":
                db = self.db
                list_players = db.table("player").all()
                if not list_players:
                    self.view.show_message("The list of players is empty")
                else:
                    self.get_all_player()
            elif option_main_menu == "5":
                self.view.show_message("__________ GOODBYE __________")
                main_menu = False
            else:
                self.view.show_message("Please make a selection from menu")

    def choice_secondary_menu(self, tournament):
        """ This function display the secondary menu
        :param tournament:
        """
        secondary_menu = True
        while secondary_menu:
            option_secondary_menu = self.view.show_secondary_menu()

            if option_secondary_menu == "1":
                round_match = tournament.generate_round()
                if round_match is None:
                    self.view.show_message("You have reached the last round of the tournament")
                else:
                    self.view.show_message("____ {} ____".format(round_match.name))
                    self.add_result_match(round_match)
            elif option_secondary_menu == "2":
                self.display_players(tournament)
            elif option_secondary_menu == "3":
                comment = self.view.prompt_user_input("Comment")
                tournament.add_comment(comment)
            elif option_secondary_menu == "4":
                self.save_all()
                secondary_menu = False
            elif option_secondary_menu == "5":
                self.choice_main_menu()
            else:
                self.view.show_message("Please make a selection from menu")

    def check_pace_entry(self):
        """
        :return:3
        """

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

    def check_tournament_exit(self):
        while True:
            name = self.view.prompt_user_input("Name")
            db = self.db
            tournaments_table = db.table("tournament")
            tour = Query()
            registered_name = tournaments_table.search(tour.name == str(name))
            if not registered_name:
                return name
            else:
                self.view.show_message("This tournament already exists, choose another name")

    def add_tournament(self):
        """
        :return:
        """
        self.view.show_message("______Tournament information______")
        name = self.check_tournament_exit()
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
        """
        :return:
        """
        tournament = self.add_tournament()
        self.tournaments.append(tournament)
        self.view.show_message("________ Player registration _______")
        for i in range(1, tournament.number_of_players + 1):
            player = self.get_player(i)
            tournament.add_player(player)
            self.players_table(player)

        self.choice_secondary_menu(tournament)

    def check_result_match_entry(self, player1, player2):
        """
        :param player1:
        :param player2:
        :return:
        """
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

            match_score = Match([player1.last_name, player1.score], [player2.last_name, player2.score])
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
            self.players_table(player)

    def display_players(self, tournament):
        """
        :param tournament:
        :return:
        """
        view_list = self.view.prompt_user_input("1 sort by ranking, 2 sort by name or 3 update ranking")
        if view_list == "1":
            list_players = tournament.sort_players_by_ranking()
            self.view.show_player_ranking(list_players)
        elif view_list == "2":
            list_players = tournament.sort_player_by_name()
            self.view.show_player_name(list_players)
        elif view_list == "3":
            self.update_ranking(tournament)
        else:
            self.view.show_message("Please choose 1, 2 or 3")

    def quit_tournament(self, tournament):
        """
        :param tournament:
        :return:
        """
        number_round = tournament.get_next_round_number()
        if number_round != tournament.number_of_round:
            result = self.view.prompt_quit_tournament()
            return result
        else:
            return False

    def players_table(self, player: Player):
        """
        :param player:
        :return:
        """
        db = self.db
        players_table = db.table("player")
        user = Query()
        players_table.upsert({
            "last_name": player.last_name,
            "first_name": player.first_name,
            "birth": player.date_of_birth,
            "gender": player.gender,
            "ranking": player.ranking,
            "score": player.score
        }, (user.last_name == str(player.last_name)) & (user.first_name == str(player.first_name)))

    def save_tournament(self, tournament: Tournament):
        """
        :param tournament:
        :return:
        """
        db = self.db
        tournaments_table = db.table("tournament")
        tour = Query()
        tournaments_table.upsert({
            "name": tournament.name,
            "location": tournament.location,
            "date": tournament.date,
            "pace": tournament.time_control,
            "comment": tournament.description,
            "players": [x.serialize() for x in tournament.list_players],
            "rounds": [x.serialize() for x in tournament.list_rounds]

        }, tour.name == str(tournament.name))

    def get_all_tournaments(self):
        """
        :return:
        """
        db = self.db
        tournaments_table = db.table("tournament").all()
        self.view.show_tournament_list(tournaments_table)
        while True:
            chosen_tournament = self.view.prompt_user_input("Choose a tournament")

            if int(chosen_tournament) > len(tournaments_table):
                self.view.show_message("Invalid value")
            else:
                tournament = Tournament.deserialize(tournaments_table[int(chosen_tournament) - 1])
                print(tournament.list_rounds)

       # tournaments = self.db.table("tournament").all()
        #return tournaments

    def get_all_player(self):
        list_players = self.db.table("player").all()
        for i in list_players:
            player = Player.deserialize(i)
            self.view.show_message("_____________________________________")
            self.view.show_message("Last name: {}".format(player.last_name))
            self.view.show_message("First name: {}".format(player.first_name))
            self.view.show_message("Date of birth: {}".format(player.date_of_birth))
            self.view.show_message("Ranking: {}".format(player.ranking))

    def save_all(self):
        for tournament in self.tournaments:
            self.save_tournament(tournament)

        #self.players_table()

    def continue_tournament(self):
        db = self.db
        tournaments_table = db.table("tournament").all()
        self.view.show_tournament_list(tournaments_table)
        while True:
            selected_tour = self.view.prompt_user_input("Choose a tournament")
            if int(selected_tour) > len(tournaments_table):
                self.view.show_message("trop haut")
            else:
                tournament = tournaments_table[int(selected_tour) - 1]
                return Tournament.deserialize(tournament)

    def run_tournament(self):
        """
        :return:
        """
        self.view.show_message("__________ WELCOME TO THE CHESS TOURNAMENT PROGRAM __________")
        self.choice_main_menu()