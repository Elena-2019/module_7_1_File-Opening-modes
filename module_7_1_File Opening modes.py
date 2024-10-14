class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

    def get_product(self):
        return f"{self.name}, {self.weight}, {self.category}\n"

class Shop:
    __file_name = 'products.txt'

    def get_product(self):
        file_1 = open(self.__file_name, 'r')
        str_1 = f"{file_1.read()}"
        file_1.close()
        return str(str_1)

    def add(self, *products):
        add_product = self.get_product()
        file_1 = open(self.__file_name, 'a')
        for product in products:
            adds_to_file = product.get_product()
            if adds_to_file not in add_product:
                file_1.write(adds_to_file)
            else:
                print(f'Продукт {product} уже есть в магазине')
        file_1.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_product())
