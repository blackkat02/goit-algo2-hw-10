# Визначення класу Teacher (без змін)
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()

    def __repr__(self):
        return f"Teacher({self.first_name},{self.last_name}, {self.age} років, Skills: {self.can_teach_subjects})"


def create_schedule(subjects, teachers):

    remaining_subjects = subjects.copy()
    available_teachers = list(teachers)

    schedule_list = []

    # Цикл продовжується, поки є предмети, які треба покрити, І є доступні вчителі.
    while len(remaining_subjects) > 0 and len(available_teachers) > 0:

        teacher_raiting_list = []

        for teacher in available_teachers:
            current_coverage_set = remaining_subjects.intersection(
                teacher.can_teach_subjects
            )
            current_coverage_len = len(current_coverage_set)

            # Додаємо до рейтингу лише тих, хто може покрити щось нове
            if current_coverage_len > 0:
                teacher_raiting_list.append(
                    (
                        teacher,
                        current_coverage_len,
                        teacher.age,
                        current_coverage_set,
                    )
                )

        # Перевірка на неможливість покриття
        if not teacher_raiting_list:
            break

        sorted_best_teacher = sorted(
            teacher_raiting_list,
            key=lambda item: (
                -item[1],
                item[2],
            ),
        )

        # Вибір та Призначення
        best_teacher = sorted_best_teacher[0][0]
        subjects_to_assign = sorted_best_teacher[0][3]

        best_teacher.assigned_subjects.update(subjects_to_assign)
        schedule_list.append(best_teacher)

        # Оновлення стану (Жадібний крок)
        remaining_subjects.difference_update(subjects_to_assign)
        available_teachers.remove(best_teacher)

    print(f"\n--- Результат виконання ---")

    # Виведення залишкових ресурсів
    if remaining_subjects:
        print(f"⚠️ {len(remaining_subjects)} предмет(ів) залишилися без викладача:")
        for subject in remaining_subjects:
            print(f"    - {subject}")

    if available_teachers:
        print(f"👤 {len(available_teachers)} викладач(ів) не призначений:")
        for teacher in available_teachers:
            print(f"    - {teacher.first_name} {teacher.last_name}")

    return schedule_list


if __name__ == "__main__":
    # Множина предметів
    subjects_initial = {"Математика", "Фізика", "Хімія", "Інформатика", "Біологія"}

    # Створення списку викладачів
    teachers_initial = [
        Teacher(
            first_name="Олександр",
            last_name="Іваненко",
            age=45,
            email="o.ivanenko@example.com",
            can_teach_subjects={"Математика", "Фізика"},
        ),
        Teacher(
            first_name="Марія",
            last_name="Петренко",
            age=38,
            email="m.petrenko@example.com",
            can_teach_subjects={"Хімія"},
        ),
        Teacher(
            first_name="Сергій",
            last_name="Коваленко",
            age=50,
            email="s.kovalenko@example.com",
            can_teach_subjects={"Інформатика", "Математика"},
        ),
        Teacher(
            first_name="Наталія",
            last_name="Шевченко",
            age=29,
            email="n.shevchenko@example.com",
            can_teach_subjects={"Біологія", "Хімія"},
        ),
        Teacher(
            first_name="Дмитро",
            last_name="Бондаренко",
            age=35,
            email="d.bondarenko@example.com",
            can_teach_subjects={"Фізика", "Інформатика"},
        ),
        Teacher(
            first_name="Олена",
            last_name="Гриценко",
            age=42,
            email="o.grytsenko@example.com",
            can_teach_subjects={"Біологія"},
        ),
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects_initial, teachers_initial)

    # Виведення розкладу
    if schedule:
        print("\n--- ✅ Фінальний Розклад Занять ---")
        for teacher in schedule:
            print(
                f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}"
            )
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("\nНеможливо покрити всі предмети наявними викладачами.")
