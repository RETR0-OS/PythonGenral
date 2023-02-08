units =["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Tweleve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

tens = ["Twenty", "Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

denominations= ["Hundred", "Thousand", "Million", "Billion", "Trillion"]

def find_length(num):
    n = str(int(num))
    if len(n) == 1 and int(n) != 0:
        return one_digit_num(n)
    if len(n) == 2:
        return two_digit_num(n)
    elif len(n) ==3:
        return three_digit_num(n)
    elif len(n) ==4:
        return four_digit_num(n)
    elif len(n) ==5:
        return five_digit_num(n)
    elif len(n) ==6:
        return six_digit_num(n)
    elif len(n) ==7:
        return seven_digit_num(n)
    elif len(n) ==8:
        return eight_digit_num(n)
    elif len(n) == 9:
        return nine_digit_num(n)
    elif len(num) ==10:
        return ten_digit_num(n)
    elif len(num) ==11:
        return eleven_digit_num(n)
            
def one_digit_num(num):
    if int(num) == 0:
        return ''
    return units[int(num)-1]

def two_digit_num(num):
    num=int(num)
    if int(num) >= 20:
        if int(str(num)[1]) != 0:
            return f"{tens[int(str(num)[0])-2]} {units[int(str(num)[1])-1]}"
        else:
            return f"{tens[int(str(num)[0])-2]}"
    else:
        return f'{units[num-1]}'

def three_digit_num(num):
    s = one_digit_num(int(str(num)[0]))
    end = find_length(str(num)[1:])
    if end != None:
        return f"{s} Hundred {end}"
    else:
         return f"{s} Hundred"
  
def four_digit_num(num):
    s = units[int(str(num)[0])-1]
    end= find_length(str(num)[1:])
    if end != None:
        return f'{s} {denominations[1]} {end}'
    else:
        return f'{s} {denominations[1]}'
def five_digit_num(num):
    s = int(str(num)[:2])
    s = two_digit_num(s)
    end = find_length(str(num)[2:])
    if end != None: 
        return f'{s} Thousand {end}'
    else:
        return f'{s} Thousand'

def six_digit_num(num):
    s = int(str(num)[:3])
    s = three_digit_num(s)
    end = find_length(str(num)[3:])
    if end != None:
        return f'{s} Thousand {end}'
    else:
        return f'{s} Thousand'

def seven_digit_num(num):
    s = int(str(num)[:1])
    s = one_digit_num(s)
    end = find_length(str(num)[1:])
    if end != None:
        return f'{s} Million {end}'
    else:
        return f'{s} Million'
  
def eight_digit_num(num):
    s = int(str(num)[:2])
    s = two_digit_num(s)
    end = find_length(str(num)[2:])
    if end != None:
        return f'{s} Million {end}'
    else:
        return f'{s} Million'

def nine_digit_num(num):
    s = int(str(num)[:3])
    s = three_digit_num(s)
    end = find_length(str(num)[3:])
    if end != None:
        return f'{s} Million {end}'
    else:
        return f'{s} Million'
    
def ten_digit_num(num):
    s = int(str(num)[:1])
    s = one_digit_num(s)
    end = find_length(str(num)[1:])
    if end != None:
        return f'{s} Billion {end}'
    else:
        return f'{s} Billion'
def eleven_digit_num(num):
    s = int(str(num)[:2])
    s = two_digit_num(s)
    end = find_length(str(num)[2:])
    if end != None:
        return f'{s} Billion {end}'
    else:
        return f'{s} Billion'
def tweleve_digit_num(num):
    s = int(str(num)[:3])
    s = three_digit_num(s)
    end = find_length(str(num)[3:])
    if end != None:
        return f'{s} Billion {end}'
    else:
        return f'{s} '

    
def convert(num):
    num_len = len(str(num))
    if num==0:
        print("Zero")
    else:
        if num <20:
            print(units[num-1])
        else:
            if num_len == 2:
                print(two_digit_num(num))
                #print(tens[int(str(num)[0])-2])
            elif num_len ==3:
                print(three_digit_num(num))
            elif num_len ==4:
                print(four_digit_num(num))
            elif num_len ==5:
                print(five_digit_num(num))
            elif num_len ==6:
                print(six_digit_num(num))
            elif num_len ==7:
                print(seven_digit_num(num))
            elif num_len == 8:
                print(eight_digit_num(num))
            elif num_len == 9:
                print(nine_digit_num(num))
            elif num_len == 10:
                print(ten_digit_num(num))
            elif num_len == 12:
                print(tweleve_digit_num(num))
            elif num_len == 13:
                print("One Trillion")

t = int(input())

for i in range(t):
    num = input()
    num = int(num)
    convert(num)

