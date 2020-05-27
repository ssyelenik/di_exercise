word=""
while len(word)!=10:
    word=input("Please enter a word with 10 characters:")

print("The first letter of the word is",word[0], "and the last letter is", word[9])
for x in range(9):
    print(word[0:x])


new_letter1=word[5]
new_letter2=word[0]
new_letter3=word[1]
new_letter4=word[9]
new_letter5=word[7]
new_letter6=word[3]
new_letter7=word[2]
new_letter8=word[4]
new_letter9=word[6]
new_letter10=word[8]

new_word=new_letter1+new_letter2+new_letter3+new_letter4+new_letter5+new_letter6+new_letter7+new_letter8+new_letter9+new_letter10
print("Here's your word jumbled:",new_word)






