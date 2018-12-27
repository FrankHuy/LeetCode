#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#Example:
#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def addTwoNumbers(self, l1, l2):
        n = 0
        rvalue = ListNode(0)
        result = rvalue
        while (l1 != None and l2 != None):
            plus = l1.val + l2.val + n
            n = plus // 10
            #result.val = plus % 10
            l1 = l1.next
            l2 = l2.next
            result.next = ListNode(plus % 10)
            result = result.next
        if (l1 != None):
            mid = l1
        elif (l2 != None):
            mid = l2
        else:
            mid = ListNode(-1)
        if (mid.val != -1):
            while (mid != None):
                plus = mid.val + n
                n = plus // 10
                mid = mid.next
                result.next = ListNode(plus % 10)
                result = result.next
        if (n == 1):
            result.next = ListNode(1)
            result = result.next
        result = rvalue.next
        return result


def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    import sys
    import io

    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            l1 = stringToListNode(line)
            line = next(lines)
            l2 = stringToListNode(line)

            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()