num = int(input())
if num%2==0:
    print("четное")
    if (num*num)%2==0:
        print("произведение четное")
else:
    print("нечетное")