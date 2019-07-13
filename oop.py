class ShoppingCart(object):
    # initialize class attribute
    def __init__(self):
        self.total = 0
        self.items = {}
        # method to add items

    def add_item(self, item_name, quantity, price):
        # add costs to current total value
        self.total += price * quantity
        # updates the quantity of items
        self.items.update({item_name: quantity})
        # remove items

    def remove_item(self, item_name, quantity, price):
        if item_name in self.items:

            if quantity < self.items[item_name] and quantity > 0:
                self.items[item_name] -= quantity
                self.total -= price * quantity

            elif quantity >= self.items[item_name]:
                self.total -= price * self.items[item_name]
                # delete item
                del self.items[item_name]

    # method to check out
    def checkout(self, cash_paid):
        if cash_paid >= self.total:
            return cash_paid - self.total
        return "Cash paid not enough"