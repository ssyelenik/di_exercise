class Sentence_Maker:

    def __init__(self):
        self.sentence=[]

    @staticmethod
    def get_words_from_file():
        words=[]
        word_file=open("sowpods.txt","r")
        words_temp=word_file.readlines()
        for word in words_temp:
            word=word.strip()
            words.append(word)
        return words
    
    @staticmethod
    def get_random_sentence(words,length):
        sentence=""
        import random
        for i in range(length):
            spec_word=random.randint(0,len(words))
            if len(sentence)==0:
                print("first word")
                sentence=words[spec_word]

            else:
                sentence=sentence+" "+words[spec_word]
        return sentence.lower()

def main():
    print("Enter a number representing the length of the desired sentence.\nPython will then randomly create a sentence of the specified length.\n")
    length=input("Enter a sentence length between 2 and 20: ")

    try:
        length = int(length)
    except:    
        print("Invalid number. Goodbye!")
        import sys
        sys.exit()
           
    while length<2 or length>20:
        print("Number out of range. Goodbye!")
        import sys
        sys.exit()

    game=Sentence_Maker()
    words=game.get_words_from_file()
    print("\nYour new sentence is:\n"+game.get_random_sentence(words,length))


if __name__ == "__main__":
    main()
        
        
