#import pdb
class Solution:
    def lengthOfLongestSubstring(self, s):
        length = len(s)
        if(length == 0):
            return 0
        lengthdict = dict()
        for movelocation in range(length):
            for cutlength in range(1,length+2):
                #pdb.set_trace()
                if((movelocation + cutlength - 1) == length):
                    #pdb.set_trace()
                    lengthdict[str(movelocation)] = cutlength-1
                    break
                #pdb.set_trace()
                ptr = s[movelocation:movelocation+cutlength]
                if(self.HasRepeatedLetter(ptr)):
                    #pdb.set_trace()
                    lengthdict[str(movelocation)] = cutlength-1
                    break
        #pdb.set_trace()
        a = max(lengthdict,key = lengthdict.get)
        return  lengthdict[str(a)]
    def HasRepeatedLetter(self,string):
        #pdb.set_trace()
        for s in string:
            if s in string[:string.index(s)]+string[string.index(s)+1:]:
                return True
        return False

def main():
    a = Solution()
    print(a.lengthOfLongestSubstring("abcdefaaaaa")

if __name__ == '__main__':
    main()