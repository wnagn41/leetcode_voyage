import random
def longestPalindrome():
    a = input("Enter a number: ") 
    offer = ['大象','狮子', '老鼠']
    random_pick = random.choice(offer)
    if a == random_pick:
        print('u lose,pick again')
        return(longestPalindrome())
    elif a == '大象':
        if random_pick == '老鼠':
            print('u lose,pick again')
            return(longestPalindrome())
        else:
            print('uwin')
            return()
    elif a == '狮子':
        if random_pick == '大象':
            print('u lose,pick again')
            return(longestPalindrome())
        else:
            print('uwin')
            return()
    elif a == '老鼠':
        if random_pick == '狮子':
            print('u lose,pick again')
            return(longestPalindrome())
        else:
            print('uwin')
            return()
    else:
        print('wrong iputd')
        return()           

        # //大象 狮子 老鼠//
        

longestPalindrome()


# solution = Solution()

# tiem = solution.longestPalindrome()

              
# print(tiem)