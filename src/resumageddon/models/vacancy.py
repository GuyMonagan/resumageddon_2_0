from typing import Optional


class Vacancy:
    """
    Модель вакансии.

    Содержит основные данные о вакансии, методы сравнения по зарплате.
    """

    __slots__ = (
        "title",
        "link",
        "salary",
        "description",
        "requirement",
        "responsibility",
        "salary_str",
    )

    def __init__(
        self,
        title: str,
        link: str,
        salary: int,
        description: str,
        requirement: Optional[str] = "",
        responsibility: Optional[str] = "",
    ):
        self.title = title
        self.link = link
        self.salary = self._validate_salary(salary)
        self.description = description
        self.requirement = requirement
        self.responsibility = responsibility
        self.salary_str: str = ""

    def _validate_salary(self, salary: int) -> int:
        """
        Проверяет корректность значения зарплаты.

        :param salary: Зарплата в числовом виде.
        :return: Изначальная зарплата, если корректна, иначе 0.
        """
        if isinstance(salary, int) and salary >= 0:
            return salary
        return 0

    def __repr__(self) -> str:
        return f"<Vacancy {self.title} ({self.salary})>"

    def __lt__(self, other: "Vacancy") -> bool:
        return self.salary < other.salary

    def __gt__(self, other: "Vacancy") -> bool:
        return self.salary > other.salary

    def __eq__(self, other):
        return (
            isinstance(other, Vacancy)
            and self.title == other.title
            and self.link == other.link
        )

    def __hash__(self):
        return hash((self.title, self.link))

    @staticmethod
    def _parse_salary(salary_data: Optional[dict]) -> int:
        """
        Парсит словарь зарплаты из API и рассчитывает числовое значение.

        :param salary_data: Данные зарплаты, содержащие поля 'from' и/или 'to'.
        :return: Среднее значение, если указаны оба, иначе одно из значений,
                 либо 0, если данных нет.
        """
        if not salary_data:
            return 0
        _from = salary_data.get("from")
        _to = salary_data.get("to")
        if _from and _to:
            return (_from + _to) // 2
        return _from or _to or 0

    @classmethod
    def from_json(cls, data: dict) -> "Vacancy":
        """
        Создаёт объект Vacancy на основе JSON-структуры API.

        :param data: Сырые данные вакансии.
        :return: Экземпляр Vacancy с заполненными данными.
        """
        title = data.get("name", "Без названия")
        link = data.get("alternate_url", "")
        salary_data = data.get("salary")
        salary = cls._parse_salary(salary_data)

        # Строка для отображения
        if not salary_data:
            salary_str = "Зарплата не указана"
        else:
            _from = salary_data.get("from")
            _to = salary_data.get("to")
            currency = salary_data.get("currency", "RUR")

            if _from and _to:
                salary_str = f"{_from:,} – {_to:,} {currency}".replace(",", " ")
            elif _from:
                salary_str = f"от {_from:,} {currency}".replace(",", " ")
            elif _to:
                salary_str = f"до {_to:,} {currency}".replace(",", " ")
            else:
                salary_str = "Зарплата не указана"

        snippet = data.get("snippet", {})
        requirement = snippet.get("requirement", "")
        responsibility = snippet.get("responsibility", "")
        description = f"{requirement} {responsibility}".strip()

        vacancy = cls(
            title=title,
            link=link,
            salary=salary,
            description=description,
            requirement=requirement,
            responsibility=responsibility,
        )

        # Добавляем динамически строку для отображения
        vacancy.salary_str = salary_str
        return vacancy

    def to_dict(self) -> dict:
        """
        Преобразует объект Vacancy в словарь.

        :return: Словарь с основными данными вакансии,
                 пригодный для сериализации в JSON.
        """
        return {
            "title": self.title,
            "link": self.link,
            "salary": self.salary,
            "description": self.description,
            "requirement": self.requirement,
            "responsibility": self.responsibility,
        }
