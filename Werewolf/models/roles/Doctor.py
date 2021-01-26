from enums.WerewolfPlayerTypeEnum import WerewolfPlayerTypeEnum;
from models.roles.RoleBase import RoleBase;

class Doctor(RoleBase):
    def __init__(self):
        super().__init__(WerewolfPlayerTypeEnum.Doctor)