class admin:
    def __init__(self, food_id, food_name, food_quantity, food_price, food_discount, food_stock):
        self.__food_id = food_id
        self.__food_name = food_name
        self.__food_quantity = food_quantity
        self.__food_price = food_price
        self.__food_discount = food_discount
        self.__food_stock = food_stock

    def __str__(self):
        return f"\nFOOD ID : {self.__food_id}, \nFOOD NAME : {self.__food_name}, \nFOOD QUANTITY : {self.__food_quantity}, \nFOOD PRICE: {self.__food_price}, \nFOOD DISCOUNT : {self.__food_discount}, \nFOOD STOCK : {self.__food_stock} \n"


    def set_food_id(self,food_id):
        self.__food_id = food_id
    def get_food_id(self):
        return self.__food_id

    def set_food_name(self,food_name):
        self.__food_name = food_name
    def get_food_name(self):
        return self.__food_name

    def set_food_quantity(self,food_quantity):
        self.__food_quantity = food_quantity
    def get_food_quantity(self):
        return self.__food_quantity

    def set_food_price(self,food_price):
        self.__food_price = food_price
    def get_food_price(self):
        return self.__food_price

    def set_food_discount(self,food_discount):
        self.__food_discount = food_discount
    def get_food_discount(self):
        return self.__food_discount

    def set_food_stock(self,food_stock):
        self.__food_stock = food_stock
    def get_food_stock(self):
        return self.__food_stock

