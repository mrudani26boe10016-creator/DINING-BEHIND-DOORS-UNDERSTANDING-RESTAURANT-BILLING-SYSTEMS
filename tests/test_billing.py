import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from billing import (
    calculate_item_total,
    calculate_subtotal,
    calculate_discount,
    calculate_tax,
    calculate_bill,
)


class TestBilling(unittest.TestCase):

    def test_item_total(self):
        self.assertEqual(calculate_item_total(150, 2), 300)

    def test_subtotal(self):
        menu = {"Burger": {"price": 150}}
        order = {"Burger": 2}
        self.assertEqual(calculate_subtotal(order, menu), 300)

    def test_discount_below_threshold(self):
        self.assertEqual(calculate_discount(500), 0)

    def test_discount_tier(self):
        self.assertEqual(calculate_discount(1000), 100)

    def test_tax(self):
        self.assertAlmostEqual(calculate_tax(100), 5)

    def test_complete_bill(self):
        menu = {"Burger": {"price": 150}}
        order = {"Burger": 2}
        bill = calculate_bill(order, menu)

        self.assertEqual(bill["subtotal"], 300)
        self.assertEqual(bill["discount"], 0)
        self.assertAlmostEqual(bill["tax"], 15)
        self.assertAlmostEqual(bill["total"], 315)


if __name__ == "__main__":
    unittest.main()
