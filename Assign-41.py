# Q.1) Write THE Lambda function to find number is even
f1=lambda n: True if n%2==0 else False
print(f1(10))

# another way
iseven= lambda n: n%2==0
print(iseven(13))

# Q.2) Write the lambda function to calculate Nth term of fibonacci series.
# fibonacci series:-0,1,1,2,3,5,8,13,21.........
fibo=lambda n: n if n==0 or n==1 else fibo(n-1)+fibo(n-2)
print(fibo(12))

# Q.3)Write the lambda expression to calculate area of circle.
Area=lambda r: 3.14*r**2
print(Area(4))

#Q.4) Write the Lambda function to count the word in give text.
countword=lambda text: len(text.split(" "))
print(countword("name vedant pradip jangam name vaishnavi pradip jangam name pallavi pradip jangam"))