from test_framework import generic_test


# 8m 11s
def roman_to_integer(s):
    # TODO - you fill in here.

    tbl = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    exceptions = {'I': ['V', 'X'], 'X': ['L', 'C'], 'C': ['D', 'M']}

    i = 0
    total = 0

    while i < len(s):
        if s[i] in exceptions and i + 1 < len(s) and s[i + 1] in exceptions[s[i]]:
            total += tbl[s[i + 1]] - tbl[s[i]]
            i += 2
        else:
            total += tbl[s[i]]
            i += 1

    return total


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "roman_to_integer.py", 'roman_to_integer.tsv', roman_to_integer))
