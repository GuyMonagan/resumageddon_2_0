import os
from typing import Dict, List

import requests
from dotenv import load_dotenv

from .abstract_api import VacancyAPI

# Загружаем переменные окружения из .env файла
load_dotenv()


class HeadHunterAPI(VacancyAPI):
    def __init__(self):
        # Берём URL из переменной окружения, иначе используем дефолт
        self._base_url = os.getenv("HH_API_BASE_URL", "https://api.hh.ru/vacancies")
        self._headers = {"User-Agent": "ResumageddonBot/1.0"}

    def _get(self, params: dict):
        """Приватный метод для отправки GET-запроса."""
        response = requests.get(self._base_url, headers=self._headers, params=params)
        if response.status_code != 200:
            raise Exception(f"Ошибка при запросе: {response.status_code}")
        return response.json()

    def get_vacancies(self, keyword: str) -> List[Dict]:
        """Получает вакансии по ключевому слову с API HH"""
        all_vacancies = []
        params = {"text": keyword, "per_page": 20, "page": 0}

        for page in range(2):
            params["page"] = page
            data = self._get(params)
            items = data.get("items", [])
            if not items:
                break
            all_vacancies.extend(items)

        return all_vacancies
