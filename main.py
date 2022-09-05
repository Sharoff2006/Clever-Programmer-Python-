# # # This is a comment

# # # Varaibles

# # age = 25
# # name = "Sharoff"
# # first_name, last_name = "Sharoff", "Haashim"
# # # print(name)
# # # print(first_name, last_name)


# # yourName = input("What's your name : ")
# # # print("Hello, " + yourName)

# # num01 = int(input("Enter a number : "))
# # num02 = int(input("Enter a number : "))
# # print(num01 + num02)


# # # Date types

# # # strings, number, float, int, list, dictionaries
# #  remaindrer = %
# # float = 0.2
# # integer = 0.2
# # Tip calculator

# food_amount = float(input("How much was your food ? : "))
# tip_paid = float(input("How much was your tip (percentage) ? : "))
# tip_amount = (tip_paid / 100) * food_amount
# total = tip_amount + food_amount
# print(f"\n")
# print("--------------------------------------------")
# print(
#     f"💁‍♂️ Tip = ${tip_amount}\n🍔 Food Amount = ${food_amount}\n💰 Total Pay Is : ${total}"
# )
# print("--------------------------------------------")
# print(f"\n")


# Boolean
# IF THEN ELSE

answer = input("How is the wheather ( Rainy, Sunny, Snowy ) : ")

if answer == "rainy":
    print("Grab your Umbrella! ☔")
elif answer == "snowy":
    print("Grab your coat! 🧥")
else:
    print("Grab your sunglasses! 😎")
