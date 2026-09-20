

discount=10

def calculate_total(price,tax_rate,discount):

    tax_rate =  0.08
  

    tax = price * tax_rate

    final_price = price + tax - discount

    print(f"Total: ${final_price}")

calculate_total(price=100)

def add_print(a,b):
    print(a+b)

add_print(a=5,b=10)

def add_return(a,b):
    return a + b


add_return(5,5)

def calculate_area(width, height):
    area = width * height
    return area

room_area = calculate_area (10,12)
# print(f"Room size: {room_area}" sq ft)