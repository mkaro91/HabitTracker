from models.Habit import Habit
from models.HabitTracker import HabitTracker

from services.Collector import Collector

from storage import Storage

class ArchiveService:
    def __init__(self):
        self.collector = Collector()
        self.storage = Storage()

    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Methods --------------------------------- #
    # ---------------------------------------------------------------------------- #
    def get_archived_habits(self) -> list[Habit]:
        """
        Loads archived Habits from JSON file

        :return list[Habit]: List of archived Habits
        """
        return self.storage.load_archive()


    def view_archived_habits(self) -> None:
        """
        Displays archived Habits if any exist
        """
        archive = self.get_archived_habits()

        print("\n=== Archived Habits ===")
        if not archive:
            print("No habits found in archive.")
        else:
            for habit in archive:
                print(f"- {habit.name}")

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

        if habit is None:
            print(f"\nHabit #{habit_id} was not found.")
            return

        # Remove Habit from current habits
        result = tracker.remove_habit(habit_id=habit_id)
        if result:
            archive.append(habit)

            self.storage.save_archive(archived_habits=archive)
            self.storage.save(tracker=tracker)

            print(f"\nHabit #{habit_id} was removed from active habits.")
            print(f"Successfully archived Habit #{habit_id}.")

        else:
            print(f"\nFailed to archive Habit #{habit_id}.")

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

        if habit is None:
            print(f"\nHabit #{habit_id} not found in archive.")
            return

        # Add Habit to current Habits and remove from archive
        tracker.add_habit(habit)
        archive.remove(habit)
        print(f"\nSuccessfully unarchived Habit #{habit_id}.")

        self.storage.save(tracker=tracker)
        self.storage.save_archive(archived_habits=archive)