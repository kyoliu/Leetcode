# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        resultnode =ListNode(0)
        curnode = resultnode
        last,resultval, val = 0,0,0
        while l1 or l2:
            val = last
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next

            last = val / 10
            resultval = val % 10

            curnode.next = ListNode(resultval)
            curnode = curnode.next
        if last == 1:
            curnode.next = ListNode(1)
        return resultnode.next

if __name__ == '__main__':
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
    result = Solution().addTwoNumbers(a, b)
    print ("{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val))
    ##a, a.next= ListNode(1), ListNode(8)
    ##b  = ListNode(0)
    ##result = Solution().addTwoNumbers(a, b)
    ##print ("{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val))