from Werewolf.game.roles.Role import Role;
from Shared.enums.PlayerTypeEnum import PlayerTypeEnum;

class Seer(Role):
    def __init__(self):
        self.__canDivineTimes = 1;

    @property
    def Type(self):
        return PlayerTypeEnum.Seer;

    @property
    def HasDayAction(self):
        return True;

    @property
    def HasNightAction(self):
        return self.CanDivine;

    @property
    def CanDivine(self):
        return self.__canDivineTimes > 0;