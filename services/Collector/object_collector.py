from enum import Enum

class ObjectCollector:
    # ---------------------------- Collect Enum Value ---------------------------- #
    def collect_enum_value(self, prompt: str, classname: Enum) -> Enum:
        """
        Ensures input is valid when converted to a given enum class

        :param prompt: Prompt to display to the user
        :param classname: Enum class for which input must be valid

        :return Enum: Enum value of inputed text
        """
        while True:
            try:
                return classname(input(prompt).lower())
            except ValueError:
                print("Invalid input.")


    # ------------------------------- Collect List ------------------------------- #
    def collect_list(self, prompt: str) -> list[str]:
        """
        Collects values from user and appends them to a list. User can break  by leaving value blank

        :param prompt: Prompt to be shown to the user when collecting values

        :return list[str]: List of values that were entered by the user
        """
        values = []

        while True:
            value = input(prompt).strip()
            if not value:
                break
            values.append(value)

        return values