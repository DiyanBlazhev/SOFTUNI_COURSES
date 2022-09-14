class Inventory:
    items = []

    def __init__(self, capacity: int):
        self.__capacity = capacity

    def add_item(self, item: str):

        self.item = item
        if len(Inventory.items) < self.__capacity:
            Inventory.items.append(self.item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        left_capacity = abs(self.__capacity - len(Inventory.items))

        return f"Items: {self.items}.\nCapacity left: {self.left_capacity}"



