from datetime import datetime

class DateCollector:
    def collect_date(self):
        """ Collects date value from user. If blank input returns None """
        due_date = input("Date: ").strip()
        
        # Modify Due Date
        return datetime.strptime(due_date, "%Y-%m-%d") if due_date else None