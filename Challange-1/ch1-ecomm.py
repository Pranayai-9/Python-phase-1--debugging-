#Faulty code
products = ["Laptop", "Mouse", "Keyboard", "Mouse"]

prices = {
    "Laptop": 55000,
    "Mouse": 500,
    "Keyboard": 1500
}

quantities = [1, 2, 1, 3]

customer = {
    "name": "Rahul",
    "membership": "premium",
    "coupon": "SAVE10"
}


def calculate_bill(products, prices, quantities, customer):

    total = 0

    for i in range(len(products)):

        product = products[i]

        price = prices[product]

        quantity = quantities[i]

        total = price + quantity

    if customer["membership"] == "Premium":
        discount = total * 0.10

    elif customer["coupon"] == "SAVE10":
        discount = total * 0.05

    final_amount = total - discount

    unique_products = len(products)

    return total, discount, final_amount, unique_products


bill = calculate_bill(products, prices, quantities, customer)

print("Order Summary:", bill)



#Debugged code: my version
products = ["Laptop", "Mouse", "Keyboard", "Mouse", "Joystick"]
prices = {
    "Laptop": 55000,
    "Mouse": 500,
    "Keyboard": 1500
}
quantities = [1,2,1,3,9]  

customer = {
    "name": "Rahul",
    "membership": "premium",
    "coupon": "SAVE10"
}

def calculate_bill(products, prices, quantities, customer):

    total = 0
    if products is not None:
        for i in range(len(products)):
            product = products[i]
            price = prices.get(product, 0)
            quantity = quantities[i]
            valuee = price*quantity
            total += valuee
        if customer["membership"] == "premium" and customer["coupon"] == "SAVE10":
            discount = total * 0.15
        elif customer["membership"] != "premium" and customer["coupon"] == "SAVE10":
            discount = total * 0.05
        elif customer["membership"] == "premium" and customer["coupon"] != "SAVE10":
            discount = total * 0.10
        else:
            discount = int(0)
    else:
        total = 0
        discount = 0
    
    final_amount = total - discount

    unique_products = len(set(products))

    return total, discount, final_amount, unique_products


bill = calculate_bill(products, prices, quantities, customer)

print("Order Summary:", bill)

#Final corrected version:
def calculate_bill(products, prices, quantities, customer):

    if products is None or quantities is None:
        raise ValueError("Order information cannot be None")

    if len(products) != len(quantities):
        raise ValueError("Products and quantities must match")

    if not products:
        return 0, 0, 0, 0

    total = 0

    for product, quantity in zip(products, quantities):

        if product not in prices:
            raise ValueError(f"Unknown product: {product}")

        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
            raise ValueError(f"Invalid quantity for {product}")

        price = prices[product]

        total += price * quantity

    if customer.get("membership") == "premium":
        discount_rate = 0.15

    elif customer.get("coupon") == "SAVE10":
        discount_rate = 0.05

    else:
        discount_rate = 0

    discount = total * discount_rate

    final_amount = total - discount

    unique_products = len(set(products))

    return total, discount, final_amount, unique_products



