from test_framework import generic_test
from list_node import ListNode


# 36m58s
def stable_sort_list(L):
    def sort_step(ls):
        if ls is None or ls.next is None:
            return ls, ls

        pivot = ls
        smallerStart = ListNode()
        smallerEnd = smallerStart
        biggerStart = ListNode()
        biggerEnd = biggerStart

        cur = pivot.next
        pivot.next = None

        while cur:
            if cur.data < pivot.data:
                smallerEnd.next = cur
                smallerEnd = cur
            else:
                biggerEnd.next = cur
                biggerEnd = cur
            cur = cur.next

        biggerEnd.next = None
        smallerEnd.next = None
        biggerStart = biggerStart.next
        smallerStart = smallerStart.next

        start = pivot
        end = pivot

        if smallerStart:
            ss, se = sort_step(smallerStart)
            start = ss
            se.next = pivot

        if biggerStart:
            bs, be = sort_step(biggerStart)
            end = be
            pivot.next = bs

        return start, end
    return sort_step(L)[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sort_list.py", 'sort_list.tsv',
                                       stable_sort_list))
