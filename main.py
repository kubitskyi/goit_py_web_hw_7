import argparse
from crud import CRUDTeacher, CRUDGroup, CRUDStudent, CRUDDiscipline, CRUDGrade
from description import text


parser = argparse.ArgumentParser(description=print(text))
parser.add_argument("--action", "-a", required=True, choices=["create", "list", "update", "remove"])
parser.add_argument("--model", "-m", required=True, choices=["Teacher", "Group", "Student", "Discipline", "Grade"])
parser.add_argument("--id", type=int)
parser.add_argument("--name", type=str)
parser.add_argument("--grade", type=int)
parser.add_argument("--teacher_id", type=int)
parser.add_argument("--group_id", type=int)
parser.add_argument("--student_id", type=int)
parser.add_argument("--discipline_id", type=int)

args = parser.parse_args()

def main(args):
    func = eval("CRUD" + args.model.capitalize() + "." + args.action)
    print(func)
    model = eval("CRUD" + args.model.capitalize()+"()")
    args_dict = vars(args)
    res = func(model,args_dict)
    model.close()
    return res

print(main(args))