import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

MPG = 20


# 11m28s

# gallons[i] is the amount of gas in city i, and distances[i] is the
# distance city i to the next city.
def find_ample_city(gallons, distances):
    allowed_distance = 0
    start = 0

    for i in range(len(gallons)):
        if allowed_distance < 0:
            allowed_distance = 0
            start = i

        allowed_distance += gallons[i] * 20 - distances[i]

    return start


@enable_executor_hook
def find_ample_city_wrapper(executor, gallons, distances):
    result = executor.run(
        functools.partial(find_ample_city, gallons, distances))
    num_cities = len(gallons)
    tank = 0
    for i in range(num_cities):
        city = (result + i) % num_cities
        tank += gallons[city] * MPG - distances[city]
        if tank < 0:
            raise TestFailure('Out of gas on city {}'.format(i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("refueling_schedule.py",
                                       'refueling_schedule.tsv',
                                       find_ample_city_wrapper))
