class Symbol:
    def __init__(self, color: str, icon: str):
        self.color = color
        self.icon = icon

    def __str__(self):
        return self.icon

class Card(Symbol):
    def __init__(self, color, icon, value: str):
        Symbol.__init__(self, color, icon)
        self.value = value

    def __str__(self):
        return f"{self.value} of {super().__str__()}"
