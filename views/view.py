
class View:
    pass

    @staticmethod
    def show_main_menu():
        """

        :return:
        """
        print()
        print("        --Main menu--")
        print(" Enter 1 to create a new tournament")
        print(" Enter 2 to display the tournament list")
        print(" Enter 3 to display the player list")
        print(" Enter 4 to exit main menu")
        print()

        response = input(" Your choice :")

        if not response:
            return None
        return response

    @staticmethod
    def show_secondary_menu():
        """

        :return:
        """
        print()
        print("      --Tournament menu--")
        print(" Enter 1 to add the results of round")
        print(" Enter 2 to display the list of players")
        print(" Enter 3 to add comment")
        print(" Enter 4 to save tournament")
        print(" Enter 5 to go to main menu")
        print()
        choice = input(" select a menu item: ")

        if not choice:
            return None
        return choice

    @staticmethod
    def prompt_user_input(text):
        """

        :param text:
        :return:
        """
        user_input = input(text + ": ")
        if not user_input:
            return None
        return user_input

    @staticmethod
    def show_message(message):
        """

        :param message:
        :return:
        """
        print(message)

    @staticmethod
    def show_players(list_players):
        """

        :param list_players:
        :return:
        """
        for player in list_players:

            print("Last name: {}".format(player.last_name))
            print("First name: {}".format(player.first_name))
            print("Date of birth: {}".format(player.date_of_birth))
            print("Ranking: {}".format(player.ranking))
            print("_____________________________________")

    @staticmethod
    def show_player_number(number):
        """

        :param number:
        :return:
        """
        print("    ------Player {} ------".format(str(number)))

    @staticmethod
    def show_opponent(k, player1, player2):
        """

        :param k:
        :param player1:
        :param player2:
        :return:
        """
        return print("Match {}: {} VS {}".format(k + 1, player1, player2))

    @staticmethod
    def prompt_of_winner(player1, player2):
        """

        :param player1:
        :param player2:
        :return:
        """
        winner = input("Winner (Enter 1 for {} , 2 for {} or 3 for draw) : ".format(player1, player2))

        if not winner:
            return None
        return winner

    @staticmethod
    def show_tournament_list(list_tournament):
        """

        :param list_tournament:
        :return:
        """
        for k, tournament in enumerate(list_tournament):
            print("{} - {}, {} {} Note: {}".format(k + 1, tournament.name, tournament.location, tournament.date,
                                                   tournament.description))

    @staticmethod
    def show_selected_tournament():
        """

        :return:
        """
        print("________Tournament menu________")
        print("1 Display players list")
        print("2 Display rounds")
        print("3 to exit")

        choice = input("select a item: ")
        if not choice:
            return None
        return choice

    @staticmethod
    def show_round(list_rounds):
        """

        :param list_rounds:
        :return:
        """
        print("_________________")
        for r in list_rounds:
            print("{}, start date:{} - end date:{}".format(r.name, r.start_date, r.end_date))

            for m in r.list_match_score:
                m1 = m.get("match")
                print("Match {} :".format(r.list_match_score.index(m) + 1))
                print("{} {}".format(m1[0][0], m1[0][1]))
                print("{} {}".format(m1[1][0], m1[1][1]))

    @staticmethod
    def show_update_ranking(list_players):
        """

        :param list_players:
        :return:
        """
        for player in list_players:
            print(list_players.index(player) + 1, player.last_name, player.first_name)

        selected_player = input("Select a player id: ")

        if not selected_player:
            return None
        return selected_player
