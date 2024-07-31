text = """
    Моделі Бази Даних (--model, -m): "Teacher", "Group", "Student", "Discipline", "Grade".
    Методи моделей (--action", -a): "create", "list", "update", "remove".
    
    --id - ід моделі в бд
    --name - імя моделі в бд Teacher/Group/Student/Discipline
    --grade - оцінка
    --teacher_id - де необхіний ід вчителя
    --group_id - де необхіний ід групи
    --student_id - де необхіний ід студента
    --discipline_id - де необхіний ід дисципліни

    ### Необхідні аргументи ### 
    Teacher:
        crete: --name
        update: --id, --name
        list:
        remove: --id
    Student:
        crete: --name, --group_id
        update: --id, --name(необов'язковий), --group_id(необов'язковий)
        list:
        remove: --id
    Group: 
        crete: --name
        update: --id, --name(необов'язковий)
        list:
        remove: --id
    Discipline:
        crete: --name, --teacher_id
        update: --id, --name(необов'язковий), --teacher_id(необов'язковий)
        list:
        remove: --id
    Grade:
        crete: --grade, --student_id, --discipline_id
        update: --id, --grade(необов'язковий), --student_id(необов'язковий), --discipline_id(необов'язковий)
        list:
        remove: --id
"""
