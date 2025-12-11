from resumageddon.api.hh_api import HeadHunterAPI
from resumageddon.storage.json_saver import JSONSaver
from resumageddon.utils.filtering import filter_by_keyword, get_top_n, sort_by_salary


def print_vacancies(vacancies):
    if not vacancies:
        print("⚠ По вашему запросу ничего не найдено.")
        return

    for v in vacancies:
        print(f"{v.title} | {v.salary_str} | {v.link}")
        print(f"Описание: {v.description}")
        print("-" * 60)


def main():
    print("🧠 Resumageddon запущен.")

    keyword = input("Введите ключевое слово для поиска (например 'Django'): ")

    # 🆕 Получаем вакансии с HH API
    api = HeadHunterAPI()
    raw_vacancies = api.get_vacancies(keyword)

    # Преобразуем JSON-данные в объекты Vacancy
    from resumageddon.models.vacancy import Vacancy

    vacancies = [Vacancy.from_json(item) for item in raw_vacancies]

    print(f"🔎 Найдено {len(vacancies)} вакансий.")

    filtered = filter_by_keyword(vacancies, keyword)
    if not filtered:
        print("⚠ По вашему запросу ничего не найдено.")
        return

    sorted_vacancies = sort_by_salary(filtered)

    try:
        top_n = int(input("Сколько топовых вакансий вывести? "))
    except ValueError:
        print("⛔ Введите корректное число.")
        return

    top_vacancies = get_top_n(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)

    saver = JSONSaver()

    while True:
        choice = input(
            "💾 Сохранить вакансии (s), очистить файл (c), выйти (q): "
        ).lower()
        if choice == "s":
            for vacancy in top_vacancies:
                saver.add_vacancy(vacancy)
            print("✅ Вакансии сохранены.")
        elif choice == "c":
            confirm = input(
                "🧹 Ты точно хочешь удалить все сохранённые вакансии? (y/n): "
            ).lower()
            if confirm == "y":
                for vacancy in saver.get_vacancies():
                    saver.delete_vacancy(vacancy)
                print("🗑️ Все вакансии удалены.")
        elif choice == "q":
            print("👋 Выход из программы.")
            break
        else:
            print("⛔ Неизвестная команда.")


if __name__ == "__main__":
    main()
