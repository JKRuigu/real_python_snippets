phone = input ("Insert your phone number")
convert_digits = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"

}
output = ""
for char in phone:
    output += convert_digits.get(char, "!") + ""
print (output)