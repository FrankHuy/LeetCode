class Solution(object):

    def __init__(self):
        self.rstr_ = ''

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if(strs.__len__() == 0):
            return self.rstr_
        elif(strs.__len__() == 1):
            return strs[0]
        minitem = min(strs, key = lambda x:len(x))
        minlen = len(minitem)
        for index in range(minlen):
            for i in range(len(strs)-1):
                if(strs[i][index] != strs[i+1][index]):
                    return self.rstr_
            self.rstr_ += strs[0][index]
        return self.rstr_


def main():
    a = Solution()
    strs = ['flow' , 'fly' , 'flight']
    st = a.longestCommonPrefix(strs)
    print(st)


if __name__ == "__main__":
    main()
