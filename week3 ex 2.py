# for ( i=0; i<=0;  i++) {}  ---> c/c++
apples=int(input("How many apples should i removed?"))
count_apples=1

while count_apples<apples:
    count_apples+=1

    print("Removed apples", count_apples)
print(f"You have removed apples", count_apples)
