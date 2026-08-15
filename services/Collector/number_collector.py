class NumberCollector:
    # -------------------------------- Collect ID -------------------------------- #
    def collect_id(self) -> int:
        """
        Collects ID value from user

        :return int: ID value inputed by the user
        """
        while True:
            try:
                return int(input("\nEnter ID: ").strip())
            except ValueError:
                print("Enter a valid ID.")

    def collect_number_nullable(self, prompt) -> int | None:
        """
        Collects a number from user input or None if input is blank

        :param prompt: Prompt to be shown to user

        :return int: Numeric input provided by user
        :return None: Input provided by user was blank
        """
        while True:
            value = input(prompt).strip()

            if not value:
                return None

            try:
                return int(value)
            except ValueError:
                print("Enter a valid number.")