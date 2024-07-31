from sqlalchemy import func
from random import choice,randint
from src.db import session
from src.models import Student, Grade, Group, Teacher, Discipline
from seed import DISCIPLINES, TEACHER_COUNT, GROUPS, STUDENT_COUNT
from pprint import pprint


def select1():
    """Знайти 5 студентів із найбільшим середнім балом з усіх предметів"""
    top_students = (
        session.query(Student.fullname.label('name'), func.round(func.avg(Grade.grade),2).label('average_grade'))
        .join(Grade)
        .group_by(Student.id)
        .order_by(func.avg(Grade.grade).desc())
        .limit(5)
        .all()
        )
    return top_students


def select2(dscp_name = choice(DISCIPLINES)):
    """Знайти студента із найвищим середнім балом з певного предмета"""
    res = (
        session.query(Student.fullname.label('name'), func.round(func.avg(Grade.grade),2).label('average_grade'))
        .join(Grade)
        .join(Discipline)
        .filter(Discipline.name == dscp_name)
        .group_by(Student.id)
        .order_by(func.avg(Grade.grade).desc())
        .first()
    )
    if res:
        return res
    else:
        None


def select3(dscp_name = choice(DISCIPLINES)):
    """Знайти середній бал у групах з певного предмета."""
    res = (
        session.query(Group.name.label('group_name'), func.round(func.avg(Grade.grade), 2).label('average_grade'))
        .join(Student, Group.id == Student.group_id)
        .join(Grade, Student.id == Grade.student_id)
        .join(Discipline, Grade.discipline_id == Discipline.id)
        .filter(Discipline.name == dscp_name)
        .group_by(Group.id)
        .order_by(func.round(func.avg(Grade.grade), 2).desc())
        .all()
    )
    return res


def select4():
    """Знайти середній бал на потоці (по всій таблиці оцінок)"""
    res = session.query(func.round(func.avg(Grade.grade), 2).label('average_grade')).scalar()
    return res


def select5(tch_id = randint(1,TEACHER_COUNT)):
    """Знайти які курси читає певний викладач"""
    res= (
        session.query(Teacher.fullname, Discipline.name)
        .join(Teacher, Discipline.teacher_id == Teacher.id)
        .filter(Teacher.id == tch_id)
        .all()
    )
    return res


def select6(gr_nm=choice(GROUPS)):
    """Знайти список студентів у певній групі."""
    res =(
        session.query(Student.fullname)
        .join(Group, Student.group_id == Group.id)
        .filter(Group.name == gr_nm)
        .all()
    )
    return {gr_nm : res}


def select7(dscp_name=choice(DISCIPLINES), gr_name=choice(GROUPS)):
    """Знайти оцінки студентів у окремій групі з певного предмета"""
    res = (
        session.query(Discipline.name, Group.name, Student.fullname, Grade.grade)
        .join(Student, Grade.student_id == Student.id)
        .join(Group, Student.group_id == Group.id)
        .filter(Discipline.name == dscp_name)
        .filter(Group.name == gr_name)
        .all()
    )
    return res

def select8(tch_id = randint(1,TEACHER_COUNT)):
    """Знайти середній бал, який ставить певний викладач зі своїх предметів"""
    res = (
        session.query(func.round(func.avg(Grade.grade), 2))
        .join(Discipline, Grade.discipline_id == Discipline.id)
        .join(Teacher, Discipline.teacher_id == Teacher.id)
        .filter(Teacher.id == tch_id)
        .scalar()
    )
    return res


def select9(st_id = randint(1, STUDENT_COUNT)):
    """Знайти список курсів, які відвідує певний студент"""
    st = session.query(Student.fullname).filter(Student.id == st_id).one()
    res=(
        session.query(Discipline.name)
        .join(Grade, Discipline.id == Grade.discipline_id)
        .filter(Grade.student_id == st_id)
        .group_by(Discipline.id)
        .all()
    )
    return {st:res}

def select10(tch_id = randint(1, TEACHER_COUNT), st_id = randint(1, STUDENT_COUNT)):
    """Список курсів, які певному студенту читає певний викладач"""
    res =(
        session.query(Discipline.name)
        .join(Teacher, Discipline.teacher_id == Teacher.id)
        .join(Grade, Discipline.id == Grade.discipline_id)
        .join(Student, Grade.student_id == Student.id)
        .group_by(Discipline.id)
        .filter(Teacher.id == tch_id)
        .filter(Student.id == st_id)
        .all()
    )
    if res:
        return res
    return None

def select11(tch_id = randint(1, TEACHER_COUNT), st_id = randint(1, STUDENT_COUNT) ):
    """Середній бал, який певний викладач ставить певному студентові"""
    res =(
        session.query(func.round(func.avg(Grade.grade), 2))
        .join(Student, Grade.student_id == Student.id)
        .join(Discipline, Grade.discipline_id == Discipline.id)
        .join(Teacher, Discipline.teacher_id == Teacher.id)
        .filter(Teacher.id == tch_id)
        .filter(Student.id == st_id)
        .scalar()
    )
    return res

def select12(dscp_name = choice(DISCIPLINES), gr_name = choice(GROUPS)):
    """Оцінки студентів у певній групі з певного предмета на останньому занятті"""
    last_dt =(
         session.query(func.max(Grade.date_of))
         .join(Discipline, Grade.discipline_id == Discipline.id)
         .filter(Discipline.name == dscp_name)
         .scalar()
    )

    res = (
        session.query(Discipline.name, Grade.grade, Student.fullname, Group.name)
        .join(Discipline, Grade.discipline_id == Discipline.id)
        .join(Student, Grade.student_id == Student.id)
        .join(Group, Student.group_id == Group.id)
        .filter(Group.name == gr_name)
        .filter(Discipline.name == dscp_name)
        .filter(Grade.date_of == last_dt)
        .all()
    )
    if res:
        return res
    return None

if __name__=="__main__":
    funcs = [eval(f"select{i}()") for i in range(1,13)] 
    for func in funcs:
        print("#"*30)
        pprint(func)