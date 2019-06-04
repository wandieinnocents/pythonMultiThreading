
import _thread
import time

def CountDown(threadName):
    count = 10
    while(count >=0):
        print("{} , count : {}".format(threadName,count))
        count-=1
        time.sleep(2)

def main():
    print("MULTI-THREADING IN PYTHON")

    #start new thread
    try:
        _thread.start_new_thread(CountDown,("Thread 1",))
        _thread.start_new_thread(CountDown, ("Thread 2",))
        _thread.start_new_thread(CountDown, ("Thread 3",))
        print("Thread operation ongoing")
    except:
        print("There is an Error running thread")
    while 1:
        pass







if __name__ == '__main__':main()
