from test_framework import generic_test
from test_framework.test_failure import TestFailure

from collections import deque

#40m53s
class QueueWithMax:
    def __init__(self):
        self.q = deque()
        self.maxq = deque()

    def enqueue(self, x):
        # TODO - you fill in here.x
        self.q.append(x)

        while len(self.maxq) >= 1 and self.maxq[-1] < x:
            self.maxq.pop()

        self.maxq.append(x)

        return

    def dequeue(self):
        # TODO - you fill in here.
        if self.q[0] == self.maxq[0]:
            self.maxq.popleft()

        return self.q.popleft()

    def max(self):
        # TODO - you fill in here.
        return self.maxq[0]


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure("Dequeue: expected " + str(arg) +
                                      ", got " + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("queue_with_max.py",
                                       'queue_with_max.tsv', queue_tester))
