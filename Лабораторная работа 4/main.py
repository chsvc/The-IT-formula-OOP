class Animal:
    """Базовый класс для животных."""

    def __init__(self, name: str, age: int):
        """
        Конструктор класса Animal.

        :param name: Имя животного.
        :param age: Возраст животного.
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть типа str")
        self._name = name

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if age < 0:
            raise ValueError("Возраст должен быть положительным числом")
        self._age = age

    def speak(self) -> str:
        """
        Метод, который возвращает звук, издаваемый животным.

        :return Звук, издаваемый животным.
        """
        pass

    def __str__(self) -> str:
        """
        Магический метод, возвращающий строковое представление объекта.

        :return: Строка, которая удобно воспринимается человеком.
        """
        return f"Имя: {self._name}, Возраст: {self._age}"

    def __repr__(self) -> str:
        """
        Магический метод, возвращающий строку, показывающую, как может быть инициализирован экземпляр.

        :return: Представление инициализации экземпляра.
        """
        return f"{self.__class__.__name__} ('name={self._name}', age={self._age})"


class Dog(Animal):
    """
    Дочерний класс для собак.
    """

    def __init__(self, name: str, age: int, breed: str):
        """
        Конструктор класса Dog.

        :param name: Имя собаки.
        :param age: Возраст собаки.
        :param breed: Порода собаки.
        """
        super().__init__(name, age)
        if not isinstance(breed, str):
            raise TypeError("Порода должна быть типа str")
        self._breed = breed

    def speak(self) -> str:
        """
        Унаследованный метод, возвращающий звук, издаваемый собакой.

        :return: Звук, издаваемый собакой.
        """
        return "Гав!"

    def fetch(self, item: str) -> str:
        """
        Метод, по которому собака "приносит" предмет.

        :param item: Предмет, который собака должна принести.

        :return: Строка, сообщающая, что собака принесла предмет.
        """
        return f"{self._name} принесла {item}!"

    def __str__(self) -> str:
        """
        Переопределенный магический метод, возвращающий строковое представление объекта.

        :return: Строка, которая удобно воспринимается человеком.

        """
        return f"Имя: {self._name}, Возраст: {self._age}, Порода: {self._breed}"

    def __repr__(self) -> str:
        """
        Переопределенный магический метод, возвращающий строку, показывающую, как может быть инициализирован экземпляр.

        :return: Представление объекта.
        """
        return f"{self.__class__.__name__} ,name='{self._name}', age={self._age}, breed='{self._breed}')"


if __name__ == "__main__":
    animal = Animal("Джесси", 5)
    print(animal)

    dog = Dog("Джесси", 5, "Лабрадор")
    print(dog)

    print(animal.speak())

    print(dog.speak())

    print(dog.fetch("Мяч"))
    pass
