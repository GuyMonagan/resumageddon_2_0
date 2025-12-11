from src.resumageddon.models.vacancy import Vacancy
from src.resumageddon.utils.filtering import (
    filter_by_keyword,
    get_top_n,
    sort_by_salary,
)


def test_filtering_keyword():
    vacancies = [
        Vacancy("Python Dev", "desc", 100000, "link", "req", "resp"),
        Vacancy("Java Dev", "desc", 80000, "link", "req", "resp"),
    ]
    result = filter_by_keyword(vacancies, "Python")
    assert len(result) == 1


def test_sort_by_salary():
    vacancies = [
        Vacancy("One", "desc", 100000, "link", "req", "resp"),
        Vacancy("Two", "desc", 200000, "link", "req", "resp"),
    ]
    sorted_vacs = sort_by_salary(vacancies)
    assert sorted_vacs[0].title == "Two"


def test_get_top_n():
    vacancies = [
        Vacancy(f"Vac {i}", "desc", i * 1000, "link", "req", "resp") for i in range(10)
    ]
    top = get_top_n(vacancies, 3)
    assert len(top) == 3
