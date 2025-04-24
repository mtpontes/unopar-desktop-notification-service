from datetime import datetime

from src.main.domain.contants import DateConsts


class DateUtils:
    @staticmethod
    def to_iso_8601(date_str: str, hour: int = 0, minute: int = 0, second: int = 0) -> str:
        return datetime \
                .strptime(date_str, DateConsts.BR_REDUZIDO_PATTERN) \
                .replace(hour=hour, minute=minute, second=second) \
                .isoformat()
