from datetime import datetime, timedelta

from models.HabitTracker import HabitTracker

from services.Collector import Collector

class HistoryService:
    def __init__(self):
        self.collector = Collector()

    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Helpers --------------------------------- #
    # ---------------------------------------------------------------------------- #
    def _convert_now(self) -> datetime:
        """
        Converts the current datetime to required format

        :return datetime: Current datetime in required format
        """
        format = "%Y-%m-%d"

        return datetime.strptime(datetime.now().strftime(format), format)

    def _create_date_string(self, date: datetime) -> str:
        """
        Creates a date string in required display format

        :param date: Date to be converted to string

        :return str: String of provided date
        """
        return date.strftime("%B %d")

    def _create_completed_label(self, completed: bool) -> str:
        """
        Creates a label representing whether habit is completed

        :param completed: Whether or not habit is completed

        :return str: String representation of habit's completed value
        """
        return 'O' if completed else 'X'

    # ---------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #


    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Methods --------------------------------- #
    # ---------------------------------------------------------------------------- #

    # -------------------------- View Completion History ------------------------- #
    def view_completion_history(self, tracker: HabitTracker, days: int = 7) -> None:
        """
        View completion history within the given number of days

        :param tracker: Habit Tracker containing Habits
        :param days: Number of days to go back in history
        """

        # Get Habit ID
        habit_id = self.collector.number_collector.collect_id()

        # Find Habit or Exit
        habit = tracker.get_habit(habit_id=habit_id)
        if habit is None:
            print(f"\nHabit #{habit_id} not found.") 
            return

        # Set Dates
        today = self._convert_now()
        target_date = today - timedelta(days=days)

        print(f"\n=== Previous {days} Days ===")

        # While target date is before today
        while target_date <= today:
            date_string = self._create_date_string(date=target_date)
            completed = habit.is_completed(date=target_date)
            completed_label = self._create_completed_label(completed=completed)

            # Display Date Information
            print(f"{date_string}: {completed_label}")

            # Increase Date
            target_date += timedelta(days=1)


    # ---------------------------- View Days Completed --------------------------- #
    def view_days_completed(self, tracker: HabitTracker, days: int = 7) -> None:
        """
        View which days a habit was completed within the given number of days

        :param tracker: Habit Tracker containing Habits
        :param days: Number of days to go back in history
        """

        # Get Habit ID
        habit_id = self.collector.number_collector.collect_id()

        # Find Habit or Exit
        habit = tracker.get_habit(habit_id=habit_id)
        if habit is None:
            return

        # Set Dates
        today = self._convert_now()
        target_date = today - timedelta(days=days)

        print(f"\n=== Previous {days} Days ===")

        # While target date is before today
        while target_date <= today:

            # If habit is completed display date information
            if habit.is_completed(date=target_date):
                date_string = self._create_date_string(date=target_date)

                print(date_string)

            # Increase date
            target_date += timedelta(days=1)

    # -------------------------- View Days Not Completed ------------------------- #
    def view_days_not_completed(self, tracker: HabitTracker, days: int = 7):
        """
        View which days a habit was incompleted within the given number of days

        :param tracker: Habit Tracker containing Habits
        :param days: Number of days to go back in history
        """

        # Get Habit ID
        habit_id = self.collector.number_collector.collect_id()

        # Find Habit or Exit
        habit = tracker.get_habit(habit_id=habit_id)
        if habit is None:
            return

        # Set Dates
        today = self._convert_now()
        target_date = today - timedelta(days=days)

        print(f"\n=== Previous {days} Days ===")

        # While target date is before today
        while target_date <= today:

            # If habit is not completed display date information
            if not habit.is_completed(date=target_date):
                date_string = self._create_date_string(date=target_date)

                print(date_string)

            # Increase Date
            target_date += timedelta(days=1)

    # -------------------------------- Lookup Date ------------------------------- #
    def lookup_date(self, tracker: HabitTracker):
        """
        Look up which habits were completed and incomplete on a specific day

        :param tracker: Habit Tracker containing Habits
        """

        # Get Date or default to Today
        date = self.collector.date_collector.collect_date()
        if not date:
            date = self._convert_now()

        date_string = self._create_date_string(date=date)
        print(f"\n=== {date_string} ===")
        
        for habit in tracker.get_all_habits():

            # If habit was created after target date, skip habit
            # Ensures no missing dates
            if habit.created_date > date:
                continue

            completed = habit.is_completed(date=date)
            completed_label = self._create_completed_label(completed=completed)

            print(f"{habit.name}: {completed_label}")

    # ---------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #