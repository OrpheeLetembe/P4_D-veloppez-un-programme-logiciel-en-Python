""" class view"""


class View:
    pass

    @staticmethod
    def show_main_menu():
        """ This function is used to display the main menu.

        :return:str
            User's choice
        """
        print()
        print("        --Main menu--")
        print(" 1 Create a new tournament")
        print(" 2 Display the tournament list")
        print(" 3 Display the player list")
        print(" 4 Quit program")
        print()

        response = input(" Your choice :")

        if not response:
            return None
        return response

    @staticmethod
    def show_secondary_menu():
        """This function is used to display the secondary menu .

        :return:str
            User's choice
        """
        print()
        print("      --Tournament menu--")
        print(" 1 Add the results of round")
        print(" 2 Update player's ranking")
        print(" 3 Add comment")
        print(" 4 Save")
        print(" 5 Main menu")
        print()

        choice = input(" select a menu item: ")

        if not choice:
            return None
        return choice

    @staticmethod
    def prompt_user_input(output):
        """ This function is used to collect the user's input.

        :param output: str
            statement of expected choice
        :return:str
            User's choice
        """
        user_input = input(output + ": ")
        if not user_input:
            return None
        return user_input

    @staticmethod
    def show_message(message):
        """ This function is used to display messages.

        :param message: str
            message to display

        """
        print(message)

    @staticmethod
    def show_players_list(player):
        """ This function is used to display the attributes of the player.

        :param player: object
        """
        print("Last name: {}".format(player.last_name))
        print("First name: {}".format(player.first_name))
        print("Date of birth: {}".format(player.date_of_birth))
        print("Ranking: {}".format(player.ranking))
        print("_____________________________________")

    @staticmethod
    def show_add_players(player, number):
        print("{} - {} {} {} ".format(number, player.last_name, player.first_name, player.ranking))

    @staticmethod
    def show_player_number(number):
        print("    ------Player {} ------".format(str(number)))

    @staticmethod
    def show_opponent(k, player1, player2):
        """ This function is used to display the opponents of a match.

        :param k:int
        :param player1:object
        :param player2:object
        """
        return print("Match {}: {} VS {}".format(k + 1, player1, player2))

    @staticmethod
    def prompt_of_winner(player1, player2):
        """ This function is used to determine the winner of a match.

        :param player1:object
        :param player2:object
        :return:str

        """
        winner = input("Winner (Enter 1 for {} , 2 for {} or 3 for draw) : ".format(player1, player2))

        if not winner:
            return None
        return winner

    @staticmethod
    def show_tournament_list(list_tournament):
        """ This function is used to display the list of tournaments.

        :param list_tournament: list
        :return: int
             User's choice
        """
        print("________Tournament list________")
        for k, tournament in enumerate(list_tournament):

            if len(tournament.list_date) == 1:
                print("{} - {}, {} {}, control time: {}".format(k + 1, tournament.name, tournament.location,
                                                                tournament.list_date[0], tournament.time_control))

                print("Description: {}".format(tournament.description))
            else:
                print("{} - {}, {} du {} au {}, control time: {}".format(k + 1, tournament.name, tournament.location,
                                                                         tournament.list_date[0],
                                                                         tournament.list_date[-1],
                                                                         tournament.time_control))

                print("Description: {}".format(tournament.description))

        choice = input("Choose a tournament ")
        if not choice:
            return None
        return choice

    @staticmethod
    def show_selected_tournament(tournament):

        print("________Tournament menu________")

        if len(tournament.list_rounds) < tournament.number_of_round:
            print("1 Display players list")
            print("2 Display rounds")
            print("3 Exit")
            print("4 Continue tournament")

            choice = input("select a item: ")
            if not choice:
                return None
            return choice

        else:
            print("1 Display players list")
            print("2 Display rounds")
            print("3 Exit")

            choice = input("select a item: ")
            if not choice:
                return None
            return choice

    @staticmethod
    def show_round(list_rounds):

        for r in list_rounds:
            print("_________________________________________")
            print("{}, start date:{} - end date:{}".format(r.name, r.start_date, r.end_date))

            for m in r.list_match_score:
                print("________ Match {} ________".format(m.name + 1))
                print("{} {}    {}".format(m.player1.last_name, m.player1.first_name, m.score_player1))
                print("{} {}    {}".format(m.player2.last_name, m.player2.first_name, m.score_player2))
