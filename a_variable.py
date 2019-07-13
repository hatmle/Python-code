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
    
    # string
    Data="software engineer"
    print(Data[0:5])
    
    # List
    Ages=[44,33,45,33,54]
    Ages.append(100)
    Ages.insert(0,33)
    print(Ages)
    
    # Tuples
    # Once a tuple is created, you cannot add items to it and remove items from it. Tuples are unchangeable.
    Ages_tuple=(44,33,45,33,54)
    print(Ages_tuple)
    # can delete the tuple completely
    del Ages_tuple    
    # Python has two built-in methods that you can use on tuples (index and count).
    
if __name__ == '__main__':
    main()
