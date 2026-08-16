from datetime import datetime

from models.Habit import Habit

class HabitTracker:
    def __init__(self):
        self.habits = {}

    # ---------------------------------------------------------------------------- #
    # -------------------------------- Persistence ------------------------------- #
    # ---------------------------------------------------------------------------- #
    @classmethod
    def from_dict(cls, data):
        tracker = cls()
        tracker.habits = {k: Habit.from_dict(v) for k, v in data['habits'].items()}
        return tracker

    def to_dict(self):
        return {
            'habits': {k: v.to_dict() for k, v in self.habits.items()}
        }

    # ---------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #


    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Helpers --------------------------------- #
    # ---------------------------------------------------------------------------- #
    def _check_id_in_habits(self, habit_id: int) -> bool:
        """
        Checks if a given ID is found in stored habits

        :param habit_id: Habit ID to check for

        :return True: Habit ID found in habits
        :return False: Habit ID not found in habits
        """
        return str(habit_id) in self.habits

    def _earn_achievement(self, habit: Habit, func) -> None:
        """
        Allows for achievement to be earned

        :param habit: Habit which is earning achievement
        :param func: Function to run to check for ahievement earning
        """
        achievement_earned = func()

        if achievement_earned:
            achievement = habit.get_latest_achievement()

            print("\nAchievement Earned!")
            print(achievement)

    # ---------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #

    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Methods --------------------------------- #
    # ---------------------------------------------------------------------------- #

    # ------------------------------- Habit Actions ------------------------------ #
    # ---------------------------------------------------------------------------- #

    # --------------------------------- Get Habit -------------------------------- #
    def get_habit(self, habit_id: int) -> Habit | None:
        """
        Searches Habits and returns Habit with matching ID if found

        :param habit_id: Habit ID to search for

        :return Habit: Habit with matching ID
        :return None: No Habit with matching ID found
        """
        habit = self.habits.get(str(habit_id), None)

        return habit

    # ------------------------------ Get All Habits ------------------------------ #
    def get_all_habits(self) -> list[Habit]:
        """
        Returns a list of all Habits found in storage

        :return list[Habit]: List of Habits found in storage
        """
        habits = list(self.habits.values())

        return habits
    
    # --------------------------------- Add Habit -------------------------------- #
    def add_habit(self, habit: Habit) -> None:
        """
        Adds a Habit to stored habits

        :param habit: Habit object to be added to storage
        """
        self.habits[habit.id] = habit

    # ------------------------------- Remove Habit ------------------------------- #
    def remove_habit(self, habit_id: str) -> bool:
        """
        Removes a Habit from storage if Habit is found in storage

        :param habit_id: Habit ID for Habit to be deleted

        :return True: Habit was successfully removed
        :return False: Habit removal failed
        """
        if not self._check_id_in_habits(habit_id=habit_id):
            return False
        
        del self.habits[str(habit_id)]
        return True


    # ------------------------ Completions & Uncompletions ----------------------- #
    # ---------------------------------------------------------------------------- #

    # ------------------------------ Complete Habit ------------------------------ #
    def complete_habit(self, habit_id: str, date: datetime) -> bool:
        """
        Complete a habit if found in storage

        :param habit_id: Habit ID for Habit to be completed
        :param date: Date to complete the Habit on

        :return True: Habit was successfully completed
        :return False: Habit was not completed
        """
        habit = self.get_habit(habit_id=habit_id)
        if habit is None:
            return False

        result = habit.complete(date=date)

        if result:
            self._earn_achievement(habit=habit, func=habit.check_for_streak_achievement)
            self._earn_achievement(habit=habit, func=habit.check_for_completion_achievement)
            return True

        return False

    # ----------------------------- Uncomplete Habit ----------------------------- #
    def uncomplete_habit(self, habit_id: str, date: datetime) -> bool:
        """
        Uncomplete a Habit if found in storage

        :param habit_id: Habit ID for Habit to be uncompleted
        :param date: Date to uncomplete the Habit on

        :return True: Habit was successfully uncompleted
        :return False: Habit was not uncompleted
        """
        habit = self.get_habit(habit_id=habit_id)
        if habit is None:
            return False

        return habit.uncomplete(date=date)

    # --------------------------- Get Completed Habits --------------------------- #
    def get_completed_habits(self, date: datetime) -> list[Habit]:
        """
        Return a list of habits that were completed on a given date

        :param date: Date to check completion on

        :return list[Habit]: List of completed Habits
        """
        completed_habits = [habit for habit in self.get_all_habits() if date in habit.completed_dates]

        return completed_habits

    # --------------------------- Get Incomplete Habits -------------------------- #
    def get_incomplete_habits(self, date: datetime) -> list[Habit]:
        """
        Returns a list of habits that were incomplete on a given date

        :param date: Date to check for incompletion on
        
        :return list[Habit]: List of incompleted Habits
        """
        incomplete_habits = [habit for habit in self.get_all_habits() if date not in habit.completed_dates]

        return incomplete_habits

    # ---------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #