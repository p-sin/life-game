from pydantic import BaseModel


class CardStat(BaseModel):
    board_section: int
    attribute: str
    value: int
