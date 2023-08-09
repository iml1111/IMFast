from pydantic import BaseModel, field_validator


class Champion(BaseModel):
    name: str
    role: str
    health: int
    affiliation: str

    @field_validator('role')
    def role_validator(cls, v):
        if v not in ('Tank', 'Damage', 'Support'):
            raise ValueError(
                'role must be one of Tank, Damage, Support')
        return v


class ChampionCreated(BaseModel):
    """Champion Create Model(Output)"""
    name: str
