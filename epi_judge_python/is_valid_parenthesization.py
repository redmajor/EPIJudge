from test_framework import generic_test


#7min 23s
def is_well_formed(s):
    chars = {'(': ')', '[': ']', '{': '}'}
    stack = []

    for c in s:
        if c in chars.keys():
            stack.append(chars[c])
        else:
            if len(stack) == 0:
                return False
            exp = stack.pop()
            if exp != c:
                return False
    return len(stack) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
