class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        reverselist = list(s)
        reverselist.reverse()
        reverse_s = ''.join(reverselist)
        if (s == reverse_s):
            return True
        else:
            return False


def main():
    a = Solution()
    result = a.isPalindrome(-123)
    print(result)


if __name__ == '__main__':
    main()
