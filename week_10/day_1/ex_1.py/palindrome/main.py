import palindrome as py

word=input("Enter a word to check if it's a palindrome: ")

while not word.isalnum()or " " in word:
    print("You entered an invalid word. Try again. ")
    word=input("Enter a word to check if it's a palindrome: ")

palindrome=py.Palindrome(word)

palindrome.check_for_palindrome()
