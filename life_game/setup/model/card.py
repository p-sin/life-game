from pydantic import BaseModel

from life_game.setup.model.card_stat import CardStat


class Card(BaseModel):
    section_1: CardStat
    section_2: CardStat
    section_3: CardStat
