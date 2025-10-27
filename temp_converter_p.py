# taking function
# for fahrenheit

def celsius_to_fahrenheit(celsius):

    return (celsius * 9 / 5) + 32


# taking function
# for celsius

def fahrenheit_to_celsius(fahrenheit):

    return (fahrenheit - 32) * 5 / 9



# apply condition
while True:
    print("1.celsius to Fahrenheit")

    print("2.Fahrenheit to celsius")


    choice = input("enter the choice (1/2):= ")  # input function for choice

    if choice == "1":

        temp = float(
            input("enter the temperature in celsius:= ")
        )  # input function for taking input as celsius

        fahrenheit = celsius_to_fahrenheit(temp)  # calling method

        print(f"{temp}°C is = {fahrenheit}°F")  # for print the value

    elif choice == "2":

        temp = float(
            input("enter temperature in fahrenheit := ")
        )  # input function for taking input as fahrenheit

        celsius = fahrenheit_to_celsius(temp)  # calling function

        print(f"{temp}°F= {celsius}°C")  # for print the value

    else:
        print(
            "Invalid choice. ,,,,try again<<<<😂😂😂😂😂😂😂😂 or/// Ghar jake so jao😎😉😉😉😉"
        )  # aanyatha ye print hogi😀😀😀😀



"""
😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎
"""