import logging
import time

logging.basicConfig(filename='test.log',level=logging.DEBUG)
logger = logging.getLogger()

def book(bok):
    
    buffer = []
    while True:
        print("> ", end="")
        line = input()
        if line == ".":
            break
        buffer.append(line)
    mul = "\n".join(buffer)
    with open(bok,'a') as f:
        f.write(str(mul))
    localtime = time.asctime( time.localtime(time.time()) )
    logger.info("{file} = {time} ".format(file = bok,time = localtime))


    # There won't be any exception #
    # try:                
    #     f = open(bok, mode="rb")
        
    # except FileNotFoundError as err:
    #     logger.error(err)
    #     raise
    # else:
    #     f.close()
    # finally:
    #     # stop_time = time.time()
    #     # dt = stop_time-start_time
    #     localtime = time.asctime( time.localtime(time.time()) )
    #     logger.info("{file} = {time} ".format(file = bok,time = localtime))
 
    return "Your book has been saved"

# if __name__ == "__main__":
#     print("write a book")

#     c = input("Enter 'yes' to write: ")
#     y = 'yes'
#     n = 'no'

#     if c == y:
#         print("test succ")
#         bok = input("enter the name of your book: ")
#         data = book(bok)
#         print(data)
#     elif c == n:
#         print("ok")
#     else:
#         print("Error")