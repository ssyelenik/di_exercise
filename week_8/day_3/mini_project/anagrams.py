exec(open(r"C:/BootCampComplete/di_exercise/week_8/day_3/mini_project/anagram_checker.py").read())
while True:
    while True:
        print("")
        print("    ***Welcome to Anagrams!!***")
        print("")
        play=input('Would you like to input a word or exit?\nType "y" to play | Type "n" to exit \n>>>')
        play=play.lower()
        print("")
        if not(play=="y" or play=="n"):
            print("Invalid entry. Try again.")
        elif (play=="n"):
            print("OK then, goodbye!")
            import sys
            sys.exit()
        elif (play=="y"):
            break
        
    while True:
        new_word=input("Enter a word: ")
        new_word=new_word.upper()
        error=anagrams.check_word(new_word)
        if error=="many_words":
            print("You may only enter one word. Try again!\n")
        elif error=="wrong_chars":
            print("You may only enter alphabetic characters. Try again!\n")
        elif error=="invalid_word":
            print("{} is invalid. Try again!\n".format(new_word))
        elif error=="no_error":
            print("{} is a valid word!\n".format(new_word))
            break

    anagram_list=anagrams.get_anagrams(new_word)

    
    print(AnagramChecker.__repr__(anagrams,new_word,anagram_list))
