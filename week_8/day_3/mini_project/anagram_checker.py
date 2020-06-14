class AnagramChecker:
    def __init__(self):
        file = open("sowpods.txt","r")
        words=[]
        for line in file:
            stripped_line=line.strip()
            words.append(stripped_line)
        file.close()
        self.words=words

    def check_word(self,new_word):
        error="no_error"
        error=self.one_word(new_word)
        if not error=="no_error":
            return error

        new_word=self.clean_word(new_word)
        
        error=self.check_chars(new_word)
        if not error=="no_error":
            return error
        error=self.is_valid_word(new_word)
        return error

    def one_word(self,new_word):
        if " " in new_word:
            return "many_words"
        else:
            return "no_error"

    def clean_word(self,new_word):
        new_word=new_word.strip()
        return new_word
        

    def check_chars(self,new_word):
        if new_word.isalpha():
            return "no_error"
        else:
            return "wrong_chars"
        
        
    def is_valid_word(self,new_word):
        if new_word in self.words:           
            return "no_error"
        else:
            return "invalid_word"

    def get_anagrams(self,new_word):
        import sys
        from itertools import permutations
        
        perms = (p for p in permutations(new_word))
        
        list_all_perms=[]
        list_all_words=[]
        list_perms=[]
        
        for x in perms:
            list_all_perms.append(x)
            
        for j in range(len(list_all_perms)):
            temp="".join(list_all_perms[j])
            list_all_words.append(temp)
            
        for h in list_all_words:     
            if self.is_valid_word(h)=="no_error" and h!=new_word and h not in list_perms:
                list_perms.append(h)
                
        return list_perms

    def __repr__ (self,new_word,anagram_list):
        if len(anagram_list)==0:
            msg='\nYOUR WORD:"{}"\nthis is a valid English word, but there are no anagrams for it.'.format(new_word)
        else:
            msg='\nYOUR WORD:"{}"\nthis is a valid English word.\nAnagrams for your word:'.format(new_word)
            for i in range(len(anagram_list)):
                if i<len(anagram_list)-1:
                    msg=msg+" "+anagram_list[i]+", "
                else:
                    msg=msg+" "+anagram_list[i]
        return msg        
        

anagrams=AnagramChecker()






