# Exercise 1
def get_full_name(**name):
    for key,value in name.items():
        print(value,end=" ")
    print("")


                
first=input("Enter your first name: ")
middle=input("Enter your middle name (optional): ")
last=input("Enter your last name: ")
if middle=="":
    get_full_name(first_name=first,last_name=last)
else:
    get_full_name(first_name=first,middle_name=middle,last_name=last)

# Exercise 3
def get_longest_word(words):
    longest=words[0]
    for x in range(0,len(words)):
        if len(words[x])>len(longest):
            longest=words[x]
            break

    return longest

def display_word(word,longest_word):
    print("*",word," "*(len(longest_word)-len(word))+"*")

def print_list(words,longest_word):
    margin=1
    frame=len(longest_word)+margin*2+2
    print("*"*frame)

    for x in words:
        display_word(x,longest_word)

    print("*"*frame)

        

user_words=input("Enter the words you wish to frame, separated by commas: ")
words=user_words.split(",")
longest_word=get_longest_word(words)
print_list(words,longest_word)


# Exercise 4: Purpose--order the list in ascending order

def insertion_sort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print(alist)


        
