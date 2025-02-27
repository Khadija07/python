# Write your solution here
def prime_numbers():
    yield(2)
    number = 3
    while number != 0:
        is_prime = True
        for i in range(2, number - 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime == True:
            yield(number)
            
        number += 1
        
        
        
        
# numbers = prime_numbers()
# for i in range(8):
#     print(next(numbers))