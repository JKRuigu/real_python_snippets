try:
    age = int(input("Age: "))
    print(age)
    income = 20000
    risk = income /age
    print (risk)

except ValueError:
    print("Invalid value, try again!")

except ZeroDivisionError:
    print("Hey, age cannot be zero")