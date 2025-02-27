
def balanced_brackets(my_string: str):
    my_string = ''.join([char for char in my_string if char in '([])'])
    #print(my_string)
    
    if len(my_string) == 0:
        return True
    if not ((my_string[0] == '(' and my_string[-1] == ')' ) or (my_string[0] == '[' and my_string[-1] == ']')):
        return False

    # remove first and last character
    return balanced_brackets(my_string[1:-1])


# # this is no good, the closing bracket doesn't match
# ok = balanced_brackets("(()]")
# print(ok)

# # different types of brackets are mismatched
# ok = balanced_brackets("([bad egg)]")
# print(ok)

