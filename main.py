def find_student(students, name):
    for student in students:
        if student["name"].lower() == name.lower():
            return student
    return None



def menu():
    print("\n--- Меню ---")
    print("1. добавить студента")
    print("2. добавить оценку")
    print("3.показать всех студентов")
    print("4.удалить студента")
    print("5.показать лучшего студента")
    print("6.выйти")

def add_student(students):
    name = input("введите имя: ")
    age = int(input("введите возраст студента: "))

    students.append({
        "name": name,
        "age": age,
        "grades": []
    })

def add_grade(students):
    name = input("введите имя студента")

    grade = float(input("введите оценку студента"))
    
    if 0 <- grade <- 100:
        students["grades"].append(grade)
        print("оценка добавлена.")
    else:
        print("оценка должна быть от 0 до 100")



def main():
    students = []
    while True:
        menu()
        choice = input("Выберите Действие: ")
        if choice == "1":
            add_student(students=)

if __name__ == "__main__":
    main()