class Solution(object):
    def longestPalindrome(self, s):
        l = list(s)
        ##print(l)
        max = 0
        a = ""
        result = ""
        if len(l) == 1 or len(l) == 0:
            return s
        for i in range(len(l)):
            for j in range(i,len(l)):
                a = l[i:j+1] 
                # print("\n")  
                # print(a)             
                ##print(l[j])
                if l[i:j+1] == a[::-1]:
                    # print("par",len(a))
                    if len(a) > max:
                        max = len(a)
                        result = a
                    
                else:
                    pass
                    # print("notpar")
                    
                

        return("".join(result))




solution = Solution()

tiem = solution.longestPalindrome("yzwhuvljgkbxonhkpnxldwkaiboqoflbotqamsxyglfqniflcrtsxbsxlwmxowwnnxychyrjedlijejqzsgwakzohghpxgamecmhcalfoyjtutxeciwqupwlxrgdcpfvybskrytvmwkvnbdjitmohjavhmjobudvbsnkvszyrahpanocltwzeubgxkkthxhjgvcvygfkjctkubtjdocncmjzmxujetybdwmqutvrrulhlsbcbripctbkacwoutkrqsohiihiegqqlasykkgjjskgphieofsjlkkmvwcltgjqbpakercxypfcqqsmkowmgjglbzbidapmqoitpzwhupliynjynsdfncaosrfegquetyfhfqohxytqhjxxpskpwxegmnnppnnmgexwpkspxxjhqtyxhoqfhfyteuqgefrsoacnfdsnyjnyilpuhwzptioqmpadibzblgjgmwokmsqqcfpyxcrekapbqjgtlcwvmkkljsfoeihpgksjjgkkysalqqgeihiihosqrktuowcakbtcpirbcbslhlurrvtuqmwdbytejuxmzjmcncodjtbuktcjkfgyvcvgjhxhtkkxgbuezwtlconapharyzsvknsbvdubojmhvajhomtijdbnvkwmvtyrksbyvfpcdgrxlwpuqwicextutjyoflachmcemagxphghozkawgszqjejildejryhcyxnnwwoxmwlxsbxstrclfinqflgyxsmaqtoblfoqobiakwdlxnpkhnoxbkgjlvuhwzy")

## 再循环中如何正确使用pass continue break

## 如何自由控制输出内容后的换行
              
print(tiem)