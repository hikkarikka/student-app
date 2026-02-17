"""
Docstring for main
"""

def find_student(students, name):
    """
    Docstring for find_student
    
    :param students: Description
    :param name: Description
    """
    for student in students:
        if student["name"].lower() == name.lower():
            return student
    return None



def menu():
    """
    Docstring for menu
    """
    print("\n--- Меню ---")
    print("1. добавить студента")
    print("2. добавить оценку")
    print("3.показать всех студентов")
    print("4.удалить студента")
    print("5.показать лучшего студента")
    print("6.выйти")

def add_student(students):
    """
    Docstring for add_student
    
    :param students: Description
    """
    name = input("введите имя: ")
    age = int(input("введите возраст студента: "))

    if find_student(students, name):
        print("студент с таким именем уже существует")
        return

    students.append({
        "name": name,
        "age": age,
        "grades": []
    })

def add_grade(students):
    """
    Docstring for add_grade
    
    :param students: Description
    """
    name = input("введите имя студента: ")

    student = find_student(students, name)
    if not student:
        print("Студент не найден")
        return

    grade = float(input("введите оценку студента: "))
    if 0 <= grade <= 100:
        student["grades"].append(grade)
        print("оценка добавлена.")
    else:
        print("оценка должна быть от 0 до 100")


def show_students(students):
    """
    Docstring for show_students
    
    :param students: Description
    """
    if not students:
        print("не")
        return
    for student in students:
        print(f"имя: {student['name']}, возраст: {student['age']}, Оценки: {student['grades']}")

def delete_student(students):
    """
    Docstring for delete_student
    
    :param students: Description
    """
    name = input("введите имя студента: ")
    student = find_student(students, name)
    if not student:
        print("студент не найден.")
        return
    students.remove(student)
    print("студент удален из списка")

def calculate_average(grades):
    """
    Docstring for calculate_average
    
    :param grades: Description
    """
    if not grades:
        return 0
    return sum(grades)/ len(grades)

def best_student(students):
    """
    Docstring for best_student
    
    :param students: Description
    """
    if not students:
        return
    best = students[0]
    best_avg = calculate_average(best["grades"])
    for student in students:
        avg = calculate_average(student["grades"])
        if avg > best_avg:
            best = student
            best_avg = avg
    print(f" лучший студент {best["name"]}, {best_avg}")


def main():
    """
    Docstring for main
    """
    students = []
    while True:
        menu()
        choice = input("Выберите Действие: ")
        if choice == "1":
            add_student(students)
        elif choice =="2":
            add_grade(students)
        elif choice =="3":
            show_students(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            best_student(students)
        elif choice == "6":
            print("вы вышли из программы")
            break
        else:
            print("некоректный ввод")

if __name__ == "__main__":
    main()
