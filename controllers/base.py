
from operator import attrgetter
from typing import List


from models.tournament import Tournament
from models.player import Player


class Controller:
    """class to accept user data, launch new tournaments, produce match results"""

    def __init__(self, view):
        """init the controller"""
        self.tournaments: List[Tournament] = []

        self.view = view

    def choice_main_menu(self):
        option_main_menu = self.view.show_main_menu(self)
        if option_main_menu == "1":
            tournament = self.add_tournament()
            self.tournaments.append(tournament)
            print(tournament.name)
            for i in range(1, 5):
                player = self.get_player(i)
                tournament.add_player(player)
            self.choice_secondary_menu(tournament)
        elif option_main_menu == "2":
            if not self.tournaments:
                self.view.show_message(self, "The list of tournaments is empty")
                self.choice_main_menu()
            else:
                self.view.show_tournament_list(self, self.tournaments)
        elif option_main_menu == "3":
            self.view.show_message(self, "Goodbye")
        else:
            self.view.show_message(self, "Please make a selection from menu")
            self.choice_main_menu()

    def choice_secondary_menu(self, tournament):
        """blabla"""
        option_secondary_menu = self.view.show_secondary_menu(self)
        if option_secondary_menu == "1":
            round = tournament.generate_round()
            self.view.show_message(self, "____{}____".format(round.name))
            self.add_result_match(round)
        elif option_secondary_menu == "2":

            print("option 2")
        elif option_secondary_menu == "3":
            print("option 3")
        elif option_secondary_menu == "4":
            print("option 4")
        else:
            self.view.show_message(self, "Please make a selection from menu")
            self.choice_secondary_menu()

    def add_tournament(self):
        """ add tournament"""
        name = self.view.prompt_tournament_name(self)
        location = self.view.prompt_tournament_location(self)
        date = self.view.prompt_tournament_date(self)
        tournament = Tournament(name, location, date)
        self.view.show_players_title(self)
        return tournament

    def check_gender_entry(self):
        while True:
            gender = self.view.prompt_player_gender(self)
            if gender == "M" or gender == "F":
                return gender
            else:
                self.view.show_message(self, "the gender of the player must be M or F")

    def check_ranking_entry(self):
        while True:
            ranking = self.view.prompt_player_ranking(self)
            result = ranking.isdigit()
            if result:
                return int(ranking)
            else:
                self.view.show_message(self, "The player's ranking must be a positive number")

    def get_player(self, number_player):
        self.view.show_player_number(number_player)
        last_name = self.view.prompt_player_last_name(self)
        first_name = self.view.prompt_player_first_name(self)
        birth = self.view.prompt_player_date_of_birth(self)
        gender = self.check_gender_entry()
        ranking = self.check_ranking_entry()
        player = Player(last_name, first_name, birth, gender, ranking)
        return player

    # def check_result_match_entry(self, round):
        # for match in round.list_match[0]:
           # match = list(match)
          #  player1 = match[0]
          #  player2 = match[1]

           # while True:
               # winner = self.view.prompt_of_winner(self, player1.last_name, player2.last_name)
               # winner_int = winner.isdigit()
               # if winner_int and int(winner) in range(1, 4):
                   # return int(winner)
                #else:

    def add_result_match(self, round):
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

    def run_tournament(self):
        self.view.show_message(self, "__________ WELCOME __________")
        self.choice_main_menu()










"""
        i = 1
        while i <= tournament.number_of_round:
            print(i)
            round = tournament.generate_round()
            print(round.name, round.list_match)
            for k, match in enumerate(round.list_match[0]):
                match = list(match)
                player1 = match[0]
                player2 = match[1]

                print("Match {}: {} VS {}".format(k + 1, player1.last_name, player2.last_name))

                winner = int(input("Winner (Enter 1 for {} , 2 for {} or 3 for draw) : ".format(player1.last_name,
                                                                                                player2.last_name)))  # add control
                if winner == 1:
                    player1.win()
                    player2.lose()
                elif winner == 2:
                    player2.win()
                    player1.lose()
                elif winner == 3:
                    player1.draw()
                    player2.draw()
            i += 1

        #running = True
       # while running:
    """       #self.choice_secondary_menu()





