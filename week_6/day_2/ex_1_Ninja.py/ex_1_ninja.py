# Exercise 1
i=0
num_list=[]
while i<10:
    num=input("Enter a number between -100 and 100: ")
    num=int(num)
    valid_num="no"
    while valid_num=="no":
        try:
            int(num)
            valid_num="yes"
        except:
            num=input("Invalid entry. Enter a number between -100 and 100: ")
            num=int(num)
    
    while num<-100 or num>100:
        num=input("Invalid entry. Enter a number between -100 and 100: ")
        num=int(num)
    num_list.append(num)
    i=i+1
else:
    print("Here's your list:",num_list)

#num_list=[3, 47, 99, -80, 22, 97, 54, -23, 5, 7]


ordered_list=sorted(num_list,reverse=True)
print("This is the list sorted largest to smallest:",ordered_list)

print("This is the sum:",sum(num_list))

first_last_list=[num_list[0],num_list[len(num_list)-1]]
print("This is the first and last items only:",first_last_list)

large_list=[]
for x in num_list:
    if x>50:
        large_list.append(x)
print("These numbers are larger than 50", large_list)

small_list=[]
for y in num_list:
    if y<10:
        small_list.append(y)
print("These numbers are smaller than 10", small_list)

exponents=[]
for z in num_list:
    exponents.append(z**2)
print("The exponent of each item is:",exponents)

print("The average of the numbers is:",sum(num_list)/len(num_list))

print("The largest number is:",ordered_list[0])

print("The smallest number is:",ordered_list[len(ordered_list)-1])
    
# Exercise 2
paragraph="Pneumonia was not a nice old gentleman. A nice old gentleman would not hurt a weak little woman from California. But Pneumonia touched Johnsy with his cold fingers. She lay on her bed almost without moving, and she looked through the window at the wall of the house next to hers."

print(paragraph)

num_characters=len(paragraph)
print("The number of characters in the paragraph is: ", num_characters)

paragraph_sentences=paragraph.split(".")
num_sentences=len(paragraph_sentences)
print("The number of sentences in the paragraph is: ",num_sentences)

paragraph_words=paragraph.split(" ")
num_words=len(paragraph_words)
print("The number of words in the paragraph is: ", num_words)


counter=0
for x in paragraph_words:
    if paragraph.count(x)>1:
        counter=counter+1
print("The number of unique words is: ", num_words-counter)

count_spaces=0
for y in paragraph:
    if y==" ":
        count_spaces=count_spaces+1
print("The number of non-white spaces is: ", num_characters-count_spaces)


#avg number of words in a sentence
sum=0
words_in_sentence=[]
words_per_sentence_list=[]
num_sentences=0
for z in paragraph_sentences:
    if not z=="":
        num_sentences=num_sentences+1
        if z[0]==" ":
            z=z[1:]
    
        words_in_sentence=z.split(" ")

        words_per_sentence_list.append(len(words_in_sentence))

    
for a in words_per_sentence_list:
    sum=sum+a
average=sum/num_sentences
print("The average number of words per sentence is: ",average)


# Exercise 3
raw_student_details = input("Enter a list in the following format: (name1,age1,score1),(name2,age2,score2):")
student_details = []

for tup in raw_student_details.split('),('):
    #tup looks like `(a,a` or `b,b`
    tup = tup.replace(')','').replace('(','')
    #tup looks like `a,a` or `b,b`
    single_student=tuple(tup.split(','))
    name,age,score=single_student
    
    age=int(age)
    score=float(score)
    single_student_fix=(name,age,score)
    student_details.append(single_student_fix)

print("Here's the list of students: ", student_details)
#sort by name then age then score
sorted_student_details = sorted(student_details, key=lambda item: (item[0], item[1], item[2]))
print("Here's the sorted list of students: ",sorted_student_details)

# Exercise 4

#sentence="New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
sentence=input("Enter a sentence: ")
words=sentence.split(" ")
sorted_words=sorted(words)

increment=0
first_occurrance=0
for i in sorted_words:
    num_occurances=sorted_words.count(i)
    first_occurrance = sorted_words.index(i)
    if increment==first_occurrance:
        print(i,":",num_occurances)
    increment=increment+1

# Exercise 5
print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)

# Exercise 6
num_input=input("Enter a list of numbers separated by commas: ")
num_list=[]
num_tuple=()
num_tuple=tuple(num_input.split(","))
num_list=num_input.split(",")
print(num_list)
print(num_tuple)

# Exercise 7
import math
C=50
H=30
D_input=input("Enter a list separated by commas for the values of D: ")
D_raw=D_input.split(",")
D=[]
for i in D_raw:
    D.append(int(i))

answers=[]
for x in D:
    Q=math.sqrt((2*C*x)/H)
    answers.append(int(Q))

print(answers)

