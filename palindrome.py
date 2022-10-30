n=int(input())
temp=n;rev=0
while(temp):
    rev=rev*10+temp%10
    temp=temp//10
if(n==rev):
    print("palindrome")
else:
    print("not palindrome")