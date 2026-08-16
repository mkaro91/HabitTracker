from datetime import datetime, timedelta

from models.HabitTracker import HabitTracker
from models.HabitStatistics import HabitStatistics

from storage import Storage

class StartupService:
    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Methods --------------------------------- #
    # ---------------------------------------------------------------------------- #

    # -------------------------- Reset If Streak Broken -------------------------- #
    def reset_if_streak_broken(self, tracker: HabitTracker) -> None:
        """
        Loops through each Habit and ensures streak is still intact.
        Resets streak if streak is broken.

        :param tracker: Habit Tracker containing Habits
        """
        # Set Dates
        format = "%Y-%m-%d"
        today = datetime.strptime(datetime.now().strftime(format), format)
        yesterday = datetime.strptime((datetime.now() - timedelta(days=1)).strftime(format), format)

        # Check each habit
        for habit in tracker.get_all_habits():

            # If habit wasn't completed yesterday or today streak has been broken - reset streak
            if today not in habit.completed_dates and yesterday not in habit.completed_dates:
                habit.streaks.reset_streak()
        
        Storage().save(tracker=tracker)

    # ------------------------------ Daily Dashboard ----------------------------- #
    def daily_dashboard(self, tracker: HabitTracker, stats: HabitStatistics):
        # Set Date
        today = datetime.now()

        # Get Stats
        completed_today = len(stats.get_completed_today())
        total_habits = stats.get_total_habits()

        if total_habits == 0:
            completion_rate = 0
        else:
            completion_rate = completed_today / total_habits * 100 

        longest_streak_habit = stats.get_most_consistent_habit()

        print("\n===== Habit Tracker====")

        print(f"\nToday: {today.strftime("%B %d, %Y")}")

        for habit in tracker.get_all_habits():
            tag = "[✓]" if habit.is_completed(date=datetime.strptime(today.strftime("%Y-%m-%d"),"%Y-%m-%d")) else "[ ]"
            print(f"{tag} {habit.name:<20} {habit.get_streak()} day streak")

        print(f"\n{completed_today}/{total_habits} completed today")
        print(f"{completion_rate:.1f}% completion")

        if longest_streak_habit == None:
            longest_streak_string = "None"
        else:
            longest_streak_string = f"{longest_streak_habit.name} - {longest_streak_habit.get_streak()} days"

        print(f"Longest current streak: {longest_streak_string}")

    # ---------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #