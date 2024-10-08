# Write your solution here
def anagrams(arg1, arg2):
    sortarg1 = sorted(arg1)
    sortarg2 = sorted(arg2)

    if sortarg1 == sortarg2:
        return True
    else:
        return False

    
