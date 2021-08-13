""" Class controller"""

from tinydb import TinyDB, Query

from operator import attrgetter
from typing import List
from datetime import datetime

from models.tournament import Tournament
from models.player import Player
from models.round import Round, Match


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
                db = self.db
                list_tournaments = db.table("tournament").all()
                if not list_tournaments:
                    self.view.show_message("The list of tournaments is empty")
                else:
                    self.get_all_tournaments()
            elif option_main_menu == "3":
                db = self.db
                list_players = db.table("player").all()
                if not list_players:
                    self.view.show_message("The list of players is empty")
                else:
                    self.get_all_player()
            elif option_main_menu == "4":
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
                comment = self.view.prompt_user_input("Comment")
                tournament.add_comment(comment)
            elif option_secondary_menu == "3":
                self.choice_main_menu()
            elif option_secondary_menu == "4":
                secondary_menu = self.quit_tournament(tournament)
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
        """

        :return:
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

    def add_tournament(self):
        """
        :return:
        """
        self.view.show_message("______Tournament information______")
        name = self.check_tournament_exit()
        location = self.view.prompt_user_input("Location")
        date = self.check_date_entry("Date (day/month/year)")
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
        birth = self.check_date_entry("Date of birth (day/month/year)")
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

    def check_id_player(self, list_players):
        while True:
            player_id = self.view.show_update_ranking(list_players)
            result = player_id.isdigit()
            if result:
                return int(player_id)
            else:
                self.view.show_message("The player's ID must be a positive number")

    def check_id_tournament(self, list_tournament):
        while True:
            tournament_id = self.view.show_tournament_list(list_tournament)
            result = tournament_id.isdigit()
            if result:
                return int(tournament_id)
            else:
                self.view.show_message("The tournament's ID must be a positive number")

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

            match_score = Match(k, player1, player1.score, player2, player2.score)
            round.add_match_score(match_score)
            round.save_end_date()
            self.save_all()

    def update_ranking(self, list_players):
        """
        :param list_players:
        :return:
        """
        self.view.show_message("______Update ranking________")
        player_id = self.check_id_player(list_players)
        if player_id < len(list_players):
            player = list_players[int(player_id) - 1]
            print("{} {} current ranking: {}".format(player.last_name, player.first_name, player.ranking))
            new_ranking = self.check_ranking_entry()
            player.ranking = new_ranking
            print("{} {} current ranking: {}".format(player.last_name, player.first_name, player.ranking))
            self.players_table(player)
        else:
            print("Please select from the list")

    def display_players(self, list_players):
        """
        :param list_players:
        :return:
        """
        display_player = True
        while display_player:
            view_list = self.view.prompt_user_input(" Enter 1 to sort by ranking, 2 to sort by name ,"
                                                    "3 to update ranking or 4 to exit")
            if view_list == "1":
                list_players = sorted(list_players, key=attrgetter("ranking"), reverse=True)
                self.view.show_message("______Players sorted by ranking______")
                self.view.show_players(list_players)
            elif view_list == "2":
                list_players = sorted(list_players, key=attrgetter("last_name"))
                self.view.show_message("______Players sorted by name______")
                self.view.show_players(list_players)
            elif view_list == "3":
                self.update_ranking(self.list_players)
            elif view_list == "4":
                display_player = False
            else:
                self.view.show_message("Please choose 1, 2 ,3 or 4")

    def quit_tournament(self, tournament):
        """
        :param tournament:
        :return:
        """
        number_round = tournament.get_next_round_number()
        if number_round != tournament.number_of_round:
            result = self.view.prompt_quit_tournament()
            if result:
                return False
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
                    self.display_players(tournament.list_players)
                elif choice == "2":
                    self.view.show_round(tournament.list_rounds)
                elif choice == "3":
                    tournament_items = False
                elif choice == "4":
                    #self.continue_tournament(tournament)
                    self.choice_secondary_menu(tournament)
                else:
                    self.view.show_message("Please choose 1, 2 or 3")

    def get_all_player(self):
        """

        :return:
        """
        list_player = self.db.table("player").all()
        self.list_players.clear()
        self.list_players = [Player.deserialize(x) for x in list_player]

        self.display_players(self.list_players)

    def save_all(self):
        """

        :return:
        """
        for tournament in self.tournaments:
            self.save_tournament(tournament)

        # self.players_table()

    def continue_tournament(self, tournament):
        list_opponent = []
        list_matchs = []
        for p in tournament.list_players:
            player = Player.deserialize(p)
            list_opponent.append(player)
        list_players = list_opponent
        list_opponent = []
        #list_round = [Round.deserialize(x) for x in tournament.list_rounds]
        #print(list_round)
        for r in tournament.list_rounds:
            round = Round.deserialize(r)
            for p in round.list_match:
                player_d = Player.deserialize(p)
                list_opponent.append(player_d)
            while list_opponent:
                player1 = list_opponent[0]
                player2 = list_opponent[1]
                list_matchs.append({player1, player2})
                round.list_match = list_matchs
                list_opponent.remove(player1)
                list_opponent.remove(player2)
                round = Round(round.name, list_match=list_players, list_match_score=round.list_match_score,
                              start_date=round.start_date, end_date=round.end_date)
            print(round.list_match)
            tournament.add_round(round)
            print(tournament.list_rounds)

            #tournament.add_round(round.name)= list_matchs
            #print(tournament.list_rounds[0])




           

        """   
           
            tournament.add_round(round)
            print(tournament.list_rounds)
        #return tournament

        #print(list_opponent)
        #print(list_matchs)

            # for m in r.list_match_score:
            # print(m.get("opponent"))
            # m1 = Match.deserialize(m)
            # print(m1.name)
                # p1 = m1.player1[0]
                # print(type(p1))
                # print(r.list_match_score)






                #player1 = Player.deserialize(m[0][0])
                #print(player1)
               # print(m[0][0], m[1][0])











            #op = r.get("match")
            #print(op[0])



        #deserialize = [r.deserialize(x)for x in tournament.list_rounds]

        #print(deserialize)


        #return Tournament.deserialize(tournament)
"""
    def run_tournament(self):
        """
        :return:
        """
        self.view.show_message("__________ WELCOME TO THE CHESS TOURNAMENT PROGRAM __________")
        self.choice_main_menu()
