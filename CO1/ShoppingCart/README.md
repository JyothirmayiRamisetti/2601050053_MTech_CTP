Online Shopping Cart System

Description

This project contains a Python script that implements an Online Shopping Cart System. The system allows users to add products to a shopping cart, remove products, change product quantities, view the cart, calculate the subtotal, apply a discount, calculate GST, and generate the final bill.

Algorithm

The script uses functions and a dictionary to manage products and their quantities. The step-by-step algorithm is as follows:

Initialize Cart: Create an empty cart to store product names, prices, and quantities.

Add Product: Ask the user to enter the product name, price, and quantity.

Check Product: Check whether the product already exists in the cart. If it exists, increase its quantity. Otherwise, add the product as a new item.

Remove Product: Ask the user for the product name and remove the product from the cart if it exists.

Change Quantity: Ask the user for the product name and the new quantity. Update the quantity of the selected product.

Display Cart: Display all products in the cart along with their prices, quantities, and individual amounts.

Calculate Subtotal: Calculate the amount of every product using price multiplied by quantity and add all product amounts to obtain the subtotal.

Apply Discount: If the subtotal is Rs.1000 or more, apply a 10% discount.

Calculate GST: Calculate 18% GST on the amount remaining after the discount.

Calculate Final Amount: Add the GST to the taxable amount to calculate the final bill amount.

Input and Output

Input

Enter choice: 1

Enter product name: Keyboard

Enter product price: 850

Enter quantity: 2

Output

2 x Keyboard added to cart.

Enter choice: 5

Output

Product             Price       Quantity  Amount
------------------------------------------------------
Keyboard            Rs.850.00   2         Rs.1700.00

Subtotal       : Rs.1700.00
Discount       : Rs.170.00
Taxable Amount : Rs.1530.00
GST (18%)      : Rs.275.40
Final Amount   : Rs.1805.40
