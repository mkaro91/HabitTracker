from models.Habit import Habit

class HabitSearcher:
    """ Class used to search through Habits """
    def __init__(self, habits: list[Habit]):
        self.habits = habits

    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Methods --------------------------------- #
    # ---------------------------------------------------------------------------- #

    # ------------------------------ Search In Name ------------------------------ #
    def search_in_name(self, keyword) -> list[Habit]:
        """
        Searches each habit's name to see if it contains given keyword

        :param keyword: Search term

        :return list[Habit]: List of habits where name contains search term
        """
        results = [habit for habit in self.habits if keyword.lower() in habit.name.lower()]
        return results

    # --------------------------- Search In Description -------------------------- #
    def search_in_description(self, keyword) -> list[Habit]:
        """
        Searches each habit's description to see if it contains given keyword

        :param keyword: Search term

        :return list[Habit]: List of habits where description contains search term
        """
        results = [habit for habit in self.habits if keyword.lower() in habit.description.lower()]
        return results

    # ---------------------------- Search In Category ---------------------------- #
    def search_in_category(self, keyword) -> list[Habit]:
        """
        Searches each habit's cateory to see if it contains given keyword

        :param keyword: Search term

        :return list[Habit]: List of habits where category contains search term
        """
        results = [habit for habit in self.habits if keyword.lower() in habit.category.lower()]
        return results

    # ---------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #