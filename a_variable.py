# assign, print out variable
def main():
    Amount=30 #amount of time spend on working
    
    data="{} is high".format(Amount) # format my data
    #data="%s is high"% Amount
    print(data,type(data))
    
    datalen="is good"
    print(len(datalen))
    print(datalen[1])
    
    # other objects
    Name="hussein"
    print(Name,type(Name))
    
    Age=22
    print(Age,type(Age))
    
    Slary=12544.5
    print(Slary,type(Slary))

if __name__ == '__main__':
    main()
