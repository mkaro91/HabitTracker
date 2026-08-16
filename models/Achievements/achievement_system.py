from .achievement import Achievement

ACHIEVEMENT_POINTS = [1, 7, 30, 60, 100, 365]

class AchievementSystem:
    def __init__(self):
        self.achievements: list[Achievement] = []
        self.streak_achievements_remaining: list[int] = ACHIEVEMENT_POINTS
        self.completion_achievements_remaining: list[int] = ACHIEVEMENT_POINTS


    # ---------------------------------------------------------------------------- #
    # -------------------------------- Persistence ------------------------------- #
    # ---------------------------------------------------------------------------- #
    @classmethod
    def from_dict(cls, data):
        system = cls()

        system.achievements = [Achievement.from_dict(achievement) for achievement in data['achievements']]
        system.streak_achievements_remaining = data['streak_achievements_remaining']
        system.completion_achievements_remaining = data['completion_achievements_remaining']

        return system

    def to_dict(self):
        return {
            'achievements': [achievement.to_dict() for achievement in self.achievements],
            'streak_achievements_remaining': self.streak_achievements_remaining,
            'completion_achievements_remaining': self.completion_achievements_remaining
        }


    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Methods --------------------------------- #
    # ---------------------------------------------------------------------------- #

    # -------------------------- Get Latest Achievement -------------------------- #
    def get_lastest_achievement(self) -> Achievement | None:
        """
        Returns the most recently added achievement

        :return Achievement: Last recorded achievement
        :return None: No achievements recorded
        """
        if not self.achievements:
            return None
        return self.achievements[-1]

    # ------------------------------ Add Achievement ----------------------------- #
    def add_achievement(self, achievement: Achievement) -> None:
        """
        Adds an achievement object to the system

        :param achievement: Achievement object to be added to system
        """
        self.achievements.append(achievement)


    # ---------------------------- Streak Achievements --------------------------- #
    # ---------------------------------------------------------------------------- #

    # ------------------- Current Streak in Streak Achievements ------------------ #
    def current_streak_in_streak_achievements(self, current_streak: int) -> bool:
        """
        Returns whether the provided current streak is found in streak achievements remaining

        :param current_streak: Current streak value

        :return True: Current streak value found in streak achievements remaining
        :return False: Current streak value not found in streak achievements remaining
        """
        is_streak_in_remaining = current_streak in self.streak_achievements_remaining

        return is_streak_in_remaining

    # ----------------- Remove From Remaining Streak Achievements ---------------- #
    def remove_from_remaining_streak_achievements(self, current_streak: int) -> None:
        """
        Removes the current streak value from streak achievements remaining

        :param current_streak: Value to be removed
        """
        self.streak_achievements_remaining.remove(current_streak)

    # --------------------- Create and Add Streak Achievement -------------------- #
    def create_and_add_streak_achievement(self, current_streak: int) -> None:
        match current_streak:
            case 1:
                achievement = Achievement(name="Fresh Streak", description="Started a fresh streak for the first time.")
            case 7:
                achievement = Achievement(name="One Week Streak", description="Accomplished a 7 day streak for the first time.")
            case 30:
                achievement = Achievement(name="All Month Long", description="Accomplished a 30 day streak for the first time.")
            case 60:
                achievement = Achievement(name="60 Day Journey", description="Accomplished a 60 day streak for the first time.")
            case 100:
                achievement = Achievement(name="Century Mark", description="Accomplish a 100 day streak for the first time")
            case 365:
                achievement = Achievement(name="One Year Marathon", description="Accomplished an incredible 365 day streak for the first time.")

        self.add_achievement(achievement=achievement)


    # -------------------------- Completion Achievements ------------------------- #
    # ---------------------------------------------------------------------------- #

    # ----------- Completion Count in Completion Achievements Remaining ---------- #
    def completion_count_in_completion_achievements_remaining(self, completion_count: int) -> bool:
        is_count_in_remaining = completion_count in self.completion_achievements_remaining

        return is_count_in_remaining

    # --------------- Remove From Remaining Completion Achievements -------------- #
    def remove_from_remaining_completion_achievements(self, completion_count: int) -> None:
        self.completion_achievements_remaining.remove(completion_count)

    # ------------------- Create and Add Completion Achievement ------------------ #
    def create_and_add_completion_achievement(self, completion_count: int) -> None:
        match completion_count:
            case 1:
                achievement = Achievement(name="First Time!", description="Complete Habit for the first time")
            case 7:
                achievement = Achievement(name="Week's Worth", description="Complete Habit 7 times.")
            case 30:
                achievement = Achievement(name="One Month Grind", description="Complete Habit 30 times.")
            case 60:
                achievement = Achievement(name="DuoMonthly", description="Complete Habit 60 times")
            case 100:
                achievement = Achievement(name="100 Miles", description="Complete Habit 100 times")
            case 365:
                achievement = Achievement(name="Long Year", description="Complete Habit 365 times.")

        self.add_achievement(achievement=achievement)

    # ---------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #