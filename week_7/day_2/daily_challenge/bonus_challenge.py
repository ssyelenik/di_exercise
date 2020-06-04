def main():
    import random

    list_of_numbers = [random.randint(0, 1000) for _ in range(2000)]
    target_number   = 3728

    pairs=[]
    pairs=sum_pairs(list_of_numbers)
    pairs_to_target_number=get_pairs_to_target_number(pairs,target_number)
    print(pairs_to_target_number,"random pairs sum up to 3728!")
    
def sum_pairs(list_of_numbers):
    sum_pairs=[]
    for index_first in range(0,len(list_of_numbers)-2):
        for index_second in range(1,len(list_of_numbers)-1):
            if index_first==index_second:
                continue
            temp_sum=list_of_numbers[index_first]+list_of_numbers[index_second]
            sum_pairs.append(temp_sum)
    return sum_pairs

def get_pairs_to_target_number(num,target_number):
    match=0
    for x in num:
        if x==target_number:
            match+=1
    return match


main()
        


