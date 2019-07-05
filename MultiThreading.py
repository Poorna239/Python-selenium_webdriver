import threading
import time


# function for printing
def sleep(name, delay):
    print("I am {}, going to sleep".format(name))
    # delay time
    time.sleep(delay)
    print("I am ready to play the game")


# initialise the thread
t = threading.Thread(target=sleep, name='Thread1', args=('kpt', 5))
# start executing the thread
t.start()

# lock the thread until it task finishes
t.join()

