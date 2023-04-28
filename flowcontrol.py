#Write a function that uses while, if and continue statements to print all the even numbers between 0 and 50. 

def even_numbers():
    num=1
    while num < 50:
        num=+1
        if num%2!=0:
            continue
        print(num)
even_numbers()

#Write a function that takes an integer argument and prints "Prime" if the number is prime, and "Not prime" if the number is not prime.
def prime_number(num):
    if num==1:
        print("Not prime")
    else:
        for i in range(2,num):
            if num%i==0:
               print("Not prime")
            else:
                print("Prime") 
prime_number(67)
# #Write a function that takes a list of integers as input and prints the sum of all the even numbers in the list.
def sum_even_numbers(group):
    for g in group:
        if g%2==0:
            print(g)
sum_even_numbers([2,89,10,22,4])

#Write a function that takes any two integers as input, and
#prints the sum of all the numbers between the two integers (inclusive) that are divisible by 3.
def sum_multiples(num1,num2):
   sum=0
   for n in range(num1,num2):
       if n%3==0:
           sum=sum+n
           print(sum)
sum_multiples(3,15)