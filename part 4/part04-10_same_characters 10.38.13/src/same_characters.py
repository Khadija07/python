# Write your solution here
# You can test your function by calling it within the following block
def same_chars(word, pos1, pos2):
    length = len(word)
    if pos1 >= length or pos2 >= length:
        return False

    else:
        if word[pos1] == word[pos2]:
            return True

        else:

            return False

    
if __name__ == "__main__":
    print(same_chars("coder", 1, 10))