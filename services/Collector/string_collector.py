from enum import Enum

class StringCollector:
    # ----------------------------- Collect Non-Blank ---------------------------- #
    def collect_non_blank(self, prompt: str) -> str:
        """
        Collects input from the user while ensuring input is not blank

        :params prompt: Prompt to display to user

        :return String: Input provided by the user
        """
        while True:
            value = input(prompt).strip()
            if value: return value
            print("Input cannot be blank.")


    # ---------------------------- Collect Menu Choice --------------------------- #
    def collect_menu_choice(self) -> str:
        """ 
        Collects a menu choice from the user 
        
        :return String: Menu choice provided by user
        """
        return self.collect_non_blank("\n> ")


    # ------------------------------ Collect Keyword ----------------------------- #
    def collect_keyword(self):
        """
        Collects a keyword term to be used in a search
        
        :return String: Keyword provided by the user
        """
        return self.collect_non_blank("\nKeyword: ")