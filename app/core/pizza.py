import uuid

pizzas_orders = []

# les pizzas en cours
def pizzas_in_progress():
    pizzas_in_progress = [pizza for pizza in pizzas_orders if pizza['status'] == "in_progress"]
    return pizzas_in_progress

# toutes les pizzas
def pizzas():
    return pizzas_orders

# commander une pizza
def order_pizza(pizza: str):
    pizzas_orders.append({'name': pizza, 'status': 'in_progress', 'order': uuid.uuid4().hex})

# livrer une pizza
def delivery_pizza(order: str):
    for order in pizzas_orders:
        if order['order'] == order:
            order['status'] = 'delivered'

# annuler une pizza
def cancel_pizza(order: str):
    for order in pizzas_orders:
        if order['order'] == order and order['status'] == 'in_progress':
            order['status'] = 'canceled'
