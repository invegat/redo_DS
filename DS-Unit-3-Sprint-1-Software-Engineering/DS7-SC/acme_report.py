#!/usr/bin/env python

import random
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']


def randomP():
    return Product(
        name=random.choice(ADJECTIVES) + ' ' + random.choice(NOUNS),
        price=random.randint(5, 100),
        weight=random.randint(5, 100),
        flammablility=random.uniform(0, 2.5)
    )


def generate_products(num_products=30):
    return [randomP() for _ in range(num_products)]


def inventory_report(l):
    # print("_______________________________")
    # for p in l:
    # print(p)
    # print("_______________________________")
    ap = sum([p.price for p in l])/len(l)
    aw = sum([p.weight for p in l])/len(l)
    af = sum([p.flammablility for p in l])/len(l)
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT", end='  ')
    print(
        f"Unique product names: {len(set([p.name for p in l  ]))} Average price: {ap}  Average Weight: {aw}  Average flammablility {af}"
    )


if  __name__ == '__main__':
    inventory_report(generate_products())
