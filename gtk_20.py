#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 14:41:37 2023

@author: rickyd
"""

BUY_IT = 0
QUANTITY = 1
PRODUCT = 2
PRODUCT_CATEGORY = 0
PRODUCT_CHILD = 1


GroceryItem = ((PRODUCT_CATEGORY, True, 0, "Cleaning Supplies"), 
               (PRODUCT_CHILD, True, 1, "Paper Towels" ),
               (PRODUCT_CHILD, True, 3, "Toilet Paper" ),
               (PRODUCT_CATEGORY, True, 0, "Food"),
               (PRODUCT_CHILD, True, 2, "Bread" ),
               (PRODUCT_CHILD, False, 1, "Butter" ),
               (PRODUCT_CHILD, True, 1, "Milk" ),
               (PRODUCT_CHILD, False, 3, "Chips" ),
               (PRODUCT_CHILD, True, 4, "Soda" ))


for row in GroceryItem:
    (ptype, buy, quant, prod) = row
    if ptype == PRODUCT_CATEGORY:
        (ptype1, buy1, quant1, prod1) = GroceryItem[1]
        print(ptype1, " ", buy1, " ", quant1, " ", prod1)
    