from fastapi import APIRouter, Header, Body
from typing import Annotated
from pydantic import BaseModel


router = APIRouter()


class BodyInput(BaseModel):
    BodyId: str
    BodyIdNumber: str
    name: str


@router.post("/test/{number}")
def test(
    number: int,
    id: Annotated[str, Header()],
    input_body: Annotated[list[BodyInput], Body()]
):
    return input_body