from sqlalchemy import select
from random import choice, randint
from datetime import date, datetime, timedelta
import faker
from src.models import Teacher, Group, Discipline, Student, Grade
from src.db import session


EDUCATION_START = datetime.strptime("2023-09-01", "%Y-%m-%d")
EDUCATION_END = datetime.strptime("2024-05-30", "%Y-%m-%d")
STUDENT_COUNT = 50
TEACHER_COUNT = 4
GROUPS = ["Ґрифіндор", "Гафелпаф", "Рейвенклов","Слизерин"]
DISCIPLINES = [
            "Історія магії",
            "Захист від темних мистецтв",   
            "Трансфігурація",
            "Зіллєваріння",
            "Маглознавство",
            "Догляд за магічними тваринами",
            "Літання на мітлах",
            "Закляття"
        ]


fake = faker.Faker()


def date_range(start: date, end: date) -> list:
    result = []
    current_date = start
    while current_date <= end:
        if current_date.isoweekday() < 6:
            result.append(current_date)
        current_date += timedelta(1)
    return result

def create_teachers(session):
    for _ in range(TEACHER_COUNT):
        teacher = Teacher(fullname = fake.name())
        session.add(teacher)
    session.commit()
    print("Add teachers complite")


def create_groups(session):
    for grp in GROUPS:
        group = Group(name = grp)
        session.add(group)
    session.commit()
    print("Add groups complite")

def create_disciplines(session):
    teachers_id = session.execute(select(Teacher.id)).scalars().all()
    for dscp in DISCIPLINES:
        discipline = Discipline(
            name = dscp,
            teacher_id = choice(teachers_id)
        )
        session.add(discipline)
    session.commit()
    print("Add disciplines complite")


def create_students(session):
    groups_id = session.execute(select(Group.id)).scalars().all()
    for _ in range(STUDENT_COUNT + 1):
        student = Student(
            fullname = fake.name(),
            group_id = choice(groups_id)
        )
        session.add(student)

    session.commit()
    print("Add students complite")


def create_grades(session):
    start_date = EDUCATION_START
    end_date = EDUCATION_END
    date_ranges = date_range(start_date,end_date)
    students_id = session.execute(select(Student.id)).scalars().all()
    disciplines_id = session.execute(select(Discipline.id)).scalars().all()

    for dt in date_ranges:
        random_disciplinen_id =  choice(disciplines_id)
        random_students_id = [choice(students_id) for _ in range(1,6)]
        for st in random_students_id:
            grade = Grade(
                grade = randint(1,5),
                date_of = dt.date(),
                student_id = st,
                discipline_id = random_disciplinen_id
            )
            session.add(grade)

        session.commit()
    print("Add grades complite")


def fill_data(session):
    create_teachers(session)
    create_groups(session)
    create_disciplines(session)
    create_students(session)
    create_grades(session)
   
    

if __name__ == "__main__":
    fill_data(session)