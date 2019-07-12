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
    
    # dictionary
    # Student={'Name':"hussein alrubaye",'Age':27,'Slary':232.5};
    Student=dict(Name="hussein alrubaye",Age=27,Slary=232.5);
    Student['Name']="Hussein Ahmed"
    Student["Dept"]="software engineer"

    print(Student,type(Student))

    del Student["Dept"]

    print(Student,type(Student))
    print(Student['Name'])
    print(Student['Age'])

    Student.clear()

    print(Student,type(Student))

if __name__ == '__main__':
    main()
