from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"

class Habit:
    """ Class that holds Habit information """
    def __init__(self, id: int, name: str, description: str, target_streak: int | None = None, target_completions: int | None = None):
        self.id = id
        self.name = name.title()
        self.description = description

        self.current_streak: int = 0
        self.max_streak: int = 0

        self.target_streak = target_streak
        self.target_completions = target_completions

        self.created_date: datetime = datetime.now()
        self.completed_dates: list[datetime] = []

    def __str__(self) -> str:
        date_string = 'Never' if not self.completed_dates else self.completed_dates[-1].strftime('%B %d')
        return f"{self.name} | Streak: {self.current_streak} | Last Completed: {date_string}"


    # ---------------------------------------------------------------------------- #
    # -------------------------------- Persistence ------------------------------- #
    # ---------------------------------------------------------------------------- #
    @classmethod
    def from_dict(cls, data):
        habit = cls(
            id = data['id'],
            name = data['name'],
            description = data['description'],
            target_streak = data.get('target_streak', None),
            target_completions = data.get('target_completions', None)
        )
        habit.current_streak = data['current_streak']
        habit.max_streak = data['max_streak']
        habit.created_date = datetime.strptime(data['created_date'], DATE_FORMAT)
        habit.completed_dates = [datetime.strptime(date, DATE_FORMAT) for date in data['completed_dates']]
        return habit

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'current_streak': self.current_streak,
            'max_streak': self.max_streak,
            'target_streak': self.target_streak,
            'target_completions': self.target_completions,
            'created_date': self.created_date.strftime(DATE_FORMAT),
            'completed_dates': [date.strftime(DATE_FORMAT) for date in self.completed_dates]
        }

    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Helpers --------------------------------- #
    # ---------------------------------------------------------------------------- #
    def _calculate_days_since_creation(self) -> int:
        """
        Calculates the number of days since a Habit object was created

        :return int: Number of days since creation
        """
        return (datetime.now() - self.created_date).days

    def _increase_streak(self) -> None:
        """
        Increases the current streak attribute by 1
        """
        self.current_streak += 1

    def _decrease_streak(self) -> None:
        """
        Decreases the current streak attribute by 1
        """
        self.current_streak = max(0, self.current_streak - 1)

    def _compare_streak_to_max(self) -> None:
        """
        Compares current streak to max streak and adjusts max streak if current streak is greater
        """
        if self.current_streak > self.max_streak:
            self.max_streak = self.current_streak


    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Methods --------------------------------- #
    # ---------------------------------------------------------------------------- #
    def complete(self, date: datetime) -> bool:
        """
        Completes a habit for a given date by adding the date to the completed dates attribute

        :param date: Date habit was completed

        :return True: Completion of Habit was successful
        :return False: Completion of Habit failed
        """
        if date not in self.completed_dates:
            self.completed_dates.add(date)

            self._increase_streak()
            self._compare_streak_to_max()
            return True
        return False

    def uncomplete(self, date: datetime) -> bool:
        """
        Uncomplete a Habit for a givn date by removing the date from completed dates attribute if date in set

        :param date: Date to remove

        :return True: Date was successfully removed
        :return False: Date doesn't exist or removal failed
        """
        if date in self.completed_dates:
            self.completed_dates.remove(date)
            self._decrease_streak()
            return True
        return False

    def is_completed(self, date: datetime) -> bool:
        """
        Returns whether or not the Habit has been completed on a given date

        :param date: Date to check for completion

        :return True: Habit was completed on given date
        :return False: Habit was not completed on given date
        """
        return date in self.completed_dates

    def get_completion_count(self) -> int:
        """
        Calculates the number of times a Habit has been completed

        :return int: Number of time Habit has been completed
        """
        return len(obj=self.completed_dates)

    def get_completion_rate(self) -> float:
        """
        Determine the completion of a Habit by dividing completion count by days since creation

        :return float: Completion rate
        """
        days_since_creation = self._calculate_days_since_creation()
        completion_count = self.get_completion_count()

        return completion_count / days_since_creation