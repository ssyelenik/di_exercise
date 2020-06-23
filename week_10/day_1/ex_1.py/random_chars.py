from random import choice
import string 
password=''.join(choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(5))
print(password)
