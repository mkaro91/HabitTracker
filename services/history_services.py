from datetime import datetime, timedelta

from models.HabitTracker import HabitTracker

from services.Collector import Collector

class HistoryService:
    def __init__(self):
        self.collector = Collector()

    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Helpers --------------------------------- #
    # ---------------------------------------------------------------------------- #
    def _convert_now(self):
        format = "%Y-%m-%d"
        return datetime.strptime(datetime.now().strftime(format), format)


    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Methods --------------------------------- #
    # ---------------------------------------------------------------------------- #
    def view_completion_history(self, tracker: HabitTracker, days: int = 7) -> None:
        """
        View completion history within the given number of days

        :param tracker: Habit Tracker containing Habits
        :param days: Number of days to go back in history
        """
        habit_id = self.collector.number_collector.collect_id()

        habit = tracker.get_habit(habit_id=habit_id)
        if habit is None: 
            return

        today = self._convert_now()
        target_date = today - timedelta(days=days)

        print(f"\n=== Previous {days} Days ===")
        while target_date <= today:
            completed = habit.is_completed(date=target_date)
            print(f"{target_date.strftime("%B %d")}: {'O' if completed else 'X'}")
            target_date += timedelta(days=1)


    def view_days_completed(self, tracker: HabitTracker, days: int = 7) -> None:
        """
        View which days a habit was completed within the given number of days

        :param tracker: Habit Tracker containing Habits
        :param days: Number of days to go back in history
        """
        habit_id = self.collector.number_collector.collect_id()

        habit = tracker.get_habit(habit_id=habit_id)
        if habit is None:
            return

        today = self._convert_now()
        target_date = today - timedelta(days=days)

        print(f"\n=== Previous {days} Days ===")
        while target_date <= today:
            if habit.is_completed(date=target_date):
                print(target_date.strftime("%B %d"))
            target_date += timedelta(days=1)

    def view_days_not_completed(self, tracker: HabitTracker, days: int = 7):
        """
        View which days a habit was incompleted within the given number of days

        :param tracker: Habit Tracker containing Habits
        :param days: Number of days to go back in history
        """
        habit_id = self.collector.number_collector.collect_id()

        habit = tracker.get_habit(habit_id=habit_id)
        if habit is None:
            return

        today = self._convert_now()
        target_date = today - timedelta(days=days)

        print(f"\n=== Previous {days} Days ===")
        while target_date <= today:
            if not habit.is_completed(date=target_date):
                print(target_date.strftime("%B %d"))
            target_date += timedelta(days=1)

    def lookup_date(self, tracker: HabitTracker):
        """
        Look up which habits were completed and incomplete on a specific day

        :param tracker: Habit Tracker containing Habits
        """
        date = self.collector.date_collector.collect_date()
        if not date:
            date = self._convert_now()

        print(f"\n=== {date.strftime("%B %d")} ===")
        for habit in tracker.get_all_habits():
            if habit.created_date > date:
                continue

            print(f"{habit.name}: {'O' if habit.is_completed(date=date) else 'X'}")