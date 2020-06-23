from bits import clean_bite as cb,reverse_bite as rb
number=input("Enter a number.")
while True:
    try:
        number=int(number)
        break
    except:
        number=input("Invalid number. Enter the number again.")

bite = bin(number)

bite=cb(bite)
print("Your number in bites is:",bite)

new_bite=rb(bite)
print("The bites reversed are:",new_bite)

reversed_int=int(new_bite,2)
print("The reversed 32 bit number is:",reversed_int)


