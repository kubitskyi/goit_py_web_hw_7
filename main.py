from sqlalchemy import func, desc, and_, distinct, select

from src.models import Teacher, Student, Discipline, Grade, Group
from src.db import session



def select_1():
    """Знайти 5 студентів із найбільшим середнім балом з усіх предметів."""

    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
            .select_from(Grade)\
            .join(Student)\
            .group_by(Student.id)\
            .order_by(desc('avg_grade'))\
            .limit(5)\
            .all()
    return result


def select_2():
    """Знайти студента із найвищим середнім балом з певного предмета."""

    subject_id = 6

    result = session.query(Student.fullname, Discipline.name,\
                            func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
            .select_from(Grade)\
            .join(Discipline)\
            .filter(Discipline.id == subject_id)\
            .group_by(Student.id, Discipline.name)\
            .order_by(func.avg(Grade.grade).desc())\
            .first()
    return result


def select_3():
    """Знайти середній бал у групах з певного предмета."""

    subject_id = 1 

    result = session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Group)\
        .join(Student, Group.id == Student.group_id)\
        .join(Grade, Student.id == Grade.student_id)\
        .join(Discipline, Grade.discipline_id == Discipline.id)\
        .filter(Discipline.id == subject_id)\
        .group_by(Group.name)\
        .order_by(Group.name)\
        .all()
    return result

def select_4():
    """Знайти середній бал на потоці (по всій таблиці оцінок)."""

    result = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')).scalar()
    return result


def select_5():
    """Знайти, які курси читає певний викладач"""
    teacher_id = 3

    result = session.query(Discipline.name).filter(Discipline.teacher_id == teacher_id).all()

    return result


def select_6():
    """Знайти список студентів у певній групі."""
    group_id = 3

    result = session.query(Student.fullname)\
        .filter(Student.group_id == group_id)\
        .all()

    return result


def select_7():
    """Знайти оцінки студентів в окремій групі з певного предмета."""
    group_id = 3
    discipline_id = 5

    result = session.query(Student.fullname, Grade.grade)\
        .join(Student, Grade.student_id == Student.id)\
        .join(Discipline, Grade.discipline_id == discipline_id)\
        .filter(Student.group_id == group_id, Discipline.id == discipline_id)\
        .all()

    return result


def select_8():
    """Знайти середній бал, який ставить певний викладач зі своїх предметів."""    
    teacher_id = 3
    

    result = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Discipline, Grade.discipline_id == Discipline.id)\
        .filter(Discipline.teacher_id == teacher_id)\
        .scalar()

    return result


def select_9():
    """Знайти список курсів, які відвідує певний студент."""
    student_id = 2

    result = session.query(Discipline.name)\
        .join(Grade, Discipline.id == Grade.discipline_id)\
        .filter(Grade.student_id == student_id)\
        .group_by(Discipline.id)\
        .all()

    return result


def select_10():
    """Знайти список курсів, які відвідує певний студент."""
    student_id = 1
    teacher_id = 1

    result = session.query(Discipline.name)\
        .join(Grade, Discipline.id == Grade.discipline_id)\
        .join(Student, Grade.student_id == Student.id)\
        .filter(Student.id == student_id, Discipline.teacher_id == teacher_id)\
        .all()

    return result


if __name__=='__main__':
    print(select_10())
        
