from src.resumageddon.models.vacancy import Vacancy


def test_vacancy_creation():
    v = Vacancy(
        title="Python Developer",
        description="Work on backend",
        salary=150000,
        link="https://example.com",
        requirement="Python, Django",
        responsibility="Develop backend services",
    )
    assert v.title == "Python Developer"
    assert v.salary == 150000
    assert isinstance(v, Vacancy)


def test_salary_validation():
    v = Vacancy(
        title="Test",
        description="desc",
        salary=-100,  # должно пройти через _validate_salary
        link="link",
    )
    assert v.salary == 0  # зарплата должна быть приведена к 0


def test_comparison():
    v1 = Vacancy("A", "", 100, "link1")
    v2 = Vacancy("B", "", 200, "link2")
    assert v1 < v2
    assert v2 > v1


def test_equality_and_hash():
    v1 = Vacancy("Dev", "", 100, "link1")
    v2 = Vacancy("Dev", "", 150, "link1")  # та же ссылка и заголовок — значит равны
    v3 = Vacancy("Another", "", 100, "link2")
    assert v1 == v2
    assert v1 != v3
    assert hash(v1) == hash(v2)
    assert hash(v1) != hash(v3)


def test_to_dict_and_from_json():
    data = {
        "name": "Python Dev",
        "alternate_url": "http://hh.ru/vacancy/123",
        "salary": {"from": 100000, "to": 150000},
        "snippet": {"requirement": "Python", "responsibility": "Backend"},
    }
    v = Vacancy.from_json(data)
    d = v.to_dict()

    assert d["title"] == "Python Dev"
    assert d["salary"] == 125000
    assert "requirement" in d
    assert "responsibility" in d
    assert "description" in d
