from itertools import permutations
class Solution(object):
    def findSubstring(self, s, words):
        words_size = len(words)
        words_len = len(words[0])
        ans=[]
        per_lis = list(permutations(words))
        concatenations = []
        sl =(words_size**2-words_size)/2
        for perm in per_lis:
            concat = ''.join(perm)
            concatenations.append(concat)
        
        print(concatenations)
        for i in range((words_len)):
            list1=[]
            for j in range((len(s)-i)//words_len):
                sliced_p = s[i+j*words_len:i+j*words_len+words_len]
                if sliced_p in words:
                    list1.append(words.index(sliced_p))
                else: 
                    list1.append(999)
            print(list1)
            for ij in range(len(list1)-words_size+1):
                sum = 0
                for k in range(words_size):
                    sum += list1[ij+k]
                print(sum)
                if sum == sl:
                    if s[i+ij*words_len:i+ij*words_len+words_size*words_len] in concatenations:
                        print("aaaaaaaaaa",s[ij*words_len:ij*words_len+words_size*words_len])
                        ans.append(i+ij*words_len)
                elif sum < 998:
                    print("asasasd",ij*words_len,s[ij*words_len:ij*words_len+words_size*words_len])
                    a,b=ij*words_len,s[i+ij*words_len:i+ij*words_len+words_size*words_len]
                    print(a,b)
                    if s[i+ij*words_len:i+ij*words_len+words_size*words_len] in concatenations:
                        ans.append(i+ij*words_len)
                
            print("/n")
        return(ans)
                
            




        

solution = Solution()

##tiem = solution.findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"])
tiem = solution.findSubstring("pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel",["dhvf","sind","ffsl","yekr","zwzq","kpeo","cila","tfty","modg","ztjg","ybty","heqg","cpwo","gdcj","lnle","sefg","vimw","bxcb"])

print(tiem)