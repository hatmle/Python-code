def main():
    # open and write
    out=open("test.txt","a")
    out.write(" \nname:salama")
    out.write(" \nname:dema")
    out.close()
    
    # read
    readFile=open("test.txt","r")
    for line in readFile:
        print(line)
    readFile.close()


# read file with exception
def main_read_exception():
    try:
        readFile=open("test.txt","r")
        for line in readFile:
            print(line)
        readFile.close()
    except IOError:
        print("File not found")
    else:
        print("File is readed")
    
if __name__ == '__main__':
    main()
