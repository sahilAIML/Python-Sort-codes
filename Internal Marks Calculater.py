def calc():
    a, b = map(int, input("Enter T1 marks (two values): ").split())
    c, d = map(int, input("Enter T2, T3 marks: ").split())
    e = int(input("Enter T4 marks: "))
    f, g, h, i = map(int, input("Enter T5 marks (four values): ").split())

    T1 = (a + b) / 3

    T5 = (f + g + h + i) / 4

    total = T1 + c + d + e + T5
    print(f"Total: {total:.2f}/60")

subjects = ["ML", "OOPs", "PTSML", "ADA"]

for subject in subjects:
    print(subject)
    calc()
    print()
