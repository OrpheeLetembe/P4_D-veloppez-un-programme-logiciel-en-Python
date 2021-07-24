
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

    def check_start_menu_entries(self):
        list_choices = [1, 2, 3]
        while True:
            choice = self.view.show_start_menu(self)
            try:
                choice = int(choice)
                if choice in list_choices:
                    return choice
                else:
                    self.view.show_message(self, "Please make a selection from menu")
            except ValueError:
                self.view.show_message(self, "Please make a selection from menu")

    def choice_start_menu(self):
        option_start_menu = self.check_start_menu_entries()
        if option_start_menu == 1:
            self.add_tournament()
            #self.get_player()
        elif option_start_menu == 2:
            if not self.tournaments:
                self.view.show_message(self, "The list of tournaments is empty")
                self.choice_start_menu()
            else:
                self.view.show_tournament_list(self, self.tournaments)
        else:
            self.view.show_message(self, "Goodbye")

    def check_secondary_menu_entries(self):
        list_choices = [1, 2, 3, 4, 5]
        while True:
            choice = self.view.show_secondary_menu(self)
            try:
                choice = int(choice)
                if choice in list_choices:
                    return choice
                else:
                    self.view.show_message(self, "Please make a selection from menu")
            except ValueError:
                self.view.show_message(self, "Please make a selection from menu")

    def choice_secondary_menu(self):
        """blabla"""
        option_secondary_menu = self.check_secondary_menu_entries()
        if option_secondary_menu == 1:
            print("option 1")
            self.add_result_match()
        elif option_secondary_menu == 2:
            print("option 2")
        else:
            print("pas de suite")

    def add_tournament(self):
        """ add tournament"""
        name = self.view.prompt_tournament_name(self)
        location = self.view.prompt_tournament_location(self)
        date = self.view.prompt_tournament_date(self)
        tournament = Tournament(name, location, date)
        self.tournaments.append(tournament)
        self.view.show_players_title(self)
        #return tournament

        # for i in range(1, 4):
        # tournament.add_player(self.get_player(i))
        # print(tournament.list_players)

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

    def get_player(self, i):
        self.view.show_player_number(i)
        last_name = self.view.prompt_player_last_name(self)
        first_name = self.view.prompt_player_first_name(self)
        birth = self.view.prompt_player_date_of_birth(self)
        gender = self.check_gender_entry()
        ranking = self.check_ranking_entry()
        player = Player(last_name, first_name, birth, gender, ranking)
        return player

    def add_result_match(self, round):
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

    def run_tournament(self):
        self.choice_start_menu()










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





