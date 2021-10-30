from pydantic import BaseModel

class GenericResponse(BaseModel):
    status: str
    status_display: str
    details: dict = None
