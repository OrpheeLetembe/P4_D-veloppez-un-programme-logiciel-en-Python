from datetime import datetime
from models.player import Player


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
        """Constructs all the necessary attributes for the round object.

        :param name: str
            name for round
        :param kwargs:
        """

        self.name = name
        self.list_match = []
        self.list_match_score = []
        self.start_date = ""
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

        """
        self.list_match.append(match)

    def add_match_score(self, match):
        self.list_match_score.append(match)

    def save_start_date(self):
        """

        :return:
        """
        self.start_date = datetime.now().strftime("%Y %m %d %H:%M:%S")

    def save_end_date(self):
        """
        saves the date and time of the end of the round
        :return: None
        """
        self.end_date = datetime.now().strftime("%Y %m %d %H:%M:%S")

    def __repr__(self):
        return repr(self.name)

    def serialize(self):
        """This function allows to serialize a round

        :return:dict
        """
        return {
            "name": self.name,
            "opponent": [x.serialize() for y in self.list_match for z in y for x in z], #for x in z],
            "match": [x.serialize() for x in self.list_match_score],
            "start": self.start_date,
            "end": self.end_date
        }

    @classmethod
    def deserialize(cls, serialize_round: dict) -> "Round":
        """This function allows the deserialization of round

        :param serialize_round:
        :return:round object
        """

        return Round(

            name=serialize_round.get("name"),
            list_match=[Player.deserialize(x) for x in serialize_round.get("opponent")],
            list_match_score=[Match.deserialize(x) for x in serialize_round.get("match")],
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

    def __init__(self, name, player1, score1, player2, score2):
        """

        :param name:
        :param player1:
        :param score1:
        :param player2:
        :param score2:
        """

        self.name = name
        self.player1 = player1
        self.score_player1 = score1
        self.player2 = player2
        self.score_player2 = score2

    def __repr__(self):
        return repr(self.name)

    def serialize(self):
        """This function allows to serialize a match

        :return: dict
        """
        return {

            "name": self.name,
            "match": ([Player.serialize(self.player1), self.score_player1],
                      [Player.serialize(self.player2), self.score_player2])

        }

    @classmethod
    def deserialize(cls, serialize_match: dict) -> "Match":
        """This function allows the deserialization of match

        :param serialize_match:
        :return: match object
        """

        return Match(
            name=serialize_match.get("name"),
            player1=Player.deserialize(serialize_match.get("match")[0][0]),
            score1=serialize_match.get("match")[0][1],
            player2=Player.deserialize(serialize_match.get("match")[1][0]),
            score2=serialize_match.get("match")[1][1]

        )