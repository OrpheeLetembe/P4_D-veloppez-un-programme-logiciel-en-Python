
class View:
    pass

    def show_main_menu(self):
        print()
        print("        --Main menu--")
        print(" Enter 1 to create a new tournament")
        print(" Enter 2 to display the tournament list")
        print(" Enter 3 to exit")
        print()

        response = input(" Your choice :")

        if not response:
            return None
        return response

    def show_secondary_menu(self):
        print()
        print("      --Tournament menu--")
        print(" Enter 1 to add the results of round")
        print(" Enter 2 to update the ranking")
        print(" Enter 3 to display the list of players")
        print(" Enter 4 to add comment")
        print(" Enter 5 to go to main menu")
        print()
        choice = input(" select a menu item: ")

        if not choice:
            return None
        return choice

    def show_message(self, message):
        print(message)

    def prompt_tournament_name(self):
        """Prompt for a name."""
        print("______Tournament information______")
        name = input("Name: ")

        if not name:
            return None
        return name

    def prompt_tournament_location(self):
        """Prompt for a location."""
        location = input("Location: ")

        if not location:
            return None
        return location

    def prompt_tournament_date(self):
        """Prompt for a date."""
        date = input("Date (day/month/year): ")

        if not date:
            return None
        return date

    def prompt_tournament_pace(self):
        """ prompt for tournament pace"""
        pace = input("Time control (Enter 1 for bullet, 2 for blitz or 3 for quick hit): ")

        if not pace:
            return None
        return pace

    def prompt_tournament_comment(self):
        comment = input("Add a comment: ")

        if not comment:
            return None
        return comment

    def show_players_title(self):
        print("________ Player registration _______")
        print()

    def show_player_number(self):
        print("    ------Player {} ------".format(str(self)))

    def prompt_player_last_name(self):
        """Prompt for a last name."""
        last_name = input("Last name: ")

        if not last_name:
            return None
        return last_name

    def prompt_player_first_name(self):
        """Prompt for a first name."""
        first_name = input("First name: ")

        if not first_name:
            return None
        return first_name

    def prompt_player_date_of_birth(self):
        """Prompt for a date of birth."""
        date_of_birth = input("Date of birth (day/month/year) : ")

        if not date_of_birth:
            return None
        return date_of_birth

    def prompt_player_gender(self):
        """Prompt for a gender."""
        gender = input("Gender (M/F): ").capitalize()

        if not gender:
            return None
        return gender

    def prompt_player_ranking(self):
        """Prompt for a ranking."""
        ranking = input("Ranking: ")

        if not ranking:
            return None
        return ranking

    def show_opponent(self, k, player1, player2):
        return print("Match {}: {} VS {}".format(k + 1, player1, player2))

    def prompt_of_winner(self, player1, player2):

        winner = input("Winner (Enter 1 for {} , 2 for {} or 3 for draw) : ".format(player1, player2))

        if not winner:
            return None
        return winner

    def show_tournament_list(self, list_tournament):
        for k, tournament in enumerate(list_tournament):
            print(k + 1, tournament)



    def show_update_kanking(self, player1, player2):
        print("{}, current ranking: {}".format(player1, player2))






