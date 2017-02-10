#Examples for using the hashmap
from hashmap import HashMap

HM = HashMap()
def hash_test():
    for i in xrange(0,30):
        HM.put(i,i)
    for j in xrange(0,10):
        result =[]
        result.append(HM.get(j))
        print result

if __name__ == "__main__":
     hash_test()