#Faulty code
customers = [
    ("C101", "Ananya", "Bangalore"),
    ("C102", "Rahul", "Mumbai"),
    ("C103", "Meera", "Bangalore"),
    ("C104", "Arjun", "Chennai"),
    ("C105", "Kiran", "Mumbai")
]

transactions = [
    {"customer_id": "C101", "amount": 5000},
    {"customer_id": "C102", "amount": 3000},
    {"customer_id": "C101", "amount": 2000},
    {"customer_id": "C104", "amount": 7000}
]


def generate_report(customers, transactions):

    total_revenue = 0

    purchased_customers = []

    cities = []

    for transaction in transactions:

        total_revenue += transaction["amount"]

        purchased_customers.append(transaction["customer_id"])

    for customer in customers:

        if customer[0] not in purchased_customers:
            purchased_customers.append(customer[0])

        cities.append(customer[2])

    unique_cities = len(cities)

    loyal_customers = []

    for transaction in transactions:

        if transaction["amount"] > 4000:
            loyal_customers.append(transaction["customer_id"])

    return {
        "revenue": total_revenue,
        "purchased": purchased_customers,
        "cities": unique_cities,
        "loyal_customers": loyal_customers
    }


report = generate_report(customers, transactions)

print(report)


#Debugged code
customers = [
    ("C101", "Ananya", "Bangalore"),
    ("C102", "Rahul", "Mumbai"),
    ("C103", "Meera", "Bangalore"),
    ("C104", "Arjun", "Chennai"),
    ("C105", "Kiran", "Mumbai")
]

transactions = [
    {"customer_id": "C101", "amount": 2000},
    {"customer_id": "C102", "amount": 3000},
    {"customer_id": "C101", "amount": 2000},
    {"customer_id": "C104", "amount": 7000}
]


def generate_report(customers, transactions):

    total_revenue = 0

    purchased_customers = []

    cities = []

    not_customers = []

    trial_customers = []

    for transaction in transactions:
        total_revenue += transaction["amount"]
        purchased_customers.append(transaction["customer_id"])
    

    for customer in customers:
        trial_customers.append(customer[0])
        cities.append(customer[2])

    unique_cities = len(set(cities))
    final_customers = set(purchased_customers) 
    not_customers = set(trial_customers) - final_customers 

    loyal_customers = []
    customer_totals = {}
    
    
    for transaction in transactions:
        customer_id = transaction["customer_id"]
        amount = transaction["amount"]
        if customer_id in customer_totals:
            customer_totals[customer_id] += amount
        else:
            customer_totals[customer_id] = amount
    print(customer_totals)


    for customer_id, amount in customer_totals.items():
        if amount > 5000:
            loyal_customers.append(customer_id)

    return {
        "revenue": total_revenue,
        "purchased": final_customers,
        "cities": unique_cities,
        "loyal_customers": loyal_customers,
        "not_customers": not_customers,
        "customer_spending": customer_totals
    }


report = generate_report(customers, transactions)

print(report)
