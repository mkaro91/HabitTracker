from datetime import datetime

from models.HabitTracker import HabitTracker
from models.HabitStatistics import HabitStatistics

from services.Collector import Collector

from storage import Storage

class DateService:
    def __init__(self):
        self.collector = Collector()

    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Helpers --------------------------------- #
    # ---------------------------------------------------------------------------- #
    def _convert_now(self) -> datetime:
        """
        Returns today's date in the required format

        :return datetime: Today's date in required format
        """
        format = "%Y-%m-%d"
        return datetime.strptime(datetime.now().strftime(format), format)

    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Methods --------------------------------- #
    # ---------------------------------------------------------------------------- #
    def complete_habit(self, tracker: HabitTracker) -> None:
        """
        Collects ID and date from user and completes a Habit for the given date

        :param tracker: Habit Tracker that contains target Habit
        """

        # Collect values
        habit_id = self.collector.number_collector.collect_id()
        date = self.collector.date_collector.collect_date()
        if not date:
            date = self._convert_now()

        # Complete habit
        result = tracker.complete_habit(habit_id=habit_id, date=date)

        if result:
            print(f"\nSuccessfully completed Habit #{habit_id}.")
            Storage().save(tracker=tracker)
        else:
            print(f"\nFailed to completed Habit #{habit_id}.")


    def uncomplete_habit(self, tracker: HabitTracker) -> None:
        """
        Collects ID and date from user and uncompletes a Habit if completed on given date

        :param tracker: Habit Tracker that contains target Habit
        """

        # Collect values
        habit_id = self.collector.number_collector.collect_id()
        date = self.collector.date_collector.collect_date()
        if not date:
            date = self._convert_now()

        # Uncomplete Habit
        result = tracker.uncomplete_habit(habit_id=habit_id, date=date)

        if result:
            print(f"\nSuccessfully uncompleted Habit #{habit_id}.")
            Storage().save(tracker=tracker)
        else:
            print(f"\nFailed to uncomplete Habit #{habit_id}.")


    def is_habit_completed_today(self, tracker: HabitTracker) -> None:
        """
        Collects ID from user and checks if coresponding Habit is completed today

        :param tracker: Habit Tracker that contains target Habit
        """

        # Collect ID
        habit_id = self.collector.number_collector.collect_id()

        # Find Habit or Exit
        habit = tracker.get_habit(habit_id=habit_id)
        if habit is None:
            print(f"\nHabit #{habit_id} not found.")
            return False

        # Check if habit is complete
        result = habit.is_completed(date=self._convert_now())

        if result:
            print(f"\nHabit #{habit_id} is complete.")
        else:
            print(f"\nHabit #{habit_id} is incomplete.")


    def view_habits_completed_today(self, stats: HabitStatistics) -> None:
        """
        Returns a list of Habits that have been completed today

        :param stats: Habit statistics tracker 
        """
        completed_today = stats.get_completed_today()

        print("\n=== Habits Completed Today ===")

        if not completed_today:
            print("No habits have been completed today.")
            return
        
        for habit in completed_today:
            print(habit)

    def view_habits_incomplete_today(self, stats: HabitStatistics) -> None:
        """
        Returns a list of Habits that are not completed today

        :param stats: Habit statistics tracker
        """
        incomplete = stats.get_incomplete_today()

        print("\n=== Habits Not Completed Today ===")

        if not incomplete:
            print("All habits have been completed today.")
            return

        for habit in incomplete:
            print(habit)