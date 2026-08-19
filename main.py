from storage import Storage

from models.HabitStatistics import HabitStatistics

from services import DateService, HabitService, HistoryService, StartupService, ArchiveService, SortingService, SearchService, TemplateService
from services.Collector import Collector

COLLECTOR = Collector()

def main():
    tracker = Storage().load()
    stats = HabitStatistics(habit_tracker=tracker)

    services = StartupService()
    services.reset_if_streak_broken(tracker=tracker)

    services.daily_dashboard(tracker=tracker, stats=stats)
    while True:
        print("\nMain Menu".center(40))
        print("=" * 40)
        print("1. Daily Operations")
        print("2. Habit Operations")
        print("3. History Operations")
        print("4. Archive Operations")
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

                    print("1. View Habits")
                    print("2. Habit Actions")
                    print("3. Sort Habits")
                    print("4. Search Habits")
                    print("0. Return to Main Menu")

                    choice = COLLECTOR.string_collector.collect_menu_choice()
                    match choice:
                        case "0": break

                        case "1": 
                            while True:
                                print("\nView Habits".center(40))
                                print('-' * 40)

                                print("1. View All Habits")
                                print("2. View Habit Goals")
                                print("3. View Habit Achievements")
                                print("0. Return to Habit Operartions")

                                choice = COLLECTOR.string_collector.collect_menu_choice()
                                match choice:
                                    case "0": break

                                    case "1": services.view_all_habits(tracker=tracker)
                                    case "2": services.view_habit_goals(tracker=tracker)
                                    case "3": services.view_habit_achievements(tracker=tracker)

                                    case _: print("Invalid choice")

                        case "2":
                            while True:
                                print("\nHabit Actions".center(40))
                                print('-' * 40)

                                print("1. Add New Habit")
                                print("2. Edit Habit")
                                print("3. Delete Habit")
                                print("0. Return to Habit Operations")

                                choice = COLLECTOR.string_collector.collect_menu_choice()
                                match choice:
                                    case "0": break 

                                    case "1": 
                                        print("\nAdd New Habit")
                                        print("-" * 40)

                                        print("1. Use Template")
                                        print("2. Create Custom")
                                        print("0. Cancel")

                                        choice = COLLECTOR.string_collector.collect_menu_choice()
                                        match choice:
                                            case "0": pass

                                            case "1":
                                                templates =  TemplateService(tracker=tracker)

                                                print("\nHabit Templates")
                                                print("-" * 40)

                                                print("1. Health Habits")
                                                print("2. Productivity Habits")
                                                print("3. Learning Habits")
                                                print("4. Personal Habits")
                                                print("0. Cancel")

                                                choice = COLLECTOR.string_collector.collect_menu_choice()
                                                match choice:
                                                    case "0": pass

                                                    case "1":
                                                        print("\nHealth Habits")
                                                        print('-' * 40)

                                                        print("1. Exercise")
                                                        print("2. Drink Water")
                                                        print("0. Cancel")

                                                        choice = COLLECTOR.string_collector.collect_menu_choice()
                                                        match choice:
                                                            case "0": pass

                                                            case "1": templates.exercise_template()
                                                            case "2": templates.drink_water_template()

                                                            case _: print("Invalid choice.")

                                                    case "2":
                                                        print("\nProductivity Habits")
                                                        print('-' * 40)

                                                        print("1. Check Email")
                                                        print("2. Limit Social Media")
                                                        print("0. Cancel")

                                                        choice = COLLECTOR.string_collector.collect_menu_choice()
                                                        match choice:
                                                            case "0": pass

                                                            case "1": templates.check_email_template()
                                                            case "2": templates.limit_social_media_template()

                                                            case _: print("Invalid choice.")

                                                    case "3": 
                                                        print("\nLearning Habits")
                                                        print("-" * 40)

                                                        print("1. Read")
                                                        print("2. Learn New Language")
                                                        print("0. Cancel")

                                                        choice = COLLECTOR.string_collector.collect_menu_choice()
                                                        match choice:
                                                            case "0": pass

                                                            case "1": templates.read_template()
                                                            case "2": templates.learn_language_template()

                                                            case _: print("Invalid choice.")

                                                    case "4":
                                                        print("\nPersonal Habits")
                                                        print("-" * 40)

                                                        print("1. Make Bed") 
                                                        print("2. Journal")
                                                        print("0. Cancel")

                                                        choice = COLLECTOR.string_collector.collect_menu_choice()
                                                        match choice:
                                                            case "0": pass

                                                            case "1": templates.make_bed_template()
                                                            case "2": templates.journal_template()

                                                            case _: print("Invalid choice.")

                                                    case _: print("Invalid choice.")


                                            case "2": services.create_habit(tracker=tracker)

                                            case _: print("Invalid choice.")

                                    case "2": services.edit_habit(tracker=tracker)
                                    case "3": services.delete_habit(tracker=tracker)

                                    case _: print("Invalid choice.")

                        case "3":
                            services = SortingService(habits=tracker.get_all_habits())

                            while True:
                                print("\nSort Habits".center(40))
                                print('-' * 40)

                                print("1. Sort by Name")
                                print("2. Sort by Streak")
                                print("3. Sort by Completion Rate")
                                print("4. Sort by Creation Date")
                                print("0. Return to Habit Operations")

                                choice = COLLECTOR.string_collector.collect_menu_choice()
                                match choice:
                                    case "0": break

                                    case "1": services.sort_by_name()
                                    case "2": services.sort_by_streak()
                                    case "3": services.sort_by_completion_rate()
                                    case "4": services.sort_by_creation_date()

                                    case _: print("Invalid choice.")

                        case "4":
                            services = SearchService(habits=tracker.get_all_habits())

                            while True:
                                print("\nSearch Habits".center(40))
                                print('-' * 40)

                                print("1. Search in Name")
                                print("2. Search in Description")
                                print("3. Search in Category")
                                print("0. Return to Habit Operations")

                                choice = COLLECTOR.string_collector.collect_menu_choice()
                                match choice:
                                    case "0": break

                                    case "1": services.search_in_name()
                                    case "2": services.search_in_description()
                                    case "3": services.search_in_category()

                                    case _: print("Invalid choice.")

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

            case "4":
                services = ArchiveService()

                while True:
                    print("\nArchive Operations".center(40))
                    print('-' * 40)

                    print("1. View Archived Habits")
                    print("2. Archive Habit")
                    print("3. Unarchive Habit")
                    print("0. Return to Main Menu")

                    choice = COLLECTOR.string_collector.collect_menu_choice()
                    match choice:
                        case "0": break

                        case "1": services.view_archived_habits()
                        case "2": services.archive_habit(tracker=tracker)
                        case "3": services.unarchive_habit(tracker=tracker)

                        case _: print("Invalid choice.")

            case _: print("Invalid choice.")

if __name__ == "__main__":
    main()