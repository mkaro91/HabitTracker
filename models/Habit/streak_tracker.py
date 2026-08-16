class StreakTracker:
    """ Class to track streak related attributes """
    def __init__(self):
        self.streak: int = 0
        self.max_streak: int = 0

    # ---------------------------------------------------------------------------- #
    # -------------------------------- Persistence ------------------------------- #
    # ---------------------------------------------------------------------------- #
    @classmethod
    def from_dict(cls, data):
        tracker = cls()
        tracker.streak = data['streak']
        tracker.max_streak = data['max_streak']
        return tracker

    def to_dict(self):
        return {
            'streak': self.streak,
            'max_streak': self.max_streak
        }

    # ---------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #


    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Helpers --------------------------------- #
    # ---------------------------------------------------------------------------- #
    def _check_if_new_max(self) -> bool:
        """
        Compares current streak to current max streak

        :return True: Current streak is greater than current max streak
        :return False: Current streak is less than or equal to current max streak
        """
        return self.streak > self.max_streak

    def _set_new_max(self) -> None:
        """
        Sets max streak to current streak
        """
        self.max_streak = self.streak

    # ---------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #


    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Methods --------------------------------- #
    # ---------------------------------------------------------------------------- #

    # ------------------------------ Increase Streak ----------------------------- #
    def increase_streak(self) -> None:
        """
        Increase streak value by one and check for max streak reset
        """
        self.streak += 1

        if self._check_if_new_max():
            self._set_new_max()

    # ------------------------------ Decrease Streak ----------------------------- #
    def decrease_streak(self) -> None:
        """
        Decrease streak value by one while ensuring streak never falls below zero
        """
        new_streak = self.streak - 1
        self.streak = max(0, new_streak)

    # ------------------------------- Reset Streak ------------------------------- #
    def reset_streak(self) -> None:
        """
        Resets the current streak value to zero
        """
        self.streak = 0

    # ---------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #