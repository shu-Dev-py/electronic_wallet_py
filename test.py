#1 задача!!!

#class Hero():
#    def __init__(self,name,health):
#        self.name = name
#        self.health = health
#
#    def show_info(self):
#        print(f"Герой {self.name} \nЗдоровье {self.health}")
#
#    def move(self):
#        print(f"{self.name} перемещается по карте.")
#
#
#class StrengthHero(Hero):
#    def __init__(self,name,health,strength):
#        super().__init__(name,health)
#        self.strength = strength
#
#    def use_strength(self):
#        print(f"{self.name} использует силу равную {self.strength}")
#
#if __name__ == "__main__":
#    axe = StrengthHero("Axe",200,25)
#    axe.show_info()
#    axe.move()
#    axe.use_strength()

#2 задача!!!

#class User():
#    def __init__(self,name,email):
#        self.name = name
#        self.email = email

#    def login(self):
#        print(f"{self.name} зашел на сайт!")
#    def show_info(self):
#        print(f"пользователь - {self.name} \nего маил - {self.email}")

#class Customer(User):
#    def __init__(self,name,email,address):
#        super().__init__(name,email)
#        self.address = address

#    def make_order(self):
#        print("="*35)
#        print(f"{self.name} оформил заказ в город {self.address}")

#if __name__ == "__main__":
#    user = Customer("Ivan",
#                    "Ivan@gmail.com",
#                    "'KAZAN'")
#    user.login()
#    user.show_info()
#    user.make_order()

#3 задача!!!


class Product():
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def show_info(self):
        print(f"товар: {self.name}\n цена: {self.price} руб")

    def apply_discount(self,percent):
        self.price = self.price - (self.price * percent/100)

class PhysicalProduct(Product):
    def __init__(self,name,price,weight):
        super().__init__(name,price)
        self.weight = weight

    def show_info(self):
        super().show_info()
        print(f"вес {self.weight} кг")

class DigitalProduct(Product):
    def __init__(self,name,price,):
        super().__init__(name,price)

    def file_size(self,file_size):
        super().show_info()
        print(f"размер файла: {file_size} мб")


if __name__ == "__main__":
    product = DigitalProduct("игровая валюта",
                             250)

    product.apply_discount(20)
    product.file_size(240)
    print("="*30)

    product2 = PhysicalProduct("приставка",
                               30000,
                               4)
    product2.show_info()


