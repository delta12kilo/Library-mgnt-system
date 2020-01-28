import os
import sys
import new


def menu():
    a = int(input("enter the no. of entry: "))
    for i in range(a):
        det = []
        bid = int(input("enter the bookid: "))
        bname = input("enter the name: ")
        det.append(bname)        
        with open("check.txt","a") as f:
            for i in det:
                f.write(str(bid) +'\n')
                f.write(str(i)+'\n')
                f.write('--------------\n')                               
    return det,str(bid),"done"

def sear(lys,ele):   
    # Binary search #
    for i in range(len(lys)):
        if lys[i] == ele:
            s = 'Book Found'
            return s+' = '+ lys[i]
    return "Not Found"
# def delete():
    

def exit():
    return "Thanks"


if __name__ == "__main__":
    c = int(input("""
    Choose menu:
    1- Write book.
    2- Enter the book detail.
    3- Search the book.
    4- Exit.\n"""))

    if c==1:
        # menu()
        print("write a book")

        c = input("Enter 'yes' to write: ")
        y = 'yes'
        n = 'no'

        if c == y:
            print("test succ")
            bok = input("enter the name of your book: ")
            data = new.book(bok)
            print(data)
        elif c == n:
            print("ok")
        else:
            print("Error") 

  
    elif c==2:
        ele = input("search book by Name = ")

        """search function using binary search Algo."""

        with open('check.txt','r') as f:

            s = f.readlines()
        lys = []
        for i in range(len(s)):
            lys.append(s[i].strip('\n'))
        print(sear(tuple(lys),ele))       
    elif c == 3:
        enter  = input("delete the book =  ")
        # with open("check.txt",'a') as f:

    # elif c == 0:

             
    else:        
        print(exit())
        

    