import numpy as np;
import math;
from operator import add, truediv;

file1 = open("./all_documents.txt", "r")
file2 = open("./Alex_report.txt", "w")
file1.seek(0,0)
# theta_d, length = 2
# probability that topic z connects to the document
document_topic_vector = np.zeros([10100,2],np.float64)
# phi_z, length = 8
# probability that word w connects to the topic
topic_word_vector  = np.zeros([2,8],np.float64)

R = np.zeros([2,10100,8],np.float64)

hashmap = {
  0:"import",
  1:"class",
  2:"hashmap",
  3:"hashset",
  4:"arraylist",
  5:"lambda",
  6:"elif",
  7:"def"
}

words=[]
line=""
try:
    for i in range(100):
        ##gets the document from the txt
        line = file1.readline()
        ##gets the terms in the document
        words = line[2:-2].split(" ")
        document_topic_vector[i][int(line[0])] = 1
        ##gets the count of each word in the vocabulary within the document
        for j in range(8):
            topic_word_vector[int(line[0])][j] += words.count(hashmap.get(j))/(len(words)*100)
        
        R[int(line[0]),i]=topic_word_vector[int(line[0])]
        #file2.write("%s\n"%document_topic_vector[i])
    # print("%s\n%s"%(topic_word_vector[1], topic_word_vector[0]))
    # print("%s\n%s"%(document_topic_vector[1], document_topic_vector[0]))

    for c in range(8):
        print("p(\"%s\"|Java): %f"%(hashmap.get(c),topic_word_vector[0][c]))
    for c in range(8):
        print("p(\"%s\"|Python): %f"%(hashmap.get(c),topic_word_vector[1][c]))

    phi_java=topic_word_vector[0]
    phi_py=topic_word_vector[1]

    # file1.seek(0,0)
    temp=1.0
    theta = [0.0,0.0]
    phi = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    for i in range(100, 10100):
        line = file1.readline()
        words = line[1:-2].split(" ")
        for j in range(8):
            theta[0] += words.count(hashmap.get(j))*phi_java[j]
            theta[1] += words.count(hashmap.get(j))*phi_py[j]
            phi[j] = words.count(hashmap.get(j))/len(words)
        
        #theta[0] = (theta[0] - words.count(hashmap.get(0))*phi_java[0] - words.count(hashmap.get(1))*phi_java[1])#*(len(words)/(words.count(hashmap.get(1))+words.count(hashmap.get(0))))
        #theta[1] = (theta[1] - words.count(hashmap.get(0))*phi_py[0] - words.count(hashmap.get(1))*phi_py[1])#*(len(words)/(words.count(hashmap.get(1))+words.count(hashmap.get(0))))

        theta[0] /= len(words)
        theta[1] /= len(words)

        
        theta[0] = theta[0]/(theta[0]+theta[1])
        
        while (theta[0]>0.5 and words.count(hashmap.get(3))+words.count(hashmap.get(2))+words.count(hashmap.get(4))<words.count(hashmap.get(5))+words.count(hashmap.get(6))+words.count(hashmap.get(7))):
            theta[0] = math.log(1+theta[0],2.5)
        
        

        if theta[0] > 0.5:
            file2.write("p(Java|document%i) = %f, topic = Java\n"%(i-100, theta[0]))
            R[0,i]=phi#topic_word_vector[0]
        else:
            file2.write("p(Java|document%i) = %f, topic = Python\n"%(i-100, theta[0]))
            R[1,i]=phi#topic_word_vector[1]
        
        document_topic_vector[i] = [theta[0],1-theta[0]]
        #file2.write("%s\n"%document_topic_vector[i])    
        
        phi = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        theta = [0.0,0.0]
        temp=1.0
        # phi_java=topic_word_vector[0]
        # phi_py=topic_word_vector[1]
    
    #print(document_topic_vector.view(dtype=np.float32, type=np.matrix))

    print("all good here")
finally:
    #print("error")
    file1.close()
    file2.close()
