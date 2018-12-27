class Solution(object):
    def convert(self, s, numRows):
        looplist = self.genaratelooplist(numRows)
        ptr = list()
        #初始化ptr
        for i in range(numRows):
            ptr.append("")
        length = len(s)
        # if (length == 0):
        #     return None
        position = 0
        while (position < length):
            for i in looplist:
                if (position < length):
                    ptr[i] += s[position]
                    position += 1
                else:
                    position = position + i
                    break
        # for i in looplist:
        #     position, k = k, k + 1
        #     while (position < length):
        #         ptr[i] += s[position]
        #         position = position + loop
        return "".join(ptr)

    #构造循环list
    #numRows等于3，list = [0,1,2,1]
    #numRows等于4，list = [0,1,2,3,2,1]
    def genaratelooplist(self, numRows):
        a = range(0, numRows)
        b = reversed(a[1:len(a) - 1])
        c = list(a) + list(b)
        return c


def main():
    a = Solution()
    print(a.convert("", 1))


if __name__ == '__main__':
    main()
