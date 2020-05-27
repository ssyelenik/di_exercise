from datetime import date
today=date.today()

birth_entry = input('Enter a date (i.e. 2017,7,1)')
year, month, day = map(int, birth_entry.split(','))

from datetime import datetime
birth_date = datetime(year, month, day)

print("Your date of birth is:", birth_date)

age=today.year-birth_date.year-((today.month,today.day)<(birth_date.month,birth_date.day))

print("You are",age,"years old.")



num_candles=age%10
if num_candles==0:
    num_candles=10


num_cakes=1
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           num_cakes=2

   else:
       num_cakes=2


print(num_cakes)

i=0
while(i<num_cakes+1):
    if num_candles%2!=0:
        spaces=(11-num_candles)/2
        print("    "+"_"*int(spaces)+"i"*int(num_candles)+"_"*int(spaces)+"    ")
    else:
        spaces=(11-num_candles-1)/2
        print("    "+"_"*int(spaces)+"i"*int(num_candles)+"_"*int(spaces+1)+"    ")
    print("   |:H:a:p:p:y:|")
    print(" __|___________|__")
    print("|^^^^^^^^^^^^^^^^^|")
    print("|:B:i:r:t:h:d:a:y:|")
    print("|                 |")
    print("~~~~~~~~~~~~~~~~~~~")
    i=i+1
     



    i=i+1
