from src.resumageddon.models.vacancy import Vacancy
from src.resumageddon.storage.json_saver import JSONSaver


def test_add_and_get_vacancy(tmp_path):
    # Создаем временный путь к JSON
    file = tmp_path / "vacancies.json"

    # Создаем экземпляр JSONSaver с этим файлом
    saver = JSONSaver(filename=str(file))

    # Создаем фейковую вакансию
    vacancy = Vacancy(
        title="Junior Python Developer",
        description="Some desc",
        salary=100000,
        link="http://example.com",
        requirement="Python",
        responsibility="Coding",
    )

    # Добавляем и читаем обратно
    saver.add_vacancy(vacancy)
    vacancies = saver.get_vacancies()

    assert len(vacancies) == 1
    assert vacancies[0].title == "Junior Python Developer"
    assert vacancies[0].salary == 100000


def test_no_duplicates(tmp_path):
    file = tmp_path / "vacancies.json"
    saver = JSONSaver(filename=str(file))

    vacancy = Vacancy(
        title="Mid Python Dev",
        description="desc",
        salary=200000,
        link="http://example.com",
        requirement="req",
        responsibility="resp",
    )

    saver.add_vacancy(vacancy)
    saver.add_vacancy(vacancy)  # добавляем второй раз

    vacancies = saver.get_vacancies()
    assert len(vacancies) == 1  # дубликат не добавился
