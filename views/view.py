
class View:
    pass

    def show_menu(self):
        print("_____MENU_____")
        print("enter 1 to create a new tournament")
        print("enter 2 option 2")
        print("enter 3 option 3")
        print("enter 4 option 4")
        print("enter 5 option 5")

        choice = input("select a menu item: ")
        if not choice:
            return None
        return choice

    def show_error_menu_entry(self):
        print("Please make a selection from menu")

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
        date = input("Date: ")
        if not date:
            return None
        return date

    def show_players_title(self):
        print("________Player registration_______")

    def show_player_number(self):
        print("       ------Player {} ------".format(str(self)))

    def show_error_gender_entry(self):
        print("the gender of the player must be M or F")

    def show_error_ranking_entry(self):
        print("The player's ranking must be a positive number")

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


