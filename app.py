from multiprocessing import Process
import numpy as np
import time
from os import getpid

from flask import Flask
app = Flask(__name__)



def testLoop():
    print(str(getpid()))
    start = time.time()
    tmp = 0.0
    for i in range(10000):
	    for j in range(i):
		    tmp = np.sqrt(tmp + j)
    end = time.time()
    return (end - start)
	


@app.route('/')
def index():
    # testLoop()
    p = Process(target=testLoop)
    p.start()
    p.join()
    return str(getpid())


if __name__ == '__main__':
    app.run()
