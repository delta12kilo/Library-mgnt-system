import logging
import time
import os

logging.basicConfig(filename='test.log',level=logging.DEBUG)
logger = logging.getLogger()

def book(bok,auth):
    
    buffer = []
    while True:
        # a = input()
        print("> ", end="")
        line = input()
        if line == ".":
            break
        buffer.append(line)
    mul = "\n".join(buffer)
    with open(bok,'a') as f:
        f.write(str(mul))
    localtime = time.asctime( time.localtime(time.time()) )
    logger.info("{file} writen by {auth} = {time} ".format(file = bok,auth = auth, time = localtime))
    return "Your book has been saved"


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
 
def dele(sd):
    # d = os.remove(sd)
    # print('the file is deleted ')
    try:
        d = os.remove(sd)
        
        print("file delete")
    except OSError as error:
        print(error)
        print("File path can not be removed")   
