from .string_collector import StringCollector
from .number_collector import NumberCollector
from .date_collector import DateCollector
from.object_collector import ObjectCollector

class Collector:
    def __init__(self):
        self.string_collector = StringCollector()
        self.number_collector = NumberCollector()
        self.date_collector = DateCollector()
        self.object_collector = ObjectCollector()