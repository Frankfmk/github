def check_palindrome(st):
    new_st = st.replace(' ', '').lower()
    lst = [l for l in new_st]
    re_lst = lst[:]
    re_lst.reverse()
    #print(lst, re_lst)
    if re_lst == lst:
        return True
    else: return False

while True:
    wrd = input('Enter your palindrome: ')
    if len(wrd) < 1:
        break
    else: print(check_palindrome(wrd))
