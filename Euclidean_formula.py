print("Calculate Distance Between Two points")
while True:
    x1,y1 = map(int, input("Enter X1 Y1").split())
    x2,y2 = map(int, input("Enter X2 Y2").split())

    f = (((x2-x1)**2)+((y2-y1)**2))**0.5

    print(f"{f:.2f}\n")
