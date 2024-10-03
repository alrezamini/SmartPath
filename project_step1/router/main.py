from fastapi import APIRouter, Header, Body, \
    HTTPException, status
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

    lst = [x for x in input_body \
            if (x.BodyIdNumber.isdigit()) \
            and (number == int(x.BodyIdNumber)) \
            and (id == x.BodyId)]

    if lst:
        return lst

    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "not found",
    )