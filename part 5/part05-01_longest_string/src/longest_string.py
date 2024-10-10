# Write your solution here
def longest(strings: list):
    max = 0
    for string in strings:
        if len(string) > max:
            max = len(string)
            longest_string = string

    return longest_string

if __name__ == "__main__":
    strings = ['first', 'second', 'third']
    print(longest(strings))