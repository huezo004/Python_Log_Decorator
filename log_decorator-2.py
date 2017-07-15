def log(originalFunc):
   	import time
        def decorator(*args):
	  print "Calling function " + originalFunc.__name__
          if len(args)==0:
	     print "No Arguments"
	     time1=time.time()
	     print "Output:"		 
	     originalResult= originalFunc(*args)
	     time2=time.time()-time1
	     print ('Execution time: {:5f}'.format(time2))
	     if originalResult==None:
	      print "No return value"
	     else:
              y=type(originalResult)
              print('Return Value: {} of type {}.'.format(originalResult,y.__name__))   
          else:
	    print "Arguments:"
	    for arg in args:
	      x=arg
	      rx=type(x)
	      print('- {} of type {}.'.format(x, rx.__name__))
	    time1=time.time()
	    print "Output:"		 
	    originalResult= originalFunc(*args)
	    time2=time.time()-time1
	    print ('Execution time: {:5f}'.format(time2))
	    if originalResult==None:
	      print "No return value"
	    else:
              y=type(originalResult)
              print('Return Value: {} of type {}.'.format(originalResult,y.__name__))   
	return decorator


@log
def waste_time(a,b,c):
	import time
	print("wasting time")
	time.sleep(1)
	return a,b,c

waste_time('one',2,'3') 

@log
def print_hello():
   print "hello"

print_hello()












