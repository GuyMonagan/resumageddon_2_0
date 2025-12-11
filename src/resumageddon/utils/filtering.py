from typing import List

from src.resumageddon.models.vacancy import Vacancy


def filter_by_keyword(vacancies: List[Vacancy], keyword: str) -> List[Vacancy]:
    """
    Фильтрует список вакансий по ключевому слову.

    :param vacancies: Список объектов вакансий
    :param keyword: Ключевое слово для фильтрации
    :return: Отфильтрованный список вакансий
    """
    keyword = keyword.lower()
    return [
        v
        for v in vacancies
        if keyword in v.description.lower() or keyword in v.title.lower()
    ]


def sort_by_salary(vacancies: List[Vacancy], reverse=True):
    """
    Сортирует список вакансий по зарплате.

    :param vacancies: Список объектов вакансий
    :param reverse: Если True — по убыванию, иначе по возрастанию
    :return: Отсортированный список вакансий
    """
    return sorted(vacancies, reverse=reverse)


def get_top_n(vacancies: List[Vacancy], n: int):
    """
    Возвращает топ-N вакансий из списка.

    :param vacancies: Список объектов вакансий
    :param n: Количество вакансий в выдаче
    :return: Список из n вакансий
    """
    return vacancies[:n]
