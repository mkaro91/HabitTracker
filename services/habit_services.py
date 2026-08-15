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
        num_habits = len(tracker.get_all_habits()) + len(Storage().load_archive())
        id = self._generate_habit_id(num_habits=num_habits)

        # Collect Values
        name = self.collector.string_collector.collect_non_blank("\nHabit Name: ")
        description = self.collector.string_collector.collect_non_blank("Habit Description: ")
        category = self.collector.string_collector.collect_non_blank("Habit Category: ")

        # Collect Tags
        tags = self.collector.object_collector.collect_list("Habit Tag: ")

        # Collect Targets
        target_streak = self.collector.number_collector.collect_number_nullable("Target Streak: ")
        target_completions = self.collector.number_collector.collect_number_nullable("Target Completions: ")
            
        # Create Habit and Save
        habit = Habit(id=id, name=name, description=description, category=category, tags=tags, target_streak=target_streak, target_completions=target_completions)
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

        new_category = input("New Habit Category: ").strip()
        new_tags = self.collector.object_collector.collect_list("New Habit Tag: ")

        new_target_streak = self.collector.number_collector.collect_number_nullable("New Target Streak: ")
        new_target_completions = self.collector.number_collector.collect_number_nullable("New Target Completions: ")

        # Set new values if not blank
        if new_name:
            habit.name = new_name.title()
        if new_description:
            habit.description = new_description

        if new_category:
            habit.category = new_category
        if new_tags:
            habit.tags = new_tags

        if new_target_streak is not None:
            habit.target_streak = new_target_streak
        if new_target_completions is not None:
            habit.target_completions = new_target_completions

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

    def view_habit_goals(self, tracker: HabitTracker):
        habit_id = self.collector.number_collector.collect_id()

        habit = tracker.get_habit(habit_id=habit_id)
        if habit is None: 
            print(f"Habit #{habit_id} was not found.")
            return

        print(f"\n{habit.name}")
        print("Target Streak:", 'None' if habit.target_streak is None else f'{habit.target_streak} Days')
        print("Target Completions:", 'None' if habit.target_completions is None else f'{habit.target_completions} Completions')

        print(f"\nCurrent Streak: {habit.current_streak}")
        print(f"Completions: {habit.get_completion_count()}")
