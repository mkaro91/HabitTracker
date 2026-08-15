import json

from pathlib import Path

from models.Habit import Habit
from models.HabitTracker import HabitTracker

DATA_DIR = Path('data')
DATA_DIR.mkdir(exist_ok=True)
SAVE_PATH = DATA_DIR/'habits.json'
ARCHIVE_PATH = DATA_DIR / 'archived.json'

class Storage:
    """ JSON Storage Class """
    def save(self, tracker: HabitTracker) -> None:
        """
        Saves Habit Tracker to JSON file

        :param tracker: Habit Tracker Object to be saved
        """
        with open(SAVE_PATH, 'w') as f:
            json.dump(obj=tracker.to_dict(), fp=f, indent=4)

    def load(self) -> HabitTracker:
        """
        Loads Habit Tracker object from JSON file

        :return HabitTracker: HabitTracker object loaded from file
        """
        try:
            with open(file=SAVE_PATH, mode='r') as f:
                return HabitTracker.from_dict(json.load(f))
        except (FileNotFoundError, json.JSONDecodeError):
            return HabitTracker()

    def load_archive(self):
        try:
            with open(file=ARCHIVE_PATH, mode='r') as f:
                return [Habit.from_dict(habit) for habit in json.load(f)]
        except (FileNotFoundError, json.JSONDecodeError):
            return[]

    def save_archive(self, archived_habits: list[Habit]):
        data = [habit.to_dict() for habit in archived_habits]
        with open(file=ARCHIVE_PATH, mode='w') as f:
            json.dump(obj=data, fp=f, indent=4)