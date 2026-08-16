from models.Habit import Habit

class HabitSorter:
    """ Class used to return Habits sorted in various formats """
    def __init__(self, habits: list[Habit]):
        self.habits = habits

    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Methods --------------------------------- #
    # ---------------------------------------------------------------------------- #

    # ------------------------------- Sort By Name ------------------------------- #
    def sort_by_name(self) -> list[Habit]:
        """
        Returns Habit list sorted alphebetically by name

        :return list[Habit]: List of habits sorted by name
        """
        sorted_by_name = sorted(self.habits, key=lambda x: x.name)

        return sorted_by_name

    # ------------------------------ Sort By Streak ------------------------------ #
    def sort_by_streak(self) -> list[Habit]:
        """
        Returns Habit list sorted by current streak

        :return list[Habit]: List of habits sorted by current streak
        """
        sorted_by_streak = sorted(self.habits, key=lambda x: x.get_streak(), reverse=True)

        return sorted_by_streak

    # -------------------------- Sort By Completion Rate ------------------------- #
    def sort_by_completion_rate(self) -> list[Habit]:
        """
        Returns Habit list sorted by completion rate

        :return list[Habit]: List of habits sorted by completion rate
        """
        sorted_by_completion_rate = sorted(self.habits, key=lambda x: x.get_completion_rate(), reverse=True)

        return sorted_by_completion_rate

    # --------------------------- Sort By Creation Date -------------------------- #
    def sort_by_creation_date(self) -> list[Habit]:
        """
        Returns Habit list sorted by creation date

        :return list[Habit]: List of habits sorted by creation date
        """
        sorted_by_creation_date = sorted(self.habits, key=lambda x: x.created_date)

        return sorted_by_creation_date