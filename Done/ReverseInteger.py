class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = list()
        if (x < 0):
            number = abs(x)
        elif (x > 0):
            number = x
        else:
            return 0
        while (number):
            result.append(str(number % 10))
            number = int(number / 10)
        rnumber = int(''.join(result))
        if (rnumber > (pow(2, 31) * (-1)) and rnumber < (pow(2, 31) - 1)):
            if (x < 0):
                return rnumber * (-1)
            else:
                return rnumber
        else:
            return 0


def main():
    a = Solution()
    print(a.reverse(1534236469))


if __name__ == '__main__':
    main()
