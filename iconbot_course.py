from iconservice import *
    #importation des param
from parms import *
    #importation des valeurs de mon iconbot
from mon_icon_bot import *

TAG = 'iconbot'

class iconbot(IconScoreBase):

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self.iconbot_name(VarDB,str) = VarDB('iconbot_name', db, value_type=str)
        self.iconbot_skinId(VarDB,int) = VarDB('iconbot_skinId', db, value_type=int)
        self.iconbot_maxEnergy(VarDB,int) = VarDB('iconbot_maxEnergy', db, value_type=int)

    def on_install(self) -> None:
        super().on_install()
        self.iconbot_name.set(botName)
        self.iconbot_skinId.set(skinId)
        self.iconbot_maxEnergy.set(MAX_ENERGY)

    def on_update(self, db: IconScoreDatabase) -> None:
        super().on_update()

    @external
    @payable
    def contribute(self) -> str:
        if self.msg.value >= 10000000000000000000:
            return 'Thanks I''l use these ICX to contribute to the ecosystem.'
        else:
            revert('Oops! Your payment is insufficient')
