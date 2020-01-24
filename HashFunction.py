#HASHbitFUNCTION.py
file = open('bit.txt','r') #opens bit.txt file in order to read
bit = file.read()#moves value from file into bit variable
file.close()#closes bit.txt as its not needed anymore
print("You are using St00gs Multi-Hash algorithm at a final size of "+str(bit)+" bit's long")#tells the user the length it will produce
bit = int(bit)#turns bit into an integer

#Set Variables
no=[]
newhex=[]
num=0
val=0
value=""
w=0
m=0
hn=0
nn=""
a=0
b=1
#Get letters as input
old=input()

#def lessthanbit
# - takes n as <bit.int and nn as <bit.str
# - returns n as bit.int and nn as bit.str
def lessthanbit():
    #defines the variables to be edited globally in this function
    global c 
    global n
    global nn
    global a
    global b
    global w
    while len(nn)<bit: #while the length of our number is less than the desired length
        m=(no[w])#m becomes the specific value defined by w in the list
        no.append(m)#m is added to the end of the list
        w=w+1#add 1 to w
        n = int("".join(map(str, no)))#n become the integer of the new no list combined
        nn = str(n)#nn become the string of the new no list combined
        print(nn)#nn is printed to the console
    m=0#m returns to 0
    print(nn)#nn is printed to the console
    if len(nn)>bit:#if length is now more than the length desired amount
        morethanbit()#run the more than desired value function

#def morethanbit 
# - takes n as >bit.int and nn as >bit.str
# - returns n as bit.int and nn as bit.str
def morethanbit():
    #defines the variables to be edited globally in this function
    global c
    global n
    global nn
    global a
    global b
    global w
    while len(nn)>bit:#while the length of our number is less than the desired length
        c = no[a] + no[b]#c becomes the a value in the list + the b value in the list
        del no[a]#a value in the list is deleted
        del no[b]#b value in the list is
        no.append(c)#c is added to the end of the list
        a=a+1#add 1 to a
        b=b+1#add 1 to b
        n = int("".join(map(str, no)))#n become the integer of the new no list combined
        nn = str(n)#nn become the string of the new no list combined
        print(nn)#nn is printed to console
    a=0#a returns to 0
    b=0#b returns to 0
    if len(nn)<bit:#if n is less than the length desired value
        lessthanbit()#run the less than desired value
#def LNUM - returns value as integer from letters
def lnum():
    #defines the variables to be edited globally in this function
    global num
    global val
    global value
    val = ord(old[num])#val is the number made from the num letter in the string that was typed in
    if 65 <= val <= 90:#if val is more than or equal to 65  and less than or equal to 90
        value=(str(val - 64))#value is the string of val-64
    elif 97 <= val <= 122:#if val is more than or equal to 97  and less than or equal to 122
        value=(str(val - 96))#value is the string of val-96
    else:#if neither of those are true
        value=str(val)#value is just the string of val
    num=num+1#add 1 to number

#def LNUM2 - returns value as integer from letters
def lnum2():
    #defines the variables to be edited globally in this function
    global num
    global val
    global value
    val = ord(nn[num])#val is the number made from the num letter in the string nn
    if 65 <= val <= 90:#if val is more than or equal to 65  and less than or equal to 90
        value=(str(val - 64))#value is the string of val-64
    elif 97 <= val <= 122:#if val is more than or equal to 97  and less than or equal to 122
        value=(str(val - 96))#value is the string of val-96
    else:#if neither of those are true
        value=str(val)#value is just the string of val
    num=num+1#add 1 to number

#def Entropy
#THIS FUNCTION IS FOR YOU TO PUT YOUR OWN CODE IN TO MAKE THE NUMBER MADE LESS OBVIOUS OF ORIGINS OF THE ORIGINAL STRING
def entropy():#define the start of the entropy function
    print('Entropy!')#Entropy! is printed to the console
    print(nn)#the final hashed nn is printed to the console
    a = hex(int(nn)).split('x')[-1]
    print("\n"*3)
    print(str(a))
    input()#waits for input

#Convert Input into number string and number list
# - returns n as long int
# - returns no as long list
# - returns total as sum of list
# - returns og as length of list
# - returns stringtotal as the string of the sum of the list
# - returns nn as the string of the long int
while num < len(old):#while num is less than the length of our original string
    lnum()#perform the letters to numbers function
    no.append(int(value))#add the value obtained from the lnum() function to end of the no list
total=sum(no)#total becomes the sum of all the digits in the no list
og = len(no)#og becomes the length of the no list
stringtotal=(str(total))#string total becomes
n = int("".join(map(str, no)))#n become the integer of the new no list combined
nn = str(n)#nn becomes the string of n

#Makes value into bit digit length
if len(nn)<bit:#if the length of nn is less than the desied length
    lessthanbit()#perform the less than bit function
    entropy()#perform the entropy function
elif len(nn)==bit:#if the length of nn is equal to the desired length
    entropy()#perform the entropy function
elif len(nn)>bit:#if the length of nn is more than the desired length
    morethanbit()#perform the more than bit function
    entropy()#perform the entropy function
