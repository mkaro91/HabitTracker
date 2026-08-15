from datetime import datetime, timedelta

from models.HabitTracker import HabitTracker
from models.HabitStatistics import HabitStatistics

from storage import Storage

class StartupService:
    def reset_if_streak_broken(self, tracker: HabitTracker) -> None:
        format = "%Y-%m-%d"
        today = datetime.strptime(datetime.now().strftime(format), format)
        yesterday = datetime.strptime((datetime.now() - timedelta(days=1)).strftime(format), format)

        for habit in tracker.get_all_habits():
            if today not in habit.completed_dates and yesterday not in habit.completed_dates:
                habit.current_streak = 0
        
        Storage().save(tracker=tracker)

    def daily_dashboard(self, tracker: HabitTracker, stats: HabitStatistics):
        today = datetime.now()
        completed_today = len(stats.get_completed_today())
        total_habits = stats.get_total_habits()
        completion_rate = completed_today / total_habits * 100
        longest_streak_habit = stats.get_most_consistent_habit()

        print("\n===== Habit Tracker====")

        print(f"\nToday: {today.strftime("%B %d, %Y")}\n")

        for habit in tracker.get_all_habits():
            tag = "[✓]" if habit.is_completed(date=datetime.strptime(today.strftime("%Y-%m-%d"),"%Y-%m-%d")) else "[ ]"
            print(f"{tag} {habit.name:<20} {habit.current_streak} day streak")

        print(f"\n{completed_today}/{total_habits} completed today")
        print(f"{completion_rate:.1f}% completion")

        print(f"Longest current streak: {longest_streak_habit.name} - {longest_streak_habit.current_streak} days")