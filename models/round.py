
""" Class round and class match"""

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

        if "start_date" in kwargs:
            self.start_date = kwargs["start_date"]

        if "end_date" in kwargs:
            self.end_date = kwargs["end_date"]

    def add_match(self, match):
        """ Adds opponents to the list of match."""
        self.list_match.append(match)

    def add_match_score(self, match):
        """ Add result of match to the list of match."""
        self.list_match_score.append(match)

    def save_start_date(self):
        """ Saves the date and time of the start of the round """
        self.start_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def save_end_date(self):
        """ Saves the date and time of the end of the round """
        self.end_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def __repr__(self):
        return repr(self.name)

    def serialize(self):
        """This function allows to serialize a round

        :return:dict
        """

        list_opponent = [x.serialize() for y in self.list_match for z in y for x in z]
        return {
            "name": self.name,
            "opponent": list_opponent,
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
        list_opponent = []
        deserialize_opponent = [Player.deserialize(x) for x in serialize_round.get("opponent")]
        while deserialize_opponent:

            p1 = deserialize_opponent[0]
            p2 = deserialize_opponent[1]
            opponent = [(p1, p2)]
            list_opponent.append(opponent)

            deserialize_opponent.remove(p1)
            deserialize_opponent.remove(p2)

        return Round(

            name=serialize_round.get("name"),
            list_match=list_opponent,
            list_match_score=[Match.deserialize(x) for x in serialize_round.get("match")],
            start_date=serialize_round.get("start"),
            end_date=serialize_round.get("end")

        )


class Match:
    """
    A class to represent a match.
    Attributes
    ----------
    name : str
        match name
    player1 : object
        object player 1
    player2 : object
        object player 2
    score1 : int
        score player 1
    score2 : int
        score player 2

    """

    def __init__(self, name, player1, score1, player2, score2):
        """ Constructs all the necessary attributes for the match object

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
