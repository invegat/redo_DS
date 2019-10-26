#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_set_product_weight(self):
        """Test  set product weight being 100."""
        prod = Product(name='Test Product', weight=100)
        self.assertEqual(prod.weight, 100)


class AcmeReportTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_num_products(self):
        """Test default number of products being 30."""
        l = generate_products()
        self.assertEqual(len(l), 30)

    def test_legal_names(self):
        """Test if all names are legal"""
        l = generate_products()
        for p in l:
            a, n = p.name.split(' ')
            self.assertIn(a, ADJECTIVES)
            self.assertIn(n, NOUNS)





if __name__ == '__main__':
    unittest.main()