# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


def checker_numb(check_object: (int, float), check_name: str = "значение"):
    """
    Функция, проверяющая числовой тип данных

    :raise TypeError: если объект не является типом int или float
    :raise ValueError: если объект <0
    :param check_object: объект проверки
    :param check_name: имя объекта
    """
    if not isinstance(check_object, (int, float)):
        raise TypeError(f"'{check_name}' должен быть типом int или float")
    if check_object <= 0:
        raise ValueError(f"'{check_name}' должен быть больше 0")


def checker_str(check_object: str, check_name: str = "значение"):
    """
        Функция, проверяющая строковый тип данных

        :raise TypeError: если объект не является типом str
        :param check_object: объект проверки
        :param check_name: имя объекта
        """
    if not isinstance(check_object, str):
        raise TypeError(f"'{check_name}' должен быть типом str")


class Car:
    def __init__(self, brand: str, max_speed: int, mileage=0):
        """
        Создание и подготовка к работе объекта "Машина"

        :param brand: марка машины
        :param max_speed: максимальная скорость
        :param mileage: пробег, изначально равен 0
        """
        checker_str(brand, "brand")
        self.brand = brand
        checker_numb(max_speed, "max_speed")
        self.max_speed = max_speed
        self.mileage = mileage

    def drive(self, distance: (int, float)):
        """
        Функция, увеличивающая пробег (mileage) автомобиля за счет пройденной дистанции (distance)

        :param distance: расстояние, пройденное автомобилем
        """
        checker_numb(distance, "distance")
        self.mileage += distance

    def get_mileage(self):
        """
        Функция, возвращающая значение пробега (mileage)

        :return: возвращение значения пробега
        """
        return self.mileage

    def upgrade_engine(self, upgrade_speed: (int, float)):
        """
        Функция, увеличивающая максимальную скорость

        :param upgrade_speed: значение, на которое увеличивается максимальная скорость
        """
        checker_numb(upgrade_speed, "upgrade_speed")
        self.max_speed += upgrade_speed


class Airplane:
    def __init__(self, brand: str, max_altitude: (int, float), max_capacity: (int, float)):
        """
                Создание и подготовка к работе объекта "Самолет"

                :param max_altitude: максимальная высота полета (м) 0 < max_altitude < 13000
                :param max_capacity: максимальная грузоподъемность (т) 0 < max_capacity < 128
                :brand: название модели
                """
        checker_numb(max_altitude, "max_altitude")
        if max_altitude >= 13000:
            raise ValueError("высота полета должна быть < 13000")
        self.max_altitude = max_altitude
        checker_numb(max_capacity, "max_capacity")
        if max_capacity >= 128:
            raise ValueError("Максимальная грузоподъемность должна быть < 128")
        self.max_capacity = max_capacity
        checker_str(brand, "brand")
        self.brand = brand

    def set_brand(self, new_brand: str):
        """
        Функция, устанавливающая новую модель
        :param new_brand: новая модель
        """
        checker_str(new_brand, "new_brand")
        self.brand = new_brand

    def remain_capacity(self, cargo: (int, float)):
        """
        Функция, добавляющая груз. Считает оставшуюся вместимость самолета
        :param cargo: добавочный вес (т)
        """
        checker_numb(cargo, "cargo")
        self.max_capacity -= cargo
        if self.max_capacity < 0:
            raise ValueError("Грузоподъемность превышена")


class Ship:
    def __init__(self, draft: (int, float), displacement: (int, float)):
        """
        Создание и подготовка к работе объекта "Корабль"

        :param draft: осадка судна (м) 0 < draft < 25
        :param displacement: водоизмещение судна (т) 0 < displacement < 500000
        """
        checker_numb(draft, "draft")
        if draft >= 25:
            raise ValueError("Осадка корабля должна быть < 25")
        self.draft = draft
        checker_numb(displacement, "displacement")
        if displacement >= 500000:
            raise ValueError("Водоизмещение не может быть больше 500000")
        self.displacement = displacement

    def suez_canal(self) -> bool:
        """
        Функция, проверяющая, может ли судно пройти через Суэцкий канал
        :return: может ли судно пройти
        """
        ...

    def instruct(self, instruction: str):
        """
        Функция, получающая инструкции для судна
        :param instruction: передаваемые инструкции
        :return: ответ судна
        """
        checker_str(instruction, "instruction")
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
