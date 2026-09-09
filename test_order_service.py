from decimal import Decimal

from order_service import calculate_total


def test_calculate_total_applies_percentage_discount():
    assert calculate_total(Decimal("100.00"), 1, Decimal("0.20")) == Decimal("80.00")


def test_calculate_total_supports_multiple_items():
    assert calculate_total(Decimal("25.00"), 4, Decimal("0.10")) == Decimal("90.00")
