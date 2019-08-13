from test_framework import generic_test


# 18m33s
def majority_search(stream):
    # TODO - you fill in here.

    count = 0
    candidate = None

    for c in stream:
        if count == 0:
            candidate = c
        if candidate == c:
            count += 1
        else:
            count -= 1

    return candidate


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("majority_element.py",
                                       'majority_element.tsv',
                                       majority_search_wrapper))
