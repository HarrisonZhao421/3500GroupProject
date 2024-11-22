import random
import time
import matplotlib.pyplot as plt
from bucketsort import bucketSort as B
from countingsort import counting_sort as C
from radix import radixSort as R

#def B(lst): return
#def R(lst): return
#def C(lst): return

def GenUniformList(size, mult, ran=1):
    lst = list() ; num = 0
    for x in range(size):
        num += ran
        for y in range(mult):
            lst.append(x)

    random.shuffle(lst)
    return lst

def GenNonUniformList(size, mult, ran=1):
    lst = list() ; count = 0 ; num = 0
    while count < size:
        num += random.randint(0, ran)
        for y in range( random.randint(1, mult) ):
            lst.append(num)
            count += 1
            if count >= size: break
    random.shuffle(lst)
    return lst

def ClusteredList(size, ran, fac = .1):
    lst = list() ; ten = int(ran * fac)
    for count in range(size):
        if count < int(size * (1-fac)): lst.append(random.randint(1, ten))
        else: lst.append(random.randint(ran-ten, ran))
    random.shuffle(lst)
    return lst
        
def ExecTime(lst, func):
    start = time.perf_counter()
    func(lst)
    end = time.perf_counter()
    return (end-start) * 10**3

def Clear(lst):
    for item in lst: item.clear()

def MultTests(pltlst):
    #Test Uniform List with low range
    b_x = pltlst[0] ; b_y = pltlst[1] ; r_x = pltlst[2] ; r_y = pltlst[3] ; c_x = pltlst[4] ; c_y = pltlst[5]

    for x in range(1000, 50000, 1000):
        #highlst = ClusteredList(x, 10, .5)
        #lowlst = ClusteredList(x, 1000000, .5)
        highlst = ClusteredList(x, 10000, .95)
        lowlst = ClusteredList(x, 10000, .5)
        b_x.append(x) ; b_y.append( ExecTime(highlst.copy(), B) )
        r_x.append(x) ; r_y.append( ExecTime(lowlst.copy(), B) )
        lowlst.clear()
        highlst.clear()
    plt_1 = plt.figure(figsize=(14, 9))
    plt.title("Clustered List Bucket Sort") ; plt.xlabel("Size of List") ;plt.ylabel("Time (ms)")
    plt.scatter(b_x, b_y, label = "NonUniform", s=5, marker="D")
    plt.scatter(r_x, r_y, label = "Uniform", s=8, marker='v')
    plt.legend() ; plt.show()
    Clear(pltlst)

def UniformLowTest(pltlst):
    #Test Uniform List with low range
    b_x = pltlst[0] ; b_y = pltlst[1] ; r_x = pltlst[2] ; r_y = pltlst[3] ; c_x = pltlst[4] ; c_y = pltlst[5]
    mult = 3
    for x in range(2, 500, 5):
        lst = GenUniformList(x, mult)
        b_x.append(x*mult) ; b_y.append( ExecTime(lst.copy(), B) )
        r_x.append(x*mult) ; r_y.append( ExecTime(lst.copy(), R) )
        c_x.append(x*mult) ; c_y.append( ExecTime(lst.copy(), C) )
        lst.clear()
    plt_1 = plt.figure(figsize=(14, 9))
    plt.title("Uniform List W/ Low Range Time Complexity") ; plt.xlabel("Size of List") ;plt.ylabel("Time (ms)")
    plt.scatter(b_x, b_y, label = "Bucket", s=5, marker="D")
    plt.scatter(r_x, r_y, label = "Radix", s=8, marker='v')
    plt.scatter(c_x, c_y, label = "Counting", s=8, marker='x')
    plt.legend() ; plt.show()
    Clear(pltlst)

def UniformHighTest(pltlst):
    #Test Uniform List with High Range
    b_x = pltlst[0] ; b_y = pltlst[1] ; r_x = pltlst[2] ; r_y = pltlst[3] ; c_x = pltlst[4] ; c_y = pltlst[5]
    sz = 1000
    for x in range(1, 1000, 9):
        lst = GenUniformList(sz, 1, x)
        b_x.append(x*sz) ; b_y.append( ExecTime(lst.copy(), B) )
        r_x.append(x*sz) ; r_y.append( ExecTime(lst.copy(), R) )
        c_x.append(x*sz) ; c_y.append( ExecTime(lst.copy(), C) )
        lst.clear()
    plt_2 = plt.figure(figsize=(14, 9))
    plt.title("Uniform List W/ High Range Time Complexity") ; plt.xlabel("Range") ;plt.ylabel("Time (ms)")
    plt.scatter(b_x, b_y, label = "Bucket", s=5, marker='D')
    plt.scatter(r_x, r_y, label = "Radix", s=8, marker='v')
    plt.scatter(c_x, c_y, label = "Counting", s=8, marker='x')
    plt.legend() ; plt.show()
    Clear(pltlst)

def NonUniformLowTest(pltlst):
    #Test NonUniform List with High Range
    b_x = pltlst[0] ; b_y = pltlst[1] ; r_x = pltlst[2] ; r_y = pltlst[3] ; c_x = pltlst[4] ; c_y = pltlst[5]
    for x in range(1, 1000, 10):
        lst = GenNonUniformList(10000, x, 10)
        b_x.append(x) ; b_y.append( ExecTime(lst.copy(), B) )
        r_x.append(x) ; r_y.append( ExecTime(lst.copy(), R) )
        c_x.append(x) ; c_y.append( ExecTime(lst.copy(), C) )
        lst.clear()
    plt_1 = plt.figure(figsize=(14, 9))
    plt.title("Non-Uniform List W/ Low Range Time Complexity") ; plt.xlabel("Non-Uniformity Factor") ;plt.ylabel("Time (ms)")
    plt.scatter(b_x, b_y, label = "Bucket", s=5, marker="D")
    plt.scatter(r_x, r_y, label = "Radix", s=8, marker='v')
    plt.scatter(c_x, c_y, label = "Counting", s=8, marker='x')
    plt.legend() ; plt.show()
    Clear(pltlst)

def NonUniformHighTest(pltlst):
    #Test NonUniform List with High Range
    b_x = pltlst[0] ; b_y = pltlst[1] ; r_x = pltlst[2] ; r_y = pltlst[3] ; c_x = pltlst[4] ; c_y = pltlst[5]
    for x in range(1, 10000, 429):
        lst = GenNonUniformList(10000, x, x)
        b_x.append(x) ; b_y.append( ExecTime(lst.copy(), B) )
        r_x.append(x) ; r_y.append( ExecTime(lst.copy(), R) )
        c_x.append(x) ; c_y.append( ExecTime(lst.copy(), C) )
        lst.clear()
    plt_1 = plt.figure(figsize=(14, 9))
    plt.title("Non-Uniform List W/ High Range Time Complexity") ; plt.xlabel("Non-Uniformity & Range Factor") ;plt.ylabel("Time (ms)")
    plt.scatter(b_x, b_y, label = "Bucket", s=5, marker="D")
    plt.scatter(r_x, r_y, label = "Radix", s=8, marker='v')
    plt.scatter(c_x, c_y, label = "Counting", s=8, marker='x')
    plt.legend() ; plt.show()
    Clear(pltlst)

def ClusterTest(pltlst):
    #Test Clustered List
    b_x = pltlst[0] ; b_y = pltlst[1] ; r_x = pltlst[2] ; r_y = pltlst[3] ; c_x = pltlst[4] ; c_y = pltlst[5]
    x = .5
    while (x >= .05):
        lst = ClusteredList(10000, 100, x)
        b_x.append(x) ; b_y.append( ExecTime(lst.copy(), B) )
        r_x.append(x) ; r_y.append( ExecTime(lst.copy(), R) )
        c_x.append(x) ; c_y.append( ExecTime(lst.copy(), C) )
        lst.clear()
        x -= .025
    plt_1 = plt.figure(figsize=(14, 9))
    plt.title("Clustered List Time Complexity") ; plt.xlabel("Cluster Factor") ;plt.ylabel("Time (ms)")
    plt.scatter(b_x, b_y, label = "Bucket", s=5, marker="D")
    plt.scatter(r_x, r_y, label = "Radix", s=8, marker='v')
    plt.scatter(c_x, c_y, label = "Counting", s=8, marker='x')
    plt.legend() ; plt.show()
    Clear(pltlst)

if __name__ == "__main__":
    b_x = list() ; b_y = list() ; r_x = list() ; r_y = [] ; c_x = [] ; c_y = list()
    pltlst = [b_x, b_y, r_x, r_y, c_x, c_y]
    #MultTests(pltlst)
    UniformLowTest(pltlst)
    UniformHighTest(pltlst)
    NonUniformHighTest(pltlst)
    NonUniformLowTest(pltlst)
    ClusterTest(pltlst)
