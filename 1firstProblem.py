number = 0 
list_number = []
total = 0 
inialization_number = 1000

def multiples_3or5 (number):
    while number < inialization_number :
        number+=1
        if number % 3 == 0  or number % 5 == 0:  
            list_number.append (number)
    total = sum(list_number) 
    print (total)

if __name__ == "__main__":
    multiples_3or5(number)

