from abc import ABC, abstractmethod
from datetime import datetime
from sqlalchemy import func
from src.db import session
from src.models import Student, Grade, Group, Teacher, Discipline

class CRUD(ABC):
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def list(self):
        pass
    
    @abstractmethod
    def remove(self):
        pass


class CRUDTeacher(CRUD):
    def __init__(self):
        self.session = session

    def create(self, args):
        name = args.get('name')
        if name == None:
            return f"--name is required argument"
        new_teacher = Teacher(fullname = name)
        self.session.add(new_teacher)
        self.session.commit()
        return f"Teacher {name} create with id: {new_teacher.id}."
    
    def update(self, args):
        id = args.get('id')
        name = args.get('name')
        if name == None:
            return f"--name is required argument"
        
        teacher = self.session.query(Teacher).filter(Teacher.id == id).first()
        if teacher:
            teacher.fullname = name
            self.session.commit()
            return f"Teacher with ID {id} updated to '{name}'."
        else:
            return f"Teacher with ID {id} not found."


    def list(self,args):
        return self.session.query(Teacher.fullname).all()
        

    def remove(self,args):
        id = args.get('id')
        teacher = self.session.query(Teacher).filter(Teacher.id == id).first()
        if teacher:
            self.session.delete(teacher)
            self.session.commit()
            return f"Teacher with ID {id} removed."
        else:
            return f"Teacher with ID {id} not found."

    def close(self):
        self.session.close()

class CRUDGroup(CRUD):
    def __init__(self) -> None:
        self.session = session

    def create(self, args):
        name = args.get('name')
        new_group = Group(name = name)
        self.session.add(new_group)
        self.session.commit()
        return f"Group {name} create with id: {new_group.id}."
    
    def update(self, args):
        name = args.get('name')
        group_id = args.get('group_id')

        group = self.session.query(Group).filter(Group.id == group_id).first()
        if group:
            group.name = name
            self.session.commit()
            return f"Group with ID {group_id} updated to '{name}'."
        else:
            return f"Group with ID {group_id} not found."

    def list(self, args):
        return self.session.query(Group.name).all()
        
    def remove(self,args):
        group_id = args.get('group_id')
        group = self.session.query(Group).filter(Group.id == group_id).first()
        if group:
            self.session.delete(group)
            self.session.commit()
            return f"Group with ID {group_id} removed."
        else:
            return f"Group with ID {group_id} not found."

    def close(self):
        self.session.close()

class CRUDStudent(CRUD):
    def __init__(self) -> None:
        self.session = session
    
    def create(self, args):
        name = args.get("name")
        if name == None:
            return f"--name is required argument"
        group_id = args.get('group_id')
        if group_id == None:
            return f"--group_id is required argument"
        
        new_student = Student(fullname = name, group_id = group_id)
        self.session.add(new_student)
        self.session.commit()
        return f"Srudent {name} group - {new_student.group} create with id: {new_student.id}."

    def list(self, args):
        return self.session.query(Student.fullname, Student.id).all()
    
    def update(self, args):
        id = args.get("id")
        if id == None:
            return f"--шd is required argument"
        name = args.get("name")
        group_id = args.get("group_id")
        if name == None:
            name = self.session.query(Student.fullname).filter(Student.id == id).scalar()
        if group_id == None:
            group_id = self.session.query(Student.group_id).filter(Student.id == id).scalar()
        
        group_name = self.session.query(Group.name).filter(Group.id == group_id).scalar()

        student = self.session.query(Student).filter(Student.id == id).first()
        if student:
            student.fullname = name
            gr = session.query(Group).filter(Group.id == group_id).scalar()
            if gr:
                student.group_id = group_id
            else:
                return f"Group with ID{group_id} not found"
            self.session.commit()
            return f"Student with ID {id} updated to '{name}' from '{group_name}'."
        else:
            return f"Student with ID {id} updated not found"
    
    def remove(self, args):
        id = args.get("id")
        student = self.session.query(Student).filter(Student.id == id).first()
        if student:
            self.session.delete(student)
            self.session.commit()
            return f"Student with ID {id} removed."
        else:
            return f"Student with ID {id} not found."

    def close(self):
        self.session.close()


class CRUDDiscipline(CRUD):
    def __init__(self) -> None:
        self.session = session
    
    def create(self, name, teacher_id):
        new_discipline = Discipline(name = name, teacher_id = teacher_id)
        teacher = self.session.query(Teacher).filter(Teacher.id == teacher_id).one()
        self.session.add(new_discipline)
        self.session.commit()
        return f"Discipline {name} with teachr { teacher.fullname} create with id: {new_discipline.id}."

    def list(self):
        return self.session.query(Discipline.name).all()
    
    def update(self, args):
        id = args.get("id")
        if id == None:
            return f"--id is required argument"
        
        name = args.get("name")
        tch_id = args.get("teacher_id")

        if name == None:
            name = self.session.query(Discipline.name).filter(Discipline.id == id).scalar()
        if tch_id == None:
            tch_id = self.session.query(Discipline.teacher_id).filter(Discipline.id == id).scalar()
    
        teacher = session.query(Teacher).filter(Teacher.id == tch_id).scalar()
        if not teacher:
            return f"Teacher wiht id{tch_id} not found"
        
        discipline = self.session.query(Discipline).filter(Discipline.id == id).first()
        if discipline:
            discipline.name = name
            discipline.teacher_id = tch_id
            self.session.commit()
            return f"Discipline with ID {id} updated to '{name}' from teachr '{teacher.fullname}'."
        else:
            return f"Discipline with ID {id} updated not found"


    def remove(self,args):
        id = args.get("id")
        if id == None:
            return f"--id is required argument"
        discipline = self.session.query(Discipline).filter(Discipline.id == id).first()
        if discipline:
            self.session.delete(discipline)
            self.session.commit()
            return f"Discipline with ID {id} removed."
        else:
            return f"Discipline with ID {id} not found."


class CRUDGrade(CRUD):
    def __init__(self) -> None:
        self.session = session
    
    def create(self,args):
        grade = args.get("grade")
        st_id = args.get("student_id")
        dscp_id = args.get("discipline_id")

        if grade == None:
            return f"--grade is required argument"
        if st_id == None:
            return f"--student_id is required argument"
        if dscp_id == None:
            return f"--discipline_id is required argument"

        new_grade = Grade(
            grade = grade,
            date_of = datetime.today().strftime("%Y-%m-%d"),
            student_id = st_id,
            discipline_id = dscp_id
        )
        self.session.add(new_grade)
        self.session.commit()
        return f"Grade {grade} to student id: {st_id} with discipline id {dscp_id}."

    def list(self, args):
        return self.session.query(Grade.id, Grade.grade).all()

    def update(self, args):
        st_id = args.get("student_id")
        dscp_id = args.get("discipline_id")
        gr = args.get("grade")
        id = args.get('id')
        if gr == None:
            return f"--grade is required argument"
        if id == None:
            return f"--id is required argument"


        if st_id == None:
            st_id = self.session.query(Grade.student_id).filter(Grade.id == id).scalar()
        if dscp_id == None:
            dscp_id = self.session.query(Grade.discipline_id).filter(Grade.id == id).scalar()

        grade = self.session.query(Grade).filter(Grade.id == id).first()
        if grade:
            grade.grade = gr
            grade.discipline_id = dscp_id
            grade.student_id = st_id
            self.session.commit()
            return f"Grade with ID {id} updated to '{gr}' from discipline id '{dscp_id}' to student id'{st_id}'."
        else:
            return f"Grade with ID {id} updated not found"

    def remove(self, args):
        id = args.get("id")
        if id == None:
            return f"--id is required argument"
        
        grade = self.session.query(Grade).filter(Grade.id == id).first()
        if grade:
            self.session.delete(grade)
            self.session.commit()
            return f"Grade with ID {id} removed."
        else:
            return f"Grade with ID {id} not found."

    def close(self):
        self.session.close()

if __name__=="__main__":
    # crud = CRUDGrade()
    # print(crud.remove(id=976))
    # print(crud.list()[-10:])
   pass