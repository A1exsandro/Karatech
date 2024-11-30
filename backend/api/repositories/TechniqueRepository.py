from database import db
from models.TechniqueModel import Technique
from schemas.TechniqueSchema import TechniqueCreate
from sqlalchemy.future import select


# C CREATE
async def create(request_body: TechniqueCreate):
    new_technique = Technique(name=request_body.name)
    db.add(new_technique)
    await db.commit()
    db.refresh(new_technique)
    return new_technique

# R READ
async def get_all():
    query = select(Technique)
    result = await db.execute(query)
    return result.scalars().all()
   

# U UPDATE
async def update(technique_id: int, request_body: TechniqueCreate):
    query = await db.get(Technique, technique_id)
    if not query:
        return {"message": "Technique not found"}
    else:
        query.name = request_body.name
        await db.commit()
        return query

# D DELETE
async def delete(technique_id: int):
    technique = await db.get(Technique, technique_id)
    if not technique:
        return {"message": "Technique not found"}
    await db.delete(technique)
    await db.commit()
    return {"message": "Technique deleted successfully"}
