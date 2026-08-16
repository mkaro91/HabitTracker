from models.Habit import Habit
from models.HabitSearcher import HabitSearcher

from services.Collector import Collector

class SearchService:
    def __init__(self, habits: list[Habit]):
        self.search_engine = HabitSearcher(habits=habits)
        self.collector = Collector()

    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Helpers --------------------------------- #
    # ---------------------------------------------------------------------------- #
    def _display_results(self, results: list[Habit]) -> None:
        """
        Displays results if results found

        :param results: Results to be displayed
        """
        if not results:
            print("No results found.")
            return

        for result in results:
            print(result)

    # ---------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #

    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Methods --------------------------------- #
    # ---------------------------------------------------------------------------- #

    # ------------------------------ Search In Name ------------------------------ #
    def search_in_name(self) -> None:
        """
        Searches through habit's names and displays results
        """
        keyword = self.collector.string_collector.collect_keyword()
        results = self.search_engine.search_in_name(keyword=keyword)
        self._display_results(results=results)

    # --------------------------- Search In Description -------------------------- #
    def search_in_description(self) -> None:
        """
        Searches through habit's descriptions and displays results
        """
        keyword = self.collector.string_collector.collect_keyword()
        results = self.search_engine.search_in_description(keyword=keyword)
        self._display_results(results=results)

    # ---------------------------- Search In Category ---------------------------- #
    def search_in_category(self) -> None:
        """
        Searches through habit's categories ad displays results
        """
        keyword = self.collector.string_collector.collect_keyword()
        results = self.search_engine.search_in_category(keyword=keyword)
        self._display_results(results=results)

    # ---------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #