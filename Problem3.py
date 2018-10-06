
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        r=""   #储存无重复子串
        maxNum=0  #最大无重复子串的长度
        for i in s:
            if i not in r:           #如果不在子串里，就代表无重复，直接插进去
                r=r+i
            else:                     #如果在子串里，就代表重复了，不能直接插进去
                if len(r)>maxNum:maxNum=len(r)     #先算出来上一个子串的长度
                r = r[r.index(i)+1:]+i          #把这个相同字符后面的保留。比如"dvdf"。第一个子串是"dv",再遍历到d的时候，需要把第一个d后面的v保留，再形成一个"vd"子串,这样还是无重复子串。不保留v的话，就不是一个完整的无重复子串了
        if len(r) > maxNum: maxNum = len(r)
        return maxNum


s="dvdf"
a=Solution()
print(a.lengthOfLongestSubstring(s))
