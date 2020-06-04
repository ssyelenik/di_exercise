alphabet="abcdefghijklmnopqrstuvwxyz"

message=input("Enter the message: ")
shift=input("What is the shift? (Enter an integer)")
while not shift.isnumeric():
    shift=input("Invalid entry. What is the shift? (Enter an integer)")
shift=int(shift)

e_d_crypt=input("Do you want to encrypt or decrypt? (Enter e for encrypt and d for decrypt)")
e_d_crypt.islower()
while not (e_d_crypt="d" or e_d_crypt="e"):
    e_d_crypt=input("Invalid input. Do you want to encrypt or decrypt? (Enter e for encrypt and d for decrypt)")

