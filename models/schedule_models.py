from typing import Optional
from sqlalchemy import ForeignKey, String, Enum
from sqlalchemy.orm import MappedAsDataclass, Mapped, mapped_column, relationship
from database import Model
import enum


class SubjectTypeEnum(enum.Enum):
    """Тип пары"""
    PRACTICE = "прак"
    LECTURE = "лек"
    LAB = "лаб"


class GroupModel(Model):
    """Таблица групп"""
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(primary_key=True)
    group_name: Mapped[str] = mapped_column(String(15))
    schedule_entries: Mapped[list["ScheduleModel"]] = relationship(back_populates="group")


class TeachersModel(Model):
    """Таблица учителей"""
    __tablename__ = "teachers"

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(100))
    schedule_entries: Mapped[list["ScheduleModel"]] = relationship(back_populates="teacher")


class ClassroomModel(Model):
    """Таблица аудиторий"""
    __tablename__ = "classrooms"

    id: Mapped[int] = mapped_column(primary_key=True)
    classroom_number: Mapped[str] = mapped_column(String(10))
    schedule_entries: Mapped[list["ScheduleModel"]] = relationship(back_populates="classroom")


class SubjectModel(Model):
    """Таблица предметов"""
    __tablename__ = "subjects"

    id: Mapped[int] = mapped_column(primary_key=True)
    subject_name: Mapped[str] = mapped_column(String(120))
    subject_type: Mapped[SubjectTypeEnum] = mapped_column(Enum(SubjectTypeEnum))
    schedule_entries: Mapped[list["ScheduleModel"]] = relationship(back_populates="subject")


class HolidaysModel(Model):
    """Таблица каникул"""
    __tablename__ = "holidays"

    id: Mapped[int] = mapped_column(primary_key=True)
    holiday_name: Mapped[str] = mapped_column(String(30))
    begin_end_date: Mapped[str] = mapped_column(String(6))
    is_active: Mapped[bool]
    schedule_entries: Mapped[list["ScheduleModel"]] = relationship(back_populates="holiday")


class ScheduleModel(Model):
    """Таблица расписания"""
    __tablename__ = "schedules"

    id: Mapped[int] = mapped_column(primary_key=True)
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"))
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teachers.id"))
    classroom_id: Mapped[int] = mapped_column(ForeignKey("classrooms.id"))
    subject_id: Mapped[int] = mapped_column(ForeignKey("subjects.id"))
    holiday_id: Mapped[int] = mapped_column(ForeignKey("holidays.id"))

    group: Mapped["GroupModel"] = relationship(back_populates="schedule_entries")
    teacher: Mapped["TeachersModel"] = relationship(back_populates="schedule_entries")
    classroom: Mapped["ClassroomModel"] = relationship(back_populates="schedule_entries")
    subject: Mapped["SubjectModel"] = relationship(back_populates="schedule_entries")
    holiday: Mapped[Optional["HolidaysModel"]] = relationship(back_populates="schedule_entries")