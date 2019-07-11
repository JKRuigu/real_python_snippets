
def digits_converts(phonenumber):
    output = ""
    convert_digits = {"1":"One", "2":"Two", "3":"Three", "4":"Four"}

    for digit in phonenumber:
        output = output + convert_digits.get(digit, "!") + ""
    return output


phone= input("Please provide your phonenumber")
print(digits_converts(phone))


#user_input = input("Insert your phone number")

#digits_converters = {
   # "1":"One",
    #"2":"Two",
    #"3":"Three",
    #"4":"Four"
#}
#output = ""
#for digit in user_input:
# output = output + digits_converters.get(digit, '!')
#print (output)