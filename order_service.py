from decimal import Decimal


def calculate_total(price: Decimal, quantity: int, discount: Decimal) -> Decimal:
    return price * quantity * (1 - discount)
