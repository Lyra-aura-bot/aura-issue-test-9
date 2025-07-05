class Pizza:
    def __init__(self, size, toppings):
        self.size = size        # "small", "medium", or "large"
        self.toppings = toppings  # e.g. ["pepperoni", "extra cheese"]

    def price(self):
        base_prices = {
            'small': 8.0,
            'medium': 10.0,
            'large': 12.0
        }
        return base_prices[self.size] + 1.0 * len(self.toppings)