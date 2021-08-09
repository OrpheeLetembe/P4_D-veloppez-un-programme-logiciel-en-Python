
class View:
    pass

    @staticmethod
    def show_main_menu():
        print()
        print("        --Main menu--")
        print(" Enter 1 to create a new tournament")
        print(" Enter 2 to display the tournament list")
        print(" Enter 3 to display the player list")
        print(" Enter 4 to exit")
        print()

        response = input(" Your choice :")

        if not response:
            return None
        return response

    @staticmethod
    def show_secondary_menu():
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
        user_input = input(text + ": ")
        if not user_input:
            return None
        return user_input

    @staticmethod
    def show_message(message):
        print(message)

    @staticmethod
    def show_players(list_players):
        for player in list_players:

            print("Last name: {}".format(player.last_name))
            print("First name: {}".format(player.first_name))
            print("Date of birth: {}".format(player.date_of_birth))
            print("Ranking: {}".format(player.ranking))
            print("_____________________________________")

    @staticmethod
    def prompt_tournament_name():
        """Prompt for a name."""
        print("______Tournament information______")
        name = input("Name: ")

        if not name:
            return None
        return name

    @staticmethod
    def prompt_tournament_location():
        """Prompt for a location."""
        location = input("Location: ")

        if not location:
            return None
        return location

    @staticmethod
    def prompt_tournament_date():
        """Prompt for a date."""
        date = input("Date (day/month/year): ")

        if not date:
            return None
        return date

    @staticmethod
    def prompt_tournament_pace():
        """ prompt for tournament pace"""
        pace = input("Time control (Enter 1 for bullet, 2 for blitz or 3 for quick hit): ")

        if not pace:
            return None
        return pace

    @staticmethod
    def prompt_tournament_comment():
        comment = input("Add a comment: ")

        if not comment:
            return None
        return comment

    @staticmethod
    def show_players_title():
        print("________ Player registration _______")
        print()

    @staticmethod
    def show_player_number(number):
        print("    ------Player {} ------".format(str(number)))

    @staticmethod
    def prompt_player_last_name():
        """Prompt for a last name."""
        last_name = input("Last name: ")

        if not last_name:
            return None
        return last_name

    @staticmethod
    def prompt_player_first_name():
        """Prompt for a first name."""
        first_name = input("First name: ")

        if not first_name:
            return None
        return first_name
    @staticmethod
    def prompt_player_date_of_birth():
        """Prompt for a date of birth."""
        date_of_birth = input("Date of birth (day/month/year) : ")

        if not date_of_birth:
            return None
        return date_of_birth

    @staticmethod
    def prompt_player_gender():
        """Prompt for a gender."""
        gender = input("Gender (M/F): ").capitalize()

        if not gender:
            return None
        return gender

    @staticmethod
    def prompt_player_ranking():
        """Prompt for a ranking."""
        ranking = input("Ranking: ")

        if not ranking:
            return None
        return ranking

    @staticmethod
    def show_opponent(k, player1, player2):
        return print("Match {}: {} VS {}".format(k + 1, player1, player2))

    @staticmethod
    def prompt_of_winner(player1, player2):

        winner = input("Winner (Enter 1 for {} , 2 for {} or 3 for draw) : ".format(player1, player2))

        if not winner:
            return None
        return winner

    @staticmethod
    def show_tournament_list(list_tournament):
        for k, tournament in enumerate(list_tournament):
            print(k + 1, tournament)

    @staticmethod
    def show_update_ranking(list_players):
        for player in list_players:
            print(list_players.index(player) + 1, player.last_name, player.first_name)

        selected_player = input("Select a player id: ")

        if not selected_player:
            return None
        return selected_player



