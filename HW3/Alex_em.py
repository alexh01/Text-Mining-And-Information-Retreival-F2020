import numpy as np;
import math;
from operator import add, truediv;


file1 = open("./all_documents.txt", "r")
file1.seek(0,0)
# theta_d, length = 2
# probability that topic z connects to the document
document_topic_vector = [0,0]
# phi_z, length = 8
# probability that word w connects to the topic
topic_word_vector = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]

dictionary = {
  "import": 0,
  "class": 1,
  "hashmap": 2,
  "hashset": 3,
  "arraylist": 4,
  "lambda": 5,
  "elif": 6,
  "def": 7
}

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

phi_py=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
phi_java=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
theta=[0.0,0.0]
Mat1 = np.zeros([10000,2],np.int8)
Mat2 = np.zeros([10000,8],np.int8)
words=[]
line=""
try:
    for i in range(100):
        ##gets the document from the txt
        line = file1.readline()
        ##gets the terms in the document
        words = line[2:-2].split(" ")

        ##gets the count of each word in the vocabulary within the document
        for j in words:
            topic_word_vector[dictionary.get(j)]+=1

        ##adds it to python/java
        if line[0]=="1":
            topic_word_vector = [x / sum(topic_word_vector, 0) for x in topic_word_vector]
            phi_py = list(map(add, phi_py, topic_word_vector))
            theta[1] += 1
            document_topic_vector[1]+=1
        else:
            topic_word_vector = [x / sum(topic_word_vector, 0) for x in topic_word_vector]
            phi_java = list(map(add, phi_java, topic_word_vector))
            theta[0] += 1
            document_topic_vector[0]+=1

    
    ##divides by the number of documents
    phi_py = [x / 100 for x in phi_py]
    
    # phi_py = [x / document_topic_vector[1] for x in phi_py]
    # phi_py[0] *= (document_topic_vector[1]/100)
    # phi_py[1] *= (document_topic_vector[1]/100)
    
    phi_java = [x / 100 for x in phi_java]
    
    # phi_java = [x / document_topic_vector[0] for x in phi_java]
    # phi_java[0] *= (document_topic_vector[0]/100)
    # phi_java[1] *= (document_topic_vector[0]/100)
    
    # theta_java[0] /= 100
    # theta_py[1] /= 100

    ##prints it
    print("%s\n%s"%(phi_java, phi_py))
    print("%s"%theta)
    # print("%s\n%s"%(theta_py, theta_java))
    file1.seek(0,0)
    # M-STEP
    s=0.0
    for i in range(10100):
        topic_word_vector = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        s=0.0
        ##gets the document from the txt
        line = file1.readline()
        ##gets the terms in the document
        words = line[1:-2].split(" ")
        for j in range(8):
            ## gets the counts of each word in each document
            s += words.count(hashmap.get(j))
            topic_word_vector[j] = words.count(hashmap.get(j))*phi_java[j]
        if (sum(topic_word_vector, 0)/len(words) > 0.2):
            print("p(Java|document%i) = %f, topic = Java"%(i+100, sum(topic_word_vector, 0)/s))

    print(Mat1.view(dtype=np.int8, type=np.matrix))
    print(Mat1[1])
    print("all good here")
finally:
    #print("error")
    file1.close()
