"""Randomly pick customer and print customer info"""

import random
import customers

def pick_winner(customers):
    """Choose a random winner from list of customers."""

    chosen_customer = random.choice(customers)
    
    name = chosen_customer.name
    email = chosen_customer.email

    print(f"Tell {name} at {email} that they've won")


def run_raffle():
    """Run the weekly raffle."""

    customer_list = customers.get_customers_from_file("customers.txt")
    pick_winner(customer_list)

if __name__ == "__main__":
    run_raffle()


