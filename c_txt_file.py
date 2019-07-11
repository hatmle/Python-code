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

if __name__ == '__main__':main()
