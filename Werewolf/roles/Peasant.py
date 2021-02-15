from Shared.enums.PlayerTypeEnum import PlayerTypeEnum;
from Werewolf.roles.RoleBase import RoleBase;

class Peasant(RoleBase):
    def __init__(self, name):
        super().__init__(name);

    @property
    def Role(self):
        return PlayerTypeEnum.Peasant;