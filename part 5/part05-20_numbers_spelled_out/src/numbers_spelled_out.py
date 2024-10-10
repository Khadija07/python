# Write your solution here
#create a dictionary with dict_of_numbers()
def dict_of_numbers():
    number = 0
    numb_dictionary = {}
    List_of_numbers0to19 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
                        'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
                        'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
                        'nineteen']
    List_of_numberstens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
                       'eighty', 'ninety']

    for number in range(20):
        numb_dictionary[number] = List_of_numbers0to19[number]

    for number in range(20, 100):
        if number%10 == 0: 
            numb_dictionary[number] = List_of_numberstens[number//10-2] 
        else: 
            numb_dictionary[number] = (List_of_numberstens[number//10-2] + '-' + List_of_numbers0to19[number%10])

    #print(numb_dictionary)
    return numb_dictionary


    
def main():
    """ main function """
    numbers = dict_of_numbers()
    #print(numbers[1])
    print(numbers[21])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])
 

if __name__ == "__main__":
    main()
    