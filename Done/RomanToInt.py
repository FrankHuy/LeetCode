class Solution(object):
    '''给定一个罗马数字，将其转换成整数，输入确保在 1 到 3999 的范围内'''
    def __init__(self):
        self._romandic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        self.result_ = 0

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        while i < len(s):
            if (i == len(s) - 1):
                self.result_ += self._romandic[s[i]]
                i += 1
            elif (self._romandic[s[i]] >= self._romandic[s[i + 1]]):
                self.result_ += self._romandic[s[i]]
                i += 1
            else:
                self.result_ += self._romandic[s[i + 1]] - self._romandic[s[i]]
                i += 2
        return self.result_


def main():
    a = Solution()
    re = a.romanToInt('LVIII')
    print(re)


if __name__ == "__main__":
    main()
