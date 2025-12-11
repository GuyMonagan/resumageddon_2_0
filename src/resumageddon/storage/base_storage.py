from abc import ABC, abstractmethod
from typing import List

from ..models.vacancy import Vacancy


class VacancyStorage(ABC):
    """
    Абстрактный интерфейс для хранилищ вакансий.

    Позволяет сохранять, извлекать и удалять объекты Vacancy
    независимо от конкретной реализации хранилища (файл, БД и т.д.).
    """

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        """
        Добавляет вакансию в хранилище.

        :param vacancy: Объект Vacancy для сохранения.
        """
        pass

    @abstractmethod
    def get_vacancies(self) -> List[Vacancy]:
        """
        Возвращает список всех сохранённых вакансий.

        :return: Список объектов Vacancy.
        """
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """
        Удаляет вакансию из хранилища.

        :param vacancy: Объект Vacancy, который требуется удалить.
        """
        pass
