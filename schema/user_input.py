from pydantic import BaseModel,Field
from typing import Annotated


class UserInput(BaseModel):
    age:Annotated[int,Field(...,lt=100,description="age of user")]
    income:Annotated[float,Field(...,gt=0,description="user salary in lpa")]
    loan:Annotated[float,Field(...,gt=0,description="loan amount")]

    