import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def length(ls):
    sz = 0

    while ls:
        sz += 1
        ls = ls.next
    return sz


def advance(ls, i):
    for _ in range(i):
        ls = ls.next
    return ls


def overlapping_no_cycle_lists(l0, l1):
    # TODO - you fill in here.

    len0 = length(l0)
    len1 = length(l1)

    if len0 > len1:
        l0 = advance(l0, len0 - len1)
    else:
        l1 = advance(l1, len1 - len0)

    while l0 and l1 and l0 is not l1:
        l0 = l0.next
        l1 = l1.next

    return l0


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(
        functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_terminated_lists_overlap.py",
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
