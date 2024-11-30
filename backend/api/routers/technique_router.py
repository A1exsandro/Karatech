from fastapi import APIRouter, HTTPException
from repositories import TechniqueRepository
from schemas.TechniqueSchema import TechniqueCreate, TechniqueResponse

router = APIRouter(
    prefix="/techniques",
    tags=["Techniques"],
)

# CREATE
@router.post("/", response_model=TechniqueResponse)
async def create_technique(request_body: TechniqueCreate):
    return await TechniqueRepository.create(request_body)

# READ
@router.get("/", response_model=list[TechniqueResponse])
async def get_all_techniques():
    return await TechniqueRepository.get_all()

# UPDATE
@router.put("/{technique_id}", response_model=TechniqueResponse | dict)
async def update_technique(technique_id: int, request_body: TechniqueCreate):
    return await TechniqueRepository.update(technique_id, request_body)

# DELETE
@router.delete("/{technique_id}")
async def delete_technique(technique_id: int):
    return await TechniqueRepository.delete(technique_id)
    