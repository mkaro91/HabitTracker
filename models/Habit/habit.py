from datetime import datetime

from .goal_tracker import GoalTracker
from .streak_tracker import StreakTracker

from models.Achievements import Achievement, AchievementSystem

DATE_FORMAT = "%Y-%m-%d"

class Habit:
    """ Class that holds Habit information """
    def __init__(self, id: int, name: str, description: str, category: str | None = None, tags: list[str] = [], target_streak: int | None = None, target_completions: int | None = None):
        self.id = id
        self.name = name.title()
        self.description = description

        self.category = category
        self.tags = tags

        self.achievements = AchievementSystem()
        self.streaks = StreakTracker()
        self.targets = GoalTracker(target_streak=target_streak, target_completions=target_completions)

        self.created_date: datetime = datetime.now()
        self.completed_dates: list[datetime] = []


    # ----------------------------------- Magic ---------------------------------- #
    def __str__(self) -> str:
        date_string = 'Never' if not self.completed_dates else self.completed_dates[-1].strftime('%B %d')
        return f"{self.name} | Streak: {self.get_streak()} | Last Completed: {date_string}"


    # ---------------------------------------------------------------------------- #
    # -------------------------------- Persistence ------------------------------- #
    # ---------------------------------------------------------------------------- #
    @classmethod
    def from_dict(cls, data):
        habit = cls(
            id = data['id'],
            name = data['name'],
            description = data['description'],
            category = data.get('category', None),
            tags = data.get('tags', []),
        )
        habit.achievements = AchievementSystem.from_dict(data['achievements'])
        habit.targets = GoalTracker.from_dict(data['targets'])
        habit.streaks = StreakTracker.from_dict(data['streaks'])
        habit.created_date = datetime.strptime(data['created_date'], DATE_FORMAT)
        habit.completed_dates = [datetime.strptime(date, DATE_FORMAT) for date in data['completed_dates']]
        return habit

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category': self.category,
            'tags': self.tags,
            'achievements': self.achievements.to_dict(),
            'streaks': self.streaks.to_dict(),
            'targets': self.targets.to_dict(),
            'created_date': self.created_date.strftime(DATE_FORMAT),
            'completed_dates': [date.strftime(DATE_FORMAT) for date in self.completed_dates]
        }

    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Helpers --------------------------------- #
    # ---------------------------------------------------------------------------- #
    def _calculate_days_since_creation(self) -> int:
        """
        Calculates the number of days since a Habit object was created

        :return int: Number of days since creation
        """
        days_since_creation = (datetime.now() - self.created_date).days

        return days_since_creation
    

    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Methods --------------------------------- #
    # ---------------------------------------------------------------------------- #

    # --------------------------------- Complete --------------------------------- #
    def complete(self, date: datetime) -> bool:
        """
        Completes a habit for a given date by adding the date to the completed dates attribute

        :param date: Date habit was completed

        :return True: Completion of Habit was successful
        :return False: Completion of Habit failed
        """
        if not self.is_completed(date=date):
            self.completed_dates.append(date)

            self.increase_streak()

            return True

        return False

    # -------------------------------- Uncomplete -------------------------------- #
    def uncomplete(self, date: datetime) -> bool:
        """
        Uncomplete a Habit for a givn date by removing the date from completed dates attribute if date in set

        :param date: Date to remove

        :return True: Date was successfully removed
        :return False: Date doesn't exist or removal failed
        """
        if self.is_completed(date=date):
            self.completed_dates.remove(date)
            self.decrease_streak()

            return True

        return False

    # ------------------------------- Is Completed ------------------------------- #
    def is_completed(self, date: datetime) -> bool:
        """
        Returns whether or not the Habit has been completed on a given date

        :param date: Date to check for completion

        :return True: Habit was completed on given date
        :return False: Habit was not completed on given date
        """
        completed = date in self.completed_dates

        return completed

    # --------------------------- Get Completion Count --------------------------- #
    def get_completion_count(self) -> int:
        """
        Calculates the number of times a Habit has been completed

        :return int: Number of time Habit has been completed
        """
        completion_count = len(self.completed_dates)

        return completion_count

    # ---------------------------- Get Complation Rate --------------------------- #
    def get_completion_rate(self) -> float:
        """
        Determine the completion of a Habit by dividing completion count by days since creation

        :return float: Completion rate
        """
        days_since_creation = self._calculate_days_since_creation()
        completion_count = self.get_completion_count()
        completion_rate = completion_count / days_since_creation

        return completion_rate

    # ---------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #


    
    # ------------------------------ Streak Methods ------------------------------ #
    # ---------------------------------------------------------------------------- #

    # -------------------------------- Get Streak -------------------------------- #
    def get_streak(self) -> int:
        return self.streaks.streak

    # ------------------------------ Get Max Streak ------------------------------ #
    def get_max_streak(self) -> int:
        return self.streaks.max_streak

    # ------------------------------ Increase Streak ----------------------------- #
    def increase_streak(self) -> None:
        self.streaks.increase_streak()

    # ------------------------------ Decrease Streak ----------------------------- #
    def decrease_streak(self) -> None:
        self.streaks.decrease_streak()

    # ---------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #



    # ------------------------------- Goal Methods ------------------------------- #
    # ---------------------------------------------------------------------------- #

    # -------------------------- Check Streak Target Met ------------------------- #
    def check_streak_target_met(self) -> bool:
        current_streak = self.get_streak()
        is_target_met = self.targets.target_streak_met(current_streak=current_streak)

        return is_target_met

    # ------------------------ Check Completion Target Met ----------------------- #
    def check_completion_target_met(self) -> bool:
        completion_count = self.get_completion_count()
        is_target_met = self.targets.target_completions_met(completion_count=completion_count)

        return is_target_met

    def get_target_streak(self):
        return self.targets.target_streak

    def get_target_completions(self):
        return self.targets.target_completions

    def set_target_streak(self, new_target):
        self.targets.target_streak = new_target

    def set_target_completions(self, new_target):
        self.targets.target_completions = new_target

    # ---------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #



    # ---------------------------- Achievement Methods --------------------------- #
    # ---------------------------------------------------------------------------- #

    def get_achievements(self) -> list[Achievement]:
        return self.achievements.achievements

    # -------------------------- Get Latest Achievement -------------------------- #
    def get_latest_achievement(self) -> Achievement | None:
        achievement = self.achievements.get_lastest_achievement()

        return achievement

    # ----------------------- Check for Streak Achievement ----------------------- #
    def check_for_streak_achievement(self) -> bool:
        current_streak = self.get_streak()

        if self.achievements.current_streak_in_streak_achievements(current_streak=current_streak):
            self.achievements.remove_from_remaining_streak_achievements(current_streak=current_streak)
            self.achievements.create_and_add_streak_achievement(current_streak=current_streak)

            return True

        return False

    # --------------------- Check for Completion Achievement --------------------- #
    def check_for_completion_achievement(self) -> bool:
        completion_count = self.get_completion_count()

        if self.achievements.completion_count_in_completion_achievements_remaining(completion_count=completion_count):
            self.achievements.remove_from_remaining_completion_achievements(completion_count=completion_count)
            self.achievements.create_and_add_completion_achievement(completion_count=completion_count)

            return True

        return False

    # ---------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #