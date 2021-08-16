with open("Currency.txt") as f:
    lines = f.readlines()

Currency_dict = {}
for line in lines:
    parsed = line.split("\t")
    Currency_dict[parsed[0]] = parsed[1]

amount = int(input("Enter amount:\n"))
print("""Enter the name of currency you want to convert this amount to?
Available options:\n
""")

[print(item) for item in Currency_dict.keys()]

currency = input("Please enter one of these values: \n")
print(f"{amount} PKR is equal to {amount*float(Currency_dict[currency])} {currency}")
