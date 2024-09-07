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





