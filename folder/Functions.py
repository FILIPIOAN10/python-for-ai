

def greetings():
    print("Hello! ")
    print("Hello Again ! ")

greetings()

def say_goodbye():
    print("GoodBye!")
    print("See you later")

say_goodbye()
say_goodbye()
say_goodbye()

def check_weather():
    temperature = 16
    if temperature > 15:
        print("It s nice hot")
    else:
        print("It's nice weather")

check_weather()

## with parameters

def calculate_total(price,tax_rate,discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total: ${final_price}")


calculate_total(100,0.08,10)