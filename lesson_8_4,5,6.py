# 4) Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
#
# 5) Продолжить работу над четрвёртым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
#
# 6) Продолжить работу над четрвёртым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
class Warehouse:
    def __init__(self):
        self.stock = {}

    def add_item(self, item):
        if isinstance(item, OfficeEquipment):
            if item.name in self.stock:
                self.stock[item.name]["count"] += 1
            else:
                self.stock[item.name] = {"count": 1, "params": item.get_params()}
            print(f"{item.name} добавлен на склад")
        else:
            print(f"{item} не является оргтехникой")

    def move_item(self, item_name, department):
        if item_name in self.stock:
            if self.stock[item_name]["count"] > 0:
                self.stock[item_name]["count"] -= 1
                print(f"{item_name} передан в подразделение {department}")
            else:
                print(f"{item_name} отсутствует на складе")
        else:
            print(f"{item_name} отсутствует на складе")

    def list_items(self):
        print("Список оргтехники на складе:")
        for name, data in self.stock.items():
            count = data["count"]
            params = ", ".join([f"{k}={v}" for k, v in data["params"].items()])
            print(f"{name} ({count}): {params}")


class OfficeEquipment:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def get_params(self):
        return {"цвет": self.color, "цена": self.price}


class Printer(OfficeEquipment):
    def __init__(self, name, color, price, is_color):
        super().__init__(name, color, price)
        self.is_color = is_color

    def get_params(self):
        params = super().get_params()
        params["цветной"] = "да" if self.is_color else "нет"
        return params


class Scanner(OfficeEquipment):
    def __init__(self, name, color, price, resolution):
        super().__init__(name, color, price)
        self.resolution = resolution

    def get_params(self):
        params = super().get_params()
        params["разрешение"] = self.resolution
        return params


class Copier(OfficeEquipment):
    def __init__(self, name, color, price, speed):
        super().__init__(name, color, price)
        self.speed = speed

    def get_params(self):
        params = super().get_params()
        params["скорость"] = self.speed
        return params


warehouse = Warehouse()
warehouse.add_item(Printer("Принтер HP", "черный", 5000, True))
warehouse.add_item(Printer("Принтер Canon", "белый", 4000, False))
warehouse.add_item(Scanner("Сканер Samsung", "серый", 2500, "600x600 dpi"))
warehouse.add_item(Copier("Ксерокс Xerox", "белый", 10000, "30 стр/мин"))
warehouse.list_items()
warehouse.move_item("Принтер HP", "Маркетинг")
warehouse.move_item("Принтер HP", "Маркетинг")
warehouse.move_item("Сканер Epson", "Кадры")
warehouse.list_items()
warehouse.add_item("Стол")
warehouse.move_item("Телефон", "Маркетинг")
warehouse.move_item("Принтер HP", "Маркетинг")
