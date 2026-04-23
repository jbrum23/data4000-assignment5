# data4000-assignment5

# Assignment 5 — Conditionals, Loops, Exceptions, and Libraries
## Required Installation
Before running Exercise 2, install the requests library by running this command in your terminal:

pip install requests

## How to Run Each Program
### Exercise 1 — Retail Checkout System
This program simulates a retail checkout system. Open the file in VS Code and run it from the terminal. It will prompt you for a student key, then enter a loop where you can add items by entering the item name, unit price, and quantity. Type DONE when you are finished entering items. The program calculates a subtotal, applies a 10% discount if 10 or more units were purchased or the subtotal reaches $100 or more, and applies a $3.00 member perk if the seed is odd. It then prints a full receipt summary.
### Exercise 2 — Inventory Management & API Spot Check
This program simulates an inventory management workflow. Open the file in VS Code and run it from the terminal. It will prompt you for a student key, then enter a loop where you can enter SKU codes and their on-hand quantities. Type DONE when you are finished. The program uses the seed to determine a reorder threshold and flags each SKU as REORDER or OK. After inventory entry, it performs a live API spot check using the iTunes Search API, searching for either weezer or drake depending on whether the seed is even or odd, and reports how many songs were returned.
## Example Run — Exercise 1
Student key: johnbrum
Enter item name (or DONE to finish): Shirt
Enter unit price: 20.00
Enter quantity: 2
Enter item name (or DONE to finish): Pants
Enter unit price: 35.00
Enter quantity: 1
Enter item name (or DONE to finish): DONE
Seed: 869
Units: 3
Subtotal: $75.00
Discount: 0%
Perk applied: YES
Total: $72.00

## Example Run — Exercise 2

Student key: johnbrum
SKU: Shirt-01
On hand: 5
SKU: Shirt-02
On hand: 8
SKU: DONE
Seed: 869
Threshold: 9
SKUs entered: 2
Reorder flagged: 2
Spotcheck term: drake
Songs returned: 5
API status: OK
