from storage import Storage

from models.HabitTracker import HabitTracker
from models.HabitStatistics import HabitStatistics
from models.Habit import Habit

from services import DateService, HabitService, HistoryService
from services.Collector import Collector

COLLECTOR = Collector()

def main():
    tracker = Storage().load()
    stats = HabitStatistics(habit_tracker=tracker)

    while True:
        print(f'\n{"=" * 40}')
        print("Habit Tracker".center(40))
        print("=" * 40)

        print("1. Daily Operations")
        print("2. Habit Operations")
        print("3. History Operations")
        print("0. Exit")

        choice = COLLECTOR.string_collector.collect_menu_choice()
        match choice:
            case "0": break

            case "1":
                services = DateService()

                while True:
                    print("\nDaily Operations".center(40))
                    print('-' * 40)

                    print("1. Complete Habit")
                    print("2. Uncomplete Habit")
                    print("3. Check if Habit Completed Today")
                    print("4. View Habits Completed Today")
                    print("5. View Habits Not Completed Today")
                    print("0. Return to Main Menu")

                    choice = COLLECTOR.string_collector.collect_menu_choice()
                    match choice:
                        case "0": break

                        case "1": services.complete_habit(tracker=tracker)
                        case "2": services.uncomplete_habit(tracker=tracker)
                        case "3": services.is_habit_completed_today(tracker=tracker)
                        case "4": services.view_habits_completed_today(stats=stats)
                        case "5": services.view_habits_incomplete_today(stats=stats)

                        case _: print("Invalid choice.")


            case "2":
                services = HabitService()

                while True:
                    print("\nHabit Operations".center(40))
                    print('-' * 40)

                    print("1. View All Habits")
                    print("2. Add New Habit")
                    print("3. Edit Habit")
                    print("4. Delete Habit")
                    print("0. Return to Main Menu")

                    choice = COLLECTOR.string_collector.collect_menu_choice()
                    match choice:
                        case "0": break

                        case "1": services.view_all_habits(tracker=tracker)
                        case "2": services.create_habit(tracker=tracker)
                        case "3": services.edit_habit(tracker=tracker)
                        case "4": services.delete_habit(tracker=tracker)

                        case _: print("Invalid choice.")

            case "3":
                services = HistoryService()

                while True:
                    print("\nHistory Operations".center(40))
                    print('-' * 40)

                    print("1. View Habit Completion History")
                    print("2. View Days Habit Completed")
                    print("3. View Days Habit Incomplete")
                    print("4. Lookup Date")
                    print("0. Return to Main Menu")

                    choice = COLLECTOR.string_collector.collect_menu_choice()
                    match choice:
                        case "0": break

                        case "1": services.view_completion_history(tracker=tracker)
                        case "2": services.view_days_completed(tracker=tracker)
                        case "3": services.view_days_not_completed(tracker=tracker)
                        case "4": services.lookup_date(tracker=tracker)

                        case _: print("Invalid choice.")

            case _: print("Invalid choice.")

if __name__ == "__main__":
    main()