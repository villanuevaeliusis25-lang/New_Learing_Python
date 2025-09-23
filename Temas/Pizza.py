def make_pizza(size, *toppings):
    """Crea una Pizza, segun numero de rebanadas y condimentos"""
    print(f"\nMaking a {size}-inch Pizza whit the following toppings")
    for topping in toppings:
        print(f"- {topping}")