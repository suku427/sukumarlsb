x = int(input("Enter x="))
rev = 0
while x > 0:
    digit = x%10
    rev = rev * 10 + digit
    x=x//10
print("Reversed num is ",rev)
    