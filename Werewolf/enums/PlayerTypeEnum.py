from enum import Enum;
from utility.Helpers import nameof;

class PlayerTypeEnum(Enum):
    # Can't escape keywords in Python :(
    _None = 0;
    Peasant = 1;
    Werewolf = 2;
    Seer = 3;
    Doctor = 4;

    def __str__(self):
        if self.value == self._None.value:
            return str();
        elif self.value == self.Peasant.value:
            return nameof(self.Peasant);
        elif self.value == self.Werewolf.value:
            return nameof(self.Werewolf);
        elif self.value == self.Seer.value:
            return nameof(self.Seer);
        elif self.value == self.Doctor.value:
            return nameof(self.Doctor);
        else:
            raise Exception("Unknown player type used.");

    def Values():
        return [\
            PlayerTypeEnum.Peasant,\
            PlayerTypeEnum.Werewolf,\
            PlayerTypeEnum.Seer,\
            PlayerTypeEnum.Doctor];