import json


students = [
    {"Surname": "Шевченко", "Name": "Олександр", "Address": "вул. Куликівська 7", "Day": 6, "Class": 8},
    {"Surname": "Шевченко", "Name": "Ольга", "Address": "вул. Куликівська 7", "Day": 7, "Class": 8},
    {"Surname": "Бойко", "Name": "Олександр", "Address": "вул. Хрещатик 121", "Day": 7, "Class": 9},
    {"Surname": "Карпенко", "Name": "Денис", "Address": "вул. Новомістенська 28", "Day": 6, "Class": 10},
    {"Surname": "Нахімова", "Name": "Ганна", "Address": "вул. Куликівська 35", "Day": 7, "Class": 11},
    {"Surname": "Горбачов", "Name": "Андрій", "Address": "вул. Ринкова 67", "Day": 6, "Class": 10},
    {"Surname": "Немова", "Name": "Катерина", "Address": "вул. Новомістенська 35А", "Day": 7, "Class": 9},
    {"Surname": "Франко", "Name": "Денис", "Address": "вул. Торгова 5", "Day": 6, "Class": 9},
    {"Surname": "Карпов", "Name": "Григорій", "Address": "вул. Хрещена 21", "Day": 7, "Class": 11},
    {"Surname": "Ремарков", "Name": "Марк", "Address": "вул. Бучанська 11", "Day": 6, "Class": 9}
]

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(students, file, ensure_ascii=False, indent=4)

def add_student(data):
    print("Додати студента:")
    name = input("Ім'я: ")
    surname = input("Прізвище: ")
    address = input("Адреса: ")
    day = int(input("День (6 для Суботи, 7 для Неділі): "))
    student_class = int(input("Клас: "))
    data.append({"Surname": surname, "Name": name, "Address": address, "Day": day, "Class": student_class})
    return data

def delete_student(data):
    print("Видалити студента:")
    name = input("Ім'я: ")
    surname = input("Прізвище: ")
    data = [student for student in data if not (student["Name"] == name and student["Surname"] == surname)]
    return data

def search_students_in_classes(data):
    result = [
        {key: value for key, value in student.items() if key in ['Surname', 'Name', 'Address', 'Day', 'Class']}
        for student in data if 8 <= student['Class'] <= 9 and student['Day'] == 6
    ]
    with open("search_results.json", "w", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=4)
    print("Результати пошуку збережено у файл 'search_results.json'")
    print(*result, sep='\n')

def menu():
    while True:
        print("Виберіть опцію:\n 1) Додати нового учня\n 2) Видалити учня\n 3) Переглянути дані\n 4) Знайти студентів 8-9 класу, що відвідують гурток в Суботу\n 5) Закінчити роботу програми")
        option = int(input("Оберіть опцію:\n"))
        if option == 1:
            with open("data.json", "r", encoding="utf-8") as file:
                students = json.load(file)
            students = add_student(students)
            with open("data.json", "w", encoding="utf-8") as file:
                json.dump(students, file, ensure_ascii=False, indent=4)
        elif option == 2:
            with open("data.json", "r", encoding="utf-8") as file:
                students = json.load(file)
            students = delete_student(students)
            with open("data.json", "w", encoding="utf-8") as file:
                json.dump(students, file, ensure_ascii=False, indent=4)
        elif option == 3:
            with open("data.json", "r", encoding="utf-8") as file:
                students = json.load(file)
            print(*students, sep='\n')
        elif option == 4:
            with open("data.json", "r", encoding="utf-8") as file:
                students = json.load(file)
            search_students_in_classes(students)
        elif option == 5:
            print("Вихід з програми.")
            break
        else:
            print("Невірна опція. Спробуйте ще раз.")

if __name__ == '__main__':
    menu()
