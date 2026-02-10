from pydantic import BaseModel, Field

# class SScheduleBase(BaseModel):
#     name_subject: str = Field(..., min_length=2, max_length=50, description="Name of educational subject")
#     subject_time: str = Field(..., min_length=1, max_length=30, description="Beginning and the end")
#     teacher: str = Field(..., min_length=10, max_length=80, description="Subject teacher")


# class SSchedule(SScheduleBase):
#     id: int


# class SScheduleAdd(SScheduleBase):
#     pass