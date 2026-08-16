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
        today = datetime.strptime(datetime.now().strftime(format), format)

        return today

    # ---------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #


    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Methods --------------------------------- #
    # ---------------------------------------------------------------------------- #
    
    # ----------------------------- Get Total Habits ----------------------------- #
    def get_total_habits(self) -> int:
        """
        Total number habits found in storage

        :return int: Number Habits found in storage
        """
        number_of_habits = len(self.habit_tracker.habits)

        return number_of_habits

    # ---------------------------- Get Completed Today --------------------------- #
    def get_completed_today(self) -> list[Habit]:
        """
        Returns list of Habits that have been completed today

        :return list[Habit]: List of Habits that have been completed today
        """
        today = self._get_today()
        completed_habits = self.habit_tracker.get_completed_habits(date=today)

        return completed_habits

    # --------------------------- Get Incomplete Today --------------------------- #
    def get_incomplete_today(self) -> list[Habit]:
        """
        Returns list of Habits that have not been completed today

        :return list[Habit]: List of Habits that have not been completed today
        """
        today = self._get_today()
        incomplete_habits = self.habit_tracker.get_incomplete_habits(date=today)

        return incomplete_habits

    # ------------------------ Get Overall Completion Rate ----------------------- #
    def get_overall_completion_rate(self) -> float:
        """
        Returns the overall completion rate of all Habits

        :return float: Average completion rate
        """
        total_completions = sum(habit.get_completion_count() for habit in self.habit_tracker.get_all_habits())
        completion_rate = total_completions / len(self.habit_tracker.get_all_habits())

        return completion_rate

    # ---------------------------- Get Best Max Streak --------------------------- #
    def get_best_max_streak(self) -> Habit | None:
        """
        Returns the highest max streak found in Habits

        :return Habit: Habit with the highest max streak attribute
        """
        habits = self.habit_tracker.get_all_habits()

        if not habits:
            return None
        
        best_max_streak_habit = max(habits, key=lambda x: x.get_max_streak())
        return best_max_streak_habit

    # ------------------------- Get Most Consistent Habit ------------------------ #
    def get_most_consistent_habit(self) -> Habit | None:
        """
        Returns the habit with the highest current streak attribute

        :return Habit: Habit with the highest current streak attribute
        """
        habits = self.habit_tracker.get_all_habits()

        if not habits:
            return None
        
        most_consistent_habit = max(habits, key=lambda x: x.get_streak())
        return most_consistent_habit

    # ---------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #
