"""" Class Player"""


class Player:
    """
    A class to represent a player.
    ...
    Attributes
    ----------
    last_name : str
        player's last name
    first_name : str
        player's first name
    birth     : str
        player's date of birth
    gender    : str
        player's gender
    ranking   : int
        player's ranking
    score     : int
        player's score
    Methods
    -------
    Win():
        Adds one point to the player's score
    draw():
        Adds 0.5 to player's score
    lose():
    """

    def __init__(self, last_name, first_name, birth, gender, ranking, score=None):
        """
        Constructs all the necessary attributes for the player object.
        :param last_name: str
            family name of the player
        :param first_name: str
            first name of the player
        :param birth: str
            date of birth of the player
        :param gender: str
            gender of the player
        :param ranking: int
            ranking of the player
        """
        if score is None:
            score = 0
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = birth
        self.gender = gender
        self.ranking = ranking
        self.score = score

    def __repr__(self):
        return repr((self.last_name, self.first_name, self.date_of_birth, self.gender, self.ranking))

    def win(self):
        """ This function allows you to add  1 to the player's score.
        :return: None
        """
        self.score += 1

    def draw(self):
        """ This function allows you to add  0.5 to the player's score.
        :return: None
        """
        self.score += 0.5

    def lose(self):
        """ This function allows you to add 0 to the player's score
        :return: None
        """
        self.score += 0

    def serialize(self):
        """This function allows to serialize a player

        :return:dict
        """
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth": self.date_of_birth,
            "gender": self.gender,
            "ranking": self.ranking,
            "score": self.score
        }

    @classmethod
    def deserialize(cls, serialized_player: dict) -> "Player":
        """ This function allows the deserialization of players

        :param serialized_player:dict
        :return: player object
        """
        return Player(
            last_name=serialized_player.get("last_name"),
            first_name=serialized_player.get("first_name"),
            birth=serialized_player.get("birth"),
            gender=serialized_player.get("gender"),
            ranking=serialized_player.get("ranking"),
            score=serialized_player.get("score"),
        )


def main():
    pass


if __name__ == "__main__":
    main()
