
from operator import attrgetter
from typing import List


from models.tournament import Tournament
from models.player import Player


class Controller:
    """class to accept user data, launch new tournaments, produce match results"""

    def __init__(self, view):
        """init the controller"""
        self.tournaments: List[Tournament] = []
        self.players: List[Player] = []

        self.view = view

    def check_start_menu_entries(self):
        list_choices = [1, 2, 3]
        while True:
            choice = self.view.show_start_menu(self)
            try:
                choice = int(choice)
                if choice in list_choices:
                    return choice
                return None
            except ValueError:
                self.view.show_error_menu_entry(self)

    def choice_start_menu(self):
        option_start_menu = self.check_start_menu_entries()
        if option_start_menu == 1:
            self.add_tournament()
        elif option_start_menu == 2:
            print("option 2")
        elif option_start_menu == 3:
            print("Quit")

    def check_secondary_menu_entries(self):
        list_choices = [1, 2, 3, 4, 5]
        while True:
            choice = self.view.show_secondary_menu(self)
            try:
                choice = int(choice)
                if choice in list_choices:
                    return choice
                return None
            except ValueError:
                self.view.show_error_menu_entry(self)

    def choice_secondary_menu(self):
        """blabla"""
        option_secondary_menu = self.check_secondary_menu_entries()
        if option_secondary_menu == 1:
            #self.add_tournament()
            self.get_player()
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
        print(self.tournaments)

    def check_gender_entry(self):
        while True:
            gender = self.view.prompt_player_gender(self)
            if gender == "M" or gender == "F":
                return gender
            else:
                self.view.show_error_gender_entry(self)

    def check_ranking_entry(self):
        while True:
            ranking = self.view.prompt_player_ranking(self)
            result = ranking.isdigit()
            if result:
                return int(ranking)
            else:
                self.view.show_error_ranking_entry(self)

    def get_player(self):
        self.view.show_players_title(self)
        for i in range(1, 9):
            self.view.show_player_number(i + 1)
            last_name = self.view.prompt_player_last_name(self)
            first_name = self.view.prompt_player_first_name(self)
            birth = self.view.prompt_player_date_of_birth(self)
            gender = self.check_gender_entry()
            ranking = self.check_ranking_entry()
            player = Player(last_name, first_name, birth, gender, ranking)
            self.players.append(player)


    def run_tournament(self):
        """blabla"""
        self.choice_start_menu()
        running = True
        while running:
           self.choice_secondary_menu()





