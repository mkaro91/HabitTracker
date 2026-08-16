from datetime import datetime

class Achievement:
    """ Class representing an Achievement """
    def __init__(self, name: str, description: str):
        self.name = name.title()
        self.description = description

        self.achieved_date = datetime.now()

    # ----------------------------------- Magic ---------------------------------- #
    def __eq__(self, other):
        return self.name == other.name

    def __str__(self) -> str:
        return f"\n{self.name}\n{self.description}\n{self.achieved_date.strftime("%B %d, %Y")}"

    # ---------------------------------------------------------------------------- #
    # -------------------------------- Persistence ------------------------------- #
    # ---------------------------------------------------------------------------- #
    @classmethod
    def from_dict(cls, data):
        achievement = cls(
            name = data['name'],
            description = data['description']
        )

        achievement.achieved_date = datetime.strptime(data['achieved_date'],'%Y-%m-%d')

        return achievement

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'achieved_date': self.achieved_date.strftime('%Y-%m-%d')
        }