import os
import sys
import new


def menu():
    # return None
    j = []
    with open("test.log","r") as f:
        s = f.read()        
        j.append(s)
        print(s.strip('\n'))



def sear(lys,ele):   
    # search #
    for i in range(len(lys)):
        if lys[i] == ele:
            # with open()
            s = 'Book Found'
            inp = input("Type 'yes' to view content: ")
            if inp == 'yes':
                
                with open(ele,"r")as f:
                    det = f.read()
                    print(det.strip('\n'))
            elif inp == 'no':
                print("thanks")
            else:
                print("Wrong Input")
            return s+' = '+ lys[i]
    return "Not Found"
# def delete():
    

def exit():
    return "Thanks"


if __name__ == "__main__":
    c = int(input("""
    Choose menu:
    1- Write book.
    2- View log of book's.
    3- Search the book.
    4- Delete book.
    5- Exit.\n"""))

    if c==1:
        
        print("write a book")

        c = input("Enter 'yes' to write: ")
        y = 'yes'
        n = 'no'

        if c == y:
            # print("test succ")
            auth = input("Name of author: ")
            bok = input("enter the name of your book: ")
            
            data = new.book(bok,auth)
            d = []
            d.append(bok)
            d.append(auth)

            with open("check.txt","a")as f:
                for i in d:
                    f.write(str(i)+'\n')
            # print("done = ",d)
            print(data)
        elif c == n:
            print("ok")
        else:
            print("Error") 

  
    elif c==2:
         
        menu()

    elif c == 3:
        ele = input("search book by Name = ")

        """search function using binary search Algo."""

        with open('check.txt','r') as f:

            s = f.readlines()
        lys = []
        for i in range(len(s)):
            lys.append(s[i].strip('\n'))
        print(sear(tuple(lys),ele)) 

    elif c == 4:
        dd = input("do want to delete: ")
        if dd == 'yes':
            sd = input("enter the name of book: ")
            new.dele(sd)
        elif dd == 'no':
            print("ok")
        else:
            print("!! wrong input !!")

    else:        
        print(exit())
        

    