def clean_bite(bite):
    new_bite=""
    for index,bit in enumerate(bite):
        if index>1:
            new_bite=new_bite+bit
    return new_bite


def reverse_bite(bite):
    length=len(bite)
    reverse_bite=""

    increment=length-1
    while increment>=0:
        reverse_bite=reverse_bite+bite[increment]
        increment-=1

    thirty_two_bit=32-length
    zeros="0"*thirty_two_bit
    reverse_bite=reverse_bite+zeros
    
    return(reverse_bite)


