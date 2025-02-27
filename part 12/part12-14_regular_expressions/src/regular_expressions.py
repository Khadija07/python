# Write your solution here
import re

def is_dotw(my_string: str):
    expression = "Mon|Tue|Wed|Thu|Fri|Sat|Sun"
    
    if re.search(expression, my_string):
        return True
    return False

def all_vowels(my_string: str):
    # re.search("^[aeiou]*$", my_string) is not None
    string = re.findall('[aeiou]', my_string)
    # print(string)
    # print(my_string)
    if len(string) == len(my_string):
        return True
    return False
    
def time_of_day(my_string: str):
        # return re.search("^([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$", my_string) is not None

    parts = my_string.split(':')
    hours = re.findall('\d+',parts[0])
    # print(hours)
    minutes = re.findall('\d+',parts[1])
    seconds = re.findall('\d+',parts[2])
    # print(hours, minutes,seconds)
  
    if len(hours) > 0 and len(minutes) > 0 and len(seconds) > 0:
        if int(hours[0]) <= 24 and int(minutes[0]) < 60 and int(seconds[0]) < 60:
            return True
        return False 
    else:
        return False
    

# # print(all_vowels("eioueioieoieou"))
# # print(all_vowels("autoooo"))
# print(time_of_day("12:43:01"))
# print(time_of_day("AB:01:CD"))
# print(time_of_day("17:59:59"))
# print(time_of_day("33:66:77"))