class Palindrome:
    def __init__(self,word):
        self.word=word

    def __reversed__(self):
        return self.word[::-1]
        
    def check_for_palindrome(self):
        #self.flip_word()
        self.flipped=reversed(self)
        is_palindrome=True
        for z in range(len(self.word)):
            if not self.word[z]==self.flipped[z]:
                is_palindrome=False
                break
        print(self.__repr__(is_palindrome))

    def __repr__(self,is_palindrome):
        if is_palindrome:
            return "{} is a palindrome!!!".format(self.word)
        else:
            return "{} is not a palindrome.\n{} flipped is {}.".format(self.word,self.word,self.flipped)

word=input("Enter a word to check if it's a palindrome: ")
while not word.isalnum()or " " in word:
    print("You entered an invalid word. Try again. ")
    word=input("Enter a word to check if it's a palindrome: ")
palindrome=Palindrome(word)
palindrome.check_for_palindrome()


            
