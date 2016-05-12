import time
import threading

def printf(i):
    for x in xrange(5):
        time.sleep(1)
        print i,

def test():
    thread_list = []
    for i in xrange(10):
        sthread = threading.Thread(target = printf, args = str(i))
#        sthread.setDaemon(True)
        sthread.start()
        thread_list.append(sthread)
#    for i in xrange(10):
#        thread_list[i].join()
import time, thread

def myfunction(string, sleeptime, lock, *args):
    while 1:
        lock.acquire()
        time.sleep(sleeptime)
        print "AA"
        lock.release()
        time.sleep(sleeptime)

if __name__ == "__main__":
    test()
    lock = thread.allocate_lock()
    thread.start_new_thread(myfunction, ("Thread #: 1", 2, lock))
    thread.start_new_thread(myfunction, ("Thread #: 2", 2, lock))

