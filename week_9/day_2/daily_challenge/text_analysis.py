class Text:
    
    def __init__(self,string):
        self.string=string
        content=[]
        with open("my_text.txt","r") as f:
            for line in f:
                line=line.strip()
                if line == "" or line==" ":
                    pass
                else:
                    content.append(line)
        self.content=str(content).lower()

    @classmethod
    def from_file(cls, txt_file):
        return cls(txt_file)

    def frequency(self):
        if self.content.count(self.string)>=1:
            return self.content.count(self.string)
        else:
            return "Your word was not found in the text."
        
    def most_common_word(self):
        res_str_temp=Text.no_stop_words
        highest_frequency=0
        frequency=0
        most_common_word=""
        for x in res_str_temp:
            frequency=res_str_temp.count(x)
            if frequency>highest_frequency:
                highest_frequency=frequency
                most_common_word=x
        Text.most_common_word=most_common_word
        return most_common_word

    def unique_words(self):
        unique_words=[]
        res_str_temp=Text.no_stop_words
        for x in res_str_temp:
            if res_str_temp.count(x)==1:
                if x not in unique_words:
                    unique_words.append(x)
        Text.unique_words=unique_words
        return unique_words

class TextModification(Text):
    def __init__(self,string):
        super().__init__(string)

    def remove_punctuation(self):
        res_str_temp=self.content.split()
        temp=""
        res_str=[]
        for x in res_str_temp:
            for y in x:
                if y.isalpha():
                    temp=temp+y
            if temp=="":
                pass
            else:
                res_str.append(temp)
            temp=""
        self.content_no_spaces=res_str
        return res_str

    def remove_stop_words(self):
        res_str_temp=self.content_no_spaces
        res_str=[]
        stop_words=["ourselves", "hers", "between", "yourself", "but", "again", "there", "about", "once", "during", "out", "very", "having", "with", "they", "own", "an", "be", "some", "for", "do", "its", "yours", "such", "into", "of", "most", "itself", "other", "off", "is", "s", "am", "or", "who", "as", "from", "him", "each", "the", "themselves", "until", "below", "are", "we", "these", "your", "his", "through", "don", "nor", "me", "were", "her", "more", "himself", "this", "down", "should", "our", "their", "while", "above", "both", "up", "to", "ours", "had", "she", "all", "no", "when", "at", "any", "before", "them", "same", "and", "been", "have", "in", "will", "on", "does", "yourselves", "then", "that", "because", "what", "over", "why", "so", "can", "did", "not", "now", "under", "he", "you", "herself", "has", "just", "where", "too", "only", "myself", "which", "those", "i", "after", "few", "whom", "t", "being", "if", "theirs", "my", "against", "a", "by", "doing", "it", "how", "further", "was", "here", "than"]
        for x in res_str_temp:
            if x not in stop_words:
                res_str.append(x)
        Text.no_stop_words=res_str
        return res_str



new_text = Text.from_file("able")
print("The frequency of '{}' in the file is {}." .format(new_text.string,new_text.frequency()))

child_text=TextModification("easy")
print("The frequency of '{}' in the file is {}." .format(child_text.string,child_text.frequency()))

print("The file without punctuation, numbers, and symbols:",child_text.remove_punctuation())

no_stop=child_text.remove_stop_words()
print("The file without stop words:",no_stop)

print("The most common word is: ",child_text.most_common_word())

print("The list of unique words is: ",child_text.unique_words())
