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

    def __init__(self, name, **kwargs):
        """
        adds a match to the match list of a round
        :param name: list
        """
        self.name = name
        self.list_match = []
        self.list_match_score = []
        self.start_date = datetime.datetime.now()
        self.end_date = ""

        if "list_match" in kwargs:
            self.list_match = kwargs["list_match"]

        if "list_match_score" in kwargs:
            self.list_match_score = kwargs["list_match_score"]

        if "star_date" in kwargs:
            self.start_date = kwargs["start_date"]

        if "end_date" in kwargs:
            self.end_date = kwargs["end_date"]

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

    def serialize(self):
        return {
            "name": self.name,
            "opponent": [x.serialise() for y in self.list_match for z in y for x in z],
            "match": [x.serialise() for x in self.list_match_score],
            "start": self.start_date,
            "end": self.end_date
        }

    @classmethod
    def deserialize(cls, serialize_round: dict) -> "Round":

        return Round(
            name=serialize_round.get("name"),
            list_match=serialize_round.get("opponent"),
            list_match_score=serialize_round.get("match"),
            start_date=serialize_round.get("start"),
            end_date=serialize_round.get("end")

        )


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

    def serialize(self):
        return {

            "match": self.name
        }