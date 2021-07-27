

import datetime


class Round:
    """
    A class to represent a round.
        ...

    Attributes
    ----------
    name : str
        round's name
    list_match : list
        round match list
    start_date     : str
        starting date of the round
    end_date   : str
        end date of the round

    Methods
    -------
    add_match(match):
        adds a match to the match list of a round
    save_end_date():
        saves the date and time of the end of the round
    lose():

    """

    def __init__(self, name):
        """
        adds a match to the match list of a round

        :param name: list
        """
        self.name = name
        self.list_match = []
        self.list_match_score = []
        self.start_date = datetime.datetime.now()
        self.end_date = ""

    def add_match(self, match):
        """

        :param match:
        :return:
        """
        self.list_match.append(match)

    def add_match_score(self, match):
        self.list_match_score.append(match)

    def save_end_date(self):
        """
        saves the date and time of the end of the round
        :return: None
        """
        self.end_date = datetime.datetime.now()

    def __repr__(self):
        return repr(self.name)


class Match:
    """
    A class to represent a match.

    Attributes
    ----------
    list1 : list





    """

    def __init__(self, list1, list2):
        """

        :param list1:
        :param list2:
        """
        self.name = (list1, list2)

    def __repr__(self):
        return repr(self.name)
