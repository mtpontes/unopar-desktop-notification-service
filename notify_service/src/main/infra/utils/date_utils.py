from datetime import datetime

from src.main.domain.constants import DateConsts


class DateUtils:

    @staticmethod
    def to_datetime(data: str) -> datetime:
        return datetime.strptime(data, DateConsts.ISO_8601_PATTERN)

    @staticmethod
    def to_date_br_str(data: str) -> str:
        return datetime.strftime(data, DateConsts.BR_PATTERN)
