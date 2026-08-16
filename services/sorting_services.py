from models.Habit import Habit
from models.HabitSorter import HabitSorter

class SortingService:
    def __init__(self, habits: list[Habit]):
        self.sorter = HabitSorter(habits=habits)


    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Helpers --------------------------------- #
    # ---------------------------------------------------------------------------- #
    def _display_habits(self, habits: list[Habit]) -> None:
        """
        Displays habits found in the provided list of habits

        :param habits: List of habits to be displayed
        """
        if not habits:
            print("No habits found.")
            return

        for habit in habits:
            print(habit)

    # ---------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #


    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Methods --------------------------------- #
    # ---------------------------------------------------------------------------- #

    # ------------------------------- Sort By Name ------------------------------- #
    def sort_by_name(self) -> None:
        """
        Sorts habits by name and displays result
        """
        habits = self.sorter.sort_by_name()

        print("\n=== Habits by Name ===")
        self._display_habits(habits=habits)

    # ------------------------------ Sort By Streak ------------------------------ #
    def sort_by_streak(self):
        """
        Sorts habits by current streak and displays result
        """
        habits = self.sorter.sort_by_streak()

        print("\n=== Habits by Streak ===")
        self._display_habits(habits=habits)

    # -------------------------- Sort By Completion Rate ------------------------- #
    def sort_by_completion_rate(self):
        """
        Sorts habits by completion rate and displays result
        """
        habits = self.sorter.sort_by_completion_rate()

        print("\n=== Habits by Completion Streak ===")
        self._display_habits(habits=habits)

    # --------------------------- Sort by Creation Date -------------------------- #
    def sort_by_creation_date(self):
        """
        Sorts habits by creation date
        """
        habits = self.sorter.sort_by_creation_date()

        print("\n=== Habits by Creation Date ===")
        self._display_habits(habits=habits)

    # ---------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #