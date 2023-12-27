
int_num=108
str_num=str(int_num)
print("int to str:",str_num)

str_num="100"
int_num=int(str_num)
print("str to int:",int_num)


def num():
 input_value=int(input("enter a number:"))
 if input_value>100:
    print("congrats")
 else:
    print("have a nice day")
num()


def mark(m1,m2):
 m1+=10
 m2+=20
 return m1,m2
m1=int(input("enter a mark 1:"))
m2=int(input("enter a mark 2:"))
updated_m1,updated_m2=mark(m1,m2)
print("The mark of (m1=updated_m1) and (m2=updated_m2)")
mark(m1,m2)
 

def prod():
    prod_code = input("Enter product code: ")
    prod_name = input("Enter product name: ")
    price = int(input("Enter price: "))
    prod_details = (f 'The "{prod_name}" with product code "{prod_code}" is sold at Rs.{price}')
    print(prod_details)
prod()


def fri():
 friend={'Y':'jone','Z':'fercy','M':'maria'}
 letter=input("enter the first letter of your friend name:").upper()
 if letter in friend:
    print("The friend name is",friend[letter])
 else:
    print("Try another letter")
fri()


def square():
    values=[]
    for i in range(1,6):
        a=int(input("enter a {i}the number:"))
        values.append(a)
        print(values)
        for a in values:
            sq=a*a
            print("the sq of the num{a}is"+str(sq))
square()


def check():
   str='JOSEPH'
   if 'S' in str:
    print("'S' exist in str.")
   else:
    print("'S'not exist in str.")
   if 'T'in str:
    print("'T' exist in str.")
   else:
    print("'T'not exist in str.")
check()


def max(x, y, z):
 x = int(input("Enter a Value x:"))
 y = int(input("Enter a Value y:"))
 z = int(input("Enter a Value z:"))
 if x >= y and x >= z:
    return x
 elif y >= x and y >= z:
    return y
 else:
    return z
result = max(x, y, z)
print("The high_value is:", result)


def big():
    values = []
    for i in range(1, 6):
        a = int(input("enter the {i}th number: "))
        values.append(a)
    print(values)
    count = 0
    for a in values:
        if a > 10:
            count += 1
    print("Number of values greater than 10 is: " + str(count))
big()


def concat():
 first_name=input("enter your first_name:")
 last_name=input("enter your last_name:")
 full_name=(first_name+" "+last_name)
 print("full name:",full_name)
concat()


def check():
 num=int(input("enter the number:"))
 if num%2==0 and num%3==0:
    print("(num)is divisible by both 2 and 3")
 else:
    print("(num)is no divisible by both 2 and 3")
check()


def even():
    sumofeven = 0
    for num in range(100, 200):
        if num % 2 == 0:
            sumofeven+=num
    print("Sum of even numbers between 100 and 200:",sumofeven)
even()
