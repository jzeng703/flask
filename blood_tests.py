def interface():
    print ("Blood Test Analysis")
    while True:
        print ("\nOptions")
        print ("1 - HDL")
        print ("2 - LDL")
        print ("9 - Quit")
        choice = input ("Enter an option: ")
        if choice == "9":
            return 
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()


def HDL_driver():
    HDL = get_HDL_input()
    analysis1 = analyze_HDL(HDL)
    output_HDL(HDL, analysis1)

def get_HDL_input():
    HDL = input("Enter HDL Level: ")
    return int(HDL)

def analyze_HDL(HDL):
    if HDL >= 60:
        return ("Normal")
    elif HDL < 40:
        return ("Low")
    else:
        return ("Borderline Low")

def output_HDL(HDL, analysis1):
    print("The HDL entered was {}".format(HDL))
    print("The level is {}".format(analysis1))


def LDL_driver():
    LDL = get_LDL_input()
    analysis2 = analyze_LDL(LDL)
    output_LDL(LDL, analysis2)

def get_LDL_input():
    LDL = input("Enter LDL Level: ")
    return int(LDL)

def analyze_LDL(LDL):
    if LDL < 130:
        return ("Normal")
    elif 130 <= LDL <= 159:
        return ("Borderline Hight")
    elif 160 <= LDL <= 189:
        return ("High")
    else:
        return ("Very High")

def output_LDL(LDL, analysis2):
    print("The LDL entered was {}".format(LDL))
    print("The level is {}".format(analysis2))

if __name__ == "__main__":
    interface()