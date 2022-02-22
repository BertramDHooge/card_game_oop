class Symbol:
    """
    Class that describes a Symbol
    """

    def __init__(self, color: str, icon: str):
        """
        Function that will initialise a new instance of a Symbol, which
        consixtsts of a color and an icon.

        :param color: The color of the symbol, default either red or black
        :param icon: The icon for our Symbol, default one of [♥, ♦, ♣, ♠]
        """

        self.color = color
        self.icon = icon

    def __str__(self) -> str:
        """
        Function that will return a printable version of our Symbol.

        :return: A str representing our Symbol, as color is included in the
                    default icons only the icon will be printed
        """

        return self.icon


class Card(Symbol):
    """
    Class that describes a Card.
    """

    def __init__(self, color, icon, value: str):
        """
        Function that will initialise a new instance of a Card, which consists
        of a Symbol and a value.

        :param color: The color of the Symbol, default either red or black
        :param icon: The icon for the Symbol, default one of [♥, ♦, ♣, ♠]
        :param value: The value of the Card, default one of [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]
        """

        Symbol.__init__(self, color, icon)
        self.value = value

    def __str__(self) -> str:
        """
        Function that will return a printable version of our Card.

        :return: A str representing our Card, printing both the Symbol and
        value of the Card.
        """

        return f"{self.value} of {super().__str__()}"
