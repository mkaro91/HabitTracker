import json

from pathlib import Path

from models.HabitTracker import HabitTracker

DATA_DIR = Path('data')
DATA_DIR.mkdir(exist_ok=True)
SAVE_PATH = DATA_DIR/'habits.json'

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