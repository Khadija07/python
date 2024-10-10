# Write your solution here
from datetime import datetime
def is_it_valid(pic: str):
    string = '0123456789ABCDEFHJKLMNPRSTUVWXY'
    c = ""
    c += pic[0:6]
    c += pic[7:10]
    control = int(c)%31
    dd = int(pic[0:2])
    mm = int(pic[2:4])
    try:
        if pic[6] == '-':
            yy = int(f"19{pic[4:6]}")
        if pic[6] == '+':
            yy = int(f"19{pic[4:6]}")
        if pic[6] == 'A':
            yy = int(f"20{pic[4:6]}")
        if string[control] == pic[10] and len(pic) == 11:
            if pic[6] == '-' or pic[6] == '+' or pic[6] == 'A':         
                date = datetime(yy,mm,dd)
                return True

    except ValueError:
        return False
    
#print(is_it_valid('290200A1239'))