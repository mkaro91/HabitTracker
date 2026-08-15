from datetime import datetime

from models.Habit import Habit
from models.HabitTracker import HabitTracker

class HabitStatistics:
    """ Class to track Statistics """
    def __init__(self, habit_tracker: HabitTracker):
        self.habit_tracker = habit_tracker


    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Helpers --------------------------------- #
    # ---------------------------------------------------------------------------- #
    def _get_today(self) -> datetime:
        """
        Get today's date in required format

        :return datetime: Today's date in required format
        """
        format = "%Y-%m-%d"
        return datetime.strptime(datetime.now().strftime(format), format)


    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Methods --------------------------------- #
    # ---------------------------------------------------------------------------- #
    def get_total_habits(self) -> int:
        """
        Total number habits found in storage

        :return int: Number Habits found in storage
        """
        return len(self.habit_tracker.habits)

    def get_completed_today(self) -> list[Habit]:
        """
        Returns list of Habits that have been completed today

        :return list[Habit]: List of Habits that have been completed today
        """
        return self.habit_tracker.get_completed_habits(date=self._get_today())

    def get_incomplete_today(self) -> list[Habit]:
        """
        Returns list of Habits that have not been completed today

        :return list[Habit]: List of Habits that have not been completed today
        """
        return self.habit_tracker.get_incomplete_habits(date=self._get_today())

    def get_overall_completion_rate(self) -> float:
        """
        Returns the overall completion rate of all Habits

        :return float: Average completion rate
        """
        total_completions = sum(habit.get_completion_count() for habit in self.habit_tracker.get_all_habits())
        return total_completions / len(self.habit_tracker.get_all_habits())

    def get_best_max_streak(self) -> Habit:
        """
        Returns the highest max streak found in Habits

        :return Habit: Habit with the highest max streak attribute
        """
        return max(self.habit_tracker.get_all_habits(), key=lambda x: x.max_streak)

    def get_most_consistent_habit(self) -> Habit:
        """
        Returns the habit with the highest current streak attribute

        :return Habit: Habit with the highest current streak attribute
        """
        return max(self.habit_tracker.get_all_habits(), key=lambda x: x.current_streak)
