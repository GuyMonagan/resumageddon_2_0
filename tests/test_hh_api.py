from unittest.mock import patch

from src.resumageddon.api.hh_api import HeadHunterAPI


def test_hh_api_get_vacancies_mock():
    mock_data = {
        "items": [
            {
                "name": "Тестовая вакансия",
                "salary": None,
                "alternate_url": "http://example.com",
            }
        ]
    }

    with patch.object(HeadHunterAPI, "_get", return_value=mock_data):
        api = HeadHunterAPI()
        result = api.get_vacancies("Python")
        assert isinstance(result, list)
        assert result[0]["name"] == "Тестовая вакансия"
