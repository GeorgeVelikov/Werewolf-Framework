from Shared.utility.Helpers import nameof;
from Shared.exceptions.GameException import GameException;

from enum import Enum;

class TimeOfDayEnum(Enum):
    # Can't escape keywords in Python :(
    _None = 0;
    Day = 1;
    Night = 2;

    def __str__(self):
        if self.value == self._None.value:
            return str();
        elif self.value == self.Day.value:
            return nameof(self.Day);
        elif self.value == self.Night.value:
            return nameof(self.Night);
        else:
            raise GameException("Unknown turn cycle type used.");

    @staticmethod
    def FromString(string):
        if string == str(TimeOfDayEnum.Day):
            return TimeOfDayEnum.Day;
        elif string == str(TimeOfDayEnum.Night):
            return TimeOfDayEnum.Night;
        else:
            return TimeOfDayEnum._None;

    @staticmethod
    def Values():
        return [\
            TimeOfDayEnum.Day,\
            TimeOfDayEnum.Night];
