from models.Habit import Habit
from models.HabitTracker import HabitTracker

from services.Collector import Collector

from storage import Storage

class ArchiveService:
    def __init__(self):
        self.collector = Collector()
        self.storage = Storage()

    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Helpers --------------------------------- #
    # ---------------------------------------------------------------------------- #
    def _save_all(self, tracker: HabitTracker, archive: list[Habit]) -> None:
        """
        Saves both habits and archied habits

        :param tracker: Habit Tracker containing habits to be saved
        :param archive: List of archived Habits
        """
        self.storage.save(tracker=tracker)
        self.storage.save_archive(archived_habits=archive)

    def _check_habit_found(self, habit: Habit | None) -> bool:
        """
        Checks if a Habit was found after searching with Habit ID

        :param habit: Habit found by search or None

        :return True: Habit was found during search
        :return False: No Habit was found during search
        """
        if habit is None:
            print(f"Habit with matching ID not found.")
            return False
        return True

    # ---------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #
    

    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Methods --------------------------------- #
    # ---------------------------------------------------------------------------- #

    # ---------------------------- Get Archived Habits --------------------------- #
    def get_archived_habits(self) -> list[Habit]:
        """
        Loads archived Habits from JSON file

        :return list[Habit]: List of archived Habits
        """
        archive = self.storage.load_archive()

        return archive

    # --------------------------- View Archived Habits --------------------------- #
    def view_archived_habits(self) -> None:
        """
        Displays archived Habits if any exist
        """
        archive = self.get_archived_habits()

        print("\n=== Archived Habits ===")

        if not archive:
            print("No habits found in archive.")
            return
        
        for habit in archive:
            print(f"- {habit.name}")

    # ------------------------------- Archive Habit ------------------------------ #
    def archive_habit(self, tracker: HabitTracker) -> None:
        """
        Archives a current Habit

        :param tracker: Habit Tracker that contains target Habit
        """

        # Load archive
        archive = self.get_archived_habits()

        # Get Habit or Exit
        habit_id = self.collector.number_collector.collect_id()
        habit = tracker.get_habit(habit_id=habit_id)

        if not self._check_habit_found(habit=habit):
            return

        # Remove Habit from current habits
        result = tracker.remove_habit(habit_id=habit_id)

        if result:
            archive.append(habit)

            self._save_all(tracker=tracker, archive=archive)

            print(f"\nHabit #{habit_id} was removed from active habits.")
            print(f"Successfully archived Habit #{habit_id}.")

        else:
            print(f"\nFailed to archive Habit #{habit_id}.")

    # ------------------------------ Unarchive Habit ----------------------------- #
    def unarchive_habit(self, tracker: HabitTracker) -> None:
        """
        Removes a Habit from the archive and places it back into current Habits

        :param tracker: Habit Tracker where the Habit is to be placed
        """

        # Load archive
        archive = self.get_archived_habits()

        # Get Habit or Exit
        habit_id = self.collector.number_collector.collect_id()
        habit = None

        for habit in archive:
            if habit.id == habit_id:
                habit = habit
                break

        if not self._check_habit_found(habit=habit):
            return

        # Add Habit to current Habits and remove from archive
        tracker.add_habit(habit)
        archive.remove(habit)

        print(f"\nSuccessfully unarchived Habit #{habit_id}.")

        self._save_all(tracker=tracker, archive=archive)

    # ---------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #