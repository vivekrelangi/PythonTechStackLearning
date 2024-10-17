#from __future__ import braces
"""print(type(3))
print(type("Hello World"))
print(type(False))
print(type(2.0))"""
"""no_of_landings=356
no_of_takeoffs=245
initial_no_of_flights=100
current_no_of_flights=initial_no_of_flights+no_of_landings-no_of_takeoffs
print("Current number of flights:",current_no_of_flights)"""
"""print("Let's see some examples.\n\nDid you notice the empty lines?")
print("Do you notice\t the tab space?\nDid you see that I have moved to next line?")
print("Do you want a \" in your text?")
print("Are you going to store more info about escape sequence in Z:\\\\user\\escape_sequence.txt??")
#Every print starts with a new line, end can change that behavior by specifying your own character
print("Did you see I start here", end=" ")
print("and I end in the same line although from a different print?")
print("As observed escape sequences help you to format your output.")"""
"""print("________________________________________________________________________")
print("\t\t\tBREAD BASKET")
print("\"Looking for a healthy breakfast, this is the place for you!!\"")
print("________________________________________________________________________")
print("Raisin Toast\t\t\t\t\t\t\t$2.50")
print("French Toast\t\t\t\t\t\t\t$2.80")
print("Mushroom Toast\t\t\t\t\t\t\t$3.00")
print("Pancake\t\t\t\t\t\t\t\t$4.00")
print("Pancake with Ice-cream\t\t\t\t\t\t$7.50")
print("Chef's speciality\t\t\t\t\t\t$10.00")
print("________________________________________________________________________")"""
"""def calculate_sum(data1, data2):
    #All the statements in the block of code must have the same level of indentation
    result_sum=data1+data2
    return result_sum

result=calculate_sum(10,20)
print(result)"""
"""#Goal of thssport_no)==8):
        if(passport_no[0]>="A" and passport_no[0]<="Z"):
            status="valid"
        else:
            status="invalid"
    else:
        status= "invalid"
    observe6="func. execution ends"
    return status

observe2="function with formal arg."
observe3="calling with actual arg."
passport_status=passport_check("M9993471")

print("Passport is",passport_status)is tryout is to create a function from scratch and invoke it for the given problem
""""""f=7#int(input("enter temperature:"))
c=(f-32)*(5/9)
print(int(c))"""
#lex_auth_01269361601342668881
"""def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    #Write your logic here
    total_ticket_cost=(no_of_adults*37550.0)+(no_of_children*(37550.0/3))
    total_ticket_cost+=total_ticket_cost*(7/100)
    total_ticket_cost-=total_ticket_cost*(1/10)
    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(3,1)
print("Total Ticket Cost:",total_ticket_cost)"""
"""observe1="What's happening!!"

def passport_check(passport_no):
    observe4="actual copied to formal"
    observe5="func. execution starts"
    if(len(pa
#observe1,2,3,4,5,6 are temporary variables used to explain this concept
"""
"""#Code1
print("code-1")
def func1(a,b):
    return a+b

res=func1(5,10)
print("Value returned:",res)


#Code2:
print("------------------------------------")
print("code-2")
def func2():
    print("This code has nothing to return")
    return

func2()

#Code3:
print("------------------------------------")
print("code-3")
def func3():
    print("This code also has nothing to return and there is no return statement")

func3()

#Code 4:
print("------------------------------------")
print("code-4")
print("------------------------------------")
def func4(a,b):
    if(a>b):
        print("returns from if block")
        return a
    print("returns from outside if block")
    return b
print("1st invocation of code-4")
print("Value returned:",func4(10,5))
print("------------------------------------")
print("2nd invocation of code-4")
print("Value returned:",func4(2,3))"""
"""#Code1
print("code-1")
def func6(a,b,c):
    res_avg=(a+b+c)/3
    return res_avg
print("1st invocation of code-1")
func6(6,8,10)
print("returned value is not assigned to any variable")

print("------------------------------------------------")
print("2nd invocation of code-1")
average=func6(10,15,20)
print("returned value assigned to a variable")
print("value of variable, average:", average)

print("------------------------------------------------")
print("3rd invocation of code-1")
print("returned value is directly printed")
print(func6(1,2,3))



#Code2
print("------------------------------------------------")
print("code-2")
print("------------------------------------------------")
def func7(a,b):
    if(a>b):
        return True
    return False
x=5
y=6

print("1st invocation of code-2")
if(func7(x,y)):
    print("inside if block")
else:
    print("inside else block")


x=6
y=5
print("------------------------------------------------")
print("2nd invocation of code-2")
if(func7(x,y)):
    print("inside if block")
else:
    print("inside else block")

"""
"""ticket_status="Confirmed"
luggage_weight=31
weight_limit=30  #Weight limit for the airline
extra_luggage_charge=0
if(ticket_status=="Confirmed"):
    if(luggage_weight>0 and luggage_weight<=weight_limit):
        print("Check-in cleared")
    #elif(luggage_weight<=(weight_limit+10)):
    #    extra_luggage_charge=300*(luggage_weight-weight_limit)
    else:
        extra_luggage_charge=500*(luggage_weight-weight_limit)
    if(extra_luggage_charge>0):
        print("Extra luggage charge is Rs.", extra_luggage_charge)
        print("Please make the payment to clear check-in")
else:
    print("Sorry, ticket is not confirmed")"""
"""passport_status="valid"
ticket_status="Confirmed"
luggage_weight=32
weight_limit=30  #Weight limit for the airline
extra_luggage_charge=0
if(passport_status=="valid"):
    print("Airport security cleared")
    if(ticket_status=="Confirmed"):
        if(luggage_weight>0 and luggage_weight<=weight_limit):
            print("Check-in cleared")
        #elif(luggage_weight<=(weight_limit+10)):
        #    extra_luggage_charge=300*(luggage_weight-weight_limit)
        else:
            extra_luggage_charge=600*(luggage_weight-weight_limit)
        if(extra_luggage_charge>0):
            print("Extra luggage charge is Rs.", extra_luggage_charge)
            print("Please make the payment to clear check-in")
    else:
        print("Sorry, ticket is not confirmed")
else:
    print("Invalid passport")"""
"""baggage_count=100
no_of_baggage_picked=0
while(baggage_count>0):
    no_of_baggage_picked = (int)(input ("Number of baggage:"))
    baggage_count = baggage_count - no_of_baggage_picked
print("No. of baggage remaining:",baggage_count)"""
"""print("Flight has landed")
print("Proceed for immigration check")
for passenger_count in 1,2,3,4,5:
    print("Immigration check done for passenger,", passenger_count)"""
"""baggage_count=100
no_of_baggage_picked=0
while(baggage_count>0):
    no_of_baggage_picked = (int)(input ("Number of baggage:"))
    baggage_count = baggage_count - no_of_baggage_picked
    print("No. of baggage remaining:",baggage_count)"""
"""for number in 1,2,3,4,5:
    print("The current number is ",number)"""
"""start=1
end=10
step=7
for number in range (start, end, step):
    print("The current number is ", number)
"""
"""for number in range(1,5):
    print ("The current number is ",number)

print("---------------------------")

for number in range(1,7,2):
    print ("The current number is ",number)

print("---------------------------")

for number in range(5,0,-1):
    print ("The current number is ",number)"""
"""number_of_passengers=5
number_of_baggage=2
security_check=True
for passenger_count in range(1, number_of_passengers+1):
    for baggage_count in range(1,number_of_baggage+1):
        if(security_check==True):
            print("Security check of passenger:", passenger_count, "-- baggage:", baggage_count,"baggage cleared")
        else:
            print("Security check of passenger:", passenger_count, "-- baggage:", baggage_count,"baggage not cleared")"""
"""number_of_passengers=5
number_of_baggage=2
security_check=True
for passenger_count in range(1, number_of_passengers+1):
    baggage_count =1
    while (baggage_count<=number_of_baggage):
        if(security_check==True):
            print("Security check of passenger:", passenger_count, "-- baggage:", baggage_count,"baggage cleared")
        else:
            print("Security check of passenger:", passenger_count, "-- baggage:", baggage_count,"baggage not cleared")
        baggage_count+=1"""
"""for passenger in "A","A", "FC", "C", "FA",  "SP", "A", "A":
    if(passenger=="FC" or passenger=="FA"):
        print("No check required")
        continue
    if(passenger=="SP"):
        print("Declare emergency in the airport")
        break
    if(passenger=="A" or passenger=="C"):
        print("Proceed with normal security check")
    print("Check the person")
    print("Check for cabin baggage")"""
"""counter = 5
while (counter >= 5):
    print(counter)
    counter = counter - 1"""
"""counter = 1
while(counter <= 3):
    print(counter)
    counter += 1"""
"""num_list = [1,2]
for num in num_list:
    print(num, end = " ")"""
"""numbers_list = [98,45,60,71,90]
count = 10
for number in numbers_list:
    if number % 10 == 0:
        count -= 1
        continue
    counter = 0
    while counter < 2:
        last_digit = number % 10
        number = number // 10
        if last_digit > 4:
            count += 1
            break
        count += 1
        counter += 1
print(count)"""
"""def get_count(num_list):
    count=0

    # Write your logic here
    for i in range(len(num_list)):
        for j in range(len(num_list)):
            if j==i+1 and num_list[i]==num_list[j]:
                count+=1
                print(i,j)

    return count

#provide different values in list and test your program
num_list=[1,2,2,3,4,4,4,10]
print(get_count(num_list)) """                          
"""#Creating a tuple
lunch_menu=("Welcome Drink","Veg Starter","Non-Veg Starter","Veg Main Course","Non-Veg Main Course","Dessert")

#These are also valid
sample_tuple="A","B","C"
sample_tuple1=("D",)

#Length of the tuple
print("Number of elements in the tuple, lunch_menu:",len(lunch_menu))

#Random read
print("Element at 2nd index position in lunch_menu:", lunch_menu[2])

print("Concatenating tuples:")
#Concatenating two tuples
sample_tuple=sample_tuple+sample_tuple1 #This will create a new tuple by combining the elements of existing sample_tuple and sample_tuple1
print(sample_tuple)

#Adding a single element to a tuple
sample_tuple=sample_tuple+("E",)  # This will also create a new tuple, sample_tuple
print(sample_tuple)


#Adding multiple elements to a tuple
sample_tuple=sample_tuple+("F","G")  # This will also create a new tuple, sample_tuple
print(sample_tuple)

print("Iterating the tuple using range()")
for index in range(0,len(lunch_menu)):
    print(lunch_menu[index])

print("Iterating the tuple using keyword in")
for food_type in lunch_menu:
    print(food_type)

print("Searching for an element in tuple")
if "Dessert" in lunch_menu:
    print("Dessert is there")
else:
    print("Dessert is not there")        

#Slicing a tuple
print("Tuple slice using positive indices:",lunch_menu[1:5])

print("Tuple slice using negative indices:",lunch_menu[-5:-1])

# comment the below code and try to visualize.
#lunch_menu[0]="" #This line will result in an error, i.e., tuple is immutable
print(lunch_menu)"""
"""#Creating a string
pancard_number="AABGT6715H"

#Length of the string
print("Length of the PAN card number:", len(pancard_number))

#Concatenating two strings
name1 ="PAN "
name2="card"
name=name1+name2
print(name)

print("Iterating the string using range()")
for index in range(0,len(pancard_number)):
    print(pancard_number[index])
    
print("Iterating the string using keyword in")
for value in pancard_number:
    print(value)

print("Searching for a character in string")
if "Z" in pancard_number:
    print("Character present")
else:
    print("Character is not present")

#Slicing a string
print("The numbers in the PAN card number:", pancard_number[5:9])
print("Last but one 3 characters in the PAN card:",pancard_number[-4:-1])

#pancard_number[2]="A" #This line will result in an error, i.e., string is immutable
print(pancard_number)"""
"""boarding_call="Good Evening, this is the final call to AI passengers for the flight AI 466 which is planned to take off at 8.40A.M."

if(boarding_call.startswith("Good Evening")):
    print(boarding_call.replace("Good Evening","Good Morning"))

if(boarding_call.find("AI"))>=0:
    print("Welcome to Air India.")

if(boarding_call.endswith("A.M.")):
    print("Passengers are requested to have their breakfast.")

a=boarding_call.split(" ")
for i in a:
    if(i.isdigit()):
        print("Flight Number is specified to the passengers.")

print("Total number of times flight service name is specified in the boarding call:",boarding_call.count("AI"))


message="Thank you all..Have a nice journey!"

print(message.upper())

print(message.lower())"""
"""row1 = (101,"Dallas",3.5)
row2 = (102,"Atlanta",5.6)
row3 = (103,"Tokyo",9.8)
table = [row1,row2,row3]
print(table[0])
print(table[1])
print(table[2])"""
"""count=0
i=1
for baggage_weight in 29, 30, 31, 32, 28:
    if(baggage_weight>=1 and baggage_weight <=30):#or changed to and to get actual output
        print("Passenger",i,": Proceed for baggage check.")
        count+=1#added to get actual output
    else:
        count+=1
        print("Passenger",i,": Maximum baggage weight allowed is 30kg.")
    i+=1
print("No. of passengers who cleared baggage check:", count)"""
"""i=1
n=10
while(i<=n):
    if(i%2==0):
        print(i)
        i+=1
    else:
        i+=1
        continue"""
"""def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    quantity=0
    #Write your logic here
    for reqd_gem in reqd_gems:
        if reqd_gem not in gems_list:
            bill_amount=-1
            return bill_amount
    for gem in reqd_gems:
        bill_amount+=price_list[gems_list.index(gem)]*reqd_quantity[quantity]
        #print(gems_list.index(gem))
        quantity+=1
    if bill_amount>30000:
        bill_amount-=(bill_amount/20)
            
    return bill_amount

#List of gems available in the store
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[1760,2119,1599,3920,3999]

#List of gems required by the customer
reqd_gems=["Ivory","Emerald","Garnet"]

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[3,10,12]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)"""
"""def create_largest_number(number_list):
    numstr=[]
    r=0
    for num in number_list:
        numstr.append("")
        numstr.append("")
    for i in range(len(number_list)):
        numstr[i]+=str(number_list[i])
        for j in range(len(number_list)):
            if i!=j:
                numstr[i]+=str(number_list[j])
    for i in range(len(number_list)):
        numstr[i+3]+=str(number_list[i])
        for k in range(len(number_list)-1,-1,-1):
            if i!=k:
                numstr[i+3]+=str(number_list[k])
    for num in number_list:
        num=int(num)
    r=max(numstr)
    return r
    #remove pass and write your logic here
number_list=[23,34,55]
largest_number=create_largest_number(number_list)
print(largest_number)"""
"""def encode(message):
    enc_msg=""
    count=0
    visited=[]
    for inc in range(len(message)):
        visited.append(False)
    print(visited)
    return enc_msg
    #Remove pass and write your logic here

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)"""
"""#Creating a dictionary
crew_details={
            "Pilot":"Kumar",
            "Co-Pilot":"Raghav",
            "Head-Strewardess":"Malini",
            "Stewardess":"Mala"
}
print(crew_details["Pilot"])

print("\nIterating the dictionary using items function")
for key,value in crew_details.items():
    print(key,":",value)


#Usually while working with dictionary, you will be interested in specific values. 
#Let’s find the value of all pilots from crew_details.
print("\nIterating the dictionary using keyword 'in'")
for key in crew_details:
    if(key=="Pilot" or key=="Co-Pilot"):
        print(crew_details[key])
#Note: Dictionary being unordered, the order of the values being displayed may vary during each execution of the above for loop.

#Dictionaries are mutable
crew_details["Pilot"]="James" # Here the value for key "Pilot" is being updated to "James"
print("\nAfter modifying the value of Pilot:", crew_details["Pilot"])

print("------------------------------------------------------------------")
print("Before update:")
# Usage of get method()
print("Co-pilot:",crew_details.get("Co-Pilot"))

#Usage of update method()
crew_details.update({"Flight Attendant":"Jane", "Co-pilot":"Henry"})

print("\nAfter update:")
print("Co-pilot:",crew_details.get("Co-pilot"))
print("Flight Attendant:",crew_details["Flight Attendant"])"""
"""#list of passengers
passengers_list=["George","Annie", "Jack","Annie","Henry", "Helen","Maria","George","Jack","Remo"]

#set function - removes the duplicates from the list and returns a set
unique_passengers=set(passengers_list)
print(unique_passengers)

#creating a set
flight_set={500,520,600,345,520,634,600,500,200,200}
print(flight_set)

flights_at_src = ["AI230","BA944","EM395","AI704","BA944","AI704"]
flights_at_dest = ["SI107","AI034","EM395","AI704","BA802","SI236"]
print(flights_at_src)
print(flights_at_dest)

#Creating list of unique flights at source and destination
uniq_src_flights = set(flights_at_src)
uniq_dest_flights = set(flights_at_dest)
print(uniq_src_flights)
print(uniq_dest_flights)


#setA-setB -> Gives the elements that are only in setA
#List of flights only at source airport
flights_only_at_src = uniq_src_flights-uniq_dest_flights
print(flights_only_at_src)

#setA&setB -> Gives the common elements between setA and setB
#List of flights common to source and destination airports
common_flights=uniq_src_flights&uniq_dest_flights
print(common_flights)

#setA|setB -> merges setA and setB after removing duplicates
#List of all flights at source and destination airports
all_flights=uniq_src_flights|uniq_dest_flights
print(all_flights)"""
"""import random
x=10
y=50
print(random.randrange(x,y)) """
"""import math
num1=234.01
num2=6
num3=-27.01

print("The smallest integer greater than or equal to num1,",num1,":",math.ceil(num1))
print("The largest integer smaller than or equal to num1,",num1,":",math.floor(num1))
print("The factorial of num2,",num2,":", math.factorial(num2))
print("The absolute value of num3",num3,":",math.fabs(num3))"""
"""import datetime,time
time.gmtime()

#Returns the current GM time

time.localtime()

#Returns the current time based on the current locality

t=str(time.localtime())
time.strftime(t,format)

#Converts t to a string as specified by the format argument and returns it.
#Where t is the time returned by time.gmtime() or time.localtime(). It is optional, default value is current time as returned by time.localtime()

date_string=datetime.date
datetime.datetime.strptime (date_string, format)

#Converts a date string in the specified format to a datetime value and returns it

datetime.date.today()
	
#Returns the current local date"""
"""import time
import datetime

#To get current GM time
print("Current GM time:",time.gmtime())
#This returns a time structure containing 9 values - year, month,day, hour, minute, sec, day of week, day of year and daylight savings.

#To get current local time
print("Current local time:",time.localtime())
#This also returns a time structure containing 9 values - year, month,day, hour, minute, sec, day of week, day of year and daylight savings.

#To extract today's date in a specified string format
print("Today's date using time module",time.strftime("%m-%m/%Y"))

#Python additionally allows use of  datetime module
#Prints today's date
print("Today's date using datetime module:", datetime.date.today())

#To extract today's date in a specified string format
print("Today's date (dd/mm/yyyy) using datetime module:", datetime.date.today().strftime("%d/%m/%Y"))


#To convert a date in string format to datetime value
print("Today's date (dd/mm/yyyy):", datetime.datetime.strptime("17/04/1","%y/%d/%m"))"""
"""a="I don't know"
b="I do know"
for c in a:
    print(c)"""
"""
def encrypt_sentence(sentence):
    sentence_list=sentence.split(" ")
    res=[]
    for i in range(len(sentence_list)):
        res.append("")
    odd_positions_list=[]
    odd_indeces_list=[]
    even_indeces_list=[]
    even_positions_list=[]
    even=[]
    vowels=['A','E','I','O','U','a','e','i','o','u']
    for i in range(len(sentence_list),2):
        odd_positions_list.append(sentence_list[i])
        odd_indeces_list.append(i)
    for i in range(1,len(sentence_list),2):
        even_positions_list.append(sentence_list[i])
        even_indeces_list.append(i)
        even.append("")
    for word in odd_positions_list:
        temp=word
        word=temp[::-1]
    for i in range(len(even_positions_list)):
        for c in even_positions_list[i]:
            if c not in vowels:
                even[i]+=c
        for c in even_positions_list[i]:
            if c in vowels:
                even[i]+=c
    for i in range(len(odd_positions_list)):
        res[odd_indeces_list[i]]=odd_positions_list[i]
    print(odd_positions_list,odd_indeces_list)
    for i in range(len(even_positions_list)):
        res[even_indeces_list[i]]=even_positions_list[i]
        
    print(even_indeces_list)
    encrypted_sentence=""
    for i in range(len(res)):
        encrypted_sentence+=res[i]
        if i!=(len(res)-1):
            encrypted_sentence+=" "
    return encrypted_sentence
    #start writing your code here

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)"""
"""def change_number(num):
    num+=10

def change_list(num_list):
    num_list.append(20)

num_val=10

print("num_val before function call:", num_val)
change_number(num_val)
print("num_val after function call:", num_val)

print("-----------------------------------------------")

val_list=[5,10,15]

print("val_list before function call:", val_list)
change_list(val_list)
print("val_list after function call:", val_list)"""
"""def check_in(baggage,boarding_pass):
    if(baggage>=1 and baggage<=30):
            boarding_pass="Issued"

def update_seat(seat_list):
    seat_list[1]=25

boarding_pass="Not Issued"
print("boarding_pass before function call:", boarding_pass)
check_in(25, boarding_pass)
print("boarding_pass after function call:", boarding_pass)
print("boarding_pass, a string is immutable")
print("-------------------------------------------------------")

passenger_seat=["Jack","NA"]
print("passenger_seat before function call:", passenger_seat)
update_seat(passenger_seat)
print("passenger_seat after function call:", passenger_seat)
print("passenger_seat, a list is mutable")"""
"""def display1(flight_number, seating_capacity):
    print("Flight Number:", flight_number)
    print("Seating Capacity:", seating_capacity)

print("code-1: positional arguments")
display1("AI789",200)
#Uncomment and execute the below function call statement and observe the output
#display1(300,"BA123")


def display2(flight_number, seating_capacity):
    print("Flight Number:", flight_number)
    print("Seating Capacity:", seating_capacity)

print("-------------------------------------------------")
print("code-2: keyword arguments")
display2(seating_capacity=250, flight_number="AI789")

def display3(flight_number, flight_make="Boeing", seating_capacity=150):
    print("Flight Number:", flight_number)
    print("Flight Make:", flight_make)
    print("Seating Capacity:", seating_capacity)

print("-------------------------------------------------")
print("code-3: default arguments")
display3("AI789","Eagle")
#Uncomment and execute the below function call statements one by one and observe the output
display3("BA234")
display3("SI678","Qantas",200)


def display4(passenger_name, *baggage_tuple):
    print("Passenger name:",passenger_name)
    total_wt=0
    for baggage_wt in baggage_tuple:
        total_wt+=baggage_wt
    print("Total baggage weight in kg:", total_wt)

print("-------------------------------------------------")
print("code-4: variable argument count")
display4("Jack",12,8,5)
#Uncomment and execute the below function call statements one by one and observe the output
display4("Chan",20,12)
display4("Henry",23)"""
"""wt_limit=30

def baggage_check(baggage_wt):
    extra_baggage_charge=0
    if not(baggage_wt>=0 and baggage_wt<=wt_limit):
        extra_baggage=baggage_wt-wt_limit
        extra_baggage_charge=extra_baggage*100
    return extra_baggage_charge

def update_baggage_limit(new_wt_limit):
    global wt_limit
    wt_limit=new_wt_limit
    print("This airline now allows baggage limit till",wt_limit,"kgs")

print("This airline allows baggage limit till",wt_limit,"kgs")
print("Pay the extra baggage charge of",baggage_check(35),"rupees")
update_baggage_limit(45)
print("Pay the extra baggage charge of",baggage_check(35),"rupees")
print(wt_limit)"""
"""wt_limit=30

def baggage_check(baggage_wt):
    extra_baggage_charge=0
    if not(baggage_wt>=0 and baggage_wt<=wt_limit):
        extra_baggage=baggage_wt-wt_limit
        extra_baggage_charge=extra_baggage*100
    return extra_baggage_charge

def update_baggage_limit(new_wt_limit):
    global wt_limit
    wt_limit=new_wt_limit
    print("This airline now allows baggage limit till",wt_limit,"kgs")

#def useless_function_to_prove_a_point():
    #print("Extra baggage:",extra_baggage)
    #print("Extra baggage charge:",extra_baggage_charge)

print("This airline allows baggage limit till",wt_limit,"kgs")
print("Pay the extra baggage charge of",baggage_check(35),"rupees")
#print("Extra baggage:",extra_baggage)
#print("Extra baggage charge:",extra_baggage_charge)
update_baggage_limit(45)
print("Pay the extra baggage charge of",baggage_check(35),"rupees")
#useless_function_to_prove_a_point() """ 
"""def factorial(number):
    f=1
    if (number==0) or (number==1):
        return f
    else:
        for i in range(1,number+1):
            f*=i
        return f
print(factorial(5))"""
"""#Program to identify the luggage weight limit
airline="AI"
if(airline=="AI"):
    max_weight=30
    print(max_weight)
elif(airline=="EM"):
    max_weight=28
    print(max_weight)
elif(airline=="BA"):
    max_weight=35
    print(max_weight)
else:
    print("Invalid airline")"""
#PF-Tryout
#Start writing your code here
"""def get_grade(score):
    grade="Z"
    if score>=80 and score<=100:
        grade="A"
    elif score>=73 and score<=79:
        grade="B"
    elif score>=65 and score<=72:
        grade="C"
    elif score>=0 and score<=64:
        grade="D"
    return grade
print(get_grade(0))"""
"""def find_pairs_of_numbers(num_list,n):
    count = 0
    num_set = set(num_list)
    for num in num_list:
        complement = n - num
        if complement in num_set:
            try:
                num_set.remove(num)
                num_set.remove(complement)
                count += 1
            except KeyError as e:
                continue

    return count
    #Remove pass and write your logic here

num_list=[1, 2, 4, 5, 6]
n=10
print(find_pairs_of_numbers(num_list,n))
                """
"""#calculating airport expenditure
def calculate_expenditure(list_of_expenditure):
    total=0
    for expenditure in list_of_expenditure:
        if(type(expenditure) is int):
            total+=expenditure
        else:
            print("Wrong data type")
            break
    print(total)
list_of_values=[100,200,300,"400",500]
calculate_expenditure(list_of_values)                                    
"""
"""def calculate_expenditure(list_of_expenditure):
    total=0
    try:
        for expenditure in list_of_expenditure:
            total+=expenditure
        print(total)
    except:
        print("Some error occured")
    print("Returning back from function.")

list_of_values=[100,200,300,"400",500]
calculate_expenditure(list_of_values)"""
"""def calculate_expenditure(list_of_expenditure):
    total=0
    try:
        for expenditure in list_of_expenditure:
            total+=expenditure
        print("Total:",total)
        avg=total/num_values
        print("Average:",avg)
    except ZeroDivisionError:
        print("Divide by Zero error")
    except TypeError:
        print("Wrong data type")
    except:
        print("Some error occured")
list_of_values=[100,200,300,"400",500]
num_values=0
calculate_expenditure(list_of_values)"""
"""def calculate_expenditure(list_of_expenditure):
    total=0
    try:
        for expenditure in list_of_expenditure:
            total+=expenditure
        print("Total:",total)
        avg=total/num_values
        print("Average:",avg)
    except ZeroDivisionError:
        print("Divide by Zero error")
    except TypeError:
        print("Wrong data type")
    except:
        print("Some error occured")

list_of_values=[100,200,300,"400",500]
num_values=0
calculate_expenditure(list_of_values)"""
"""def calculate_sum(list_of_expenditure):
    total=0
    try:
        for expenditure in list_of_expenditure:
            total+=expenditure
        print("Total:",total)
        avg=total/no_values
        print("Average:",avg)
    except ZeroDivisionError:
        print("Divide by Zero error")
    except TypeError:
        print("Wrong data type")

try:
    list_of_values=[100,200,300,400,500]
    num_values=len(list_of_values)
    calculate_sum(list_of_values)
except NameError:
    print("Name error occured")
except:
    print("Some error occured")"""
"""balance=1000
amount="300Rs"
def take_card():
    print("Take the card out of ATM")
try:
    if balance>=int(amount):
        print("Withdraw")
    else:
        print("Invalid amount")

except TypeError:
    print("Type Error Occurred")
except ValueError:
    print("Value Error Occurred")
except:
    print("Some error Occurred")
finally:
    take_card()"""
"""def find_average(mark_list):
	try:
		total=0
		marks_avg=0
		for i in range(0,len(mark_list)):
			total+=mark_list[i]
		marks_avg=total/len(mark_list)
	except:
		print("Some error ocurred")
	return marks_avg

m_list=[1,2,3,4]
print("Average marks:", find_average(m_list))"""
"""def human_tower(no_of_people):
    if(no_of_people==1):
        return 1*(50)
    else:
        return no_of_people*(50)+human_tower(no_of_people-2)
print("Total weight of human tower: ",human_tower(35))"""
"""def tower_of_hanoi(n, source,destination,temp):
    if(n==1):
        disk=source.pop(0) #Removes the element in specified position
        destination.insert(0,disk) #Inserts the given element in specified position
        return
    tower_of_hanoi(n-1, source, temp, destination)
    disk=source.pop(0)
    destination.insert(0,disk)
    tower_of_hanoi(n-1, temp, destination, source)
    return

source=["blue","green","orange"]
destination=[]
temp=[]
tower_of_hanoi(3, source, destination, temp)
print("Source:",source)
print("Destination:",destination)"""
"""def find_ten_substring(num_str):
    try:
        # Validate input to ensure it only contains digits
        if not num_str.isdigit():
            raise ValueError("Input string must contain only digits.")
        
        ten_substrings = []
        length = len(num_str)
        substrings=[]
        for i in range(length):
            substrings.append(num_str[:i])
            print(substrings)

        for i in range(length):
            current_sum = 0
            substring = ""
            for j in range(i, length):
                current_sum += int(num_str[j])
                substring += num_str[j]
                
                if current_sum == 10:
                    ten_substrings.append(substring)
                    break
                elif current_sum > 10:
                    break
        
        return ten_substrings
    
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Testing the function
num_str = "3523014"
print("The number is:", num_str)
result_list = find_ten_substring(num_str)
print(result_list)"""
"""def find_all_substrings(input_str):
    substrings = []
    length = len(input_str)

    # Generate all substrings
    for i in range(length):
        for j in range(i + 1, length + 1):
            substrings.append(input_str[i:j])

    return substrings

def find_ten_substrings(num_str):
    try:
        # Validate input to ensure it only contains digits
        if not num_str.isdigit():
            raise ValueError("Input string must contain only digits.")

        # Get all substrings
        all_substrings = find_all_substrings(num_str)
        ten_substrings = []

        # Filter substrings whose sum of digits equals 10
        for substring in all_substrings:
            if sum(int(char) for char in substring) == 10:
                ten_substrings.append(substring)

        return ten_substrings

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Test the function
num_str = "3523014"
print("The number is:", num_str)
result_list = find_ten_substrings(num_str)
print("10-substrings are:", result_list)"""
"""def find_duplicates(list_of_numbers):
    # Create a dictionary to store the count of each number
    count_dict = {}
    # Create a list to store duplicates in order of appearance
    duplicates = []
    #create a list to store duplicates properly
    res = []
    
    # Iterate through the list
    for num in list_of_numbers:
        # If the number is already in the dictionary and not in duplicates, add it to duplicates
        if num in count_dict and num not in duplicates:
            duplicates.append(num)
        # Add or update the count of the number in the dictionary
        count_dict[num] = count_dict.get(num, 0) + 1
    
    for num in list_of_numbers:
        if num in duplicates and num not in res:
            res.append(num)

    return res

# Test the function
list_of_numbers = [1, 2, 3, 22, 33, 11, 34, 2, 34, 2, 1]
list_of_duplicates = find_duplicates(list_of_numbers)
print(list_of_duplicates)"""
"""try:
    flight_file=open("flight.txt","r")
    text=flight_file.read()
    print(text)
    flight_file.write(",Good Morning")
    flight_file.close()
except Exception as e:
    print("error occured")
    if flight_file.closed:
        print("File is closed")
    else:
        print("File is open")
        flight_file.close()"""
"""try:
    flight_file=open("flight.txt","r")
    text=flight_file.read()
    print(text)
    flight_file.write(",Good Morning")
except:
    print("Error occurred")
finally:
    print("File is being closed")
    flight_file.close()
    if flight_file.closed:
        print("File is closed")
    else:
        print("File is open")"""
"""try:
    hello_file=open("flight.txt","w")
    text="Hello everyone! Welcome"
    hello_file.write(text)
except:
    print("Error occurred, not able to write to file")
finally:
    hello_file.close()
try:
    hello_file=open("flights.txt","r")
    text_from_file=hello_file.read()
    print(text_from_file)
except:
    print("Error Occurred, not able to read from file")
finally:
    hello_file.close()"""
"""try:
    hello_file=open("flight.txt","w")
    text="Hello everyone! Welcome"
    hello_file.write(text)
except:
    print("Error occurred, not able to write to file")
finally:
    hello_file.close()
try:
    hello_file=open("flight.txt","r")
    text_from_file=hello_file.read()
    print(text_from_file)
except:
    print("Error Occurred, not able to read from file")
finally:
    hello_file.close()"""
"""def check_anagram(data1, data2):
    # Convert strings to lowercase to make comparison case insensitive
    data1 = data1.lower()
    data2 = data2.lower()

    # Check if the lengths of the two strings are the same
    if len(data1) != len(data2):
        return False
    
    # Create dictionaries to store the characters and their positions
    positions1 = {}
    positions2 = {}
    
    for i in range(len(data1)):
        if data1[i] in positions1:
            positions1[data1[i]].append(i)
        else:
            positions1[data1[i]] = [i]
        
        if data2[i] in positions2:
            positions2[data2[i]].append(i)
        else:
            positions2[data2[i]] = [i]
    
    # Compare the dictionaries of character positions
    for char in positions1:
        if positions1[char] != positions2.get(char, []):
            return False
    
    return True

# Test cases
print(check_anagram("eat", "tea"))  # Expected output: True
print(check_anagram("backward", "drawback"))  # Expected output: False
print(check_anagram("Reductions", "discounter"))  # Expected output: True
print(check_anagram("About", "table"))  # Expected output: False"""
"""def check_anagram(data1, data2):
    # Convert strings to lowercase to make comparison case insensitive
    data1 = data1.lower()
    data2 = data2.lower()

    # Check if the lengths of the two strings are the same
    if len(data1) != len(data2):
        return False
    
    # Check for frequency of characters
    freq_data1 = {}
    freq_data2 = {}
    
    for i in range(len(data1)):
        if data1[i] in freq_data1:
            freq_data1[data1[i]].append(i)
        else:
            freq_data1[data1[i]] = [i]
        
        if data2[i] in freq_data2:
            freq_data2[data2[i]].append(i)
        else:
            freq_data2[data2[i]] = [i]
    
    # Check if character frequencies match but positions don't
    for char in freq_data1:
        if sorted(freq_data1[char]) != sorted(freq_data2.get(char, [])):
            return False
        # Check that the positions are not identical
        if freq_data1[char] == freq_data2[char]:
            return False
    
    return True

# Test cases
print(check_anagram("eat", "tea"))  # Expected output: True
print(check_anagram("backward", "drawback"))  # Expected output: False
print(check_anagram("Reductions", "discounter"))  # Expected output: True
print(check_anagram("About", "table"))  # Expected output: False"""
"""def check_anagram(data1, data2):
    # Convert both strings to lowercase for case-insensitive comparison
    data1 = data1.lower()
    data2 = data2.lower()
    
    # Check if the lengths are the same
    if len(data1) != len(data2):
        return False
    
    # Check if the strings are identical
    if data1 == data2:
        return False
    
    # Check if each character is different at the same position
    # and if both strings contain the same characters
    return all(data1[i] != data2[i] for i in range(len(data1))) and sorted(data1) == sorted(data2)

print(check_anagram("eat", "tea"))
print(check_anagram("backward", "drawback"))  # Expected output: False
print(check_anagram("Reductions", "discounter"))  # Expected output: True
print(check_anagram("About", "table"))"""
"""def validate_name(name):
    return name and len(name) <= 15 and name.isalpha()

def validate_phone_no(phno):
    return (len(phno) == 10 and phno.isdigit() and
            len(set(phno)) > 1)  # Ensures not all digits are the same

def validate_email_id(email_id):
    if '@' not in email_id or not email_id.endswith('.com'):
        return False
    username, domain = email_id.split('@')
    domain_name = domain.split('.')[0]
    return domain_name in ['gmail', 'yahoo', 'hotmail']

def validate_all(name, phone_no, email_id):
    if not validate_name(name):
        print("Invalid Name")
    elif not validate_phone_no(phone_no):
        print("Invalid phone number")
    elif not validate_email_id(email_id):
        print("Invalid email id")
    else:
        print("All the details are valid")

# Provide different values for name, phone_no and email_id and test your program
validate_all("Tina", "9994599998", "tina@yahoo.com")"""
"""def ducci_sequence(test_list, n):
    

    sequence = [test_list]
    for _ in range(n+1):
        next_list = [abs(a - b) for a, b in zip(sequence[-1], sequence[-1][1:] + [sequence[-1][0]])]
        sequence.append(next_list)
    print(sequence)
    sequence.remove(test_list)
    sequence.append(test_list)
    print(sequence)
    return sequence[n]

ducci_element = ducci_sequence([0, 653, 1854, 4063], 1)
print(ducci_element)"""
"""class Vehicle:
    def __init__(self, fuel_left, mileage):
        self.mileage = mileage
        self.fuel_left = fuel_left
        self.reserve_fuel = 5
        self.vehicle_name="Car"

    def identify_distance_that_can_be_travelled(self):
        if self.fuel_left <= self.reserve_fuel:
            return 0
        else:
            return (self.fuel_left - self.reserve_fuel) * self.mileage

    def identify_distance_travelled(self, initial_fuel):
        fuel_consumed = initial_fuel - self.fuel_left
        return fuel_consumed * self.mileage

# Create a vehicle instance
my_vehicle = Vehicle(12, 20)

# Test identify_distance_that_can_be_travelled()
distance_can_travel = my_vehicle.identify_distance_that_can_be_travelled()
print(f"Distance that can be travelled: {distance_can_travel} km")

# Test identify_distance_travelled()
initial_fuel = 30
distance_travelled = my_vehicle.identify_distance_travelled(initial_fuel)
print(f"Distance already travelled: {distance_travelled} km")"""
"""class Applicant:
    __application_dict={"A":0,"B":0,"C":0}
    __applicant_id_count=1000
    
    def __init__(self,applicant_name):
        self.__applicant_name=applicant_name
        self.__applicant_id=None 
        self.__job_band=None 
        
    def generate_applicant_id(self):
        Applicant.__applicant_id_count+=1 
        self.__applicant_id = Applicant.__applicant_id_count
        
        
    def apply_for_job(self,job_band):
        if Applicant.__application_dict[job_band]==5:
            return -1
        else:
            Applicant.__application_dict[job_band]+=1 
            self.generate_applicant_id()
            self.__job_band=job_band
            
    @staticmethod
    def get_application_dict():
        return Applicant.application_dict()
        
    def get_applicant_id(self):
        return self.__applicant_id
        
    def get_applicant_name(self):
        return self.__applicant_name
        
    def get_job_band(self):
        return self.__job_band
        
        
        
a=Applicant("Jack")
a.apply_for_job("C")
a.apply_for_job("C")
a.apply_for_job("C")
a.apply_for_job("C")
print(a.apply_for_job("C"))
print(a.get_applicant_id())
#job_band-Aapplicant_name-Jack(Method invoked 5 times)"""
"""class Tollbooth:
    def __init__(self):
        self.__no_of_vehicle = 0
        self.__total_amount = 0

    def count_vehicle(self):
        self.__no_of_vehicle += 1

    def calculate_amount(self, vehicle_type):
        self.vehicle_type = vehicle_type.lower()
        
        if self.vehicle_type == "car":
            return 70
        elif self.vehicle_type == "bus":
            return 100
        elif self.vehicle_type == "truck":
            return 150
        else:
            return 70  # Default amount for any other vehicle type

    def collect_toll(self, owner_type, vehicle_type):
        owner_type = owner_type.lower()
        if owner_type != "vip":
            amount = self.calculate_amount(vehicle_type)
            self.__total_amount += amount
        self.count_vehicle()

    def get_no_of_vehicle(self):
        return self.__no_of_vehicle

    def get_total_amount(self):
        return self.__total_amount

# Test the calculate_amount method
tollbooth = Tollbooth()

# Test cases with debug output
print("Truck:", tollbooth.calculate_amount("Truck"))  # Expected output: 150
print("Car:", tollbooth.calculate_amount("Car"))  # Expected output: 70
print("Bus:", tollbooth.calculate_amount("Bus"))  # Expected output: 100
print("Van:", tollbooth.calculate_amount("Van"))  # Expected output: 70 (Default)"""
"""from datetime import date, timedelta
import time

class GarmentOrder:
    # Static dictionary
    garment_dict = {
        "shirt": [45, 400, 30],
        "trousers": [250, 500, 25],
        "saree": [500, 750, 10],
        "jersey": [750, 200, 5]
    }

    def __init__(self, cloth_type, no_of_piece):
        self.cloth_type = cloth_type
        self.no_of_piece = no_of_piece
        self.order_date = time.strftime("%d/%m/%Y")
        self.delivery_date = None
        return self.order_date

    def get_cloth_type(self):
        return self.cloth_type

    def get_no_of_piece(self):
        return self.no_of_piece

    def get_order_date(self):
        return self.order_date

    def get_delivery_date(self):
        return self.delivery_date

    def calculate_amount(self):
        if self.cloth_type in GarmentOrder.garment_dict:
            price_per_piece = GarmentOrder.garment_dict[self.cloth_type][1]
            return self.no_of_piece * price_per_piece
        return 0

    def update_stock(self):
        if self.cloth_type in GarmentOrder.garment_dict:
            available_pieces = GarmentOrder.garment_dict[self.cloth_type][0]
            delivery_days = GarmentOrder.garment_dict[self.cloth_type][2]
            if self.no_of_piece <= available_pieces:
                # Update stock
                GarmentOrder.garment_dict[self.cloth_type][0] -= self.no_of_piece
                # Calculate delivery date
                delivery_date_obj = date.today() + timedelta(days=delivery_days)
                self.delivery_date = delivery_date_obj.strftime("%d/%m/%Y")
                return True
        return False

    def take_order(self):
        if self.cloth_type in GarmentOrder.garment_dict and self.no_of_piece <= GarmentOrder.garment_dict[self.cloth_type][0]:
            total_amount = self.calculate_amount()
            self.update_stock()
            return total_amount
        else:
            return -1

# Example usage:
order1 = GarmentOrder("shirt", 2)
amount1 = order1.take_order()
print("Order 1 - Cloth Type:", order1.get_cloth_type())
print("Order 1 - Number of Pieces:", order1.get_no_of_piece())
print("Order 1 - Order Date:", order1.get_order_date())
print("Order 1 - Delivery Date:", order1.get_delivery_date())
print("Order 1 - Total Amount:", amount1)
print("Remaining stock for shirts:", GarmentOrder.garment_dict["shirt"][0])

order2 = GarmentOrder("trousers", 300)  # Exceeds available stock
amount2 = order2.take_order()
print("Order 2 - Cloth Type:", order2.get_cloth_type())
print("Order 2 - Number of Pieces:", order2.get_no_of_piece())
print("Order 2 - Total Amount:", amount2)  # Should return -1 since it exceeds stock"""
"""class Laptop:
    def __init__(self, grcode, expiry):
        self.__grcode = grcode
        self.__expiry = expiry
    
    def get_grcode(self):
        return self.__grcode
        
    def get_expiry(self):
        return self.__expiry

class Scanner:
    def __init__(self, emp_laptop_dict):
        self.__emp_laptop_dict = emp_laptop_dict

    def scan(self, empid, laptop):
        if empid in self.__emp_laptop_dict:
            allocated_laptop = self.__emp_laptop_dict[empid]
            if allocated_laptop.__grcode == laptop.__grcode and not allocated_laptop.__expiry:
                return True
        return False

# Example usage
if __name__ == "__main__":
    # Create some Laptop objects
    laptop1 = Laptop("QR123", False)  # Not expired
    laptop2 = Laptop("QR456", True)   # Expired

    # Initialize emp_laptop_dict
    emp_laptop_dict = {"E123": laptop1, "E456": laptop2}

    # Create a Scanner object
    scanner = Scanner(emp_laptop_dict)

    # Test scan method
    empid = "E123"
    laptop_to_scan = Laptop("QR123", False)
    result = scanner.scan(empid, laptop_to_scan)
    if result:
        print(f"Laptop with QR code {laptop_to_scan.qrcode} is allocated to employee {empid}.")
    else:
        print(f"Laptop with QR code {laptop_to_scan.qrcode} is not allocated to employee {empid} or has expired.")"""
"""def factorial(number):
    f=1
    if number == 0 or number == 1:
        return f
    elif number > 1:
        for i in range(1,number+1):
            f*=i
        return f
     #remove pass and write your logic to find and return the factorial of given number


def find_strong_numbers(num_list):
    res=[]
    for num in num_list:
        fact=0
        for digit in str(num):
            fact+=factorial(int(digit))
        if fact == num:
            res.append(num)
    return res #remove pass and write your logic to find and return the list of strong numbers from the given list


num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)"""
"""nums=[1,2,3,4,5]
for i in range(len(nums)):
    for j in range(len(nums)):
        if i!=j:
            print(i,j)"""
"""def find_pairs_of_numbers(num_list,n):
    res=[]
    resc=0
    for i in range(len(num_list)):
        for j in range(len(num_list)):
            if i!=j:
                #print(i,j)
                if num_list[i]+num_list[j] == n:
                    if i not in res and j not in res:
                        res.append(i)
                        res.append(j)
                        resc+=1
                    #if j not in res:
                        #res.append(j)
    return resc
    #Remove pass and write your logic here

num_list=[1, 2, 4, 5, 6]
n=6
print(find_pairs_of_numbers(num_list,n))"""
"""def sum_of_numbers(list_of_num,filter_func=None):
    sum=0
    if filter_func!=None:
        #f=filter_func
        f=[]
        if filter_func is even:
            f=even(list_of_num)
        else:
            f=odd(list_of_num)
        for num in f:
            sum+=num
    else:
        for num in list_of_num:
            sum+=num
    return sum  #Remove pass and write the logic here

def even(data):
    e=[]
    for n in data:
        if n%2 == 0:
            e.append(n)
    return e #Remove pass and write the logic here

def odd(data):
    o=[]
    for n in data:
        if n%2 != 0:
            o.append(n)
    return o #Remove pass and write the logic here

sample_data = range(1,11)

print(sum_of_numbers(sample_data,odd))"""
"""def check_double(number):
    digits=[]
    digitsd=[]
    double=0
    if number==0:
        return False
    elif number>0:
        double=2*number
        if len(str(double)) == len(str(number)):
            for digitd in str(double):
                digitsd.append(digitd)
            for digit in str(number):
                digits.append(digit)
            digits.sort()
            digitsd.sort()
            for i in range(len(digits)):
                if digits[i] == digitsd[i]:
                    pass
                else:
                    return False
                if i == len(digits)-1:
                    return True
        else:
            return False
    else:
        return False
    #Remove pass and write your logic here

#Provide different values for number and test your program
print(check_double(12874))"""
"""def calculate(distance,no_of_passengers):
    price_per_litre=70
    mileage_of_bus_in_kmpl=10
    price_per_ticket=80
    #profit=0
    total_ticket_amount=no_of_passengers*80
    petrol_cost_for_distance=(distance/10)*70
    if petrol_cost_for_distance>total_ticket_amount:
        return -1
    else:
        return abs(petrol_cost_for_distance-total_ticket_amount)
    #Remove pass and write your logic here



#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))"""
"""list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    total_marks=0
    no_of_students_with_gt_avg_marks=0
    for mark in list_of_marks:
        total_marks+=mark
    average=total_marks/average
    for mark in list_of_marks:
        if mark>average:
            no_of_students_with_gt_avg_marks+=1
    return no_of_students_with_gt_avg_marks*10
    
    #Remove pass and write your logic here

def sort_marks():
    slist=list(list_of_marks)
    slist.sort()
    return slist
    #Remove pass and write your logic here

def generate_frequency():
    lm=[]
    for i in range(26):
        lm.append(0)
    for i in range(26):
        count=0
        for j in list_of_marks:
            if i==j:
                count+=1
        lm[i]=count
    return lm
    #Remove pass and write your logic here

#print(find_more_than_average())
print(generate_frequency())
#print(sort_marks())"""
"""def find_average(mark_list):
	try:
		total=0
		for i in range(0, len(mark_list)):
		    total+=mark_list[i]
		marks_avg=total/len(mark_list)
		return marks_avg
	except:
		print("yo")

m_list=[1,2,3,4]
print("Average marks:", find_average(m_list))"""
"""class Employee_1:  
    def __init__(self, name, age, salary=20000):  
        self.name = name  
        self.age = age  
        self.salary = salary

 
E_1 = Employee_1("pqr", 20, 25000)  
# E1 is the instance of class Employee.  
#__init__ allocates memory for E1.   
print(E_1.name)  
print(E_1.age)  
print(E_1.salary)
E_2 = Employee_1("pqr", 20)
print(E_2.name)  
print(E_2.age)  
print(E_2.salary)"""
"""def human_tower(no_of_people):
    if(no_of_people==0):
        return 50
    elif (no_of_people<0):
        return 0
    else:
        return no_of_people*(50)+human_tower(no_of_people-2) #remove pass and place the recursive code the you had written earlier for this function

def find_maximum_people(max_weight):
    no_of_people=0
    for i in range(1,max_weight,2):
        if max_weight<human_tower(i):
            no_of_people=i-2
            break#write your logic here. You may invoke recursive function human_pyramid() wherever applicable 
    return no_of_people

#Provide different values for max_weight and test your program
max_people=find_maximum_people(1000)
print(max_people)
print(human_tower(9))"""
"""class Mobile:
    pass

mob1=Mobile()
mob2=Mobile()

print(id(mob1))
print(id(mob2))"""
"""class Mobile:
    pass

mob1=Mobile()
mob2=Mobile()

mob1.price=20000
mob1.brand="Apple"

mob2.price=3000
mob2.brand="Samsung"

print(mob1.price,mob1.brand,mob2.price,mob2.brand)"""
"""class Mobile:
    pass

mob1=Mobile()
mob2=Mobile()

mob1.price=20000
mob1.brand="Apple"
mob1.ios_version=10

mob2.price=3000
mob2.brand="Samsung"

print(mob1.price,mob1.brand,mob1.ios_version)
print(mob2.price,mob2.brand) """
"""class Mobile:
    pass

mob1=Mobile()
mob2=Mobile()

mob1.price=20000
mob1.brand="Apple"
mob1.ios_version=10

mob1.ios_version=11

mob2.price=3000
mob2.brand="Samsung"

mob2.android_version="Marshmallow"

print(mob1.ios_version)
print(mob2.android_version)"""
"""class Mobile:
    pass

mob1=Mobile()
mob2=Mobile()

mob1.price=20000
mob1.brand="Apple"
mob1.ios_version=10

mob2.price=3000
mob2.brand="Samsung"

print(mob1.ios_version)
print(mob2.ios_version)"""
"""class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
"""def subseq():
    s="leeeeetcode"
    t="yyyyylyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyeyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyeyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyeyyyyyyeyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyeyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyeyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyytyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyycyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyoyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyydyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyeyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
    visited=[]
    visitedval=[]
    d=dict()
    ret=t.__contains__(s)
    if ret==True:
        return ret
    sl=list(s)
    tl=list(t)
    for sli,slv in enumerate(sl):
        for tli,tlv in enumerate(tl):
            #print(sli,slv,tli,tlv)
            if slv==tlv and sli not in visited:
                if tlv in visitedval:
                    continue
                else:
                    d[tlv]=tli
                visited.append(sli)
                visitedval.append(tlv)
                print(sli,slv,tli,tlv)

    l=len(tl)
    i=0
    def poping(l):
        if tl[l] in sl and l>=0:
            d[i]=tl.pop(i)
            l-=1
            poping(len(tl)-1)
        elif l==0:
            return
        else:
            l-=1
    poping(l-1)
    print(d,sl,tl)
print(subseq())"""
"""def isSubsequence(s:str,t:str) -> bool:
    i,j=0,0
    while i<len(s) and j<len(t):
        print(i,j)
        if s[i]==t[j]:
            print(s[i])
            i+=1
        print(t[j])
        j+=1
    return i == len(s)
s="abc"
t="ahbgdc"
print(isSubsequence(s,t))"""
"""def is_palindrome(word):
    word=word.lower()
    if len(word)<=1:
        return True
    
    if word[0]==word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False
    #Remove pass and write your logic here

#Provide different values for word and test your program
result=is_palindrome("MadAMa")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")"""
"""class Mobile:
    def __init__(self):
        print("Inside constructor")
mob1=Mobile()"""
"""class Mobile:
    def __init__(self):
        print("Id of self in constructor", id(self))
mob1=Mobile()"""
"""class Mobile:
    def __init__(self):
        print("Inside constructor")
        

mob1=Mobile()
mob2=Mobile()"""
"""class Mobile:
    def __init__(self, brand, price):
        print("Inside constructor")
        self.brand = brand
        self.price = price

mob1=Mobile("Apple", 20000)
print("Mobile 1 has brand", mob1.brand, "and price", mob1.price)

mob2=Mobile("Samsung",3000)
print("Mobile 2 has brand", mob2.brand, "and price", mob2.price)
"""
"""class Mobile:
    def __init__(self,one,two):
        print("Inside constructor")

#Uncomment each line below. Try it out and observe the output.

#mob1=Mobile()
mob1=Mobile(100,200,300)"""
"""class Mobile:
    def __init__(self, price, brand):
        print("Id of self in constructor", id(self))
        self.price = price
        self.brand = brand

mob1=Mobile(1000, "Apple")
print("Id of mob1 in driver code", id(mob1))

mob2=Mobile(1000, "Apple")
print("Id of mob2 in driver code", id(mob2))"""
"""class Mobile:
    def __init__(self):
        print ("Inside the Mobile constructor")
        self.brand = None
        brand = "Apple" #This is a local variable.
        #Variables without self are local and they dont
        #affect the attributes.

        #Local varaibles cannot be accessed outside the init
        #Using self creates attributes which are
        #accessible in other methods as well

mob1=Mobile()
print(mob1.brand)#This does not print Apple
#This prints None because brand=Apple creates
#a local variable and it does not affect the attribute"""
"""class Mobile:
    def __init__(self):
        print("Inside constructor")

    def purchase (self):
        print("Purchasing a mobile")

mob1=Mobile()
mob1.purchase()"""
"""class Mobile:
    def __init__(self, brand, price):
        print("Inside constructor")
        self.brand = brand
        self.price = price
        
    def purchase(self):
        print("Purchasing a mobile")
        print("This mobile has brand", self.brand, "and price", self.price)
        
print("Mobile-1")
mob1=Mobile("Apple", 20000)
mob1.purchase()

print("Mobile-2")
mob2=Mobile("Samsung",3000)
mob2.purchase()"""
"""class Mobile:
    def display(self):
        print("Displaying details")

    def purchase(self):
        self.display()
        print("Calculating price")

Mobile().purchase()"""
"""class Mobile:
    def __init__(self,price,brand):
        print (id(self))
        self.price = price
        self.brand = brand

    def return_product(self):
        print (id(self))
        print ("Brand being returned is ",self.brand," and price is ",self.price)

mob1 = Mobile(1000, "Apple")
print ("Mobile 1 has id", id(mob1))

mob2=Mobile(2000, "Samsung")
print ("Mobile 2 has id", id(mob2))

mob2.return_product()
Mobile.return_product(mob2)"""
"""class Mobile:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

mob1=Mobile(1000, "Apple")
print(mob1.price)
#We are able to access the object
#in subsequent lines because we
#have a reference variable. This is
#like holding a balloon with a ribbon"""
"""class Mobile:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

print(Mobile(1000, "Apple").price)
#After the above line the Mobile
# object created is lost and unusable"""
"""class Mobile:
    def __init__(self, price, brand):
        print ("Inside constructor")
        self.price = price
        self.brand = brand

mob1=Mobile(1000, "Apple")
mob2=mob1
print ("Id of object referred by mob1 reference variable is :", id(mob1))
print ("Id of object referred by mob2 reference variable is :", id(mob2))
#mob1 and mob2 are reference variables to the same object"""
"""class Mobile:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

mob1=Mobile(1000, "Apple")
print("Price of mobile 1 :", mob1.price)

mob2=mob1
mob2.price=3000

print("Price of mobile 1 :", mob1.price)
print("Price of mobile 2 :", mob2.price)"""
"""class Mobile:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

mob1=Mobile(1000, "Apple")

mob2=mob1
mob2=Mobile(2000," Samsung")
mob2.price=3000

print("Mobile", "Id","Price")
print("mob1", id(mob1), mob1.price)
print("mob2", id(mob2), mob2.price)"""
"""
#Tried
class Vehicle:
    def __init__(self,mileage,fuel_left):
        self.mileage=mileage
        self.fuel_left=fuel_left
        
    def identify_disctance_that_can_be_travelled(self):
        distance=0
        if self.fuel_left<=5:
            return distance
        else:
            fuelwithoutreserve=self.fuel_left-5
            distance=fuelwithoutreserve*self.mileage
            return distance
    def identify_distance_travelled(self,initial_fuel):
        return (initial_fuel-self.fuel_left)*self.mileage

v=Vehicle(20,2)
print(v.identify_disctance_that_can_be_travelled())
print(v.identify_distance_travelled(3))"""
"""
#Actual Class
class Vehicle:
    def __init__(self):
        self.fuel_left=None
        self.mileage=None
        self.initial_fuel=10
        
    def identify_distance_that_can_be_travelled(self):
        if self.fuel_left>5:
            self.fuel=self.fuel_left-5
            self.distance=self.fuel*self.mileage
            return self.distance
        else:
            return 0
        
    def identify_distance_travelled(self,initial_fuel):
        self.initial_fuel=initial_fuel
        self.fuel=self.initial_fuel-self.fuel_left
        self.distance=self.fuel*self.mileage
        return self.distance
        
v1=Vehicle()
v1.mileage=50
v1.fuel_left=7
print(v1.identify_distance_that_can_be_travelled())
print(v1.identify_distance_travelled(20))"""
"""class Mobile:
    def __init__(self, brand, price):
        print("Inside constructor")
        self.brand = brand
        self.price = price
    def purchase(self):
        print("Purchasing a mobile")
        print("This mobile has brand", self.brand, "and price", self.price)
print("Mobile-1")
mob1=Mobile("Apple", 20000)
mob1.purchase()
print("Mobile-2")
mob2=Mobile("Samsung",3000)
mob2.purchase()"""
"""class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.wallet_balance = wallet_balance

    def update_balance(self,amount):
        if amount < 1000 and amount > 0:
            self.wallet_balance += amount

    def show_balance(self):
            print("The balance is ",self.wallet_balance)

c1=Customer(100, "Gopal", 24, 1000)
c1.update_balance(500)
c1.show_balance()"""
"""class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.wallet_balance = wallet_balance

    def update_balance(self, amount):
        if amount < 1000 and amount > 0:
            self.wallet_balance += amount

    def show_balance(self):
        print ("The balance is",self.wallet_balance)

c1=Customer(100, "Gopal", 24, 1000)
c1.wallet_balance = 10000000000

c1.show_balance()"""
"""class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance

    def update_balance(self, amount):
        if amount < 1000 and amount > 0:
            self.__wallet_balance += amount

    def show_balance(self):
        print ("The balance is ",self.__wallet_balance)

c1=Customer(100, "Gopal", 24, 1000)
#print(c1.__wallet_balance)
c1.update_balance(500)
c1.show_balance()"""
"""class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance

    def update_balance(self, amount):
        if amount < 1000 and amount > 0:
            self.__wallet_balance += amount

    def show_balance(self):
        print ("The balance is ",self.__wallet_balance)

c1=Customer(100, "Gopal", 24, 1000)
c1.__wallet_balance = 10000000000
c1.show_balance()"""
"""class Customer:
    def __init__(self, cust_id, name, age,wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance

    def update_balance(self, amount):
        if amount < 1000 and amount> 0:
            self.__wallet_balance += amount

    def show_balance(self):
        print ("The balance is ",self.__wallet_balance)

c1=Customer(100, "Gopal", 24, 1000)
c1._Customer__wallet_balance = 10000000000
c1.show_balance()"""
"""class Customer:
    def __init__(self, id, name, age, wallet_balance):
        self.id = id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance

    def set_wallet_balance(self, amount):
        if amount < 1000 and amount > 0:
            self.__wallet_balance = amount

    def get_wallet_balance(self):
        return self.__wallet_balance

c1=Customer(100, "Gopal", 24, 1000)
c1.set_wallet_balance(120)
print(c1.get_wallet_balance())"""
"""class Athlete:
    def __init__(self,name,gender):
        self.__name=name
        self.__gender=gender

    def set_name(self,name):
        self.__name=name
    def set_gender(self,gender):
        self.__gender=gender
    def get_name(self):
        return self.__name
    def get_gender(self):
        return self.__gender
    def running(self):
        if(self.__gender=="girl"):
            print("150mtr running")
        else:
            print("200mtr running")
                                    
a=Athlete("yo","male")
print(a.get_gender())
print(a.get_name())
a.set_gender("female")
a.set_name("yoyo")
print(a.get_gender())
print(a.get_name())
a.running()
"""
"""class Customer:
    def __init__(self, id, name, age, wallet_balance):
        self.id = id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance
    def set_wallet_balance(self, amount):
        if amount < 1000 and amount>  0:
            self.__wallet_balance = amount
    def get_wallet_balance(self):
        return self.__wallet_balance
c1=Customer(100, "Gopal", 24, 1000)
c1.set_wallet_balance(120)
print(c1.get_wallet_balance())"""
#Tried Class
"""class Vehicle:
    def __init__(self) -> None:
        self.__vehicle_id=None
        self.__vehicle_type=None
        self.__vehicle_cost=None
        self.__premium_amount=None
    
    def set_id(self,vehicle_id):
        self.__vehicle_id=vehicle_id

    def set_type(self,vehicle_type):
        if vehicle_type=="Two Wheeler" or vehicle_type=="Four Wheeler":
            self.__vehicle_type=vehicle_type
        else:
            print("Invalid vehicle type entered valid types are Two Wheeler and Four Wheeler try again with valid types")

    def set_cost(self,vehicel_cost):
        self.__vehicle_cost=vehicel_cost

    def get_id(self):
        return self.__vehicle_id
    
    def get_type(self):
        return self.__vehicle_type
    
    def get_cost(self):
        return self.__vehicle_cost
    
    def get_premium(self):
        return self.__premium_amount
    
    def calculate_premium(self):
        if self.__vehicle_type=="Two Wheeler":
            self.__premium_amount=0.2*self.__vehicle_cost
        elif self.__vehicle_type=="Four Wheeler":
            self.__premium_amount=0.6*self.__vehicle_cost
        else:
            print("Invalid vehicle type")

    def display_vehicle_details(self):
        print("Vehicle id:",self.__vehicle_id)
        print("Vehicle type:",self.__vehicle_type)
        print("Vehicle cost:",self.__vehicle_cost)
        print("Premium amount:",self.__premium_amount)"""
"""class Laptop:
    def __init__(self, qrcode, allocation_expiry_date):
        self.__qrcode = qrcode
        self.__allocation_expiry_date = allocation_expiry_date

    def get_qrcode(self):
        return self.__qrcode

    def is_expired(self):
        return self.__allocation_expiry_date


class Scanner:
    emp_laptop_dict = {}

    def __init__(self, emp_laptop_dict):
        Scanner.emp_laptop_dict = emp_laptop_dict

    def validate_expiry_date(self, laptop):
        return not laptop.is_expired()

    def validate_emp_laptop(self, emp_id, laptop):
        if emp_id in Scanner.emp_laptop_dict:
            assigned_laptop = Scanner.emp_laptop_dict[emp_id]
            if assigned_laptop.get_qrcode() == laptop.get_qrcode():
                return self.validate_expiry_date(assigned_laptop)
        return False

    def scan(self, emp_id, laptop):
        return self.validate_emp_laptop(emp_id, laptop)


# Test the implementation

# Creating Laptop objects
laptop1 = Laptop("QR001", False)  # Not expired
laptop2 = Laptop("QR002", True)   # Expired
laptop3 = Laptop("QR003", False)  # Not expired

# Creating an employee-laptop dictionary
emp_laptop_dict = {
    "EMP001": laptop1,
    "EMP002": laptop2,
    "EMP003": laptop3
}

# Creating a Scanner object
scanner = Scanner(emp_laptop_dict)

# Testing the scan method
print(scanner.scan("EMP001", laptop1))  # Expected output: True (Laptop matches and not expired)
print(scanner.scan("EMP002", laptop2))  # Expected output: False (Laptop matches but expired)
print(scanner.scan("EMP003", laptop1))  # Expected output: False (Laptop does not match)
print(scanner.scan("EMP003", laptop3))  # Expected output: True (Laptop matches and not expired)
print(scanner.scan("EMP004", laptop3))  # Expected output: False (Employee ID not found)
"""
"""def find_factors(num):
    #Accepts a number and returns the list of all the factors of a given number
    factors = []
    for i in range(2,(num+1)):
        if(num%i==0):
            factors.append(i)
    return factors

def is_prime(num, i):
    #Accepts the number num and num/2 --> i and returns True if the number is prime ,else returns False
    if(i==1):
        return True
    elif(num%i==0):
        return False
    else:
        return(is_prime(num,i-1))

def find_largest_prime_factor(list_of_factors):
    prime_factor=None
    for i in list_of_factors:
        pf=is_prime(i,i//2)
        if pf == True:
            prime_factor=i
    return prime_factor
    #Accepts the list of factors and returns the largest prime factor

def find_f(num):
    factors=find_factors(num)
    return find_largest_prime_factor(factors)
    #Accepts the number and returns the largest prime factor of the number

def find_g(num):
    res=0
    for inc in range(num,num+9):
        res+=find_f(inc)
    return res
    #Accepts the number and returns the sum of the largest prime factors of the 9 consecutive numbers starting from the given number

#Note: Invoke function(s) from other function(s), wherever applicable.

print(find_g(10))"""
"""def find_factors(num):
    # Accepts a number and returns the list of all the factors of a given number
    factors = []
    for i in range(2, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def is_prime(num, i):
    # Accepts the number num and num/2 --> i and returns True if the number is prime, else returns False
    if i == 1:
        return True
    elif num % i == 0:
        return False
    else:
        return is_prime(num, i - 1)

def find_largest_prime_factor(list_of_factors):
    # Accepts the list of factors and returns the largest prime factor
    largest_prime = None
    for factor in list_of_factors:
        if is_prime(factor, factor // 2):
            largest_prime = factor
    return largest_prime

def find_f(num):
    # Accepts the number and returns the largest prime factor of the number
    factors = find_factors(num)
    return find_largest_prime_factor(factors)

def find_g(num):
    # Accepts the number and returns the sum of the largest prime factors of the 9 consecutive numbers starting from the given number
    total_sum = 0
    for i in range(num, num + 9):
        total_sum += find_f(i)
    return total_sum

# Note: Invoke function(s) from other function(s), wherever applicable.

print(find_g(10))"""
"""def findMaxAverage( nums: list[int], k: int):
    e=len(nums)
    s=0
    d=e-k
    lofk=k
    avgs=[]
    while s<=d and k<=e:
        l=nums[s:k]
        #print(l,s,k)
        sum=0
        for i in l:
            sum+=i
        avg=sum/lofk
        #print(avg)
        avgs.append(avg)
        s+=1
        k+=1
    return max(avgs)
    #print(l,s,k)"""
"""def findMaxAverage(nums, k):
    # Calculate the sum of the first 'k' elements
    current_sum = sum(nums[:k])
    max_sum = current_sum
    
    # Slide the window across the array
    for i in range(k, len(nums)):
        # Adjust the sum by removing the element leaving the window
        # and adding the new element entering the window
        current_sum += nums[i] - nums[i - k]
        
        # Update the maximum sum encountered so far
        max_sum = max(max_sum, current_sum)
    
    # Return the maximum average
    return max_sum / k

# Example usage
nums = [1, 12, -5, -6, 50, 3]
k = 4
result = findMaxAverage(nums, k)
print(result)  # Output should be 12.75
"""
"""#Tried
def find_smallest_number(num):
    #start writing your code here
    if num==0:
        return 0
    elif num==1:
        return 1
    elif num==2:
        return 2
    for i in range(3,100001):
        divisorcount=0
        for j in range(1,100001):
            if i%j==0:
                divisorcount+=1
        if divisorcount==num:
            return i

num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)"""
"""#Correct
def find_smallest_number(num):
    try:
        if not isinstance(num, int) or num <= 0:
            raise ValueError("Input must be a positive integer.")
        
        def count_divisors(n):
            count = 0
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    if i == n // i:
                        count += 1
                    else:
                        count += 2
            return count

        smallest_number = 1
        while count_divisors(smallest_number) != num:
            smallest_number += 1
        
        return smallest_number
    
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Testing the function
num = 16
print("The number of divisors:", num)
result = find_smallest_number(num)
if result:
    print("The smallest number having", num, "divisors:", result)"""
"""def largestAltitude(gain: list[int]):
    alts=[0]
    ind=0
    for g in gain:
        alts.append(g+alts[ind])
        ind+=1
    return max(alts)
gain = [-5,1,5,0,-7]
print(largestAltitude(gain))"""
"""def find_ten_substring(num_str):
    pass
    #Remove pass and write your logic here

num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)"""
"""class Laptop:
    def __init__(self, grcode, expiry):
        self.__grcode = grcode
        self.__expiry = expiry

    def get_grcode(self):
        return self.__grcode

    def get_expiry(self):
        return self.__expiry


class Scanner:
    #self.__emp_laptop_dict = {} 

    def __init__(self, emp_laptop_dict):
        self.__emp_laptop_dict = emp_laptop_dict
        #emp_laptop_dict=emp_laptop_dict

    def validate_expiry_date(self, laptop):
        return not laptop.get_expiry()

    def validate_emp_laptop(self, empid, laptop):
        if empid in self.__emp_laptop_dict:
            assigned_laptop = self.__emp_laptop_dict[empid]
            if assigned_laptop.get_grcode() == laptop.get_grcode():
                return self.validate_expiry_date(assigned_laptop)
        return False

    def scan(self, empid, laptop):
        return self.validate_emp_laptop(empid, laptop)


# Test the implementation

# Creating Laptop objects
laptop1 = Laptop("QR001", False)  # Not expired
laptop2 = Laptop("QR002", True)   # Expired
laptop3 = Laptop("QR003", False)  # Not expired
laptop4 = Laptop("QR004", False)  # Not expired

# Step 2: Initializing emp_laptop_dict with employee ID as the key and Laptop objects as values
emp_laptop_dict = {
    101: laptop1,  # Employee 101 is assigned laptop1 (QR001)
    102: laptop2,  # Employee 102 is assigned laptop2 (QR002)
    103: laptop3   # Employee 103 is assigned laptop3 (QR003)
}

# Step 3: Creating a Scanner object using the emp_laptop_dict
scanner = Scanner(emp_laptop_dict)

# Step 4: Testing the scan method by passing different empid and laptop combinations
print(scanner.scan(101, laptop1))  # Expected: True (Correct laptop, not expired)
print(scanner.scan(102, laptop2))  # Expected: False (Laptop is expired)
print(scanner.scan(103, laptop1))  # Expected: False (Employee 103 does not have laptop1)
print(scanner.scan(101, laptop3))  # Expected: False (Employee 101 does not have laptop3)
print(scanner.scan(103, laptop3))  # Expected: True (Correct laptop, not expired)
print(scanner.scan(104, laptop4))  # Expected: False (Employee 104 is not in the dictionary)"""
"""def pivotIndex(nums):
    p=0
    while p<len(nums):
        leftsum=0
        rightsum=0
        if p!=0:
            for i in range(0,p):
                leftsum+=nums[i]
        if p!=len(nums)-1:
            for i in range(p+1,len(nums)):
                rightsum+=nums[i]
        if leftsum==rightsum:
            return p
        #print(p,leftsum,rightsum)
        if p==len(nums)-1:
            break
        p+=1
    return -1

print(pivotIndex([1,2,3]))"""
"""def pivotIndex(nums):
    sumLeft=[]
    sumRight=[]
    #for i in range(len(nums)):
        
    for i in range(len(nums)):
        sumLeft.append(0)
        sumRight.append(0)
        sumLeft[i]=sum(nums[0:i])
        #for j in range(i):
            #sumLeft[i]+=nums[j]
        sumRight[i]=sum(nums[i+1:len(nums)])
        #for k in range(i+1,len(nums)):
            #sumRight[i]+=nums[k]
        if sumLeft[i]==sumRight[i]:
            return i
    #print(sumLeft,sumRight)    
    return -1

print(pivotIndex([1,2,3]))
"""
"""class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

rect = Rectangle(10, 5)
for dim in rect:
    print(dim)

# Output:
# {'length': 10}
# {'width': 5}"""
"""# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal started")
    time.sleep(5)  # Simulating a long-running task
    print("Signal finished")

# views.py
from django.contrib.auth.models import User

def create_user(request):
    print("Before user creation")
    user = User.objects.create(username="new_user")  # This triggers the post_save signal
    print("After user creation")

# Output:
# Before user creation
# Signal started
# (5 seconds delay)
# Signal finished
# After user creation"""
"""def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    s1=list(set(nums1))
    s2=list(set(nums2))
    c=[]
    for i in s1:
        if i in s2:
            c.append(i)
    print(s1,s2,c)
    for i in c:
        if i in s1:
            s1.remove(i)
        if i in s2:
            s2.remove(i)
    r=[s1,s2]
    return r

print(findDifference([1,2,3],[2,4,6]))"""
"""
#Tried answer
class RecentCounter:

    def __init__(self):
        self.counter=0
        self.requests=[]  
        self.r=[]     

    def ping(self, t: int) -> int:
        self.counter=0
        self.requests.append(t)
        self.r=[t-3000,t]
        for i in self.requests:
            #print("i being checked:",i)
            if i in range(self.r[0],self.r[1]+1):
                #print(i)
                self.counter+=1
        return self.counter
        


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
param_1 = obj.ping(1)
print(obj.requests,obj.r,obj.counter)
param_2 = obj.ping(100)
print(obj.requests,obj.r,obj.counter)
param_3 = obj.ping(3001)
print(obj.requests,obj.r,obj.counter)
param_4 = obj.ping(3002)
print(param_1,param_2,param_3,param_4,obj.requests,obj.r)"""
"""#Submitted answer
from collections import deque

class RecentCounter:

    def __init__(self):
        self.requests = deque()  # Use a deque to store only recent requests

    def ping(self, t: int) -> int:
        self.requests.append(t)
        
        # Remove requests that are out of the 3000 ms range
        while self.requests[0] < t - 3000:
            self.requests.popleft()  # Efficiently remove old requests
        
        # The length of the queue is the count of recent requests
        return len(self.requests)
"""
"""def find_ten_substring(num_str):
    result_list=[]
    for i in range(len(num_str)):
        num=0
        num+=int(num_str[i])
        eles=""
        eles+=num_str[i]
        #print("num:",num,"eles:",eles)
        if i==len(num_str)-1:
            break
        for j in range(i+1,len(num_str)):
            num+=int(num_str[j])
            eles+=num_str[j]
            if num == 10:
                #print("eles:",eles)
                result_list.append(eles)
            #print(num,end=" ")
        #print()
        #print(type(num))
    return result_list
    #Remove pass and write your logic here

num_str="3523014"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)"""
"""def find_duplicates(list_of_numbers):
    #start writing your code here
    count=[0]*len(list_of_numbers)
    ret=[]
    for i in range(len(list_of_numbers)):
        print(i,list_of_numbers[i])
        for j in range(len(list_of_numbers)):
            if list_of_numbers[i]==list_of_numbers[j]:
                count[i]+=1
    for inc in range(len(count)):
        if count[inc]>1 and list_of_numbers[inc] not in ret:
            ret.append(list_of_numbers[inc])
    return ret

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)"""
"""#Tried
class Instructor:
    def __init__(self, instructor_name, technology_skill, experience, avg_feedback):
        self.__instructor_name=instructor_name
        self.__technology_skill=technology_skill
        self.__experience=experience
        self.__avg_feedback=avg_feedback
    
    def set_instructor_name(self, instructor_name):
        self.__instructor_name=instructor_name
    
    def get_instructor_name(self):
        return self.__instructor_name
    
    def set_technology_skill(self, technology_skill):
        self.__technology_skill=technology_skill
    
    def get_technology_skill(self):
        return self.__technology_skill
    
    def set_experience(self, experience):
        self.__experience=experience
    
    def get_experience(self):
        return self.__experience
    
    def set_avg_feedback(self, avg_feedback):
        self.__avg_feedback=avg_feedback
    
    def get_avg_feedback(self):
        return self.__avg_feedback

    def check_eligibilty(self, technology):
        if technology in self.__technology_skill:
            if self.__experience>3 and self.__avg_feedback>=4.5:
                return True
            elif self.__experience<=3 and self.__avg_feedback>=4:
                return True
            else:
                return False
        else:
            return False

    def allocate_course(self, technology):
        if self.check_eligibilty(technology) == True:
            return True
        else:
            return False"""
"""#Actual
class Instructor:
    def __init__(self):
        self.__instructor_name=None
        self.__experience=None
        self.__avg_feedback=None
        self.__technology_skill=None
        
    def set_instructor_name(self,instructor_name):
        self.__instructor_name=instructor_name
        
    def set_experience(self,experience):
        self.__experience=experience
        
    def set_avg_feedback(self,avg_feedback):
        self.__avg_feedback=avg_feedback
        
    def set_technology_skill(self,technology_skill):
        self.__technology_skill=technology_skill
        
    def get_instructor_name(self):
        return self.__instructor_name
    
    def get_experience(self):
        return self.__experience
        
    def get_avg_feedback(self):
        return self.__avg_feedback
        
    def get_technology_skill(self):
        return self.__technology_skill
        
    def check_eligibility(self):
        if self.__experience>3 and self.__avg_feedback>=4.5:
            return True
        elif self.__experience<=3 and self.__avg_feedback>=4:
            return True
        else:
            return False
            
    def allocate_course(self,technology):
        if((technology==self.__technology_skill) or (technology=="C++")):
            return True
        else:
            return False"""
"""#Tried
class Student:
    def __init__(self):
        self.__student_id=None
        self.__marks=None
        self.__age=None
        self.__course_id=None
        self.__fees=None
    
    def set_course_id(self, course_id):
        self.__course_id=course_id

    def get_course_id(self):
        return self.__course_id
    
    def set_fees(self, fees):
        self.__fees=fees

    def get_fees(self):
        return self.__fees  

    def set_student_id(self, student_id):
        self.__student_id=student_id
    
    def get_student_id(self):
        return self.__student_id
    
    def set_marks(self, marks):
        self.__marks=marks

    def get_marks(self):
        return self.__marks
    
    def set_age(self, age):
        self.__age=age
    
    def get_age(self):
        return self.__age

    def validate_age(self):
        if self.__age>20:
            return True
        else:
            return False
    
    def validate_marks(self):
        if self.__marks>=0 and self.__marks<=100:
            return True
        else:
            return False
        
    def check_qualification(self):
        if self.validate_marks() and self.validate_age():
            if self.__marks>=65:
                return True
            else:
                return False
        else:
            return False

    def choose_course(self, course_id):
        if course_id in [1001,1002]:
            if course_id==1001:
                self.set_course_id(course_id)
                self.set_fees(25575.0)
                if self.__marks>85:
                    self.__fees/=4
                    #self.get_fees
                return True
            elif course_id==1002:
                self.set_course_id(course_id)
                self.set_fees(15500.0)
                if self.__marks>85:
                    self.__fees/=4
                    #self.get_fees()
                return True
        else:
            return False


maddy=Student()
maddy.set_student_id(1004)
maddy.set_age(21)
maddy.set_marks(89)
if(maddy.check_qualification()):
    print("Student has qualified")
    if(maddy.choose_course(1001)):
        print("Course allocated")
    else:
        print("Invalid course id")
else:
    print("Student has not qualified")
print(maddy.get_fees())"""
"""#Actual
class Student:
    def __init__ (self):
            self.__student_id=None
            self.__age=None
            self.__marks=0
            self.__course_id=None
            self.__fees=None
            
    def set_student_id(self, student_id):
            self.__student_id = student_id
    def get_student_id(self):
        return self.__student_id
    
    def set_age(self, age):
            self.__age = age
    def get_age(self):
        return self.__age   
    
    def set_marks(self, marks):
            self.__marks =marks
    def get_marks(self):
        return self.__marks
        
    def get_course_id(self):
        return self.__course_id
    def get_fees(self):
        return self.__fees
        
    def validate_marks(self):
             if(self.__marks>=0 and self.__marks<=100):
                 return True
             else:
                 return False   
    
    def validate_age(self):
            if(self.__age>20):
                 return True
            else:
                 return False
                 
    def check_qualification(self):
            if(self.__age>20 and self.__marks>=65 and self.validate_marks()):
                 return True
            else:
                 return False
        
    def choose_course(self,course_id):
        if(self.check_qualification() and (course_id==1001 or course_id==1002)):
            self.__course_id=course_id
            if(course_id==1001):
                self.__fees=25575.0
            elif(course_id==1002):
                self.__fees=15500.0
            if(self.__marks>85):
                self.__fees=self.__fees-(self.__fees*25/100)
            return True
        return False
    
maddy=Student()
maddy.set_student_id(1001)
maddy.set_age(21)
maddy.set_marks(84)
if(maddy.check_qualification()):
    print("Student has qualified")
    if(maddy.choose_course(1002)):
        print("Course allocated")
    else:
        print("Invalid course id")
else:
    print("Student has not qualified")"""
"""class s:
    print("s inside class")
    def __init__(self) -> None:
        pass

so=s()"""
"""#Correct code
def check_anagram(data1,data2):
    #start writing your code here
    if len(data1) != len(data2):
        return False
    elif data1.lower() == data2.lower():
        return False
    for i in range(len(data1)):
        if data1[i].lower() not in data2.lower():
            return False
        for j in range(len(data2)):
            if data2[j].lower() not in data1.lower():
                return False
            if data1[i].lower() == data2[j].lower() and i==j:
                return False        
    return True

print(check_anagram("Schoolmaster","Theclassroom"))"""
"""class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

mob1=Mobile("Apple", 1000)
mob2=Mobile("Samsung", 2000)
mob3=Mobile("Apple", 3000)
mob4=Mobile("Samsung", 4000)
mob5=Mobile("Apple", 5000)

list_of_mobiles=[mob1, mob2, mob3, mob4, mob5]

for mobile in list_of_mobiles:
    print (mobile.brand,mobile.price)"""
"""class Mobile:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

mob1=Mobile("Apple", 1000)
mob2=Mobile("Samsung", 5000)
mob3=Mobile("Apple", 3000)

mob_dict={
          "m1":mob1,
          "m2":mob2,
          "m3":mob3
          }

for key,value in mob_dict.items():
    if value.price > 3000:
        print (value.brand,value.price)"""
"""class Customer:
    def __init__(self, cust_id, cust_name, location):
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.location = location

list_of_customers = [Customer(101, 'Mark', 'US'),
Customer(102, 'Jane', 'Japan'),
Customer(103, 'Kumar', 'India')]
dict_of_customer={}
for i in list_of_customers:
    dict_of_customer[i.location]=i

print(dict_of_customer)"""
"""class Customer:
    def __init__(self, cust_id, cust_name, location):
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.location = location

list_of_customers = [Customer(101, 'Mark', 'US'),
                     Customer(102, 'Jane', 'Japan'),
                     Customer(103, 'Kumar', 'India')]

dict_of_customer = {}
for customer in list_of_customers:
    dict_of_customer[customer.location] = customer

print ("Customer name in India is "+dict_of_customer["India"].cust_name)

for key,value in dict_of_customer.items():
    print ("Location: "+key+", Name: "+value.cust_name+", Id: "+(str(value.cust_id)))"""
"""class Mobile:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
        self.discount = 0
    def purchase(self):
        total = self.price - self.price * self.discount / 100
        print (self.brand, "mobile with price", self.price, "is available after discount at", total)
def enable_discount(list_of_mobiles):
    for mobile in list_of_mobiles:
        mobile.discount=50
def disable_discount(list_of_mobiles):
    for mobile in list_of_mobiles:
        mobile.discount=0
mob1=Mobile(20000, "Apple")
mob2=Mobile(30000, "Apple")
mob3=Mobile(5000, "Samsung")
mob4=Mobile(6000, "Samsung")
list_of_mobiles=[mob1,mob2,mob3,mob4]
mob1.purchase()
enable_discount(list_of_mobiles)
mob2.purchase()
mob3.purchase()
disable_discount(list_of_mobiles)
mob4.purchase()"""
"""class Mobile:
    discount = 50
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def purchase(self):
        total = self.price - self.price * Mobile.discount / 100
        print (self.brand, "mobile with price", self.price, "is available after discount at", total)

mob1=Mobile(20000, "Apple")
mob2=Mobile(30000, "Apple")
mob3=Mobile(5000, "Samsung")

mob1.purchase()
mob2.purchase()
mob3.purchase()"""
"""class Mobile:
    discount = 50
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def purchase(self):
        total = self.price - self.price * Mobile.discount / 100
        print (self.brand, "mobile with price", self.price, "is available after discount at", total)

def enable_discount():
    Mobile.discount = 50

def disable_discount():
    Mobile.discount = 0

mob1=Mobile(20000, "Apple")
mob2=Mobile(30000, "Apple")
mob3=Mobile(5000, "Samsung")

enable_discount()
mob1.purchase()
mob2.purchase()
disable_discount()
mob3.purchase()"""
"""class Mobile:
    __discount = 50
    def __init__(self):
        pass
    def get_discount(self):
        return Mobile.__discount

    def set_discount(self,discount):
        Mobile.__discount = discount

m1=Mobile()
m2=Mobile()
print(m1.get_discount())
Mobile().set_discount(30)
print(m1.get_discount(),m2.get_discount())"""
"""class Mobile:
    __discount = 50
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def purchase(self):
        total = self.price - self.price * Mobile.__discount / 100
        print ("Total is ",total)

    def get_discount(self):
        return Mobile.__discount

    def set_discount(self,discount):
        Mobile.__discount = discount

mob1=Mobile(20000, "Apple")
mob2=Mobile(30000, "Apple")
mob3=Mobile(5000, "Samsung")

print(mob1.get_discount())"""
"""class Mobile:
    __discount = 50
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def purchase(self):
        total = self.price - self.price * Mobile.__discount / 100
        print ("Total is ",total)

    @staticmethod
    def get_discount():
        return Mobile.__discount

    @staticmethod
    def set_discount(discount):
        Mobile.__discount = discount

print (Mobile.get_discount())"""
"""#The complete solution
class Mobile:
    __discount = 50
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def purchase(self):
        total = self.price - self.price * Mobile.__discount / 100
        print (self.brand, "mobile with price", self.price, "is available after discount at", total)

    @staticmethod
    def enable_discount():
        Mobile.set_discount(50)

    @staticmethod
    def disable_discount():
        Mobile.set_discount(0)

    @staticmethod
    def get_discount():
        return Mobile.__discount

    @staticmethod
    def set_discount(discount):
        Mobile.__discount = discount

mob1=Mobile(20000, "Apple")
mob2=Mobile(30000, "Apple")
mob3=Mobile(5000, "Samsung")

Mobile.disable_discount()

mob1.purchase()

Mobile.enable_discount()

mob2.purchase()

Mobile.disable_discount()

mob3.purchase()"""
"""class Mobile:
    counter = 1000
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
        self.mobile_id = Mobile.counter
        Mobile.counter += 1

mob1=Mobile(20000, "Apple")
mob2=Mobile(30000, "Apple")
mob3=Mobile(5000, "Samsung")

print("mobile_id for mob1 is", mob1.mobile_id)
print("mobile_id for mob2 is", mob2.mobile_id)
print("mobile_id for mob3 is", mob3.mobile_id)

print("Current value of counter is", Mobile.counter)"""
"""class Example:
    def __init__(self):
        self.__num=10
    @staticmethod
    def display():
        self.__num+=1
        print(self.__num)
obj=Example()
obj.display()"""
"""class Ticket:
    counter=0
    def __init__(self,passenger_name,source,destination) -> None:
        self.__passenger_name=passenger_name
        self.__source=source
        self.__destination=destination
        self.__ticket_id=None

    def validate_source_destination(self):
        if self.__source=="Delhi".lower() and self.__destination.lower() in ["mumbai","chennai","pune","kolkata"]:
            return True
        else:
            return False

    def generate_ticket(self):
        if self.validate_source_destination():
            Ticket.counter+=1
            self.__ticket_id=""
            self.__ticket_id+="D"
            self.__ticket_id+=self.__destination[0]
            if Ticket.counter in [1,2,3,4,5,6,7,8,9]:
                self.__ticket_id+="0"
                self.__ticket_id+=str(Ticket.counter)
            else:
                self.__ticket_id+=str(Ticket.counter)
        else:
            self.__ticket_id=None

    def get_ticket_id(self):
        return self.__ticket_id

    def get_passenger_name(self):
        return self.__passenger_name
    
    def get_source(self):
        return self.__source
    
    def get_destination(self):
        return self.__destination
    
t=Ticket("Ram","delhi","Chennai")
print(t.validate_source_destination())"""
"""class Flower:
    def __init__(self):
        self.__flower_name=None
        self.__price_per_kg=None
        self.__stock_available=None
    
    def validate_flower(self):
        if self.__flower_name.lower() in ["orchid","rose","jasmine"]:
            return True
        else:
            return False
        
    def validate_stock(self,required_quantity):
        if required_quantity <= self.__stock_available:
            return True
        else:
            return False

    def check_level(self):
        if self.__flower_name.lower()=="orchid" and self.__stock_available<15:
            return True
        elif self.__flower_name.lower()=="rose" and self.__stock_available<25:
            return True
        elif self.__flower_name.lower()=="jasmine" and self.__stock_available<40:
            return True
        else:
            return False
           
    def sell_flower(self, required_quantity):
        if self.validate_flower() and self.validate_stock(required_quantity):
            self.__stock_available-=required_quantity

    def set_flower_name(self, flower_name):
        self.__flower_name=flower_name
    
    def get_flower_name(self):
        return self.__flower_name
    
    def set_price_per_kg(self, price_per_kg):
        self.__price_per_kg=price_per_kg

    def get_price_per_kg(self):
        return self.__price_per_kg
    
    def set_stock_available(self, stock_available):
        self.__stock_available=stock_available

    def get_stock_available(self):
        return self.__stock_available"""
"""class CallDetail:
    def __init__(self,phoneno,called_no,duration,call_type):
        self.__phoneno=phoneno
        self.__called_no=called_no
        self.__duration=duration
        self.__call_type=call_type

class Util:
    def __init__(self):
        self.list_of_call_objects=None

    def parse_customer(self,list_of_call_string):
        customers=[]
        for i in list_of_call_string:
            customers.append(i.split(","))
        self.list_of_call_objects=[]
        for j in customers:
            self.list_of_call_objects.append(CallDetail(j[0],j[1],j[2],j[3]))
        return self.list_of_call_objects
        

call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'

list_of_call_string=[call,call2,call3]
print(Util().parse_customer(list_of_call_string))"""
"""class Bill:
    def __init__(self,bill_id,patient_name):
        self.__bill_id=bill_id
        self.__patient_name=patient_name
        self.__bill_amount=0

    def get_bill_id(self):
        return self.__bill_id
    
    def get_patient_name(self):
        return self.__patient_name
    
    def get_bill_amount(self):
        return self.__bill_amount
    
    def calculate_bill_amount(self,consultation_fees,quantity_list,price_list):
        self.__bill_amount+=consultation_fees
        for i in range(len(quantity_list)):
            self.__bill_amount+=quantity_list[i]*price_list[i]"""
"""class Classroom:
    classroom_list=[]
    @staticmethod
    def search_classroom(class_room):
        for i in range(len(Classroom.classroom_list)):
            if class_room.lower() == Classroom.classroom_list[i].lower():
                return "Found"
        return -1"""
"""class Customer:
    def __init__(self, name, age, phone_no, address):
        self.name = name
        self.age = age
        self.phone_no = phone_no
        self.address = address

    def view_details(self):
        print (self.name, self.age, self.phone_no)
        print (self.address.get_door_no(), self.address.get_street(), self.address.get_pincode())

class Address:
    def __init__(self, door_no, street, pincode):
        self.__door_no = door_no
        self.__street = street
        self.__pincode = pincode

    def get_door_no(self):
        return self.__door_no


    def get_street(self):
        return self.__street


    def get_pincode(self):
        return self.__pincode


    def set_door_no(self, value):
        self.__door_no = value


    def set_street(self, value):
        self.__street = value


    def set_pincode(self, value):
        self.__pincode = value


    def update_address(self):
        pass


add1=Address(123, "5th Lane", 56001)
cus1=Customer("Jack", 24, 1234, add1)

cus1.view_details()"""
"""class Customer:
    def __init__(self, name, age, phone_no):
        self.name = name
        self.age = age
        self.phone_no = phone_no

    def purchase(self, payment):
        if payment.type == "card":
            print ("Paying by card")
        elif payment.type == "e-wallet":
            print ("Paying by wallet")
        else:
            print ("Paying by cash")

class Payment:
    def __init__(self, type):
        self.type = type

payment1=Payment("card")
c=Customer("Jack",23,1234)

c.purchase(payment1)"""
"""class Foo:
    def __init__(self,num1,num2):
        self.__num1=num1
        self.num2=num2

    def __str__(self):
        return str(self.__dict__)
f1=Foo(10,20)
f2=Foo(20,30)
f3=Foo(30,40)
print(f1,f2,f3)"""
"""class Parrot:
    __counter=7000
    def __init__(self,name,color):
        Parrot.__counter+=1
        self.__name=name
        self.__color=color
        self.__unique_number=Parrot.__counter

    def get_name(self):
        return self.__name

    def get_color(self):
        return self.__color
    
    def get_unique_number(self):
        return self.__unique_number"""
"""class Customer:
    def __init__(self,phone_no,name,age):
        self.phone_no=phone_no
        self.name=name
        self.age=age
        self.list_of_calls=None

class CallDetail:
    def __init__(self,phone_no,called_no,duration):
        self.phone_no=phone_no
        self.called_no=called_no
        self.duration=duration

class Util:
    def __init__(self):
        self.list_of_customer_calldetail_objects=None
    def parse_customer(self,list_of_customers,list_of_calls):
        self.list_of_customer_calldetail_objects=[]
        for customer in list_of_customers:
            customer.list_of_calls=[]
            for call in list_of_calls:
                if customer.phone_no == call.phone_no:
                    customer.list_of_calls.append(call)
            self.list_of_customer_calldetail_objects.append(customer)



cust1=Customer(9900009901,'cust1',23)
cust2=Customer(9900009902,'cust2',24)
cust3=Customer(9900009903,'cust3',25)
list_of_customers=[cust1,cust2,cust3]

call1=CallDetail(9900009901,8800123401,5)
call2=CallDetail(9900009903,8800123402,10)
call3=CallDetail(9900009902,8800123403,2)
call4=CallDetail(9900009901,8800123404,8)
call5=CallDetail(9900009901,8800123405,7)
call6=CallDetail(9900009903,8800123406,9)
call7=CallDetail(9900009903,8800123407,4)
list_of_calls=[call1,call2,call3,call4,call5,call6,call7]
#Util().parse_customer(list_of_customers, list_of_calls)
u1=Util()
u1.parse_customer(list_of_customers,list_of_calls)
c1=u1.list_of_customer_calldetail_objects[0]
#print(c1.list_of_calls)
for c in c1.list_of_calls:
    print(c.phone_no,c.called_no,c.duration)
c2=u1.list_of_customer_calldetail_objects[1]
for c in c2.list_of_calls:
    print(c.phone_no,c.called_no,c.duration)
c3=u1.list_of_customer_calldetail_objects[2]
for c in c3.list_of_calls:
    print(c.phone_no,c.called_no,c.duration)
#c4=u1.list_of_customer_calldetail_objects[3]"""
"""[Customer(phone_no:9900009901 , name:cust1 , age:23), Customer(phone_no:9900009902 , name:cust2 , age:24), Customer(phone_no:9900009966 , name:cust3 , age:25)],[CallDetail(phone_no:9900009901 , called_no:8800123401 , duration:5), CallDetail(phone_no:9900009903 , called_no:8800123402 , duration:10), CallDetail(phone_no:9900009902 , called_no:8800123403 , duration:2), CallDetail(phone_no:9900009901 , called_no:8800123404 , duration:8), CallDetail(phone_no:9900009901 , called_no:8800123405 , duration:7), CallDetail(phone_no:9900009909 , called_no:8800123406 , duration:9), CallDetail(phone_no:9900009903 , called_no:8800123407 , duration:4)]"""
"""def remove_duplicates(value):
    #start writing your code here
    # l=list(value)
    # s=set(l)
    # d=list(s)
    # ret=''.join(d)
    # visited=[]
    # retres=''
    # for i in range(len(value)):
    #     for j in range(len(ret)):
    #         #print(value[i],ret[j])
    #         if value[i]==ret[j] and j not in visited and value[i] not in retres:
    #             retres+=value[j]
    #             visited.append(j)
    retres=''
    s=list(set(list(value)))
    print("s:",s)
    ind=[]
    #count=[0]*len(s)
    for i in range(len(s)):
        # for j in range(len(value)):
        ind.append(value.index(s[i]))
            
            # if value[i]==value[j]:
            #     count[i]+=1
    # print(count)
    # for k in range(len())
    # print("ind:",ind)
    ind.sort()
    # print("ind:",ind)
    for j in range(len(ind)):
        retres+=value[ind[j]]
    return retres

print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))"""
"""def check_perfect_number(number):
    #start writing your code here
    if number==0:
        return False
    divisors=[]
    for i in range(1,number):
        # divisors=[]
        if number%i==0:
            divisors.append(i)
    if sum(divisors)==number:
        return True
    elif divisors == []:
        return False
    else:
        return False


def check_perfectno_from_list(no_list):
    #start writing your code here
    ret=[]
    for i in range(len(no_list)):
        if check_perfect_number(no_list[i]):
            ret.append(no_list[i])
    return ret

perfectno_list=check_perfectno_from_list([18,6,4,2,1,28,0])
print(perfectno_list)
#code solved all test cases"""
"""#Sample ticket list - ticket format: "flight_no:source:destination:ticket_no"
#Note: flight_no has the following format - "airline_name followed by three digit number

#Global variable
ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056", "BA896:MUM:LON:067", "SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148","AI567:CHE:SIN:015","AI077:MUM:SIN:050","AI077:MUM:LON:051","SI267:MUM:SIN:146"]

def find_passengers_flight(airline_name="AI"):
    #This function finds and returns the number of passengers travelling in the specified airline.
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        if(string_list[0].startswith(airline_name)):
            count+=1
    return count

def find_passengers_destination(destination):
    #Write the logic to find and return the number of passengers traveling to the specified destination
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        if(string_list[2].startswith(destination)):
            count+=1
    return count
    #Remove pass and write your logic here

def find_passengers_per_flight():
    '''Write the logic to find and return a list having number of passengers traveling per flight based on the details in the ticket_list
    In the list, details should be provided in the format:
    [flight_no:no_of_passengers, flight_no:no_of_passengers, etc.].'''
    ret=[]
    for i in ticket_list:
        string_list=i.split(":")
        #ret.append(string_list[0])
        count=0
        for j in ticket_list:
            if j.startswith(string_list[0]):
                count+=1
        if string_list[0]+":"+str(count) not in ret:
            ret.append(string_list[0]+":"+str(count))
    return ret
    
    #Remove pass and write your logic here

def sort_passenger_list():
    #Write the logic to sort the list returned from find_passengers_per_flight() function in the descending order of number of passengers
    l=find_passengers_per_flight()
    ret=[]
    # for i in l:
    #     s_list=i.split(":")
    #     f[int(s_list[1])]=s_list[0]
    # n=f.keys()
    # n.sort(reverse=True)
    # for i in range:
    n=[]
    for i in l:
        s_list=i.split(":")
        n.append(int(s_list[1]))
    n.sort(reverse=True)
    #print(n)
    for i in n:
        #print("i:",i)
        #s_list=i.split(":")
        for j in l:
            #print("j:",j)
            if j.endswith(str(i)) and j not in ret:
                #print("yes")
                ret.append(j)
    return ret
    #Remove pass and write your logic here

#Provide different values for airline_name and destination and test your program.
print(find_passengers_flight("BA"))
print(find_passengers_destination("LON"))
print(find_passengers_per_flight())
print(sort_passenger_list())"""
"""def nearest_palindrome(number):
    #start writitng your code here
    while(True):
        number+=1
        numstr=str(number)
        reversenum=numstr[::-1]
        if str(number) == reversenum:
            break
    return number

number=12300
print(nearest_palindrome(number))"""
"""def check_prime(number):
    if number<=1:
        return False
    for i in range(2,number):
        if number%i==0:
            return False
    return True #remove pass and write your logic here. if the number is prime return true, else return false

def rotations(num):
    ret = []
    for i in range(len(str(num))):
        ret.append(int(str(num)[i:len(str(num))]+str(num)[0:i]))
    return ret#remove pass and write your logic here. It should return the list of different combinations of digits of the given number.
	#Rotation should be done in clockwise direction. For example, if the given number is 197, the list returned should be [197, 971, 719]

def get_circular_prime_count(limit):
    #circular_primes=[]
    count=0
    for i in range(limit):
        if check_prime(i):
            l=rotations(i)
            addit=True
            for j in l:
                if check_prime(j):
                    continue
                else:
                    addit=False
                    break
            if addit:
                #circular_primes.append(i)
                count+=1
    return count #remove pass and write your logic here.It should return the count of circular prime numbers below the given limit.

#Provide different values for limit and test your program
print(get_circular_prime_count(100))
print(check_prime(7))
print(rotations(197))"""
"""#import re
def validate_name(name):
    #Start writing your code here
    if name!="" and len(name)<=15 and name.isalpha():
        return True
    else:
        return False


def validate_phone_no(phno):
    #Start writing your code here
    if phno.isdigit() and len(phno) == 10:
        s=list(set(list(phno)))
        if len(s)>1:
            return True
    return False

def validate_email_id(email_id):
    #Start writing your code here
    if email_id.count("@") == 1 and email_id.count(".") == 1:
        s=email_id.split("@")
        s1=s[1].split(".")
        if s[0].isalpha and s1[0] in ['gmail','yahoo','hotmail'] and s1[1] == 'com':
            return True
    return False

def validate_all(name,phone_no,email_id):
    #Start writing your code here
    # Use the below given print statements to display appropriate messages
    # Also, do not modify them for verification to work
    #print("Invalid Name")
    #print("Invalid phone number")
    #print("Invalid email id")
    #print("All the details are valid")
    if validate_name(name) and validate_email_id(email_id) and validate_phone_no(phone_no):
        print("All the details are valid")

    elif validate_name(name) == False:
        print("Invalid Name")
    elif validate_phone_no(phone_no) == False:
        print("Invalid phone number")
    elif validate_email_id(email_id) == False:
        print("Invalid email id")



#Provide different values for name, phone_no and email_id and test your program
validate_all("Tina", "9994599998", "tina@yahoo.com")
print(validate_name("evaro"))  
print(validate_phone_no("@2345"))"""
"""def validate_credit_card_number(card_number):
    #start writing your code here
    if len(str(card_number)) == 16:
        sec=[]
        fir=[]
        for i in range(14,-1,-2):
            d=int(str(card_number)[i])*2
            if d > 9:
                s=0
                for i in range(len(str(d))):
                    s+=int(str(d)[i])
                sec.append(s)
                continue
            sec.append(d)
        for i in range(15,-1,-2):
            fir.append(int(str(card_number)[i]))
        print(sec)
        print(fir)
        if (sum(sec)+sum(fir))%10 == 0:
            return True
    return False

card_number= 5239512608615007#1456734512345698 #4539869650133101  #1456734512345698 # #5239512608615007
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")"""
"""def add_string(str1):
  #start writing your code here
  if len(str1)<3:
    return str1
  elif str1.endswith("ing"):
    str1+="ly"
    return str1
  else:
    str1+="ing"
    return str1


str1="com"
print(add_string(str1))"""
"""def bracket_pattern(input_str):
    #Remove pass and write your code here
	if input_str.startswith(")") or input_str.endswith("(") or input_str.count("(")!=input_str.count(")"):
		return False
	return True

    
input_str="(())("
print(bracket_pattern(input_str))"""
"""def create_new_dictionary(prices):
    #start writing your code here
    new_dict={}
    for k,v in prices.items():
        if v>200:
            new_dict[k]=v

    
    return new_dict

prices = { 'ACME': 45.23,'AAPL': 612.78,'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}
print(create_new_dictionary(prices))"""
"""def find_nine(nums):
    #Remove pass and write your code here
	if len(nums)<4:
		if 9 in nums:
			return True
	elif len(nums)>=4:
		if 9 in nums[0:4]:
			return True
	return False
    

nums=[1,9,4]
print(find_nine(nums))"""
"""def count_digits_letters(sentence):
    #start writing your code here
    count=[0,0]
    for i in range(len(sentence)):
        if sentence[i].isdigit():
            count[1]+=1
        elif sentence[i].isalpha():
            count[0]+=1
    
    return count

sentence="Infosys Mysore 570027"
print(count_digits_letters(sentence))"""
"""def list123(nums):
    #start writing your code here
    # if [1,2,3] in nums:
    #     return True
    sublistsoflen3=[]
    if len(nums)>=3:
        for i in range(len(nums)):
            for j in range(len(nums)+1):
                if abs(i-j) == 3 and nums[i:j] != []:
                    sublistsoflen3.append(nums[i:j])
        if [1,2,3] in sublistsoflen3:
            return True
        #print(sublistsoflen3)
    return False

    

nums=[1,2,3,4,5]
print(list123(nums))"""
"""def seed_no(number,ref_no):
    #start writing your code here
    res=number
    for i in range(len(str(number))):
        res*=int(str(number)[i])
    print(res)
    if res == ref_no:
        return True
    return False
number=123
ref_no=738
print(seed_no(number,ref_no))"""
"""def calculate_net_amount(trans_list):
    #start writing your code here
    net_amount=0 
    for i in trans_list:
        print(i)
        sl=i.split(":")
        if sl[0] == 'D':
            net_amount+=int(sl[1])
        elif sl[0] == 'W':
            net_amount-=int(sl[1])
        print(net_amount)
    
    return net_amount

trans_list=["D:300","D:200","W:200","D:100"]
print(calculate_net_amount(trans_list))"""
"""def generate_dict(number):
	#start writing your code here
	new_dict={}
	for i in range(1,number+1):
		new_dict[i]=i*i
	return new_dict

number=20
print(generate_dict(number))"""
"""def string_both_ends(input_string):
	#start writing your code here
    if len(input_string)<2:
        return -1
    else:
        return input_string[0:2]+input_string[len(input_string)-2:len(input_string)]

input_string="w3w"
print(string_both_ends(input_string))"""
"""def find_upper_and_lower(sentence):
    #start writing your code here
    result_list=[0,0]
    # s=sentence.split(" ")
    # sen=""
    # for i in s:
    #     sen+=i
    # # print(sen)
    # # print(sentence,s)
    for i,v in enumerate(sentence):
        # if sentence[i]
        #print(i,v)
        if v.isalpha():
            if v.lower() == v:
                result_list[1]+=1
            elif v.upper() == v:
                result_list[0]+=1
    return result_list

sentence="Come Here"
print(find_upper_and_lower(sentence))"""
"""def generate_sentences(subjects,verbs,objects):
	#start writing your code here
	sentence_list=[]
	for i in subjects:
		for j in verbs:
			for k in objects:
				sentence_list.append(i+" "+j+" "+k)

	
	return sentence_list

subjects=["I","You"]
verbs=["love", "play"]
objects=["Hockey","Football"]
print(generate_sentences(subjects,verbs,objects))"""
"""def check_22(num_list):
    #start writing your code here
    for i in range(len(num_list)):
        for j in range(len(num_list)):
            if i == j-1 and num_list[i] ==2 and num_list[j] == 2:
                return True
    return False
        
print(check_22([3,2,5,1,2,1,2,2]))"""
"""def divisible_by_sum(number):
    #start writing your code here
    d=0
    for i in str(number):
        d+=int(i)
    if number%d==0:
        return True
    return False

    
number=42
print(divisible_by_sum(number))"""
"""def find_gcd(num1,num2):
    #start writing your code here
    divisors=[]
    if num1<=num2:
        num=num1
    else:
        num=num2
    for i in range(1,num+1):
        if num1%i == 0 and num2%i == 0:
            divisors.append(i)
    return max(divisors)
    

num1=45
num2=9
print(find_gcd(num1,num2))"""
"""def list_of_count(word_list):
    #start writing your code here
    count_list=[]
    for i in range(len(word_list)):
        count_list.append(0)
        count_list[i]=len(word_list[i])
    return count_list

word_list=["COme","here"]
print(list_of_count(word_list))"""
"""def check_occurence(string):
    #start writing your code here
    s=string.split(" ")
    count=[0,0]
    for i in s:
        if i.lower() == 'mat':
            count[0]+=1
        elif i.lower() == 'jet':
            count[1]+=1
    if count[0]==count[1]:
        return True
    return False
        
string="Jet on the Mat but mat is too long"
print(check_occurence(string))"""
"""def check_for_ten(num1,num2):
    #start writing your code here
    if num1 == 10 or num2 == 10:
        return True
    elif num1+num2 == 10:
        return True
    return False
    
print(check_for_ten(10,9))"""
"""def exchange_list(number_list):
    #start writing your code here
    ret=number_list[len(number_list):len(number_list)//2-1:-1]
    # for i in range(len(number_list)//2):
    #     print(i,number_list[i])
    #     ret.append(number_list.pop(i))
    #     print(number_list)
    # for j in ret:
    #     number_list.append(j)
    ret1=number_list[0:len(number_list)//2]
    number_list=ret+ret1
    

    
    return number_list
     
number_list=[1,2,3,4,5,6]
print(exchange_list(number_list))"""
"""def sum_of_elements(num_list,number):
    inds=[]
    result_sum=0
    for i,v in enumerate(num_list):
        if v==number and i not in inds:
            inds.append(i)
            if 0<=i-1<len(num_list) and i-1 not in inds:
                inds.append(i-1)
            if 0<=i+1<len(num_list) and i+1 not in inds:
                inds.append(i+1) 
    for i,v in enumerate(num_list):
        if i not in inds:
            result_sum+=v
    return result_sum
      
num_list=[1,7,3,4,1,7,10,5]
number=7
print(sum_of_elements(num_list, number))"""
"""def check_well_formatted(input_item,list_label):
    #Start writing your code here
    if type(input_item) == list:
        print("1",input_item)
        if len(input_item) >= 2:
            print("2")
            if input_item[0] in list_label:
                print("3")
                if all((type(item) is str) or check_well_formatted(item,list_label) for item in input_item[1:len(input_item)]):
                    print("4")
                    print("all(type(item) is str for item in input_item[1:len(input_item)]):",all(type(item) is str for item in input_item[1:len(input_item)]))
                    print("all(check_well_formatted(item,list_label) for item in input_item[1:len(input_item)])",all(check_well_formatted(item,list_label) for item in input_item[1:len(input_item)]))
                    return True
                else:
                    print("here")
                    print("all(type(item) is str for item in input_item[1:len(input_item)]):",all(type(item) is str for item in input_item[1:len(input_item)]))
                    print("all(check_well_formatted(item,list_label) for item in input_item[1:len(input_item)])",all(check_well_formatted(item,list_label) for item in input_item[1:len(input_item)]))
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

input_list1=[1, [2, 'oui', [1, 'no']], 'no']
list_label1=[1, 2]
result=check_well_formatted(input_list1,list_label1)
if result is True:
    print("Well formatted")
else:
    print("Not Well formatted")"""
"""def convert_to_roman(num):
    d={}
    d[1000]='M'
    d[900]='CM'
    d[800]='DCCC'
    d[700]='DCC'
    d[600]='DC'
    d[500]='D'
    d[400]='CD'
    d[300]='CCC'
    d[200]='CC'
    d[100]='C'
    d[90]='XC'
    d[80]='LXXX'
    d[70]='LXX'
    d[60]='LX'
    d[50]='L'
    d[40]='XL'
    d[30]='XXX'
    d[20]='XX'
    d[10]='X'
    d[9]='IX'
    d[8]='VIII'
    d[7]='VII'
    d[6]='VI'
    d[5]='V'
    d[4]='IV'
    d[3]='III'
    d[2]='II'
    d[1]='I'
    val=""
    vals=[]
    for i in range(1,len(str(num))+1):
        #print(num%(10**i),i,(10**i))
        vals.append(num%(10**i))
        num-=num%(10**i)
        #print(num)
    for i in vals[::-1]:
        if i in d.keys():
            val+=d[i]
        elif i%1000 == 0:
            inc = i//1000
            for j in range(inc):
                val+=d[1000]
        # else:
        #     diff=0
        #     for k in d.keys():
        #         for k1 in d.keys():
        #             if k>i>k1:
        #                 print(i,k,k1)
        #                 val+=d[k1]
        #                 diff=i-k1
        #                 break
        #         if diff:
        #             convert_to_roman(i-k1) 
        #             break
        #     # for k in d.keys():
        #     #     if i%k == 0:
        #     #         quo=i//k
        #     #         for inc in range(quo):
        #     #             val+=d[k]
        #     #         break
            

    #print(vals)
    return val


for num in range(1,5000):    
    print(num," : ",convert_to_roman(num))
#print("roman numeral for respective number is:",convert_to_roman(4998))"""
"""train_list=[
{"train_no":16453,"name":"Prasanti Express","from":"SBC","to":"BBS","days_of_run":['Mo','We','Th'],"sleeper_fare":600,"ac_fare": 987},
{"train_no":25627,"name":"Karnataka Express","from":"SBC","to":"DEC","days_of_run":['Su','Tu'],"sleeper_fare":1600,"ac_fare": 2500},
{"train_no":22642,"name":"Trivandrum SF Express","from":"VSKP","to":"TVM","days_of_run":['Mo','Tu','We','Th','Fr','Sa'],"sleeper_fare":800,"ac_fare": 1256},
{"train_no":22905,"name":"Okha Howrah Express","from":"ST","to":"KOAA","days_of_run":['We','Sa'],"sleeper_fare":987,"ac_fare": 2879}]

def get_train_name (train_no):
    #start writing your code here
    for train in train_list:
        if train["train_no"]==train_no:
            return train
    else:
        return "Invalid Train_no"

def get_trains_for_day(day_of_run):
    #start writing your code here
    if day_of_run not in ['Su','Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']:
        return "Invalid day"
    ret=[]
    for train in train_list:
        if day_of_run in train["days_of_run"]:
            ret.append(train["train_no"])
    return ret


def get_total_fare(train_no,passenger_dict):
    #start writing your code here
    td=get_train_name(train_no)
    total_fare=td["sleeper_fare"]*passenger_dict["sleeper"]+td["ac_fare"]*passenger_dict["ac"]
    return total_fare
    
print(get_train_name(25627))
print(get_trains_for_day("Mo"))
print(get_total_fare(22642,{"sleeper":5, "ac":1}))"""
"""def ducci_sequence(test_list,n):
    #start writing your code here
    final_list=[test_list]
    for i in range(n+1):
        final_list.append([0,0,0,0])
        for j in range(len(final_list[i])):
            if j+1==len(final_list[i+1]):
                final_list[i+1][j]=abs(final_list[i][j]-final_list[i][-(len(final_list[i+1]))])
            else:
                final_list[i+1][j]=abs(final_list[i][j]-final_list[i][j+1])
    # for i in range(n+1):
    #     final_list.append(final_list[i])
    #     for j in range(len(final_list[i])):
    #         if j+1==len(final_list[i]):
    #             final_list[i][j]=abs(final_list[i][j]-final_list[i][-(len(test_list))])
    #         else:   
    #             final_list[i][j]=abs(final_list[i][j]-final_list[i][j+1])
    print(final_list)   
    
    return final_list[n+1]

ducci_element=ducci_sequence([0, 653, 1854, 4063] , 1)
print(ducci_element)"""
"""def list_rotate(uniquecode_list):
    rotated_list=[]
    #Write your code here
    def validate_uniq(uniquecode_list):
        if len(uniquecode_list)!=0:
            for i in uniquecode_list:
                sl=i.split("-")
                countalpha=0
                countzero=0
                for j in sl[0]:
                    if j.isalpha():
                        countalpha+=1
                for k in sl[1]:
                    if k == '0':
                        countzero+=1
                if countalpha<1 or countzero>0:
                    return False
                else:
                    return True
        return False
    if validate_uniq(uniquecode_list):                
        for i in uniquecode_list:
            s=i.split("-")
            rot=""
            countalpha1=0
            for j in s[0]:
                if j.isalpha():
                    rot+=j
                    countalpha1+=1
            rot+=s[1][countalpha1:len(s[1])]+s[1][0:countalpha1]
            rotated_list.append(rot)
    else:
        for i in uniquecode_list:
            s=i.split("-")
            rot=""
            countalpha1=0
            for j in s[0]:
                if j.isalpha():
                    rot+=j
                    countalpha1+=1
            rot+=s[1][countalpha1:len(s[1])]+s[1][0:countalpha1]
            rotated_list.append(rot)
                
                

    return rotated_list

#You may modify the below code for testing
uniquecode_list=['G221-1011','S621-9699']
rotated_list = list_rotate(uniquecode_list)
print(rotated_list)"""
"""#from typing import Any

#Tried
class Customer:
    def __init__(self,customer_id,customer_name,address):
        self.__customer_id=customer_id
        self.__customer_name=customer_name
        self.__address=address

    def validate_customer_id(self):
        if len(str(self.__customer_id)) == 6:
            if str(self.__customer_id)[0] == '1':
                for i in range(len(str(self.__customer_id))):
                    if str(self.__customer_id)[i].isdigit():
                        continue
                    else:
                        return False
                return True
        return False

    def get_customer_id(self):
        return self.__customer_id
    
    def get_customer_name(self):
        return self.__customer_name
    
    def get_address(self):
        return self.__address
    
class Freight:
    count=198
    def __init__(self,recipient_customer,from_customer,weight,distance):
        self.__freight_id=Freight.count+2
        self.__recipient_customer=recipient_customer
        self.__from_customer=from_customer
        self.__weight=weight
        self.__distance=distance
        self.__freight_charge=None

    def validate_weight(self):
        if self.__weight % 5 == 0:
            return True
        return False
    
    def validate_distance(self):
        if 500<=self.__distance<=5000:
            return True
        return False
    
    def forward_cargo(self):
        if self.__from_customer.validate_customer_id() and self.__recipient_customer.validate_customer_id() and self.validate_weight() and self.validate_distance():
            Freight.count+=2
            self.__freight_id=Freight.count
            self.__freight_charge=(self.__weight*150)+(self.__distance*60)
        else:
            self.__freight_charge

    def get_freight_charge(self):
        return self.__freight_charge
    
    def get_freight_id(self):
        return self.__freight_id
    
    def get_recipient_customer(self):
        return self.__recipient_customer
    
    def get_from_customer(self):
        return self.__from_customer
    
    def get_weight(self):
        return self.__weight
    
    def get_distance(self):
        return self.__distance
    
fc=Customer(100000,'A','X')
rc=Customer(100001,'B','Y')
fr=Freight(rc,fc,875,5000)
fr.forward_cargo()
fr.forward_cargo()
fr.forward_cargo()
fr.forward_cargo()
fr.forward_cargo()
print(fr.get_freight_charge(),fr.get_freight_id())"""
"""#Actual
class Customer:
    def __init__(self,customer_id,customer_name,address):
        self.__customer_id=customer_id
        self.__customer_name=customer_name
        self.__address=address
        
    def validate_customer_id(self):
        id=str(self.__customer_id)
        if len(id)==6:
            if id[0]=="1":
                return True
        return False
        
    def get_customer_id(self):
        return self.__customer_id
        
    def get_customer_name(self):
        return self.__customer_name
        
    def get_address(self):
        return self.__address
        
    
class Freight:
    counter=198
    def __init__(self,recipient_customer,from_customer,weight,distance):
        self.__recipient_customer=recipient_customer
        self.__from_customer=from_customer
        self.__weight=weight
        self.__distance=distance
        self.__freight_id=Freight.counter + 2
        self.__freight_charge=None
        
    def validate_weight(self):
        if self.__weight%5==0:
            return True
        return False
        
    def validate_distance(self):
        if 500<=self.__distance<=5000:
            return True
        return False
        
    def forward_cargo(self):
        if Customer.validate_customer_id(self.__from_customer) and Customer.validate_customer_id(self.__recipient_customer) and self.validate_distance() and self.validate_weight():
            
            Freight.counter += 2
            
            self.__freight_charge=self.__weight*150 + self.__distance*60
            
        else:
            self.__freight_charge=0 
    
    def get_freight_charge(self):
        return self.__freight_charge
        
    def get_freight_id(self):
        return self.__freight_id
        
    def get_recipient_customer(self):
        return self.__recipient_customer
        
    def get_from_customer(self):
        return self.__from_customer
        
    def get_weight(self):
        return self.__distance
        
    def get_distance(self):
        return self.__distance"""
"""class Bill:
    counter=1000
    def __init__(self) -> None:
        self.__bill_id=None
        self.__bill_amount=None

    def generate_bill_amount(self,item_quantity,items):
        self.__bill_amount=0
        Bill.counter+=1
        self.__bill_id="B"+str(Bill.counter)
        for k,v in item_quantity.items():
            for i in items:
                if k.lower() == i.get_item_id().lower():
                    self.__bill_amount+=v*i.get_price_per_quantity()


    def get_bill_id(self):
        return self.__bill_id
    
    def get_bill_amount(self):
        return self.__bill_amount


class Customer:
    def __init__(self,customer_name) -> None:
        self.__customer_name=customer_name
        self.__payment_status=None

    def pays_bill(self,bill):
        self.__payment_status='Paid'
        print("customer name:",self.get_customer_name,", bill id:",bill.get_bill_id(),", bill amount:",bill.get_bill_amount())

    
    def get_customer_name(self):
        return self.__customer_name
    
    def get_payment_status(self):
        return self.__payment_status

class Item:
    def __init__(self,item_id,description,price_per_quantity) -> None:
        self.__item_id=item_id
        self.__description=description
        self.__price_per_quantity=price_per_quantity

    def get_item_id(self):
        return self.__item_id
    
    def get_description(self):
        return self.__description
    
    def get_price_per_quantity(self):
        return self.__price_per_quantity"""
"""class Ticket:
    counter=0
    def __init__(self,passenger_name,source,destination) -> None:
        self.__ticket_id=None
        self.__passenger_name=passenger_name
        self.__source=source
        self.__destination=destination

    def validate_source_destination(self):
        if self.__source.lower() == 'Delhi'.lower() and self.__destination.lower() in ['mumbai', 'chennai', 'pune', 'kolkata']:
            return True
        return False
    
    def generate_ticket(self):
        if self.validate_source_destination():
            Ticket.counter+=1
            self.__ticket_id=""+self.__source[0].upper()+self.__destination[0].upper()
            if 1<=Ticket.counter<=9:
                self.__ticket_id+='0'
                self.__ticket_id+=str(Ticket.counter)
            else:
                self.__ticket_id+=str(Ticket.counter)
        else:
            self.__ticket_id=None
    
    def get_ticket_id(self):
        return self.__ticket_id
    
    def get_passenger_name(self):
        return self.__passenger_name
    
    def get_source(self):
        return self.__source
    
    def get_destination(self):
        return self.__destination"""
"""#Tried
class Applicant:
    __application_dict={'A':0,'B':0,'C':0}
    __applicant_id_count=1000

    def __init__(self,applicant_name) -> None:
        Applicant.__applicant_id_count=1000
        Applicant.__applicant_id_count+=1
        self.__applicant_id=None
        self.__applicant_name=applicant_name
        self.__job_band=None

    def generate_applicant_id(self):
        self.__applicant_id=Applicant.__applicant_id_count
        Applicant.__applicant_id_count+=1
        

    def apply_for_job(self,job_band):
        try:
            if Applicant.__application_dict[job_band] == 5:
                return -1
            else:
                Applicant.__application_dict[job_band]+=1
                self.generate_applicant_id()
                self.__job_band=job_band   
        except:
            print("some error occured")
            
    
    @staticmethod
    def get_application_dict():
        return Applicant.__application_dict
    
    def get_applicant_id(self):
        return self.__applicant_id
    
    def get_applicant_name(self):
        return self.__applicant_name
    
    def get_job_band(self):
        return self.__job_band
    
a=Applicant("Jack")
Applicant._Applicant__applicant_dict={'C':0,'A':0,'B':0}
a.apply_for_job('A')
a.apply_for_job('A')
a.apply_for_job('A')
a.apply_for_job('A')
a.apply_for_job('A')
print(Applicant.get_application_dict(),a.get_applicant_id(),Applicant._Applicant__applicant_id_count)"""
"""#Actual
class Applicant:
    __application_dict = {"A": 0, "B": 0, "C": 0}  # Private static dictionary to track application counts
    __applicant_id_count = 1000  # Private static variable to keep track of the applicant ID
    
    def __init__(self, applicant_name):
        self.__applicant_name = applicant_name  # Private instance variable for the applicant's name
        self.__applicant_id = None  # Private instance variable for the applicant's ID
        self.__job_band = None  # Private instance variable for the job band the applicant applied for
    
    def generate_applicant_id(self):
        if Applicant.__applicant_id_count is None:
            Applicant.__applicant_id_count = 1000  # Re-initialize if somehow set to None
        # Increment the static applicant ID count and assign it to the instance variable
        Applicant.__applicant_id_count += 1
        self.__applicant_id = Applicant.__applicant_id_count
    
    def apply_for_job(self, job_band):
        # Check if the application limit for the specified job band has been reached
        if Applicant.__application_dict[job_band] is None:
            Applicant.__application_dict[job_band] = 0  # Initialize if somehow set to None
        
        if Applicant.__application_dict[job_band] == 5:
            return -1  # Return -1 if the limit has been reached
        else:
            # Increment the application count for the job band
            Applicant.__application_dict[job_band] += 1
            # Generate an applicant ID and set the job band
            self.generate_applicant_id()
            self.__job_band = job_band
            return self.__applicant_id  # Return the applicant ID
    
    @staticmethod
    def get_application_dict():
        # Static method to return the application dictionary
        return Applicant.__application_dict
    
    def get_applicant_id(self):
        # Getter method for the applicant ID
        return self.__applicant_id
    
    def get_applicant_name(self):
        # Getter method for the applicant's name
        return self.__applicant_name
    
    def get_job_band(self):
        # Getter method for the job band
        return self.__job_band

# Testing the updated implementation

# Create an applicant object
a = Applicant("Jack")

# The applicant applies for job band 'A' multiple times
a.apply_for_job("A")
a.apply_for_job("A")
a.apply_for_job("A")
a.apply_for_job("A")
print(a.apply_for_job("A"))  # This should return the applicant ID or -1 if the limit is reached

# Display the applicant's ID
print(a.get_applicant_id())

# Output the current state of application_dict
print(Applicant.get_application_dict())
"""
"""class Patient:
    def __init__(self,patient_id,patient_name,list_of_lab_test_ids) -> None:
        self.__patient_id=patient_id
        self.__patient_name=patient_name
        self.__list_of_lab_test_ids=list_of_lab_test_ids
        self.__lab_test_charge=None

    def calculate_lab_test_charge(self):
        self.__lab_test_charge=0
        for i in self.__list_of_lab_test_ids:
            if LabTestRepository.get_test_charge(i)==-1:
                self.__lab_test_charge+=0
            else:
                self.__lab_test_charge+=LabTestRepository.get_test_charge(i)

    def get_patient_id(self):
        return self.__patient_id
    
    def get_patient_name(self):
        return self.__patient_name
    
    def get_list_of_lab_test_ids(self):
        return self.__list_of_lab_test_ids
    
    def get_lab_test_charge(self):
        return self.__lab_test_charge
    
class LabTestRepository:
    __list_of_hospital_lab_test_ids=["L101","L102","L103","L104"]
    __list_of_lab_test_charge=[2020,1750.50,5700,1320.50]
    # def __init__(self) -> None:
    #     pass
    @staticmethod
    def get_test_charge(lab_test_id):
        if lab_test_id == None or lab_test_id not in LabTestRepository.__list_of_hospital_lab_test_ids:
            return -1
        else:
            return LabTestRepository.__list_of_lab_test_charge[LabTestRepository.__list_of_hospital_lab_test_ids.index(lab_test_id)]

lab_test_list1=["L101","L103","L104",'L105']
patient1=Patient(1010,"Sam",lab_test_list1)
patient1.calculate_lab_test_charge()
print("Patient id:",patient1.get_patient_id(),"\nPatient name:",patient1.get_patient_name(),"\nPatient's test ids:",patient1.get_list_of_lab_test_ids(), "\nTotal lab test charge:",patient1.get_lab_test_charge())    """
"""class Multiplex:
    #__counter=0
    __list_movie_name=["movie1","movie2"]
    __list_total_tickets=[100,60]
    __list_last_seat_number=[None,None]
    __list_ticket_price=[150,200]
    def __init__(self):
        self.__seat_numbers=None
        self.__total_price=None
    def calculate_ticket_price(self,movie_index,number_of_tickets):
        self.__total_price= Multiplex.__list_ticket_price[movie_index]*number_of_tickets
    def check_seat_availability(self,movie_index,number_of_tickets):
        if(Multiplex.__list_total_tickets[movie_index]<number_of_tickets):
            return False
        else:
            return True
    def get_total_price(self):
        return self.__total_price
    def get_seat_numbers(self):
        return self.__seat_numbers
    def book_ticket(self, movie_name, number_of_tickets):
        '''Write the logic to book the given number of tickets for the specified movie.'''
        if movie_name not in Multiplex.__list_movie_name:
            return 0
        elif self.check_seat_availability(Multiplex.__list_movie_name.index(movie_name), number_of_tickets) == False:
            return -1
        else:
            self.__seat_numbers=self.generate_seat_number(Multiplex.__list_movie_name.index(movie_name), number_of_tickets)
            self.calculate_ticket_price(Multiplex.__list_movie_name.index(movie_name), number_of_tickets)
    def  generate_seat_number(self,movie_index, number_of_tickets):
        '''Write the logic to generate and return the list of seat numbers'''
        generated_seats=[]
        if Multiplex.__list_movie_name[movie_index] == "movie1":
            if Multiplex.__list_last_seat_number[0]==None:
                for i in range(1,number_of_tickets+1):
                    Multiplex.__list_last_seat_number[0]="M1-"+str(i)
                    Multiplex.__list_total_tickets[0]-=1
                    generated_seats.append(Multiplex.__list_last_seat_number[0])
                return generated_seats
            else:
                s=Multiplex.__list_last_seat_number[0].split("-")
                for i in range(1,number_of_tickets+1):
                    Multiplex.__list_last_seat_number[0]="M1-"+str(int(s[1])+i)
                    Multiplex.__list_total_tickets[0]-=1
                    generated_seats.append(Multiplex.__list_last_seat_number[0])
                return generated_seats
        elif Multiplex.__list_movie_name[movie_index] == "movie2":
            if Multiplex.__list_last_seat_number[1]==None:
                for i in range(1,number_of_tickets+1):
                    Multiplex.__list_last_seat_number[1]="M2-"+str(i)
                    Multiplex.__list_total_tickets[1]-=1
                    generated_seats.append(Multiplex.__list_last_seat_number[1])
                return generated_seats
            else:
                s=Multiplex.__list_last_seat_number[1].split("-")
                for i in range(1,number_of_tickets+1):
                    Multiplex.__list_last_seat_number[1]="M2-"+str(int(s[1])+i)
                    Multiplex.__list_total_tickets[1]-=1
                    generated_seats.append(Multiplex.__list_last_seat_number[1])
                return generated_seats
        
booking1=Multiplex()
status=booking1.book_ticket("movie1",10)
if(status==0):
    print("invalid movie name")
elif(status==-1):
    print("Tickets not available for movie-1")
else:
    print("Booking successful")
    print("Seat Numbers :", booking1.get_seat_numbers())
    print("Total amount to be paid:", booking1.get_total_price())
print("-----------------------------------------------------------------------------")
booking2=Multiplex()
status=booking2.book_ticket("movie2",6)
if(status==0):
    print("invalid movie name")
elif(status==-1):
    print("Tickets not available for movie-2")
else:
    print("Booking successful")
    print("Seat Numbers :", booking2.get_seat_numbers())
    print("Total amount to be paid:", booking2.get_total_price())"""
"""class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

    def return_phone(self):
        print ("Returning a phone")

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    def __init__(self, os, ram):
        self.os = os
        self.ram = ram
        print ("Inside SmartPhone constructor")

    def buy(self):
        print ("Buying a SmartPhone")

s=SmartPhone("Android", 2)

print(s.os)
print(s.brand)"""
"""class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

    def return_phone(self):
        print ("Returning a phone")

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    pass

s=SmartPhone(20000, "Apple", 13)

s.buy()"""
"""class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

    def return_phone(self):
        print ("Returning a phone")

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    def buy(self):
        #super().buy()

        print ("Buying a smartphone")

s=SmartPhone(20000, "Apple", 13)

s.buy()"""
"""class Rider:
    def __init__(self,trained_status,experience) -> None:
        self.__trained_status=trained_status
        self.__experience=experience

    def rides_vehicle(self):
        print("Rides Vehicle")

class CycleRider(Rider):
    def rides_blindfolded(self):
        print("Rides Blindfolded")

class BikeRider(Rider):
    def __init__(self, trained_status, experience,race_license) -> None:
        super().__init__(trained_status, experience)
        self.__race_license=race_license

    def rides_in_dome(self):
        print("Rides In Dome")"""
"""#Multilevel Inheritance
class Product:
    def review(self):
        print ("Product customer review")

class Phone(Product):
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

    def return_phone(self):
        print ("Returning a phone")

class SmartPhone(Phone):
    pass

s=SmartPhone(20000, "Apple", 12)

s.buy()
s.review()"""
"""#Hierarchical Inheritance
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

    def return_phone(self):
        print ("Returning a phone")

class SmartPhone(Phone):
    pass

class FeaturePhone(Phone):
    pass

SmartPhone(1000,"Apple","13px").buy()"""
"""#Multiple Inheritance
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

    def return_phone(self):
        print ("Returning a phone")

class Product:
    def review(self):
        print ("Customer review")

class SmartPhone(Phone, Product):
    pass

s=SmartPhone(20000, "Apple", 12)

s.buy()
s.review()"""
"""#Multiple Inhritance another example
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

    def return_phone(self):
        print ("Returning a phone")

class Product:
    def buy(self):
        print ("Product buy method")

class SmartPhone(Product, Phone):
    pass

s=SmartPhone(20000, "Apple", 12)

s.buy()"""
"""class Apparel:
    counter=100
    def __init__(self,price,item_type) -> None:
        self.__item_id=None
        self.__price=price
        self.__item_type=item_type
        Apparel.counter+=1
        self.__item_id=""+self.__item_type[0]+str(Apparel.counter)
    
    def calculate_price(self):
        self.__price+=(self.__price/20)

    def get_item_id(self):
        return self.__item_id
    
    def get_price(self):
        return self.__price
    
    def get_item_type(self):
        return self.__item_type
    
    def set_price(self,price):
        self.__price=price

class Cotton(Apparel):
    def __init__(self, price, discount):
        super().__init__(price, item_type="Cotton")
        self.__discount=discount
        #self.__price=price
    def calculate_price(self):
        super().calculate_price()
        p=super().get_price()
        p-=(p*(self.__discount/100))
        p+=(p/20)
        super().set_price(p)

    def get_discount(self):
        return self.__discount

class Silk(Apparel):
    def __init__(self, price):
        super().__init__(price, item_type="Silk")
        self.__points=None

    def calculate_price(self):
        super().calculate_price()
        p=super().get_price()
        if p>10000:
            self.__points=10
        else:
            self.__points=3
        p+=(p/10)
        super().set_price(p)
        
    def get_points(self):
        return self.__points
    
c=Cotton(8000,2)
c.calculate_price()
print(c.get_discount(),c.get_item_type(),c.get_item_id(),c.get_price())
s=Silk(10001)
s.calculate_price()
print(s.get_points(),s.get_price(),s.get_item_id(),s.get_item_type())"""
"""class Purchase:
    __counter=101
    def __init__(self,customer,fruit_name,quantity):
        self.__customer=customer
        self.__fruit_name=fruit_name
        self.__quantity=quantity
        self.__purchase_id=None

    def get_purchase_id(self):
        return self.__purchase_id
    
    def get_customer(self):
        return self.__customer
    
    def get_quantity(self):
        return self.__quantity
    
    def calculate_price(self):
        price=FruitInfo.get_fruit_price(self.__fruit_name)
        if price!=-1:
            totalfruitprice=price*self.__quantity
            if price == max(FruitInfo.get_fruit_price_list()) and self.__quantity>1:
                totalfruitprice-=(totalfruitprice/50)
            elif price == min(FruitInfo.get_fruit_price_list()) and self.__quantity>=5:
                totalfruitprice-=(totalfruitprice/20)
            if self.__customer._Customer__cust_type == "wholesale":
                totalfruitprice-=(totalfruitprice/10)
            self.__purchase_id="P"+str(Purchase.__counter)
            Purchase.__counter+=1
            return totalfruitprice
        else:
            return -1

class Customer:
    def __init__(self, customer_name, cust_type):
        self.__customer_name=customer_name
        self.__cust_type=cust_type

    def get_customer_name(self):
        return self.__customer_name
    
    def get_customer_type(self):
        return self.__cust_type
    
class FruitInfo:
    __fruit_name_list=['Apple','Guava','Orange','Grape','Sweet Lime']
    __fruit_price_list=[200,80,70,110,60]

    @staticmethod
    def get_fruit_price(fruit_name):
        for i in range(len(FruitInfo.__fruit_name_list)):
            if FruitInfo.__fruit_name_list[i]==fruit_name:
                return FruitInfo.__fruit_price_list[i]
        return -1
    
    @staticmethod
    def get_fruit_name_list():
        return FruitInfo.__fruit_name_list
    
    @staticmethod
    def get_fruit_price_list():
        return FruitInfo.__fruit_price_list

c=Customer("Tom","wholesale")
FruitInfo._FruitInfo__fruit_price_list=[100, 800, 70, 110, 600]
FruitInfo._FruitInfo__fruit_name_list=['Apple', 'Guava', 'Orange', 'Grape', 'Sweet Lime']
FruitInfo._Purchase__counter=101
p=Purchase(c,"Apple",10)
p.calculate_price()
p.calculate_price()
p.calculate_price()
p.calculate_price()
print(p.calculate_price(),p.get_purchase_id())"""
"""#This class represents ThemePark
class ThemePark:
    #dict_of_games contains the game name as key, price/ride and points that can be earned by customer in a list as value
    dict_of_games={"Game1":[35.5,5], "Game2":[40.0,6],"Game3":[120.0,10], "Game4":[60.0,7],"Game5":[25.0,4]}
    @staticmethod
    def validate_game(game_input):
        if game_input in ThemePark.dict_of_games.keys():
            return True
        return False
        #Remove pass and write the logic here
        #If game_input is present in ThemePark, return true. Else, return false.
    @staticmethod
    def get_points(game_input):
        return ThemePark.dict_of_games[game_input][1]
        #Remove pass and write the logic here
        #Return the points that can be earned for the given game_input.
    @staticmethod
    def get_amount(game_input):
        return ThemePark.dict_of_games[game_input][0]
        #Remove pass and write the logic here
        #Return the price/ride for the given game_input

#This class represents ticket
class Ticket:
    __ticket_count=200
    def __init__(self):
        self.__ticket_id=None
        self.__ticket_amount=0
    def generate_ticket_id(self):
        Ticket.__ticket_count+=1
        self.__ticket_id=Ticket.__ticket_count
        #Remove pass and write the logic here
        #Auto-generate ticket_id starting from 201
    def calculate_amount(self, list_of_games):
        
        #Remove pass and write the logic here
        '''Validate the games in the list_of_games.
        If all games are valid, calculate total ticket amount and assign it to attribute, ticket_amount and return true. Else, return false'''
        if all(ThemePark.validate_game(game) for game in list_of_games):
            for game in list_of_games:
                self.__ticket_amount+=ThemePark.get_amount(game)
            return True
        return False
    def get_ticket_id(self):
        return self.__ticket_id
    def get_ticket_amount(self):
        return self.__ticket_amount

class Customer:
    def __init__(self, name, list_of_games):
        self.__name=name
        self.__points_earned=0
        self.__food_coupon="No"
        self.__ticket=Ticket()
        self.__list_of_games=list_of_games
    def play_game(self):
        if "Game3" in self.__list_of_games:
            self.__list_of_games.append("Game2")
        for game in self.__list_of_games:
            if ThemePark.validate_game(game):
                self.__points_earned+=ThemePark.get_points(game)

    def update_food_coupon(self):
        if "Game4" in self.__list_of_games and self.__points_earned>15:
            self.__food_coupon="Yes"
    def book_ticket(self):
        if self.__ticket.calculate_amount(self.__list_of_games):
            self.__ticket.generate_ticket_id()
            self.play_game()
            self.update_food_coupon()
            return True
        return False
    def get_name(self):
        return self.__name
    def get_list_of_games(self):
        return self.__list_of_games
    def get_ticket(self):
        return self.__ticket
    def get_points_earned(self):
        return self.__points_earned
    def get_food_coupon(self):
        return self.__food_coupon
    #Remove pass and implement class Customer here
    #Represent customers and display all details of the customer, if he is able to book the ticket and play the game. Else, display appropriate error message
"""
"""class Product:
    def return_policy(self):
        pass
class Mobile(Product):
    pass
class Shoe(Product):
    pass
"""
"""class Product:
    def return_policy(self):
        pass

class Mobile(Product):
    def return_policy(self):
        print("All mobiles must be returned within 10 days of purchase")

class Shoe(Product):
    def return_policy(self):
        print("All shoes must be returned within 7 days of purchase")
                                                    
m=Mobile()
m.return_policy()
s=Shoe()
s.return_policy()"""
"""from abc import ABCMeta, abstractmethod
class Product(metaclass=ABCMeta):
    @abstractmethod
    def return_policy(self):
        pass"""
"""from abc import ABCMeta, abstractmethod
class Product(metaclass=ABCMeta):
    @abstractmethod
    def return_policy(self):
        pass

Product()"""
"""from abc import ABCMeta, abstractmethod
class Product(metaclass=ABCMeta):
    @abstractmethod
    def return_policy(self):
        pass

class Furniture(Product):
    pass

Furniture()"""
"""from abc import ABCMeta, abstractmethod
class Product(metaclass=ABCMeta):
    @abstractmethod
    def return_policy(self):
        pass

class Furniture(Product):
    def return_policy(self):
        print("Furnitures cannot be returned")

class Sofa(Furniture):
    pass

Sofa()"""
"""from abc import ABCMeta, abstractmethod
class DirectToHomeService(metaclass=ABCMeta):
    __counter=101
    def __init__(self,consumer_name) -> None:
        self.__consumer_number=DirectToHomeService.__counter
        DirectToHomeService.__counter+=1
        self.__consumer_name=consumer_name

    def get_consumer_name(self):
        return self.__consumer_name
    
    def get_consumer_number(self):
        return self.__consumer_number
    
    @abstractmethod
    def calculate_monthly_rent(self):
        pass

class BasePackage(DirectToHomeService):
    def __init__(self, consumer_name, base_pack_name, subscription_period) -> None:
        super().__init__(consumer_name)
        self.__subscription_period=subscription_period
        self.__base_pack_name=base_pack_name

    def get_base_pack_name(self):
        return self.__base_pack_name
    
    def get_subscription_period(self):
        return self.__subscription_period
    
    def validate_base_pack_name(self):
        if self.__base_pack_name in ["Silver","Gold","Platinum"]:
            pass
        else:
            self.__base_pack_name="Silver"
            print("Base package name is incorrect, set to Silver")

    def calculate_monthly_rent(self):
        if self.__subscription_period in range(1,25):
            self.validate_base_pack_name()
            monthly_rent=0
            if self.__base_pack_name == "Silver":
                monthly_rent=350.00
            elif self.__base_pack_name == "Gold":
                monthly_rent=440.00
            else:
                monthly_rent=560.00
            discount_amount=0
            if self.__subscription_period>12:
                discount_amount=monthly_rent
            final_monthly_rent=((monthly_rent*self.__subscription_period)-discount_amount)/self.__subscription_period
            return final_monthly_rent
        return -1"""
"""class CreditCard:
    def __init__(self, card_no, balance):
        self.card_no = card_no
        self.balance = balance
class Customer:
    def __init__(self,cards):
        self.cards=cards
    def purchase_item(self, price, card_no):
        if price < 0:
            raise Exception("Invalid Price")
        if card_no not in self.cards:
            raise Exception("Wrong Card Number")
        if price>self.cards[card_no].balance:
            raise Exception("Insufficient Balance, Try choosing another card")
card1=CreditCard(101,800)
card2=CreditCard(102,2000)
cards={card1.card_no:card1,card2.card_no:card2}
c=Customer(cards)
while(True):
    card_no=int(input("Please enter a card number"))
    try:
        c.purchase_item(1200,card_no)
        break
    except Exception as e:
        if str(e) == "Invalid Price":
            print(str(e))
            break
        elif str(e) == "Insufficient Balance, Try choosing another card":
            print(str(e))
            continue 
            # break
        elif str(e) == "Wrong Card Number":
            print(str(e))
            continue
        print("Something went wrong. "+str(e))"""
"""class InvalidPrice(Exception):
    pass
class WrongCard(Exception):
    pass
class InsufficientBalance(Exception):
    pass
class CreditCard:
    def __init__(self, card_no, balance):
        self.card_no = card_no
        self.balance = balance
class Customer:
    def __init__(self,cards):
        self.cards=cards
    def purchase_item(self, price, card_no):
        if price < 0:
            raise InvalidPrice("Invalid Price")
        if card_no not in self.cards:
            raise WrongCard("Wrong Card Number")
        if price>self.cards[card_no].balance:
            raise InsufficientBalance("Insufficient Balance, Try choosing another card")
card1=CreditCard(101,800)
card2=CreditCard(102,2000)
cards={card1.card_no:card1,card2.card_no:card2}
c=Customer(cards)
while(True):
    card_no=int(input("Please enter a card number"))
    try:
        c.purchase_item(1200,card_no)
        break
    # except Exception as e:
    #     if str(e) == "Invalid Price":
    #         print(str(e))
    #         break
    #     elif str(e) == "Insufficient Balance, Try choosing another card":
    #         print(str(e))
    #         continue 
    #         # break
    #     elif str(e) == "Wrong Card Number":
    #         print(str(e))
    #         continue
    #     print("Something went wrong. "+str(e))
    except InvalidPrice as e:
        print(str(e))
        break
    except InsufficientBalance as e:
        print(str(e))
        continue
    except WrongCard as e:
        print(str(e))
        continue
    # except KeyboardInterrupt as k:
    #     print(str(k))
    #     break
    except Exception as e:
        print("Something went wrong. "+str(e))"""
"""class InvalidPrice(Exception):
    pass
class WrongCard(Exception):
    pass

try:
    raise InvalidPrice()
# except Exception as e:
#     print("Exception")
except InvalidPrice:
    print("InvalidPrice")
except WrongCard:
    print("WrongCard")
except Exception as e:
    print("Exception")"""
"""try:
    1/0
# except Exception:
#     print("Exception")
except ZeroDivisionError:
    print("Zero division")
except Exception:
    print("Exception")"""
"""
#Tried
class Company:
    #Stores hike% based on job level.
    dict_hike={"A":5, "B":6, "C":10 , "D":11}
    #Consider incentive provided in all classes to be in Rupees(Rs).
    __c_incentive=5000
    def __init__(self,name):
        self.name=name
    @staticmethod
    def get_c_incentive():
        return Company.__c_incentive
class Employee:
    def __init__(self, emp_id,e_incentive, job_level,salary, performance_list):
        self.emp_id=emp_id
        self.__e_incentive=e_incentive
        self.__salary=salary
        self.__job_level=job_level
        self.__performance_list=performance_list
    def get_e_incentive(self):
        return self.__e_incentive
    def get_performance_list(self):
        return self.__performance_list
    def get_salary(self):
        return self.__salary
    def get_job_level(self):
        return self.__job_level
    def identify_performance_hike(self):
        return None
    def identify_job_level_hike(self):
        return None
    def identify_incentive(self):
        return None
    def update_salary(self,hike, incentive):
        self.__salary= (self.__salary+ self.__salary*hike/100) + incentive
    def calculate_salary(self):
        jl_hike=self.identify_job_level_hike()
        ex_hike=self.identify_performance_hike()
        if(jl_hike!=None):
            hike=jl_hike
            if(ex_hike!=None):
                hike+=ex_hike
            incentive=self.identify_incentive()
            self.update_salary(hike, incentive)
            return True
        else:
            return False
#Implement the class here
class PermanentEmployee(Employee):
    def __init__(self,emp_id, e_incentive, job_level, salary, performance_list, p_incentive):
        # self.__p_incentive=p_incentive
        super().__init__(emp_id,e_incentive, job_level,salary, performance_list)
        self.__p_incentive=p_incentive
        # self.emp_id=emp_id
        # self.__e_incentive=e_incentive
        # self.__salary=salary
        # self.__job_level=job_level
        # self.__performance_list=performance_list
    # def get_e_incentive(self):
    #     return self.__e_incentive
    # def get_performance_list(self):
    #     return self.__performance_list
    # def get_salary(self):
    #     return self.__salary
    # def get_job_level(self):
    #     return self.__job_level
    def identify_performance_hike(self):
        performance_list=self.get_performance_list()
        if performance_list[4]==1 and performance_list[3]==1:
            return 5
        elif performance_list[4]==1 and performance_list[3]==2 and performance_list[2]==1:
            return 3
        return None
    def identify_job_level_hike(self):
        job_level=Employee.get_job_level(self)
        if job_level in Company.dict_hike.keys():
            return Company.dict_hike[job_level]
        return None
    def identify_incentive(self):
        c_incentive=Company.get_c_incentive()
        e_incentive=Employee.get_e_incentive(self)
        return c_incentive + e_incentive + self.__p_incentive
    # def update_salary(self,hike, incentive):
    #     self.__salary= (self.__salary+ self.__salary*hike/100) + incentive
    def calculate_salary(self):
        jl_hike=self.identify_job_level_hike()
        ex_hike=self.identify_performance_hike()
        if(jl_hike!=None):
            hike=jl_hike
            if(ex_hike!=None):
                hike+=ex_hike
            incentive=self.identify_incentive()
            Employee.update_salary(self,hike, incentive)
            return True
        else:
            return False
        #super().calculate_salary()
    
    def get_p_incentive(self):
        return self.__p_incentive

c=Company("AXR Limited")
p=PermanentEmployee(2134,1000,"A",130000,[1,2,1,1,1], 3000)  
print(p.calculate_salary(),p.get_salary())"""
"""#Actual code
class Company:
    #Stores hike% based on job level.
    dict_hike={"A":5, "B":6, "C":10 , "D":11}
    #Consider incentive provided in all classes to be in Rupees(Rs).
    __c_incentive=5000
    def __init__(self,name):
        self.name=name
    @staticmethod
    def get_c_incentive():
        return Company.__c_incentive
class Employee:
    def __init__(self, emp_id,e_incentive, job_level,salary, performance_list):
        self.emp_id=emp_id
        self.__e_incentive=e_incentive
        self.__salary=salary
        self.__job_level=job_level
        self.__performance_list=performance_list
    def get_e_incentive(self):
        return self.__e_incentive
    def get_performance_list(self):
        return self.__performance_list
    def get_salary(self):
        return self.__salary
    def get_job_level(self):
        return self.__job_level
    def identify_performance_hike(self):
        return None
    def identify_job_level_hike(self):
        return None
    def identify_incentive(self):
        return None
    def update_salary(self,hike, incentive):
        self.__salary= (self.__salary+ self.__salary*hike/100) + incentive
    def calculate_salary(self):
        jl_hike=self.identify_job_level_hike()
        ex_hike=self.identify_performance_hike()
        if(jl_hike!=None):
            hike=jl_hike
            if(ex_hike!=None):
                hike+=ex_hike
            incentive=self.identify_incentive()
            self.update_salary(hike, incentive)
            return True
        else:
            return False
#Implement the class here
class PermanentEmployee(Employee):
    def __init__(self, emp_id,e_incentive, job_level,salary, performance_list,p_incentive):
        super().__init__(emp_id,e_incentive, job_level,salary, performance_list)
        self.__p_incentive=p_incentive
        
    
    def get_p_incentive(self):
        return self.__p_incentive
        
    def identify_performance_hike(self):
        performance_list=self.get_performance_list()
        if performance_list[4]==1 and performance_list[3]==1:
            hike=5 
        elif performance_list[4]==1 and performance_list[3]==2 and performance_list[2]==1:
            hike=3 
        else:
            hike = None
        return hike
        
    def identify_job_level_hike(self):
        job_level = Employee.get_job_level(self)
        if job_level in Company.dict_hike.keys():
            job_hike=Company.dict_hike[job_level]
            return job_hike
        else:
            return None
            
    def identify_incentive(self):
        c_incentive=Company.get_c_incentive()
        e_incentive=Employee.get_e_incentive(self)
        incentive=e_incentive + self.__p_incentive + c_incentive
        return incentive
        
    def calculate_salary(self):
        jl_hike=self.identify_job_level_hike()
        ex_hike=self.identify_performance_hike()
        if(jl_hike!=None):
            hike=jl_hike
            if(ex_hike!=None):
                hike+=ex_hike
            incentive=self.identify_incentive()
            Employee.update_salary(self, hike, incentive)
            return True
        else:
            return False
            
p = PermanentEmployee(2134,1000,"A",130000,[1, 2, 1, 1, 1],3000)
#Implement the class here"""
"""class Customer:
    def __init__(self, customer_name, quantity):
        self.__customer_name=customer_name
        self.__quantity=quantity

    def validate_quantity(self):
        if 1<=self.__quantity<=5:
            return True
        return False

    def get_customer_name(self):
        return self.__customer_name
        
    def get_quantity(self):
        return self.__quantity

class Pizzaservice:
    counter=100
    def __init__(self, customer, pizza_type, additional_topping):
        self.__customer=customer
        self.__pizza_type=pizza_type
        self.__additional_topping=additional_topping
        self.__service_id=None
        self.pizza_cost=None

    def validate_pizza_type(self):
        if self.__pizza_type.lower() in ["small","medium"]:
            return True
        return False

    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and self.__customer.validate_quantity():
            if self.__pizza_type.lower() == "small":
                if self.__additional_topping:
                    self.pizza_cost=185 * self.__customer.get_quantity() 
                else:
                    self.pizza_cost=150 * self.__customer.get_quantity()
            elif self.__pizza_type.lower() == "medium":
                if self.__additional_topping:
                    self.pizza_cost=250 * self.__customer.get_quantity()
                else:
                    self.pizza_cost=200 * self.__customer.get_quantity()
            Pizzaservice.counter+=1
            self.__service_id=self.__pizza_type[0]+str(Pizzaservice.counter)
        else:
            self.pizza_cost=-1

    def get_service_id(self):
        return self.__service_id

    def get_pizza_type(self):
        return self.__pizza_type

    def get_customer(self):
        return self.__customer
    
    def get_additional_topping(self):
        return self.__additional_topping

class Doordelivery(Pizzaservice):
    def __init__(self, customer, pizza_type, additional_topping, distance_in_kms):
        super().__init__(customer, pizza_type, additional_topping)
        self.__delivery_charge=None
        self.__distance_in_kms=distance_in_kms

    def validate_distance_in_kms(self):
        if 1<=self.__distance_in_kms<=10:
            return True
        return False

    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms():
            super().calculate_pizza_cost()
            if self.pizza_cost!=-1:
                if self.__distance_in_kms<=5:
                    self.__delivery_charge=self.__distance_in_kms*5
                    self.pizza_cost+=self.__delivery_charge
                else:
                    self.__delivery_charge=25+(self.__distance_in_kms-5)*7
                    self.pizza_cost+=self.__delivery_charge
        else:
            self.pizza_cost=-1

    def get_delivery_charge(self):
        return self.__delivery_charge

    def get_distance_in_kms(self):
        return self.__distance_in_kms

c = Customer("Asha",3)
p = Pizzaservice(c, "Medium", False)
#d = Doordelivery()
p.calculate_pizza_cost()
print(p.pizza_cost)"""
"""

o=OccasionalCustomer("David",5)
r=RegularCustomer("b",5)
print(o.calculate_bill_amount())
print(r.calculate_bill_amount())"""
"""from abc import ABCMeta, abstractmethod
class Employee(metaclass=ABCMeta):
    #table={"A":4,"B":6,"C":10,"D":13,"E":16,"F":20}
    #table1={}
    def __init__(self, job_band, employee_name, basic_salary, qualification):
        self.__job_band=job_band
        self.__employee_name=employee_name
        self.__basic_salary=basic_salary
        self.__qualification=qualification

    def get_job_band(self):
        return self.__job_band
    
    def get_employee_name(self):
        return self.__employee_name

    def get_basic_salary(self):
        return self.__basic_salary

    def get_qualification(self):
        return self.__basic_salary

    @abstractmethod
    def validate_job_band(self):
        pass

    def validate_basic_salary(self):
        if self.__basic_salary>3000:
            return True
        else:
            return False

    def validate_qualification(self):
        if self.__qualification in ["Bachelors","Masters"]:
            return True
        else:
            return False

    @abstractmethod
    def calculate_gross_salary(self):
        pass

class Graduate(Employee):
    def __init__(self, job_band, employee_name, basic_salary, qualification, cgpa):
        super().__init__(job_band, employee_name, basic_salary, qualification)
        self.__cgpa=cgpa

    def get_cgpa(self):
        return self.__cgpa

    def validate_job_band(self):
        job_band=self.get_job_band()
        if job_band in ["A","B","C"]:
            return True
        else:
            return False

    def calculate_gross_salary(self):
        if self.validate_basic_salary() and self.validate_qualification() and self.validate_job_band():
            if 4<=self.__cgpa<=4.25:
                tpi_amount=1000
            elif 4.26<=self.__cgpa<=4.5:
                tpi_amount=1700
            elif 4.51<=self.__cgpa<=4.75:
                tpi_amount=3200
            elif 4.76<=self.__cgpa<=5:
                tpi_amount=5000
            basic_salary=self.get_basic_salary()
            job_band=self.get_job_band()
            if job_band=="A":
                incentive=4
            elif job_band=="B":
                incentive=6
            elif job_band=="C":
                incentive=10
            gross_salary=basic_salary+(basic_salary*0.12)+((basic_salary*incentive)/100)+tpi_amount
        else:
            gross_salary=-1
        return gross_salary

class Lateral(Employee):
    def __init__(self, job_band, employee_name, basic_salary, qualification, skill_set):
        super().__init__(job_band, employee_name, basic_salary, qualification)
        self.__skill_set=skill_set

    def get_skill_set(self):
        return self.__skill_set

    def validate_job_band(self):
        job_band=self.get_job_band()
        if job_band in ["D","E","F"]:
            return True
        else:
            return False

    def calculate_gross_salary(self):
        if self.validate_basic_salary() and self.validate_qualification() and self.validate_job_band():
            if self.__skill_set=="AGP":
                sme_bonus=6500
            elif self.__skill_set=="AGPT":
                sme_bonus=8200
            elif self.__skill_set=="AGDEV":
                sme_bonus=11500
            basic_salary=self.get_basic_salary()
            job_band=self.get_job_band()
            if job_band=="D":
                incentive=13
            elif job_band=="E":
                incentive=16
            elif job_band=="F":
                incentive=20
            gross_salary=basic_salary+(basic_salary*0.12)+((basic_salary*incentive)/100)+sme_bonus
        else:
            gross_salary=-1
        return gross_salary

g=Graduate("A","Amit",5000,"Bachelors",5)
l=Lateral("D","Barghav",5000,"Masters","AGPT")
print(g.calculate_gross_salary())
print(l.calculate_gross_salary())"""
"""from abc import ABCMeta, abstractmethod
class Logistics(metaclass=ABCMeta):
    __counter=7000  
    def __init__(self,start_reading,end_reading):
        self.__consumer_id=None
        self.__start_reading=start_reading
        self.__end_reading=end_reading
    def get_consumer_id(self):
        return self.__consumer_id
    def get_start_reading(self):
        return self.__start_reading
    def get_end_reading(self):
        return self.__end_reading
    def validate_meter_reading(self):
        if(self.__start_reading < self.__end_reading):
            return True
        else:
            return False
    def generate_consumer_id(self):
        if Logistics.__counter == None:
            Logistics.__counter=7000
        Logistics.__counter+=1
        self.__consumer_id=Logistics.__counter # implement the code to generate the consumer id
    @abstractmethod
    def calculate_bill_amount(self):
        pass
class PassengerLogistics(Logistics):
    __list_vehicle=["BMW","TOYOTA","FORD"]
    __list_minimum_charge=[3000,1500,1000] #these lists are storing vehicle type, minimum charge, rate per kilometer for first hundred and rate per kilometer for rest of distance
    __list_charge_for_hundred=[30,15,10]   #there is a one to one correspondence
    __list_charge_after_hundred=[25,12,7]
    def __init__(self,vehicle_type,start_reading,end_reading):
        super().__init__(start_reading,end_reading)
        self.__vehicle_type=vehicle_type
    def get_vehicle_type(self):
        return self.__vehicle_type
    def validate_vehicle_type(self):
        for index in range(0,len(PassengerLogistics.__list_vehicle)):
            if(PassengerLogistics.__list_vehicle[index]==self.__vehicle_type):
                print(PassengerLogistics.__list_vehicle[index],self.__vehicle_type)
                return index
        return -1
        # if self.__vehicle_type in PassengerLogistics.__list_vehicle:
        #     return PassengerLogistics.__list_vehicle.index(self.__vehicle_type)
        # else:
        #     return -1
    def calculate_bill_amount(self):
        if self.validate_vehicle_type()!=-1 and self.validate_meter_reading():
            # print("yes")
            self.generate_consumer_id()
            distance_travelled=self.get_end_reading()-self.get_start_reading()
            bill_amount=0
            if distance_travelled<=100:
                bill_amount=PassengerLogistics.__list_charge_for_hundred[PassengerLogistics.__list_vehicle.index(self.__vehicle_type)]*distance_travelled
            else:
                bill_amount=PassengerLogistics.__list_charge_for_hundred[PassengerLogistics.__list_vehicle.index(self.__vehicle_type)]*100+PassengerLogistics.__list_charge_after_hundred[PassengerLogistics.__list_vehicle.index(self.__vehicle_type)]*(distance_travelled-100)
            if bill_amount<PassengerLogistics.__list_minimum_charge[PassengerLogistics.__list_vehicle.index(self.__vehicle_type)]:
                bill_amount=PassengerLogistics.__list_minimum_charge[PassengerLogistics.__list_vehicle.index(self.__vehicle_type)]
            bill_amount+=bill_amount*0.05
        else:
            # if self.validate_vehicle_type()==False:
            #     print("no1")
            # else:
            #     print("yes1")
            # if self.validate_meter_reading()==False:
            #     print("no2")
            # else:
            #     print("yes2")
            # print("no")
            bill_amount=-1
        return bill_amount
             # implement the code to calculate the bill amount according to the requirement
class GoodsLogistics(Logistics):
    __carrier_dict={"TATA":20,"EICHER":30,"FORCE":35} # stores the carrier type and rate per kilometer for 1000kg
    def __init__(self,carrier_type,goods_weight,start_reading,end_reading):
        super().__init__(start_reading,end_reading)
        self.__carrier_type=carrier_type
        self.__goods_weight=goods_weight
    def get_carrier_type(self):
        return self.__carrier_type
    def get_goods_weight(self):
        return self.__goods_weight
    def validate_carrier_type(self):
        for carrier in GoodsLogistics.__carrier_dict.keys():
            if(carrier==self.__carrier_type):
                return True
        return False
    def calculate_bill_amount(self):
        if(self.validate_carrier_type()):
            if(self.validate_meter_reading()):
                # print("yes")
                self.generate_consumer_id()
                total_distance=self.get_end_reading()-self.get_start_reading()
                if(self.__goods_weight<=1000):
                    charge_per_kilometer=self.__carrier_dict[self.__carrier_type]
                elif(self.__goods_weight >1000 and self.__goods_weight<=2000):
                    charge_per_kilometer=self.__carrier_dict[self.__carrier_type]*2
                elif(self.__goods_weight >2000 and self.__goods_weight<=3000):
                    charge_per_kilometer=self.__carrier_dict[self.__carrier_type]*4
                else:
                    charge_per_kilometer=200
                bill_amount=total_distance*charge_per_kilometer
                bill_amount=bill_amount+(bill_amount*0.1)+2000
                return bill_amount
            else:
                # print("no1")
                return -1
        else:
            # print("no2")
            return -1
passenger_logistic=PassengerLogistics("BMW1",300,400)
bill_amount=passenger_logistic.calculate_bill_amount()
if(bill_amount==-1):
    print("Invalid vehicle type or meter reading ")
else:
    print("Consumer id    :",passenger_logistic.get_consumer_id())
    print("Start reading  :",passenger_logistic.get_start_reading())
    print("End reading    :",passenger_logistic.get_end_reading())
    print("Total Amount   :",bill_amount)
print("------------------------------------------------------------")
goods_logistic=GoodsLogistics("FORCE",3000,300,400)
bill_amount=goods_logistic.calculate_bill_amount()
if(bill_amount==-1):
    print("Invalid career type or meter reading ")
else:
    print("Consumer id    :",goods_logistic.get_consumer_id())
    print("Goods weight   :",goods_logistic.get_goods_weight())
    print("Start reading  :",goods_logistic.get_start_reading())
    print("End reading    :",goods_logistic.get_end_reading())
    print("Total Amount   :",bill_amount)"""
"""class Employee:
    __Emp_count=0
    def __init__(self, name):
        self.__name = name
        Employee.__Emp_count += 1
    
    def is_eligible_for_discount(self):
        if(Employee.__Emp_count > 5):
            return False
        else:
            return True
    
    def hi(self):
        print("hi")
        #return "hi"
    #hi()
    def get_discount(self):
        if(self.is_eligible_for_discount()): 
            return 10
        else:
            return 0
       
employee1 = Employee ("John")
print(employee1.get_discount())"""
"""class Purchase:
    list_of_items=['Apple', 'Biscuits', 'Chocolates', 'Jam', 'Butter', 'Milk', 'Soap', 'Hand Sanitizer']
    list_of_count_of_each_item_sold=[0, 0, 0, 0, 0, 0, 0, 0]

    def __init__(self):
        self.__items_purchased=[]
        self.__item_on_offer=None

    def get_items_purchased(self):
        return self.__items_purchased

    def get_item_on_offer(self):
        return self.__item_on_offer

    def sell_items(self, list_of_items_to_be_purchased):
        #itemsinlowercase=[]
        for item in list_of_items_to_be_purchased:
            for i in Purchase.list_of_items:
                if item.lower()==i.lower():
                    Purchase.list_of_count_of_each_item_sold[Purchase.list_of_items.index(i)]+=1
            # if item.lower()=="soap":
            #     self.provide_offer()
                    self.__items_purchased.append(item)
        for item in self.__items_purchased:
            if item.lower() == "soap":
                self.provide_offer()
        # if "soap" in self.__items_purchased:
        #     self.provide_offer()

    def provide_offer(self):
        # if "soap" in self.__items_purchased:
        #     Purchase.list_of_count_of_each_item_sold[4]+=1
        #     self.__item_on_offer="HAND SANITIZER"
        for item in self.__items_purchased:
            if item.lower() == "soap":
                for itm in Purchase.list_of_items:
                    if itm.lower() == "hand sanitizer":
                        Purchase.list_of_count_of_each_item_sold[Purchase.list_of_items.index(itm)]+=1
                self.__item_on_offer="HAND SANITIZER"

    @staticmethod
    def find_total_items_sold():
        s=0
        for i in Purchase.list_of_count_of_each_item_sold:
            s+=i
        return s

p=Purchase()
p.sell_items(["JAM", "CHOcolates", "Ghee", "Soap"])
print(Purchase.find_total_items_sold(),Purchase.list_of_count_of_each_item_sold,p.get_item_on_offer())"""
"""class Dog:
    counter=100
    dog_breed_dict={"Labrador Retriever":5, "German Shepherd":12, "Beagle":10}
    def __init__(self, breed_list, accessories_required):
        self.__dog_id_list=[]
        self.__breed_list=breed_list
        self.__accessories_required=accessories_required
        self.__price=0

    def get_dog_id_list(self):
        return self.__dog_id_list

    def get_breed_list(self):
        return self.__breed_list

    def get_accessories_required(self):
        return self.__accessories_required

    def get_price(self):
        return self.__price

    def get_dog_price(self, breed):
        if breed=="Labrador Retriever":
            return 800
        elif breed=="German Shepherd":
            return 1230
        elif breed=="Beagle":
            return 650

    def generate_dog_id(self, breed):
        Dog.counter+=1
        dog_id=breed[0]+str(Dog.counter)
        return dog_id

    def validate_breed(self):
        for breed in self.__breed_list:
            if breed in Dog.dog_breed_dict.keys():
                continue
            else:
                return False
        return True

    def validate_quantity(self):
        for breed in self.__breed_list:
            if Dog.dog_breed_dict[breed]>=1:
                continue
            else:
                return False
        return True

    def calculate_total_price(self):
        if self.validate_breed() and self.validate_quantity():
            for breed in self.__breed_list:
                Dog.dog_breed_dict[breed]-=1
                self.__dog_id_list.append(self.generate_dog_id(breed))
                self.__price+=self.get_dog_price(breed)
            if self.__accessories_required:
                self.__price+=350
            if self.__price>1500:
                self.__price-=(self.__price/20)
            return self.__price
        elif self.validate_breed() == False:
            return -1
        elif self.validate_quantity() == False:
            return -2

d=Dog(["Labrador Retriever", "German Shepherd", "Beagle"], True)
print(d.calculate_total_price())"""
"""class Tollbooth:
    def __init__(self):
        self.__no_of_vehicle=0
        self.__total_amount=0

    def get_no_of_vehicle(self):
        return self.__no_of_vehicle

    def get_total_amount(self):
        return self.__total_amount

    def calculate_amount(self, vehicle_type):
        if vehicle_type.lower() == "car":
            self.__total_amount+=70
        elif vehicle_type.lower() == "bus":
            self.__total_amount+=100
        elif vehicle_type.lower() == "truck":
            self.__total_amount+=150
        else:
            self.__total_amount+=70

    def count_vehicle(self):
        self.__no_of_vehicle+=1

    def collect_toll(self, owner_type, vehicle_type):
        if owner_type.lower() == "vip":
            self.count_vehicle()
        else:
            self.count_vehicle()
            self.calculate_amount(vehicle_type)

t=Tollbooth()
t.collect_toll("Vip","Truck")
t.collect_toll("p","caR")
print(t.get_no_of_vehicle(),t.get_total_amount())"""
"""import time
import datetime
class GarmentOrder:
    garment_dict={"shirt":[45,400,30],"trousers":[250,500,25],"saree":[500,750,10],"jersey": [750,200,5]}
    def __init__(self, cloth_type, no_of_piece):
        self.__cloth_type=cloth_type
        self.__no_of_piece=no_of_piece
        self.__delivery_date=None
        self.__order_date=time.strftime("%d/%m/%Y")
    
    def get_cloth_type(self):
        return self.__cloth_type
    
    def get_no_of_piece(self):
        return self.__no_of_piece

    def get_delivery_date(self):
        return self.__delivery_date

    def get_order_date(self):
        return self.__order_date

    def take_order(self):
        if self.__cloth_type in GarmentOrder.garment_dict.keys():
            if self.__no_of_piece <= GarmentOrder.garment_dict[self.__cloth_type][0]:
                calculated_amount=self.calculate_amount()
                self.update_stock()
                return calculated_amount
            else:
                print("insufficient no. of pieces")
                return -1
        print("invalid cloth type")
        return -1

    def calculate_amount(self):
        total_amount=self.__no_of_piece*GarmentOrder.garment_dict[self.__cloth_type][1]
        return total_amount

    def update_stock(self):
        #order_date = datetime.datetime.strptime(self.__order_date, "%d/%m/%y")
        #d = order_date + datetime.timedelta(days=GarmentOrder.garment_dict[self.__cloth_type][2])
        d = datetime.date.today()+datetime.timedelta(days=GarmentOrder.garment_dict[self.__cloth_type][2])#d.strftime("%d/%m/%Y")
        self.__delivery_date=d.strftime("%d/%m/%Y")
        GarmentOrder.garment_dict[self.__cloth_type][0]-=self.__no_of_piece
        #print(d, self.__delivery_date)

g=GarmentOrder("shirt",40)
print(g.take_order(), g.get_order_date())
print(g.get_delivery_date(), GarmentOrder.garment_dict)"""
"""class Laptop:
    def __init__(self, grcode, expiry):
        self.__grcode = grcode
        self.__expiry = expiry

    def get_grcode(self):
        return self.__grcode

    def get_expiry(self):
        return self.__expiry


class Scanner:
    #self.__emp_laptop_dict = {} 

    def __init__(self, emp_laptop_dict):
        self.__emp_laptop_dict = emp_laptop_dict
        #emp_laptop_dict=emp_laptop_dict

    def validate_expiry_date(self, laptop):
        return not laptop.get_expiry()

    def validate_emp_laptop(self, empid, laptop):
        if empid in self.__emp_laptop_dict:
            assigned_laptop = self.__emp_laptop_dict[empid]
            if assigned_laptop.get_grcode() == laptop.get_grcode():
                return self.validate_expiry_date(assigned_laptop)
        return False

    def scan(self, empid, laptop):
        return self.validate_emp_laptop(empid, laptop)


# Test the implementation

# Creating Laptop objects
laptop1 = Laptop("QR001", False)  # Not expired
laptop2 = Laptop("QR002", True)   # Expired
laptop3 = Laptop("QR003", False)  # Not expired
laptop4 = Laptop("QR004", False)  # Not expired

# Step 2: Initializing emp_laptop_dict with employee ID as the key and Laptop objects as values
emp_laptop_dict = {
    101: laptop1,  # Employee 101 is assigned laptop1 (QR001)
    102: laptop2,  # Employee 102 is assigned laptop2 (QR002)
    103: laptop3   # Employee 103 is assigned laptop3 (QR003)
}

# Step 3: Creating a Scanner object using the emp_laptop_dict
scanner = Scanner(emp_laptop_dict)

# Step 4: Testing the scan method by passing different empid and laptop combinations
print(scanner.scan(101, laptop1))  # Expected: True (Correct laptop, not expired)
print(scanner.scan(102, laptop2))  # Expected: False (Laptop is expired)
print(scanner.scan(103, laptop1))  # Expected: False (Employee 103 does not have laptop1)
print(scanner.scan(101, laptop3))  # Expected: False (Employee 101 does not have laptop3)
print(scanner.scan(103, laptop3))  # Expected: True (Correct laptop, not expired)
print(scanner.scan(104, laptop4))  # Expected: False (Employee 104 is not in the dictionary)"""
"""class Laptop:
    def __init__(self, grcode, expiry):
        self.__grcode=grcode
        self.__expiry=expiry

    def get_grcode(self):
        return self.__grcode

    def get_expiry(self):
        return self.__expiry
        
class Scanner:
    emp_laptop_dict={"101":Laptop("QR001",False)}
    def __init__(self, emp_laptop_dict):
        Scanner.emp_laptop_dict=emp_laptop_dict
        self.__emp_laptop_dict=emp_laptop_dict
    
    def get_emp_laptop_dict(self):
        return self.__emp_laptop_dict

    def validate_expiry_date(self, laptop):
        if laptop.get_expiry():
            return False
        return True

    def validate_emp_laptop(self, emp_id, laptop):
        if emp_id in Scanner.emp_laptop_dict.keys() and Scanner.emp_laptop_dict[emp_id] == laptop:
            return True
        return False

    def scan(self, empid, laptop):
        if self.validate_emp_laptop(empid, laptop):
            if self.validate_expiry_date(laptop):
                return True
            else:
                print("Expired")
                return False
        else:
            print("empid invalid")
            return False

l1=Laptop("QR001",True)
l2=Laptop("QR002",False)
l3=Laptop("QR003",True)
dictonary={1:l1,2:l2,3:l3}
s=Scanner({'7555':['OOP_101_7'], '8632':['OOP_101_8'], '1682':['OOP_101_9']})
print(s.scan('7555', Laptop(grcode="GR777" , expiry=False)))
#submitted code with a failed test case due to incorrect problem statement"""
"""
#Practice Problem 7
class Employee: 
    __employee_count = 1000 
    def __init__(self): 
        self.__employee_id = self.generate_employee_id() 
        #@staticmethod 
    def generate_employee_id(self): 
        Employee.__employee_count += 1 
        return "E"+str(Employee.__employee_count)

class Project: 
    def __init__(self, project_id, number_of_employees): 
        self.__project_id = project_id 
        self.__number_of_employees = number_of_employees
    
    def get_project_id(self):
        return self.__project_id

    def get_number_of_employees(self):
        return self.__number_of_employees

    def update_number_of_employees(self): 
        self.__number_of_employees += 1

class Department: 
    __dep_project_list = [] 
    __employee_dict = {} 
    @staticmethod 
    def add_project(project_list): 
        if len(Department.__dep_project_list) + len(project_list) <= 5: 
            Department.__dep_project_list.extend(project_list) 
        else: 
            return -1 
    @staticmethod 
    def add_employee(employee, project_id): 
        project = next((p for p in Department.__dep_project_list if p.get_project_id() == project_id), None) 
        if not project: 
            print("Project not available in the department") 
            return -1 
        if project.get_number_of_employees() >= 10: 
            print("Project already has 10 employees") 
            return -2 
        employee_id = employee.generate_employee_id() 
        Department.__employee_dict[employee_id] = project_id 
        project.update_number_of_employees()

p1=Project(1,1)
p2=Project(2,2)
p3=Project(3,3)
p_list=[p1,p2,p3]
Department.add_project(p_list)
e1=Employee()
e2=Employee()
Department.add_employee(e1,1)
Department.add_employee(e2,3)
print(p1.get_number_of_employees(),p2.get_number_of_employees(),p3.get_number_of_employees())
#solved test cases not passed"""
"""class CabRepository:
    cab_type_list=["Hatch Back", "Sedan", "SUV"]
    charge_per_km=[9, 12, 5]
    no_of_cars=[2, 5, 10]

class CabService:
    __counter=1000
    def __init__(self, cab_type, distance_in_kms):
        self.__cab_type=cab_type
        self.__distance_in_kms=distance_in_kms
        self.__service_id=None

    def get_cab_type(self):
        return self.__cab_type

    def get_distance_in_kms(self):
        return self.__distance_in_kms

    def get_service_id(self):
        return self.__service_id

    def get_cab_charge(self):
        pass

    def calculate_waiting_charge(self, waiting_time_mins):
        if waiting_time_mins <= 30:
            return 0
        else:
            return (waiting_time_mins-30)*5

    def get_cab_charge(self, index):
        return CabRepository.charge_per_km[index]

    def booking(self, waiting_time_mins):
        if self.check_availability()!=-1:
            ind=self.check_availability()
            cab_charge=self.get_cab_charge(ind)*self.__distance_in_kms
            waiting_charge=self.calculate_waiting_charge(waiting_time_mins)
            CabRepository.no_of_cars[ind]-=1
            CabService.__counter+=1
            self.__service_id=CabService.__counter
            return cab_charge+waiting_charge
        else:
            return -1

    def check_availability(self):
        if self.__cab_type in CabRepository.cab_type_list and CabRepository.no_of_cars[CabRepository.cab_type_list.index(self.__cab_type)]>0:
            return CabRepository.cab_type_list.index(self.__cab_type)
        else:
            return -1
        
# c=CabService("SUV", 10)
# print(c.booking(31))
#cab_type-Hatch Back,distance_in_kms-10,cab_type_list-['Sedan', 'SUV', 'Hatch Back'],_CabService__counter-1000,charge_per_km-[17, 15, 13],no_of_cars-[1, 2, 0]
CabRepository.cab_type_list=['Sedan', 'SUV', 'Hatch Back']
CabService._CabService__counter=1000
CabRepository.charge_per_km=[17, 15, 13]
CabRepository.no_of_cars=[1, 2, 0]
c=CabService("Hatch Black",7)
print(c.check_availability())"""
"""class SmartCard:
    def __init__(self, card_no):
        self.__card_no=card_no
        self.__account_balance=500

    def get_card_no(self):
        return self.__card_no
    
    def get_account_balance(self):
        return self.__account_balance
    
    def set_account_balance(self, account_balance):
        self.__account_balance=account_balance

class Employee:
    def __init__(self,employee_id, employee_name, smart_card):
        self.__employee_id=employee_id
        self.__employee_name=employee_name
        self.smart_card=smart_card

    def get_employee_id(self):
        return self.__employee_id
    
    def get_employee_name(self):
        return self.__employee_name
    
    def validate_employee_id(self):
        if 1001<=self.__employee_id<=700000:
            return True
        return False
    
    def validate_card_no(self):
        def checkallnum(l):
            for i in l:
                if i.isdigit():
                    continue
                else:
                    return False
            return True
        card_no=self.smart_card.get_card_no()
        if len(card_no) == 9:
            if card_no[:3]=="INF":
                if checkallnum(card_no[3:9]):
                    return True
        return False
    
class Transaction:
    def __init__(self):
        self.__transaction_id=None

    def get_transaction_id(self):
        return self.__transaction_id
    
    def top_up_card(self, employee, amount):
        if 500<=amount<=10000:
            if employee.validate_employee_id() and employee.validate_card_no():
                existing_balance=employee.smart_card.get_account_balance()
                amount+=existing_balance
                employee.smart_card.set_account_balance(amount)
                return "all fine"
            else:
                print("Invalid: ",employee.validate_employee_id(),employee.validate_card_no())
                return -1
        else:
            return -1
    
    def make_payment(self, employee, amount):
        existing_balance=employee.smart_card.get_account_balance()
        if amount<=existing_balance:
            if employee.validate_employee_id() and existing_balance!=None:
                if existing_balance-amount>=500:
                    a=existing_balance-amount
                    employee.smart_card.set_account_balance(a)
                    card_no=employee.smart_card.get_card_no()
                    emp_id=employee.get_employee_id()
                    self.__transaction_id="T"+str(emp_id)[0]+str(card_no[3:5])
                    return "all fine"
        return -1
    
s=SmartCard("INF012345")
print(s.get_account_balance())
e=Employee(1001,"Emp1",s)
t=Transaction()
print(t.top_up_card(e,500))
print(s.get_account_balance())
print(t.make_payment(e,500))
print(s.get_account_balance())"""
"""class Consultant:
    def __init__(self, name, registered_company_list, vacancy_list, registered_student_dict):
        self.__name=name
        self.__registered_company_list=registered_company_list
        self.__vacancy_list=vacancy_list
        self.__registered_student_dict=registered_student_dict

    def get_name(self):
        return self.__name
    
    def get_registered_company_list(self):
        return self.__registered_company_list
    
    def get_vacancy_list(self):
        return self.__vacancy_list
    
    def get_registered_student_dict(self):
        return self.__registered_student_dict
    
    def validate_vacancy(self, company_name):
        if company_name in self.__registered_company_list:
            if self.__vacancy_list[self.__registered_company_list.index(company_name)] > 0:
                return self.__registered_company_list.index(company_name)
        return -1
    
    def register_student_for_placement(self, index, student_id):
        self.__vacancy_list[index]-=1
        self.__registered_student_dict[self.__registered_company_list[index]].append(student_id)

class Student:
    def __init__(self, name, student_id, branch, aggregate_percentage, year_of_passing):
        self.__name=name
        self.__student_id=student_id
        self.__branch=branch
        self.__aggregate_percentage=aggregate_percentage
        self.__year_of_passing=year_of_passing

    def get_name(self):
        return self.__name
    
    def get_student_id(self):
        return self.__student_id
    
    def get_branch(self):
        return self.__branch
    
    def get_aggregate_percentage(self):
        return self.__aggregate_percentage
    
    def get_year_of_passing(self):
        return self.__year_of_passing
    
    def check_eligibility(self):
        if self.__aggregate_percentage>=65 and self.__year_of_passing==2015:
            return True
        return False
    
    def apply_for_job(self, company_name, consultant):
        if consultant.validate_vacancy(company_name) != -1:
            if self.check_eligibility():
                ind=consultant.validate_vacancy(company_name)
                consultant.register_student_for_placement(ind, self.__student_id)
                return "all fine"
            else:
                return -1
        else:
            return -1
        
s=Student("Athadu",101,"CSE",65,2015)
c=Consultant("Athanu",["Meta","Amazon","Apple","Netflix","Google"],[10,10,10,10,10],{"Meta":[102,103],"Amazon":[104],"Apple":[105],"Netflix":[106],"Google":[107]})
print(s.apply_for_job("Meta",c))"""
"""class Letter:
    counter=1
    def __init__(self, sender_area, receiver_area):
        self.__sender_area=sender_area
        self.__receiver_area=receiver_area
        self.letter_id=Letter.counter
        Letter.counter+=1

    def get_sender_area(self):
        return self.__sender_area
    
    def get_receiver_area(self):
        return self.__receiver_area
    
class PostMan:
    counter=100
    def __init__(self, name):
        PostMan.counter+=1
        self.postman_id="P"+str(PostMan.counter)
        self.__name=name
        self.__post_list_to_deliver=[]

    def get_name(self):
        return self.__name
    
    def get_post_list_to_deliver(self):
        return self.__post_list_to_deliver
    
    # def set_post_list_to_deliver(self, letter):
    #     self.__post_list_to_deliver.append(letter)
    
class PostOffice:
    def __init__(self, area_list, postmen_list):
        self.__area_list=area_list
        self.__postmen_list=postmen_list

    def get_area_list(self):
        return self.__area_list
    
    def get_postmen_list(self):
        return self.__postmen_list
    
    def validate_letter(self, letter):
        receiver_area=letter.get_receiver_area()
        if receiver_area in self.__area_list:
            return self.__area_list.index(receiver_area)
        return -1
    
    def allocate_posts(self, letter_list):
        invalid_letter_list=[]
        for letter in letter_list:
            if self.validate_letter(letter) != -1:
                ind = self.validate_letter(letter)
                #self.__postmen_list[ind].set_post_list_to_deliver(letter)
                self.__postmen_list[ind]._PostMan__post_list_to_deliver.append(letter)
            else:
                invalid_letter_list.append(letter)
        return invalid_letter_list
    
l1=Letter("HYD","KKD")
pman=PostMan("ThePostMan")
p_list=[pman]
a_list=["KKD"]
poffice=PostOffice(a_list,p_list)
l_list=[l1]
poffice.allocate_posts(l_list)
print(pman.get_post_list_to_deliver())"""
"""
#Practice Problem 13 (Test cased not passed)
class Security:
    employee_list=[]
    visitor_list=[]
    def __init__(self, employee_list):
        Security.employee_list=employee_list
        for emp in employee_list:
            Security.visitor_list.append(None)
    
    def security_check(self, employee, visitor):
        if employee in Security.employee_list:
            if visitor == Security.visitor_list[Security.employee_list.index(employee)]:
                if visitor.get_valid_id() in ["Passport", "Voter id", "PAN Card"]:
                    return True
        return False
    
class Employee:
    def __init__(self, employee_name, employee_id):
        self.__employee_name=employee_name
        self.__employee_id=employee_id

    def get_employee_name(self):
        return self.__employee_name
    
    def get_employee_id(self):
        return self.__employee_id
    
    def register_visitor(self, visitor):
        emp_ids=[]
        inds=[]
        for i,emp in enumerate(Security.employee_list):
            inds.append(i)
            emp_ids.append(emp.get_employee_id())
        if self.__employee_id in emp_ids:
            if Security.visitor_list[inds[emp_ids.index(self.__employee_id)]] == None:
                if visitor.get_relationship_with_emp() in ["Parent","Sibling","Spouse","Child"]:
                    Security.visitor_list[inds[emp_ids.index(self.__employee_id)]]=visitor
                    return True
        return False
    
class Visitor:
    def __init__(self, visitor_name, relationship_with_emp, valid_id):
        self.__visitor_name=visitor_name
        self.__relationship_with_emp=relationship_with_emp
        self.__valid_id=valid_id

    def get_visitor_name(self):
        return self.__visitor_name
    
    def get_relationship_with_emp(self):
        return self.__relationship_with_emp
    
    def get_valid_id(self):
        return self.__valid_id
    
e=Employee("emp1",101)
v=Visitor("vst1","Parent","Passport")
s=Security([e])
print(Security.employee_list, Security.visitor_list)
e.register_visitor(v)
print(Security.employee_list, Security.visitor_list)
print(v)"""
"""class OnlinePortal:
    item_list=[]
    quantity_list=[]
    price_list=[]
    @staticmethod
    def search_item(item):
        if item in OnlinePortal.item_list:
            return OnlinePortal.item_list.index(item)
        return -1
    
    @staticmethod
    def place_order(index, emi, quantity):
        OnlinePortal.quantity_list[index]-=quantity
        total_cost=OnlinePortal.price_list[index]*quantity
        if emi:
            total_cost+=(total_cost*0.02)
        else:
            total_cost-=(total_cost*0.02)
        return total_cost
    
    @staticmethod
    def add_stock(item_name, quantity):
        if OnlinePortal.search_item(item_name) != -1:
            if OnlinePortal.quantity_list[OnlinePortal.item_list.index(item_name)] <= 10:
                OnlinePortal.quantity_list[OnlinePortal.item_list.index(item_name)]+=quantity
            else:
                print("quantity is sufficent")
                return -1
        else:
            print("item does not exist")
            return -2
        
    @staticmethod    
    def add_item(item_name, price, quantity):
        if OnlinePortal.search_item(item_name) != -1:
            return -2
        else:
            OnlinePortal.item_list.append(item_name)
            OnlinePortal.price_list.append(price)
            OnlinePortal.quantity_list.append(quantity)

class Buyer:
    def __init__(self, name, email_id):
        self.__name=name
        self.__email_id=email_id

    def get_name(self):
        return self.__name
    
    def get_email_id(self):
        return self.__email_id
    
    def purchase(self, item_name, quantity, emi):
        if OnlinePortal.search_item(item_name) != -1:
            index=OnlinePortal.search_item(item_name)
            if OnlinePortal.quantity_list[index]>=quantity:
                cost=OnlinePortal.place_order(index,emi,quantity)
                return cost
            else:
                return -1
        else:
            return -2
        
# b=Buyer("buyer1","buyer1@yo.com")
# o=OnlinePortal()
# print(b.purchase("sugar",1,True))
OnlinePortal.price_list=[7000, 21000, 30000, 13000]
OnlinePortal.quantity_list=[30, 20, 11, 22]
OnlinePortal.item_list=['Acer', 'Motorola', 'Blackberry', 'Sony']      
print(OnlinePortal.add_stock("Nokia",10))"""          



    





        


        



    
        




    

        


    


            






    
        

        
    

        


















    





                                                    
                                                    
                                                    
                                                    





                                                    





    










    
















        
                                                    






                                                   
                                                










