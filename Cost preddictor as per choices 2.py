n=int(input("Enter the rounds of trip:"))


for i in range(n):
    choice,km,hour=input("Enter choice, distance, and hour: ").split()
    choice=int(choice)
    km=float(km)
    hour=int(hour)
    if choice==1:
        base_rate=10
    elif choice==2:
        base_rate=20
    elif choice==3:
        base_rate=30
    else:
        print("Invalid choice")
        continue
    if 5<=hour<=9 or 17<=hour<=24:
        surge=1.5
    else:
        surge=1
    fare=base_rate*surge*km
    print(f"Trip{i+1}:",fare)