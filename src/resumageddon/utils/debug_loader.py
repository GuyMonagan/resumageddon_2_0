import json
from typing import List

from ..models.vacancy import Vacancy


def load_vacancies_from_file(filename: str) -> List[Vacancy]:
    """
    Загружает вакансии из локального JSON-файла
    в формате API (с ключом "items").

    :param filename: Путь к JSON-файлу.
    :return: Список объектов Vacancy.
    """
    with open(filename, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    items = raw_data.get("items", [])
    vacancies = [Vacancy.from_json(item) for item in items]
    return vacancies
