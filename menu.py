class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, gas,sugar,chocolate,coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
            "gas":gas,
            "sugar":sugar,
            "chocolate":chocolate
            
        }

class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu =[
            MenuItem(name="latte,", water=200, milk=150, coffee=24, chocolate=0, gas=0, sugar=0 , cost=750),
            MenuItem(name="espresso,", water=50, milk=0, coffee=18, sugar=0, chocolate=0, gas=0  ,cost=600),
            MenuItem(name="cappuccino,", water=250, milk=50, coffee=24, sugar=0, chocolate=0,gas=0 ,cost=350),
            MenuItem(name="hot_tea,",water=220, milk=50, sugar=60, gas=100, coffee=0, chocolate=0 ,cost=300),
            MenuItem(name="shake,",water=100, milk=100, sugar=30, chocolate=0, coffee=0, gas=0 ,cost=200),
            MenuItem(name="orio_shake,",water=50, milk=100, sugar=80, chocolate=200, coffee=0, gas=0 ,cost=499),
            MenuItem(name="milkshake,",water=60, milk=150, sugar=100, chocolate=0, gas=0, coffee=0, cost=300),
            MenuItem(name="chocolate_shake,",water=100, milk=150, sugar=10, chocolate=2, gas=0, coffee=0 ,cost=399)
        ]
        
    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
