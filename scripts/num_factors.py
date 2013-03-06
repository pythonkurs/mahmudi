from multiprocessing import Process, Queue
from IPython.parallel import Client
from collections import Counter
from time import time
import os
import sys


def factorize(n):
    if n < 2:
        return []
    factors = []
    p = 2
    
    while True:
        if n == 1:
            return factors
        r = n % p
        if r == 0:
            factors.append(p)
            n = n / p
        elif p * p >= n:
            factors.append(n)
            return factors
        elif p > 2:
            p += 2
        else:
            p += 1


""" This function works in multiprocessing mode -p, distributing work to all available processes
    """
def worker(tasks, results):
    t = tasks.get()
    f=factorize(t)
    d = []
    d.append(t)
    d.append(f)
    results.put(d)


"""
    Expects two arguments i.e. mode of execution and highest number to be factorized.
    e.g. num_factors.py -s 50000
    for serial mode use -s
    for parallel mode use -p
    for ipython mode use -ip
    """
    

if __name__ == "__main__":
        
    if(len(sys.argv)!=3):
        print "ERROR: Wrong number of arguments."
        print "Expects two arguments i.e. mode of execution and highest number to be factorized."
        print "e.g. num_factors.py -s 50000"
        quit()
    start = time()
    option=sys.argv[1]
    n=int(sys.argv[2])
    n=n+1
    
    if option == "-p":

        my_tasks = Queue()
        my_results = Queue()
    
        workers = [Process(target=worker, args=(my_tasks, my_results)) for i in xrange(2,n)]
    
        for proc in workers:
            proc.start()
    
    	for i in xrange(2,n):
            my_tasks.put(i)
        
        uniq_factors_list=[]
        
    	for i in xrange(2,n):
            result = my_results.get()
            key = result[0]
            f = result[1]
            s=list(set(f))
            
            uniq_factors_list.append(len(s))
    
            print "%20s" % str(key),
            print "%20s" % str(f),
            print "%20s" % str(s),
            print "%20s" % str(len(s))
        
        c = Counter(uniq_factors_list)
        
        print c
        totaltime= time() - start
        print "Time elapsed is " + str(totaltime)
        
    elif option == "-ip":

        cli = Client()
        
        dview = cli[:]        

        @dview.parallel(block=True)
        def factorize(n):
            if n < 2:
                return []
            factors = []
            p = 2
            
            while True:
                if n == 1:
                    return factors
                r = n % p
                if r == 0:
                    factors.append(p)
                    n = n / p
                elif p * p >= n:
                    factors.append(n)
                    return factors
                elif p > 2:
                    p += 2
                else:
                    p += 1   

        uniq_factors_list=[]
        factors = factorize.map(xrange(2, n))
        slist=[]
        for f in factors:
            s=list(set(f))
            slist.append(s)
            uniq_factors_list.append(len(s))

        c = Counter(uniq_factors_list)
        

        for i in xrange(len(factors)):
            print "%20s" % str(factors[i]),
            print "%20s" % str(slist[i]),
            print "%20s" % str(uniq_factors_list[i])

        print c

        totaltime= time() - start
        print "Time elapsed is " + str(totaltime)

    elif option == "-s":

        uniq_factors_list=[]
        for i in xrange(2,n):
            f=factorize(i)
    	    s=list(set(f))
            uniq_factors_list.append(len(s))

            print "%20s" % str(i),
            print "%20s" % str(f),
            print "%20s" % str(s),
            print "%20s" % str(len(s))

        c = Counter(uniq_factors_list)
            
        print c
        totaltime= time() - start
        print "Time elapsed is " + str(totaltime)



