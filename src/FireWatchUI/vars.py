from enum import Enum


class LogColumn(str, Enum):
    EventDate = 'Date of event'


class LogCategory(str, Enum):
    Training = 'Training *including Drill Night*'