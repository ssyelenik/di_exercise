def clean_bite(bite):
    new_bite=""
    for index,bit in enumerate(bite):
        if index>1:
            new_bite=new_bite+bit
    return new_bite


def reverse_bite(bite):
    length=len(bite)
    reverse_bite=""

    increment=length-1
    while increment>=0:
        reverse_bite=reverse_bite+bite[increment]
        increment-=1

    thirty_two_bit=32-length
    zeros="0"*thirty_two_bit
    reverse_bite=reverse_bite+zeros
    
    return(reverse_bite)


number=input("Enter a number.")
while True:
    try:
        number=int(number)
        break
    except:
        number=input("Invalid number. Enter the number again.")

bite = bin(number)

bite=clean_bite(bite)
print("Your number in bites is:",bite)

new_bite=reverse_bite(bite)
print("The bites reversed are:",new_bite)

reversed_int=int(new_bite,2)
print("The reversed 32 bit number is:",reversed_int)

