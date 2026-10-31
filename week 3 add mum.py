# sum of first 100 numbers
number=1
sum=0
print(" calculating the sum of first 100 numbers")
while number <=100:
    sum=sum+number
    number+=1
    print(f"Current number: {number}")
    print(" Current sum", sum)

print(f"final sum: {sum}")
