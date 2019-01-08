# import pdb
# from collections import Counter
# class Solution(object):
#         def __init__(self):
#                 self._dict = {'(':')',')':'(','[':']',']':'[','{':'}','}':'{'}

#         def isValid(self, s):
#                 if(len(s)%2==1):
#                         return False
#                 c = Counter(s)
#                 counter_dict = dict(c)
#                 if(len(counter_dict)%2==1):
#                         return False
#                 #list_c = list(counter_dict.keys())
#                 for key in counter_dict.keys():
#                         if not counter_dict.get(self._dict[key]):
#                                 return False
#                 sort_counter_list = sorted(counter_dict.items(),key = lambda x:x[0])
#                 for i in range(int(len(sort_counter_list)/2)):
#                         if(sort_counter_list[i*2][1]!=sort_counter_list[i*2+1][1]):
#                                 return False
#                 return True

# def main():
#         s = Solution()
#         print(s.isValid('(]'))
# #pdb.set_trace()
# if __name__ == '__main__':
#         main()


class Solution(object):
    def __init__(self):
        self._leftlist = ['(', '[', '{']
        self._rightlist = [')', ']', '}']
        self._stack = list()

    def isValid(self, s):
        if (len(s) == 0):
            return True
        for cha in s:
            if self._leftlist.__contains__(cha):
                self._stack.append(cha)
            elif self._rightlist.__contains__(cha):
                if (len(self._stack) == 0):
                    return False
                elif (self._rightlist.index(cha) == self._leftlist.index(
                        self._stack[len(self._stack) - 1])):
                    self._stack.pop()
                else:
                    return False
            else:
                return False
        if (len(self._stack) == 0):
            return True
        else:
            return False


def main():
    s = Solution()
    print(s.isValid('([)]'))


# pdb.set_trace()
if __name__ == '__main__':
    main()
