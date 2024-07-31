import datetime
from typing import Optional, List
from sqlalchemy import select, String, Date, ForeignKey, Integer
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column, relationship
from src.db  import engine, session


Base = declarative_base()


class Teacher(Base):
    __tablename__ = 'teachers'
    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[str] = mapped_column(String)


class Group(Base):
    __tablename__ = 'groups'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)


class Student(Base):
    __tablename__ = 'students'
    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[str] = mapped_column(String)
    group_id: Mapped[int] = mapped_column(ForeignKey('groups.id', ondelete='CASCADE'))
    group: Mapped["Group"] = relationship('Group', backref='students')


class Discipline(Base):
    __tablename__ = "disciplines"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    teacher_id: Mapped[int] = mapped_column(ForeignKey('teachers.id', ondelete='CASCADE'))
    teacher: Mapped["Group"] = relationship('Teacher', backref='disciplines')


class Grade(Base):
    __tablename__ = "grades"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    grade: Mapped[int] = mapped_column(Integer)
    date_of: Mapped[Optional[datetime.date]] = mapped_column(Date, nullable=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id", ondelete='CASCADE'))
    discipline_id: Mapped[int] = mapped_column(ForeignKey("disciplines.id", ondelete='CASCADE'))
    student: Mapped["Student"] = relationship('Student', backref='grades')
    discipline: Mapped["Discipline"] = relationship('Discipline', backref='grades')


Base.metadata.create_all(engine)
