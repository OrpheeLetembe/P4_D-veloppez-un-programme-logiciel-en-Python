
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

    def check_menu_entry(self, choice):
        list_choices = [1, 2, 3, 4, 5]
        choice = self.view.show_menu(self)
        try:
            choice = int(choice)
            if choice in list_choices:
                return choice
            return None
        except ValueError:
            print("Please make a selection from the menu")

    def choice_menu(self):
        """blabla"""
        option_menu = self.check_menu_entry(self)
        if option_menu == 1:
            self.add_tournament()
            self.get_player()
        elif option_menu == 2:
            print("option 2")
        else:
            print("bouboubou")
            self.view.show_menu(self)

    def add_tournament(self):
        """ add tournament"""
        name = self.view.prompt_tournament_name(self)
        location = self.view.prompt_tournament_location(self)
        date = self.view.prompt_tournament_date(self)
        tournament = Tournament(name, location, date)
        self.tournaments.append(tournament)
        print(self.tournaments)

    def check_gender_entry(self, gender):
        while True:
            gender = self.view.prompt_player_gender(self)
            if gender == "M" or gender == "F":
                return gender
            else:
                print("the gender of the player must be M or F")

    def check_ranking_entry(self, ranking):
        while True:
            ranking = self.view.prompt_player_ranking(self)
            result = ranking.isdigit()
            if result:
                return int(ranking)
            else:
                print("The player's ranking must be a positive number")

    def get_player(self):
        print("________Player registration_______")
        for i in range(1, 9):
            print("       ------Player" + " " + str(i) + "------")
            last_name = self.view.prompt_player_last_name(self)
            first_name = self.view.prompt_player_first_name(self)
            birth = self.view.prompt_player_date_of_birth(self)
            gender = self.check_gender_entry(self)
            ranking = self.check_ranking_entry(self)
            player = Player(last_name, first_name, birth, gender, ranking)
            self.players.append(player)

    def sort_player_ranking(self):
        player_list_rank = sorted(self.players, key=attrgetter("ranking"))
        print(player_list_rank)

    def run_tournament(self):
        """blabla"""
        self.choice_menu()

       #self.sort_player_ranking()


