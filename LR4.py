from abc import ABC, abstractmethod


class BuildingMaterial(ABC):
    """
    Базовый класс для всех строительных материалов.

    Инкапсулирует общие свойства:
    - название материала (защищено от прямого изменения)
    - цена за единицу
    - количество на складе
    """

    def __init__(self, name: str, price_per_unit: float, quantity: float) -> None:
        """
        Инициализация строительного материала.

        :param name: Название материала
        :param price_per_unit: Цена за единицу (руб.)
        :param quantity: Количество на складе
        """
        self._name = name
        self.price_per_unit = price_per_unit
        self.quantity = quantity

    @property
    def name(self) -> str:
        """Геттер для названия материала (только чтение)."""
        return self._name

    def calculate_total_cost(self) -> float:
        """
        Расчет общей стоимости материала на складе.

        :return: Общая стоимость (цена * количество)
        """
        return self.price_per_unit * self.quantity

    @abstractmethod
    def calculate_shipping_cost(self, distance: float) -> float:
        """
        Абстрактный метод расчета стоимости доставки.
        Должен быть переопределен в дочерних классах.

        :param distance: Расстояние доставки в км
        :return: Стоимость доставки
        """
        pass

    def __str__(self) -> str:
        """Пользовательское строковое представление."""
        return f"{self._name}: {self.quantity} ед. по {self.price_per_unit} руб."

    def __repr__(self) -> str:
        """Техническое строковое представление для разработчиков."""
        return f"BuildingMaterial(name='{self._name}', price={self.price_per_unit}, quantity={self.quantity})"


class Brick(BuildingMaterial):
    """Класс для кирпича - дочерний от BuildingMaterial."""

    def __init__(self, name: str, price_per_unit: float, quantity: float,
                 brick_type: str, weight_per_unit: float) -> None:
        """
        Расширение конструктора базового класса.

        :param brick_type: Тип кирпича
        :param weight_per_unit: Вес одного кирпича в кг
        """
        super().__init__(name, price_per_unit, quantity)
        self.brick_type = brick_type
        self.weight_per_unit = weight_per_unit
        self._is_fireproof = (brick_type == "керамический")

    @property
    def is_fireproof(self) -> bool:
        """Является ли кирпич огнеупорным."""
        return self._is_fireproof

    def calculate_shipping_cost(self, distance: float, price_per_km: float = 30.0,
                                price_per_kg: float = 10.0) -> float:
        """
        Переопределение метода расчета доставки.

        Причина переопределения: кирпич тяжелый, стоимость доставки зависит от веса.

        :param distance: Расстояние доставки
        :param price_per_km: Стоимость доставки за 1 км (по умолчанию 30 руб.)
        :param price_per_kg: Стоимость доставки за 1 кг веса (по умолчанию 10 руб.)
        :return: Стоимость доставки с учетом веса
        """
        total_weight = self.quantity * self.weight_per_unit
        return (distance * price_per_km) + (total_weight * price_per_kg)

    def __str__(self) -> str:
        """
        Перегрузка магического метода __str__.

        Добавляется информация о типе кирпича.
        """
        base_string = super().__str__()
        return f"{base_string} - {self.brick_type} кирпич, вес: {self.weight_per_unit} кг"

    def __repr__(self) -> str:
        """
        Перегрузка магического метода __repr__.

        Полное техническое представление с параметрами кирпича.
        """
        return (f"Brick(name='{self._name}', price={self.price_per_unit}, "
                f"quantity={self.quantity}, type='{self.brick_type}', "
                f"weight={self.weight_per_unit})")


if __name__ == "__main__":
    brick = Brick("Красный", 50, 1000, "керамический", 3.5)
    print(brick)
    print(repr(brick))
    print(f"Стоимость доставки (100 км): {brick.calculate_shipping_cost(100)} руб.")
    print(
        f"Стоимость доставки (100 км, свои тарифы): {brick.calculate_shipping_cost(100, price_per_km=40, price_per_kg=12)} руб.")
    print(f"Огнеупорный: {brick.is_fireproof}")
