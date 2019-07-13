def main():
    # simple if
    Age=input("enter your Age:")
    if(int(Age)>18):
        print("welcome")

    # if - else
    Age=input("enter your Age:")
    if(int(Age)>18):
        print("welcome")
    else:
        print("Not Welcome")
        
    # if - elif
    Age=input("enter your Age:")
    if(int(Age)>=8 and int(Age)<=10):
        print("children")
        print("children")
        print("children")
        print("children")
    elif(int(Age)>=11 and int(Age)<=15):
        print("kids")
    elif(int(Age)>=16 and int(Age)<=18):
        print("Tingers")
    elif(int(Age)>=19 and int(Age)<=30):
        print("Young")
    else:
        print("Out of range")
    print("End")
    
    # if - nested
    Degree=input("enter your Degree:")
    if(int(Degree)>=90 ):
        print("hi")
        x=5
        if(int(Degree)>94):
              print("Your Score is +A")
        else:
            print("Your Score is -A")
    elif(int(Degree)>=80 and int(Degree)<=89):
        print("Your Score is B")
    elif(int(Degree)>=70 and int(Degree)<=79):
        print("Your Score is C")
    elif(int(Degree)>=60 and int(Degree)<=69):
        print("Your Score is D")
    elif(int(Degree)>=50 and int(Degree)<=59):
        print("Your Score is E")
    else:
        print("You Fail")

if __name__ == '__main__':
    main()
