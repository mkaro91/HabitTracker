from models.Habit import Habit
from models.HabitTracker import HabitTracker

from services.Collector import Collector

from storage import Storage

class HabitService:
    def __init__(self):
        self.collector = Collector()

    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Helpers --------------------------------- #
    # ---------------------------------------------------------------------------- #
    def _generate_habit_id(self, num_habits: int) -> int:
        """
        Generates an ID value for a Habit

        :return int: ID
        """
        return num_habits + 1


    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Methods --------------------------------- #
    # ---------------------------------------------------------------------------- #
    def create_habit(self, tracker: HabitTracker) -> None:
        """
        Adds a Habit object to Storage

        :param tracker: Tracker object to add Habit to
        """

        # Generate ID
        id = self._generate_habit_id(num_habits=len(tracker.get_all_habits()))

        # Collect Values
        name = self.collector.string_collector.collect_non_blank("\nHabit Name: ")
        description = self.collector.string_collector.collect_non_blank("Habit Description: ")

        # Create Habit and Save
        habit = Habit(id=id, name=name, description=description)
        tracker.add_habit(habit=habit)
        Storage().save(tracker=tracker)

        print(f"\nHabit #{habit.id} was created successfully.")


    def edit_habit(self, tracker: HabitTracker) -> None:
        """
        Edits a Habit's values

        :param tracker: Habit Tracker object that contains the Habit
        """

        # Collect Habit ID
        habit_id = self.collector.number_collector.collect_id()

        # Find Habit or Exit
        habit = tracker.get_habit(hait_id=habit_id)
        if habit is None:
            print(f"\nHabit #{habit_id} not found.")
            return

        # Collect new values from user
        new_name = input("New Habit Name: ").strip()
        new_description = input("New Habit Description: ")

        # Set new values if not blank
        if new_name:
            habit.name = new_name.title()
        if new_description:
            habit.description = new_description

        # Save
        Storage().save(tracker=tracker)
        print(f"\nSuccessfully updated Habit #{habit_id}.")


    def delete_habit(self, tracker: HabitTracker) -> None:
        """
        Removes a Habit object from Storage

        :param tracker: Habit tracker object that contains Habit
        """

        # Collect Habit ID
        habit_id = self.collector.number_collector.collect_id()

        # Record result and save
        result = tracker.remove_habit(habit_id=habit_id)
        Storage().save(tracker=tracker)

        if result:
            print(f"\nSuccessfully deleted Habit #{habit_id}.")
        else:
            print(f"Failed to delete Habit #{habit_id}.")


    def view_all_habits(self, tracker: HabitTracker) -> None:
        """
        View all stored Habits

        :param tracker: Habit Tracker object containing Habits
        """

        # Get all habits
        habits = tracker.get_all_habits()

        # Print results
        print("\n=== Habits ===")
        if not habits:
            print("No habits found in storage.")
            return

        for habit in habits:
            print(habit)