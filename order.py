from pizza import Pizza
from utils import format_currency

def calculate_order(order_items):
    """
    order_items: list of dicts, e.g.
      [{"size": "large", "toppings": ["pepperoni", "mushrooms"]}, ...]
    """
    total = 0.0
    for item in order_items:
        p = Pizza(item['size'], item['toppings'])
        total += p.price()
    return total

def print_receipt(order_items):
    total = calculate_order(order_items)
    print("Your total is:", format_currency(total))