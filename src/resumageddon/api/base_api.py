from abc import ABC, abstractmethod
from typing import Dict, List


class VacancyAPI(ABC):
    """
    Абстрактный интерфейс для работы с API вакансий.

    Классы, реализующие этот интерфейс, должны предоставлять метод
    для получения списка вакансий по ключевому слову.
    """

    @abstractmethod
    def get_vacancies(self, keyword: str) -> List[Dict]:
        """
        Запрашивает вакансии из внешнего API.

        :param keyword: Ключевое слово для поиска.
        :return: Список словарей с данными о вакансиях,
                 полученных от API.
        """
        pass
