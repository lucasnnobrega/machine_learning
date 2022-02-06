import cupy as cp 
import time

cp.show_config()

def example1():
    start = time.time()

    a = cp.array([[i for i in range(10)] for j in range(10)])

    b = a * a

    c = b
    for array in [a, b ,c]:
        print(array, array.device)


    for i in range(10):
        c = b * c
        #time.sleep(5)

    print(time.time() - start)

    print(b)

    print(a)

    print(c)

def example2():
        
    import cupy as cp
    import cupyx.scipy.fft as cufft
    import scipy.fft
    scipy.fft.set_global_backend(cufft)

    a = cp.random.random(100).astype(cp.complex64)
    b = scipy.fft.fft(a)  # equivalent to cufft.fft(a)

    print(b)


#example1()
example2()