""" Class controller"""

from tinydb import TinyDB, Query

from operator import attrgetter
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
        self.list_players = []

        self.view = view

    def choice_main_menu(self):
        """ This function display the main menu.
        it allows the creation of a new tournament, the display of the list of tournaments
        and the display of the list of all players

        """
        main_menu = True
        while main_menu:
            option_main_menu = self.view.show_main_menu()

            if option_main_menu == "1":
                self.generate_tournament()
                main_menu = False
            elif option_main_menu == "2":
                db = self.db
                list_tournaments = db.table("tournament").all()

                if not list_tournaments:
                    self.view.show_message("The list of tournaments is empty")
                else:
                    self.get_all_tournaments()
                    main_menu = False

            elif option_main_menu == "3":
                db = self.db
                list_players = db.table("player").all()

                if not list_players:
                    self.view.show_message("The list of players is empty")
                else:
                    self.get_all_player()
                    main_menu = False

            elif option_main_menu == "4":
                self.view.show_message("__________ THANK YOU FOR USING THE CHESS PROGRAM, GOODBYE __________")
                main_menu = False

            else:
                self.view.show_message("Please make a selection from menu")

    def choice_secondary_menu(self, tournament):
        """ This function display the secondary menu.
        it allows you to add the results of the matches, update the players' ranking,
        add comments and save the tournament.

        :param tournament: Tournament object
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
                self.update_ranking(tournament.list_players)
            elif option_secondary_menu == "3":
                comment = self.view.prompt_user_input("Comment")
                tournament.add_comment(comment)
            elif option_secondary_menu == "4":
                self.save_all()
            elif option_secondary_menu == "5":
                self.choice_main_menu()
                secondary_menu = False
            else:
                self.view.show_message("Please make a selection from menu")

    def check_tournament_exit(self):
        """This function checks if the name of the tournament entered by the user
        is not already present in the list of registered tournaments.

        :return:str
            tournament name
        """
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

    def check_date_entry(self, text):
        """ This function checks that the date entered by the user is in day/month/year format.
        :return: str
           date entered by user
        """
        while True:
            date = self.view.prompt_user_input(text)
            try:
                date_time = datetime.strptime(date, '%d/%m/%Y')

                if date_time:
                    return date
            except ValueError:
                self.view.show_message("Please enter a date in day/month/year format (example 4/10/2000)")

    def check_pace_entry(self):
        """This function checks if the user's input complies with the different
        time management types of a tournament.
        :return:str
            Type of time management chosen by the user

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

    def add_tournament(self):
        """ The purpose of this function is to create a new tournament
        :return:tournament object
        """
        self.view.show_message("______Tournament information______")
        name = self.check_tournament_exit()
        location = self.view.prompt_user_input("Location")
        date = datetime.now().strftime("%d/%m/%Y")
        pace = self.check_pace_entry()
        comment = self.view.prompt_user_input("Add a comment")
        tournament = Tournament(name, location, date, pace, comment)
        tournament.add_date(date)

        return tournament

    def check_gender_entry(self):
        """ This function checks that the user's entered gender is m or f.
        :return:str
             Player's gender
        """
        while True:
            gender = self.view.prompt_user_input("Gender")
            list_gender = ["m", "f"]

            if gender in list_gender:
                return gender.capitalize()
            else:
                self.view.show_message("The gender of the player must be M or F")

    def check_ranking_entry(self):
        """ This function checks that the ranking entered by the user is a number

        :return:int
            player's ranking
        """
        while True:
            ranking = self.view.prompt_user_input("Ranking")
            result = ranking.isdigit()

            if result:
                return int(ranking)
            else:
                self.view.show_message("The player's ranking must be a positive number")

    def check_id_player(self):
        """ This function checks that the ID entered by the user is a number.

        :return: int
            player's ID
        """
        while True:
            player_id = self.view.prompt_user_input("Select a player ID ")
            result = player_id.isdigit()

            if result:
                return int(player_id)
            else:
                self.view.show_message("The player's ID must be a positive number")

    def add_new_players(self, tournament, number):
        """ This function allows to add a new player to the tournament and the list of players

        :param tournament: tournament object
        :param number:int

        """
        player = self.get_player(number)
        tournament.add_player(player)
        self.players_table(player)

    def get_player(self, number_player):
        """ This function allows the creation of a new player.

        :param number_player: int
        :return:player object
        """
        self.view.show_player_number(number_player)
        last_name = self.view.prompt_user_input("Last name")
        first_name = self.view.prompt_user_input("First name")
        birth = self.check_date_entry("Date of birth (day/month/year)")
        gender = self.check_gender_entry()
        ranking = self.check_ranking_entry()
        player = Player(last_name, first_name, birth, gender, ranking)

        return player

    def add_player_from_list_players(self, tournament):
        """ This function allows to add a player from the list of players to the tournament

        :param tournament: tournament objet

        """
        db = self.db
        list_players = db.table("player").all()
        list_players_deserialize = [Player.deserialize(x) for x in list_players]

        for player in list_players_deserialize:
            self.view.show_add_players(player, list_players_deserialize.index(player) + 1)

        selected_player = self.check_id_player()
        player = list_players_deserialize[selected_player - 1]
        tournament.add_player(player)

        self.view.show_message(" Number of registered players :{}".format(len(tournament.list_players)))

    def old_or_new_players(self, tournament):
        """ This function allows the user to choose between adding a player from the list and adding a new player.

        :param tournament: tournament object
        """
        number_registered_players = 1
        while number_registered_players < tournament.number_of_players + 1:
            choice = self.view.prompt_user_input("1 add from the list of players  2 add a new player")

            if choice == "1":
                self.add_player_from_list_players(tournament)
                number_registered_players += 1
            elif choice == "2":
                self.add_new_players(tournament, number_registered_players)
                number_registered_players += 1
            else:
                self.view.show_message("Please select from the list")

    def generate_tournament(self):
        """ This function allows to generate a tournament."""
        tournament = self.add_tournament()
        self.tournaments.append(tournament)
        self.view.show_message("________ Player registration _______")

        db = self.db
        list_players = db.table("player").all()

        if not list_players:
            for i in range(1, tournament.number_of_players + 1):
                self.add_new_players(tournament, i)
        else:
            self.old_or_new_players(tournament)

        self.choice_secondary_menu(tournament)

    def check_result_match_entry(self, player1, player2):
        """ This function checks that the result entered by the user is a number between 1 and 3.

        :param player1: object
        :param player2: objet
        :return:int
            user's choice
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

    def add_result_match(self, r):
        """ This function is used to assign points to players and to create a match instance.

        :param r: Round object

        """
        for k, match in enumerate(r.list_match[0]):
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

            match_score = Match(k, player1, player1.score, player2, player2.score)
            r.add_match_score(match_score)
            r.save_end_date()
            self.save_all()

    def check_id_tournament(self, list_tournament):
        """ This function checks that the ID entered by the user is a number

        :param list_tournament: list
        :return: int
            tournament ID
        """
        while True:
            tournament_id = self.view.show_tournament_list(list_tournament)
            result = tournament_id.isdigit()

            if result:
                return int(tournament_id)
            else:
                self.view.show_message("The tournament's ID must be a positive number")

    def players_table(self, player: Player):
        """ This function is used to register players and to update the players' table.

        :param player: object

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

    def update_ranking(self, list_players):
        """ This function is used to update the players' ranking.

        :param list_players: list

        """
        self.view.show_message("______Update ranking________")
        for player in list_players:
            self.view.show_message("{} {} {}".format(list_players.index(player) + 1, player.last_name,
                                                     player.first_name))

        player_id = self.check_id_player()

        if player_id < len(list_players):
            player = list_players[int(player_id) - 1]
            self.view.show_message("{} {} current ranking: {}".format(player.last_name, player.first_name,
                                                                      player.ranking))
            new_ranking = self.check_ranking_entry()
            player.ranking = new_ranking

            self.players_table(player)
        else:
            self.view.show_message("Please select from the list")

    def display_players_list(self, list_players):
        """ This function is used to display all the players in alphabetical order or by ranking.

        :param list_players: list

        """
        display_player = True
        while display_player:
            view_list = self.view.prompt_user_input(" Enter 1 to sort by ranking, 2 to sort by name or 3 to exit")

            if view_list == "1":
                list_players = sorted(list_players, key=attrgetter("ranking"), reverse=True)
                self.view.show_message("______Players sorted by ranking______")
                for player in list_players:
                    self.view.show_players_list(player)
            elif view_list == "2":
                list_players = sorted(list_players, key=attrgetter("last_name"))
                self.view.show_message("______Players sorted by name______")
                for player in list_players:
                    self.view.show_players_list(player)
            elif view_list == "3":
                display_player = False
                self.choice_main_menu()
            else:
                self.view.show_message("Please choose 1, 2 or 3")

    def save_tournament(self, tournament: Tournament):
        """ This function is used to register tournaments and to update the tournaments table.

        :param tournament:object

        """
        db = self.db
        tournaments_table = db.table("tournament")
        tour = Query()
        tournaments_table.upsert({
            "name": tournament.name,
            "location": tournament.location,
            "date": tournament.date,
            "list_date": tournament.list_date,
            "pace": tournament.time_control,
            "comment": tournament.description,
            "players": [x.serialize() for x in tournament.list_players],
            "rounds": [x.serialize() for x in tournament.list_rounds]

        }, tour.name == str(tournament.name))

    @staticmethod
    def next_date(tournament):
        """ This function is used to compare the current date with the date recorded when the tournament was created.

        :param tournament: object
        :return: bool
        """
        now = datetime.now().strftime("%d/%m/%Y")
        str_now = datetime.strptime(str(now), "%d/%m/%Y")
        first_date_tournament = datetime.strptime(tournament.list_date[0], "%d/%m/%Y")

        return str_now == first_date_tournament

    @staticmethod
    def change_date(tournament):
        """ This function is used for updating the list of tournament dates.

        :param tournament: object

        """
        date = datetime.now().strftime("%d/%m/%Y")
        tournament.list_date.append(date)

    def get_all_tournaments(self):
        """ This function is used to display the tournament menu.
            it allows to access to the list of players, to the update of the rankings and to the list of rounds

        """
        db = self.db
        tournaments_table = db.table("tournament").all()
        self.tournaments = [Tournament.deserialize(x) for x in tournaments_table]

        chosen_tournament = self.check_id_tournament(self.tournaments)

        if chosen_tournament > len(tournaments_table):
            self.view.show_message("Invalid value")
        else:
            tournament = self.tournaments[int(chosen_tournament) - 1]
            tournament_items = True
            while tournament_items:
                choice = self.view.show_selected_tournament(tournament)

                if choice == "1":
                    self.display_players_list(tournament.list_players)
                    tournament_items = False
                elif choice == "2":
                    self.view.show_round(tournament.list_rounds)
                elif choice == "3":
                    tournament_items = False
                    self.choice_main_menu()
                elif choice == "4":

                    if self.next_date(tournament):
                        self.choice_secondary_menu(tournament)
                        tournament_items = False
                    else:
                        self.change_date(tournament)
                        self.choice_secondary_menu(tournament)
                        tournament_items = False
                else:
                    self.view.show_message("Please choose 1, 2 or 3")

    def get_all_player(self):
        """ This function allows you to access the list of all players.

        :return:
        """
        list_player = self.db.table("player").all()
        self.list_players = [Player.deserialize(x) for x in list_player]

        self.display_players_list(self.list_players)

    def save_all(self):
        """ This function allows to save the tournaments in the database.

        :return:
        """
        for tournament in self.tournaments:
            self.save_tournament(tournament)

    def run_tournament(self):
        """
        :return:
        """
        self.view.show_message("__________ WELCOME TO THE CHESS TOURNAMENT PROGRAM __________")
        self.choice_main_menu()
