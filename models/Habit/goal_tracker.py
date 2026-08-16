class GoalTracker:
    def __init__(self, target_streak: int | None, target_completions: int | None):
        self.target_streak = target_streak
        self.target_completions = target_completions

    # ---------------------------------------------------------------------------- #
    # -------------------------------- Persistence ------------------------------- #
    # ---------------------------------------------------------------------------- #
    @classmethod
    def from_dict(cls, data):
        return cls(
            target_streak = data['target_streak'],
            target_completions = data['target_completions']
        )

    def to_dict(self):
        return {
            'target_streak': self.target_streak,
            'target_completions': self.target_completions
        }

    # ---------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #


    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Helpers --------------------------------- #
    # ---------------------------------------------------------------------------- #
    def _target_not_set(self, value) -> bool:
        return value == None

    # ---------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #


    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Methods --------------------------------- #
    # ---------------------------------------------------------------------------- #

    # ----------------------------- Target Streak Met ---------------------------- #
    def target_streak_met(self, current_streak: int) -> bool:
        if self._target_not_set(value=self.target_streak):
            return False
        
        return current_streak == self.target_streak

    # -------------------------- Target Completions Met -------------------------- #
    def target_completions_met(self, completion_count: int) -> bool:
        if self._target_not_set(value=self.target_completions):
            return False
        
        return completion_count == self.target_completions

    # ---------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #