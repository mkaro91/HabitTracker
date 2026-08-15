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