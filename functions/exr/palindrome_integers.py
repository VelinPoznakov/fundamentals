# 123, 323, 421, 121
def reverse_numner(int_num):
    rev_num = int_num[::-1]
    #print(f'Reversed value = {rev_num}')
    return rev_num

def is_palindrome(org_num):
    if reverse_numner(org_num) == org_num:
        return True
    else:
        return False

x = [str(x) for x in input().split(', ')]
#print(x)
#small_list = []
for num in x:
    int(num)
    #print(f'Original value = {num}')
    #print(f'Result = {is_palindrome(num)}')
    print(is_palindrome(num))

