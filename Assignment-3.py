print("Question 1")

#Program to count the number of occurence of a particular word
word = input("Enter word : ")
my_char = input("Enter char : ")
i=0
count=0

while(i<len(word)):
    if(word[i]==my_char):
        count = count + 1
    i = i+1
    
print("Number of times", my_char,"has occured is:",count)

print("-" * 160)

print("Question 2")

#Program to print next date of input date

#Condition for leap year
year = int(input("Input a year: "))

if(year % 400==0):
    leap_year=True
elif(year % 100==0):
    leap_year=False
elif(year % 4==0):
    leap_year=True
else:
    leap_year=False
    
#Condition for months
month = int(input("Input a month [1-12]: "))
if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30

#Condition for day
day = int(input("Input a day [1-31]: "))
if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))

print("-" * 160)

print("Question 3")

# Program to create a list of tuple of a given list, in which 2nd element is square of 1st element
#Creating a list
list1=[3,6,9]

#USING LIST COMPREHENSION TO ITERATE EACH VALUE IN LIST AND CREATE A TUPLE
result=[(x,x**2) for x in list1]

#PRINT THE RESULT
print(result)


print("-" * 160)

print("Question 4")

#Program to print the Letter grade and Performance According to the Grade Points
Dict={4:"Poor",5:"Below Average",6:"Average",7:"Good",8:"Very Good",9:"Excellent",10:"Outstanding"}
n=int(input("Input your Grade:"))

if(n<4):
    print("ERROR")
else:
    print("Your Grade Is ",end="")
    print(n)
    print(" and ",end="")
    print(Dict.get(n),end=" Performance")

print()
print("-" * 160)    

print("QUESTION 5")

i=0
a="ABCDEFGHIJK"

#FOR HAVING ITERATIONS TO PRINT THE GIVEN PATTERN
for i in range(6):
    j=i
    while(j>0):
        print(" ",end="")
        j=j-1
    k=0
    for k in range(len(a)-2*i):
        print(a[k],end="")
        
    print("")


print("-" * 160)


print("Question 6")
#Program to perform operations on DICTIONARY used to store Student's details 

SID=int(input("Enter YOUR SID:"))
Name=input("Enter NAME:")
students={SID:Name}

while True:
    option=input("Do you want to Enter Another Student Entry(Y or N):").upper()
    if option=="Y":
        SID=int(input("Enter SID:"))
        Name=input("Enter NAME:")
        students[SID]=Name
    elif option=="N":
        break
    else:
        print("Invalid Input!!")


#PART a
#To Print The DICTIONARY

print("<a>\n",students)

#PART b
#To sort The Student's Details According To Their Names

print("<b>\n",{k:v for k,v in sorted(students.items(),key=lambda x:x[1])})

#PART c
#To sort According To Their SIDs

print("<c\n",{k:v for k,v in sorted(students.items())})

#PART d
#To Search for a Student By Their SID

SID=int(input("Search Name With SID for:\n"))
print("<d>\n",students[SID])


print()
print("-" * 160)

print("Question 7")

#Program To Print The FIBONACCI SERIES and Print the average of the resultant series

#To Print A FIBONACCI SERIES for nterms entered by the user
def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))

nterms=int(input("Enter A Number for The Number of terms of The FIBONACCI SEQUENCE:"))


#check if The Number of terms is valid
if nterms<=0:
    print("Please Enter a Positive integer")
else:
    print("FIBONACCI SEQUENCE:")
    sum=0
    for i in range(nterms):
        print(recur_fibo(i))
        sum=sum+recur_fibo(i)
avg=float(sum/nterms)
print("Average of the Resultant FIBONACCI SERIES is:",avg)
 

print()
print("-" * 160)



print("Question 8")

#Program To Perform Operations On Given Sets of Numbers
s1={1,2,3,4,5}
s2={2,4,6,8}
s3={1,5,9,13,17}


#PART a
#To take The union,intersection and Then To Perform The given Question
print("PART a")

Set_union=s1.union(s2)
Set_intersection=s1.intersection(s2)
a=Set_union-Set_intersection
print("<a>\n",a)


#PART b
#To Print elements that are only in one of the three sets 
print("PART b")

b=s1.union(s2.union(s3))-s1.intersection(s2)-s2.intersection(s3)-s3.intersection(s1)
print("<b>\n",b)

#PART c
#To subtract intersection of 3 from 2 taken at one at a time
print("PART c")

c=((s1.intersection(s2)).union((s1.intersection(s3)).union(s2.intersection(s3))))-s1.intersection(s2.intersection(s3))
print("<c>\n",c)

#PART d
#To ignore the numbers from 1 to 10 that are occuring in s1
print("PART d")

d=set()
for i in range(1,11):
    if i not in s1:
        d.add(i)
    print("<d>\n",d)

#PART e
print("PART e")
e=set()
if i in range(1,11):
  if i not in s1 and i not in s2 and i not in s3:
    e.add(i)
print("<e>\n",e)
