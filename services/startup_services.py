from datetime import datetime, timedelta

from models.HabitTracker import HabitTracker

from storage import Storage

class StartupService:
    def reset_if_streak_broken(self, tracker: HabitTracker) -> None:
        today = datetime.strptime(datetime.now().strftime(format), format)
        yesterday = datetime.strptime((datetime.now() - timedelta(days=1)).strftime(format), format)

        for habit in tracker.get_all_habits():
            if today not in habit.completed_dates and yesterday not in habit.completed_dates:
                habit.current_streak = 0
        
        Storage.save(tracker=tracker)