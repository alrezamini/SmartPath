from fastapi import APIRouter, Header, Body, \
    HTTPException, status
from typing import Annotated
from pydantic import BaseModel

# instance of APIRouter (it is imported in main.py located in project_step1 directory)
router = APIRouter()


class BodyInput(BaseModel):
    BodyId: str
    BodyIdNumber: str
    name: str


@router.post("/test/{number}",status_code= status.HTTP_200_OK)
def test(
    number: int,
    id: Annotated[str, Header()],
    input_body: Annotated[list[BodyInput], Body()]
):
    """
        it returns list of objects if match the conditions (number==BodyIdNumber and id==BodyId). 
        it raises exception if none of the objects match the conditions 
    """

    # list comprehension which loops through the input_body and filters the objects of list
    lst = [x for x in input_body \
            if (x.BodyIdNumber.isdigit()) \
            and (number == int(x.BodyIdNumber)) \
            and (id == x.BodyId)]

    # if lst is not empty then return the list which contains objects
    if lst:
        return lst

    # if lst is empty then raise exception
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "not found",
    )