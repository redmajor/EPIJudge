import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Person = collections.namedtuple('Person', ('age', 'name'))


# 22m20s
def group_by_age(people):
    # TODO - you fill in here.

    tbl = {}

    for person in people:
        if person.age not in tbl:
            tbl[person.age] = 0
        tbl[person.age] += 1

    total = 0
    for age, qty in tbl.items():
        total += qty
        tbl[age] = total - 1

    for i in range(len(people)):
        pos = tbl[people[i].age]
        while pos > i:
            tbl[people[i].age] -= 1
            people[i], people[pos] = people[pos], people[i]
            pos = tbl[people[i].age]

    return


@enable_executor_hook
def group_by_age_wrapper(executor, people):
    if not people:
        return
    people = [Person(*x) for x in people]
    values = collections.Counter()
    values.update(people)

    executor.run(functools.partial(group_by_age, people))

    if not people:
        raise TestFailure('Empty result')

    new_values = collections.Counter()
    new_values.update(people)
    if new_values != values:
        raise TestFailure('Entry set changed')

    ages = set()
    last_age = people[0]

    for x in people:
        if x.age in ages:
            raise TestFailure('Entries are not grouped by age')
        if last_age != x.age:
            ages.add(last_age)
            last_age = x.age


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("group_equal_entries.py",
                                       'group_equal_entries.tsv',
                                       group_by_age_wrapper))
