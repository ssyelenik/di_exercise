matrix=[
    ["7"," ","3"],
    ["T","s","i"],
    ["h","%","x"],
    ["i"," ","#"],
    ["s","M"," " ],
    ["$","a"," " ],
    ["#","t","%"],
    ["i","r","!"]
    ]

def main():
    col1=get_column(0)
    col2=get_column(1)
    col3=get_column(2)

    msg1=extract_msg(col1)
    msg2=extract_msg(col2)
    msg3=extract_msg(col3)
    print(msg1,msg2,msg3)

    message=concat_messages(msg1,msg2,msg3)

    print_msg(message)

def get_column(col):
    column=[]
    for index in matrix:
        column.append(index[col])
    return column

def extract_msg(code):
    symbols="!@#$%^&*()_-+={}[]"
    message=[]
    for index,char in enumerate(code):
        if char==" " or char.isnumeric():
            continue
        elif char.isalnum():
            message.append(char)
        elif char in symbols:
            if index<len(code)-1:
                if code[index+1] in symbols:
                    continue
                else:
                    message.append(" ")
    return message
            
def concat_messages(msg1,msg2,msg3):
    message=msg1+msg2+msg3

    return message

def print_msg(message):
    for p in message:
        print(p,end="")
main()
