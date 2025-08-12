customers = [
    {
        "customer_id": "C001",
        "name": "Jessica",
        "orders": [
            {
                "order_time": "14:30",  # 2:30 PM
                "items": [
                    {"name": "Caesar Salad", "price": 12.99},
                    {"name": "Grilled Salmon", "price": 24.99},
                    {"name": "Wine", "price": 18.50}
                ]
            },
            {
                "order_time": "19:15",  # 7:15 PM
                "items": [
                    {"name": "Steak", "price": 32.00},
                    {"name": "Soup", "price": 8.50},
                    {"name": "Dessert", "price": 12.00}
                ]
            }
        ]
    },
    {
        "customer_id": "C002", 
        "name": "Marcus",
        "orders": [
            {
                "order_time": "20:45",  # 8:45 PM
                "items": [
                    {"name": "Pizza", "price": 16.75},
                    {"name": "Breadsticks", "price": 6.99},
                    {"name": "Soda", "price": 3.50}
                ]
            },
            {
                "order_time": "12:00",  # 12:00 PM
                "items": [
                    {"name": "Burger", "price": 14.99},
                    {"name": "Fries", "price": 5.99}
                ]
            }
        ]
    }
]

# Your task: Create a variable called 'expensive_evening_items' using a list comprehension
# that contains the prices of items costing more than $15.00 from orders placed after 6 PM (18:00)
# 
# Hint: To check if an order was placed after 6 PM, you can compare the hour part of the time string
# You can extract the hour by splitting the time string: order["order_time"].split(":")[0]
# Then convert to integer and check if it's >= 18

# Complete the task using a regular loop
new_list = []
for customer in customers:
    for order in customer['orders']:
        # print(f'Order Time: {order['order_time']}')
        for item in order['items']:
            # print(f'Item Ordered: {item['name']} | Price: {item['price']}')
            if int(order['order_time'].split(':')[0]) >= 18 and item['price'] > 15:
                new_list.append(item['price'])
print(new_list)
                

# Extract the expensive orders
expensive_evening_items = [item['price'] for customer in customers for order in customer['orders'] for item in order['items'] if int(order['order_time'].split(':')[0]) >= 18 and item['price'] > 15]
print(expensive_evening_items)