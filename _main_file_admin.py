from admin_functions import admin_function

class admin_main_file:
    def __init__(self):
        self.admin_function_obj = admin_function()       

    def execute(self):
        try:
            if choice == 1:
                self.admin_function_obj.add_food_item()

            elif choice == 2:
                food_id = int(input("ENTER FOOD ID : "))
                food = self.admin_function_obj.search_food_item(food_id)
                print("\n**  FOOD ITEM  **")
                print(food)

            elif choice == 3:
                self.admin_function_obj.update_food_item()

            elif choice == 4:
                self.admin_function_obj.view_food_item()

            elif choice == 5:
                self.admin_function_obj.remove_food_item()

            else:
                quit()
                
        except Exception as ex:
            print("PLEASE TRY AGAIN", ex)


if __name__ == "__main__":
    admin_obj = admin_main_file()
    while True:
        try:
            choice = int(input("\nPLEASE CHOOSE AN OPTION FROM BELOW \n1 = TO ADD FOOD ITEM \n2 = TO SEARCH FOOD ITEM \n3 = TO EDIT FOOD ITEM \n4 = TO VIEW ALL FOOD ITEMS \n5 = TO DELETE FOOD ITEM \n0 = EXIT \nENTER YOUR OPTION : "))
            admin_obj.execute()
        except Exception as ex:
            print("PLEASE TRY AGAIN", ex)


