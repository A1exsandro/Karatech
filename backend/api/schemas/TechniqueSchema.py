from pydantic import BaseModel

class TechniqueBase(BaseModel):
    name: str

class TechniqueCreate(TechniqueBase):
    pass

class TechniqueResponse(TechniqueBase):
    id: int

    class Config:
        orm_mode = True
