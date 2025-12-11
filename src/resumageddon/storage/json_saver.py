import json
import os
from typing import List

from ..models.vacancy import Vacancy
from .base_storage import VacancyStorage


class JSONSaver(VacancyStorage):
    """
    Хранилище вакансий в JSON-файле.

    Реализует добавление, получение и удаление объектов Vacancy
    через работу с локальным JSON-файлом.
    """

    def __init__(self, filename: str = "data/saved_vacancies.json"):
        self._filename = filename
        if not os.path.exists(self._filename):
            with open(self._filename, "w", encoding="utf-8") as f:
                json.dump([], f)

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """
        Добавляет новую вакансию, избегая дублирования.

        :param vacancy: Объект Vacancy.
        """
        all_vacancies = self.get_vacancies()
        # не добавляем дубликаты
        if vacancy not in all_vacancies:
            all_vacancies.append(vacancy)
            self._write(all_vacancies)

    def get_vacancies(self) -> List[Vacancy]:
        """
        Загружает вакансии из JSON-файла.

        :return: Список объектов Vacancy или пустой список при ошибке/пустом файле.
        """
        if not os.path.exists(self._filename):
            return []

        try:
            with open(self._filename, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content:
                    return []
                data = json.loads(content)
                return [Vacancy(**item) for item in data]
        except (json.JSONDecodeError, TypeError):
            return []

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """
        Удаляет указанную вакансию из JSON-файла.

        :param vacancy: Объект Vacancy, который нужно удалить.
        """
        all_vacancies = self.get_vacancies()
        filtered = [v for v in all_vacancies if v != vacancy]
        self._write(filtered)

    def _write(self, vacancies: List[Vacancy]) -> None:
        """
        Записывает список вакансий в JSON-файл.

        :param vacancies: Список объектов Vacancy.
        """
        with open(self._filename, "w", encoding="utf-8") as f:
            json.dump([v.to_dict() for v in vacancies], f, ensure_ascii=False, indent=2)
