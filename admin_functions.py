from admin_encapsulation import admin

class admin_function:

    food_menu = [] 

    def add_food_item(self):
        print("\n*** ADD FOOD ITEM ***")
        try:
            food_id = int(input("ENTER FOOD ID : "))
            food_name = input("ENTER FOOD NAME : ")
            food_quantity = input("ENTER FOOD QUANTITY : ")
            food_price = float(input("ENTER FOOD PRICE : "))
            food_discount = int(input("ENTER FOOD DISCOUNT : "))
            food_stock = input("ENTER FOOD STOCK : ")
            food_obj = admin(food_id, food_name, food_quantity, food_price, food_discount, food_stock)
            self.food_menu.append(food_obj)
            print("*** FOOD ITEM ADDED SUCCESSFULLY ***")
        except Exception as ex:
            print("PLEASE TRY AGAIN", ex)
            


    def search_food_item(self,food_id):
        try:
            for foods in self.food_menu:
                if foods.get_food_id() == food_id:
                    return foods
        except Exception as ex:
            print("PLEASE TRY AGAIN", ex)

    def update_food_item(self):
        try:
            print("**  UPDATE FOOD  **")
            food_id = int(input("ENTER FOOD ID : "))
            food = self.search_food_item(food_id)
            if food:
                food_name = input("ENTER FOOD NAME : ")
                food_quantity = input("ENTER FOOD QUANTITY : ")
                food_price = float(input("ENTER FOOD PRICE : "))
                food_discount = int(input("ENTER FOOD DISCOUNT : "))
                food_stock = input("ENTER FOOD STOCK : ")

                food.set_food_name(food_name)
                food.set_food_quantity(food_quantity)
                food.set_food_price(food_price)
                food.set_food_discount(food_discount)
                food.set_food_stock(food_stock)

                print("**  SUCCESSFULLY FOOD UPDATED  **")
        except Exception as ex:
            print("PLEASE TRY AGAIN", ex)

    def view_food_item(self):
        try:
            print("\n***  ALL FOOD ITEMS LIST  **")
            for foods in self.food_menu:
                print(foods,'\n')
        except Exception as ex:
            print("PLEASE TRY AGAIN", ex)

    def remove_food_item(self):
        try:
            print("**  DELETE FOOD  **")
            food_id = int(input("ENTER FOOD ID : "))
            food = self.search_food_item(food_id)
            if food:
                self.food_menu.remove(food)
                print("**  SUCCESSFULLY DELETED  **")
        except Exception as ex:
            print("PLEASE TRY AGAIN", ex)