from pydantic import BaseModel, EmailStr, Field

class SuccessMessage(BaseModel):
    success_message : str = Field(..., description="The success message")
    