import doctest


# TODO Написать 3 класса с документацией и аннотацией типов


class Glass:
    def __init__(self, strength: float, volume_water: float):
        """
        Создание и подготовка объекта Стакан

        :param strength: Твердость стекла стакана
        :param volume_water: Объем воды в стакане

        Примеры:
        >>> glass = Glass(500, 0)  # инициализация экземпляра класса
        """

        if not isinstance(strength, (int, float)):
            raise TypeError("Значение твердости должно быть типа int или float")
        if strength < 0:
            raise ValueError("Значение твердости должно быть положительным числом")
        self.strength = strength

        if not isinstance(volume_water, (int, float)):
            raise TypeError("Объем воды должен быть типа int или float")
        if volume_water < 0:
            raise ValueError("Объем воды должен быть положительным числом")
        self.volume_water = volume_water

    def break_glass(self, break_power):
        """
        Метод, который проверяет, разобьется ли стакан

        :param break_power: Сила, которую необходимо приложить, чтобы разбить стакан

        :return: Разобьется ли стакан

        Примеры:
        >>> glass = Glass(500, 0)  # инициализация экземпляра класса
        >>> glass.break_glass(999)
        """
        if not isinstance(break_power, (int, float)):
            raise TypeError("Сила должна быть типа int или float")
        if break_power <= 0:
            raise ValueError("Сила должна быть положительным числом")
        ...

    def is_empty_glass(self) -> bool:
        """
        Метод, который проверяет является ли стакан пустым

        :return: Является ли стакан пустым

        Примеры:
        >>> glass = Glass(500, 0)
        >>> glass.is_empty_glass()
        """
        ...


class Book:
    def __init__(self, author: str, pages: int):
        """
        Создание и подготовка объекта Книга

        :param author: Имя автора
        :param pages: Количество страрниц в книге

        Примеры:
        >>> book = Book("А.С. Пушкин", 413)  # инициализация экземпляра класса
        """
        if not isinstance(author, str):
            raise TypeError("Имя автора может быть только типа str")
        self.author = author
        if not isinstance(pages, int):
            raise TypeError("Количество страниц может быть только типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

    def last_read_page(self, read_pages: int):
        """
        Метод увеличивает последнюю прочитанную страницу.

        :param read_pages: Количество прочитанных страниц

        :return Какая последняя прочитанная страница

        Примеры:
        >>> book = Book("А.С. Пушкин", 413)
        >>> book.last_read_page(13)
        """
        if not isinstance(read_pages, int):  # проверяем, что прочитанные страницы типа int
            raise TypeError("Прочитанные страницы должны быть типа int")  # вызываем ошибку
        if read_pages < 0:
            raise ValueError("Прочитанные страницы должны быть положительным числом")
        ...

    def language(self, author):
        """
        Метод, который определяет принадлежность к русской или к зарубежной литературе по тому, на каком языке написано
        имя автора

        :param author: Имя автора

        :return: К какой литературе относится книга

        Примеры:
        >>> book = Book("А.С. Пушкин", 413)
        >>> book.language(book.author)
        """
        if not isinstance(author, str):
            raise TypeError("Имя автора может быть только типа str")
        ...


class Flap:
    def __init__(self, color: str, size: float):
        """
        Создание и подготовка объекта Лоскут

        :param color: Цвет лоскута
        :param size: Размер лоскута в сантиметрах

        Примеры:
        >>> flap = Flap("red", 10)
        """
        if not isinstance(color, str):
            raise TypeError("Цвет может быть только типа str")
        self.color = color
        if not isinstance(size, int):
            raise TypeError("Размер может быть типа int или float")
        self.size = size

    def recolor(self, new_color):
        """
        Метод, перекрашывающий лоскут в новый цвет

        :param new_color: Цвет, в который перекрасится лоскут

        :return Новый цвет лоскута

        Примеры:
        >>> flap = Flap("red", 10)
        >>> flap.recolor("blue")
        """
        ...

    def sew_flap(self, other_flap):
        """
        Метод, который сшивает лоскуты одного цвета и не сшивает разных цветов

        :param other_flap: Лоскут, с которым будет происходить сшивание

        :return: Были ли сшиты лоскуты

        Примеры:
        >>> flap_1 = Flap("red", 10)
        >>> flap_2 = Flap("blue", 20)
        >>> flap_1.sew_flap(flap_2)
        """
        if not isinstance(other_flap, Flap):
            raise TypeError("Лоскут для сшивания должен быть объектом класса Flap")
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
