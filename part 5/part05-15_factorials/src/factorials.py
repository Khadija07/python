def factorials(n: int):
    k = {}
    f = 1
    for i in range(1, n+1):
        f *= i
        k[i] = f
    return k
    
def k(n: int):
    return factorials(n)
    
if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])