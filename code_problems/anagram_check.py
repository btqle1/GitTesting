# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s = len(s)
        len_p = len(p)
        check_str = ""
        index = []
        p_sort = ''.join(sorted(p))
        for i in range (len_s - len_p +1):
            check_str = s[i:(i+len_p)]
            check_str_sort = ''.join(sorted(check_str))
            if check_str_sort == p_sort:
                index.append(i)
        print(index)
        return(index)