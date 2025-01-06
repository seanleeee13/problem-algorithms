a, b = input().split()
if a == "1" and b == "1":
    print("2")
elif (a == "1" and b == "2") or (a == "2" and b == "1"):
    print("3")
elif (a == "1" and b == "3") or (a == "2" and b == "2") or (a == "3" and b == "1"):
    print("4")
elif (a == "1" and b == "4") or (a == "2" and b == "3") or (a == "3" and b == "2") or (a == "4" and b == "1"):
    print("5")
elif (a == "1" and b == "5") or (a == "2" and b == "4") or (a == "3" and b == "3") or \
    (a == "4" and b == "2") or (a == "5" and b == "1"):
    print("6")
elif (a == "1" and b == "6") or (a == "2" and b == "5") or (a == "3" and b == "4") or \
    (a == "4" and b == "3") or (a == "5" and b == "2") or (a == "6" and b == "1"):
    print("7")
elif (a == "1" and b == "7") or (a == "2" and b == "6") or (a == "3" and b == "5") or (a == "4" and b == "4") or \
    (a == "5" and b == "3") or (a == "6" and b == "2") or (a == "7" and b == "1"):
    print("8")
elif (a == "1" and b == "8") or (a == "2" and b == "7") or (a == "3" and b == "6") or (a == "4" and b == "5") or \
    (a == "5" and b == "4") or (a == "6" and b == "3") or (a == "7" and b == "2") or (a == "8" and b == "1"):
    print("9")
elif (a == "1" and b == "9") or (a == "2" and b == "8") or (a == "3" and b == "7") or \
    (a == "4" and b == "6") or (a == "5" and b == "5") or (a == "6" and b == "4") or \
    (a == "7" and b == "3") or (a == "8" and b == "2") or (a == "9" and b == "1"):
    print("10")
elif (a == "2" and b == "9") or (a == "3" and b == "8") or (a == "4" and b == "7") or (a == "5" and b == "6") or \
    (a == "6" and b == "5") or (a == "7" and b == "4") or (a == "8" and b == "3") or (a == "9" and b == "2"):
    print("11")
elif (a == "3" and b == "9") or (a == "4" and b == "8") or (a == "5" and b == "7") or (a == "6" and b == "6") or \
    (a == "7" and b == "5") or (a == "8" and b == "4") or (a == "9" and b == "3"):
    print("12")
elif (a == "4" and b == "9") or (a == "5" and b == "8") or (a == "6" and b == "7") or \
    (a == "7" and b == "6") or (a == "8" and b == "5") or (a == "9" and b == "4"):
    print("13")
elif (a == "5" and b == "9") or (a == "6" and b == "8") or (a == "7" and b == "7") or \
    (a == "8" and b == "6") or (a == "9" and b == "5"):
    print("14")
elif (a == "6" and b == "9") or (a == "7" and b == "8") or (a == "8" and b == "7") or (a == "9" and b == "6"):
    print("15")
elif (a == "7" and b == "9") or (a == "8" and b == "8") or (a == "9" and b == "7"):
    print("16")
elif (a == "8" and b == "9") or (a == "9" and b == "8"):
    print("17")
elif a == "9" and b == "9":
    print("18")