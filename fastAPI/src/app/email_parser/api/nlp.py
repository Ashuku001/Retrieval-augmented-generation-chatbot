from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from typing import Any
from pydantic import BaseModel

class EmailRequest(BaseModel):
    contact_info: dict
    body: str


router = APIRouter()

@router.post("/email_parser")
async def ner(request: Any = Body(...)):
    print(request)
    return {"status": "success", "data": request}