import argparse
from crud import CRUDTeacher, CRUDGroup, CRUDStudent, CRUDDiscipline, CRUDGrade


parser = argparse.ArgumentParser(description="CLI for CRUD operations on models.")
parser.add_argument("--action", "-a", required=True, choices=["create", "list", "update", "remove"], help="CRUD action")
parser.add_argument("--model", "-m", required=True, choices=["Teacher", "Group", "Student", "Discipline", "Grade"], help="Model to perform action on")
parser.add_argument("--id", type=int, help="ID of the model instance")
parser.add_argument("--name", type=str, help="Name of the Teacher/Group/Student/Discipline")
parser.add_argument("--grade", type=int, help="Grade")
parser.add_argument("--teacher_id", type=int, help="Teacher ID")
parser.add_argument("--group_id", type=int, help="Group ID")
parser.add_argument("--student_id", type=int, help="Student ID")
parser.add_argument("--discipline_id", type=int, help="Discipline ID")

args = parser.parse_args()

def main(args):
    func = eval("CRUD" + args.model.capitalize() + "." + args.action)
    print(func)
    self = eval("CRUD" + args.model.capitalize()+"()")
    args_dict = vars(args)
    res = func(self,args_dict)
    self.close()
    return res

print(main(args))