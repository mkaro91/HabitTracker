from models.Habit import Habit
from models.HabitTracker import HabitTracker

from services.habit_services import HabitService

from services.Collector import Collector

# All templates default to a target streak and target completion of 10
TARGET = 10

class TemplateService:
    def __init__(self, tracker: HabitTracker):
        self.collector = Collector()
        self.tracker = tracker

    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Helpers --------------------------------- #
    # ---------------------------------------------------------------------------- #
    def _get_num_habits(self) -> int:
        """
        Returns the number of habits currently found in the Habit Tracker

        :return int: Number of current habits
        """
        return len(self.tracker.get_all_habits())

    def _get_new_habit_id(self) -> int:
        """
        Generates a new ID for the templated Habit

        :return int: ID value
        """
        num_habits = self._get_num_habits()
        return HabitService()._generate_habit_id(num_habits=num_habits)

    def _add_template_habit(self, habit: Habit) -> None:
        """
        Adds templated habit to habits in Habit Tracker
        """
        self.tracker.add_habit(habit=habit)

    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Methods --------------------------------- #
    # ---------------------------------------------------------------------------- #
    
    # Health Templates

    # ----------------------------- Exercise Template ---------------------------- #
    def exercise_template(self) -> None:
        id = self._get_new_habit_id()

        name = "Exercise"

        minutes_per_day = self.collector.number_collector.collect_number(prompt="\nHow many minutes of exercise per day: ")
        description = f"Exercise {minutes_per_day} minutes per day."

        tags = [category := "Health"]

        habit = Habit(id=id, name=name, description=description, category=category, tags=tags, target_streak=TARGET, target_completions=TARGET)
        self._add_template_habit(habit=habit)

    # --------------------------- Drink Water Template --------------------------- #
    def drink_water_template(self) -> None:
        id = self._get_new_habit_id()

        name = "Drink Water"

        cups_per_day = self.collector.number_collector.collect_number(prompt="\nHow many cups of water per day: ")
        description = f"Drink {cups_per_day} cups of water daily."

        tags = [category := "Health"]

        habit = Habit(id=id, name=name, description=description, category=category, tags=tags, target_streak=TARGET, target_completions=TARGET)
        self._add_template_habit(habit=habit)

    # Productivity Templates

    # --------------------------- Check Email Template --------------------------- #
    def check_email_template(self) -> None:
        id = self._get_new_habit_id()

        name = "Check Emails"
        description = "Check emails daily"

        tags = [category := "Productivity"]

        habit = Habit(id=id, name=name, description=description, category=category, tags=tags, target_streak=TARGET, target_completions=TARGET)
        self._add_template_habit(habit=habit)

    # ------------------------ Limit Social Media Template ----------------------- #
    def limit_social_media_template(self) -> None:
        id = self._get_new_habit_id()

        name = "Limit Social Media"

        minutes_per_day = self.collector.number_collector.collect_number(prompt="How many minutes of social media per day: ")
        description = f"Limit social media to {minutes_per_day} minutes daily."

        tags = [category := "Productivity"]

        habit = Habit(id=id, name=name, description=description, category=category, tags=tags, target_streak=TARGET, target_completions=TARGET)
        self._add_template_habit(habit=habit)

    # Learning

    # ------------------------------- Read Template ------------------------------ #
    def read_template(self) -> None:
        id = self._get_new_habit_id()

        name = "Read"

        minutes_per_day = self.collector.number_collector.collect_number("Number of minutes to read per day: ")
        description = f"Read for {minutes_per_day} minutes daily."

        tags = [category := "Learning"]

        habit = Habit(id=id, name=name, description=description, category=category, tags=tags, target_streak=TARGET, target_completions=TARGET)
        self._add_template_habit(habit)

    # -------------------------- Learn Language Template ------------------------- #
    def learn_language_template(self) -> None:
        id = self._get_new_habit_id()

        language = self.collector.string_collector.collect_non_blank("\nWhich language are you learning: ").title()
        name = f"Learn {language}"

        minutes_per_day = self.collector.number_collector.collect_number(prompt="How many minutes per day do you want to learn for: ")
        description = f"Learn {language} for {minutes_per_day} minutes per day."

        tags = [category := "Learning"]

        habit = Habit(id=id, name=name, description=description, category=category, tags=tags, target_streak=TARGET, target_completions=TARGET)
        self._add_template_habit(habit=habit)

    # Personal

    # ----------------------------- Make Bed Template ---------------------------- #
    def make_bed_template(self) -> None:
        id = self._get_new_habit_id()

        name = "Make Bed"
        description = "Make your Bed"
        tags = [category := "Personal"]

        habit = Habit(id=id, name=name, description=description, category=category, tags=tags, target_streak=TARGET, target_completions=TARGET)
        self._add_template_habit(habit=habit)

    # ----------------------------- Journal Template ----------------------------- #
    def journal_template(self) -> None:
        id = self._get_new_habit_id()

        name = "Journal"
        description = "Complete daily journaling"
        tags = [category := "Personal"]

        habit = Habit(id=id, name=name, description=description, category=category, tags=tags, target_streak=TARGET, target_completions=TARGET)
        self._add_template_habit(habit=habit)