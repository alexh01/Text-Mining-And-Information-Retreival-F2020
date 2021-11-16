import os;


fnumbers=0
k = []
reader = open("../python_qid2all.txt", "r")
writer = open("./jsonfiles/python%i.JSON"%fnumbers,"w")
try:
    for i in range(485827):
        k = reader.readline().split('\t')
        k[3]=k[3][:-1]
        writer.write("{\"index\": {\"_id\": \""+k[0]+"\"} }\n")
        writer.write("{\"title\": \""+k[1]+"\",\"body\": \""+k[2]+"\",\"answer\": \""+k[3]+"\"}\n")
        if os.path.getsize("./jsonfiles/python%i.JSON"%fnumbers)>=50000000:
            writer.close()
            fnumbers+=1
            writer=open("./jsonfiles/python%i.JSON"%fnumbers,"w")
    reader.close()
    writer.close()
finally:
    print("problem")
    reader.close()
    writer.close()

fnumbers=0
reader = open("../java_qid2all.txt", "r")
writer = open("./jsonfiles/java%i.JSON"%fnumbers,"w")
try:
    for i in range(700552):
        k = reader.readline().split('\t')
        k[3]=k[3][:-1]
        writer.write("{\"index\": {\"_id\": \""+k[0]+"\"} }\n")
        writer.write("{\"title\": \""+k[1]+"\",\"body\": \""+k[2]+"\",\"answer\": \""+k[3]+"\"}\n")
        if os.path.getsize("./jsonfiles/java%i.JSON"%fnumbers)>=50000000:
            writer.close()
            fnumbers+=1
            writer=open("./jsonfiles/java%i.JSON"%fnumbers,"w")
    reader.close()
    writer.close()
finally:
    print("problem")
    reader.close()
    writer.close()

fnumbers=0
reader = open("../javascript_qid2all.txt", "r")
writer = open("./jsonfiles/javascript%i.JSON"%fnumbers,"w")
try:
    for i in range(1319382):
        k = reader.readline().split('\t')
        k[3]=k[3][:-1]
        writer.write("{\"index\": {\"_id\": \""+k[0]+"\"} }\n")
        writer.write("{\"title\": \""+k[1]+"\",\"body\": \""+k[2]+"\",\"answer\": \""+k[3]+"\"}\n")
        if os.path.getsize("./jsonfiles/javascript%i.JSON"%fnumbers)>=50000000:
            writer.close()
            fnumbers+=1
            writer=open("./jsonfiles/javascript%i.JSON"%fnumbers,"w")
    reader.close()
    writer.close()
finally:
    print("problem")
    reader.close()
    writer.close()
reader.close()
writer.close()
#python 485827
#java 700552
#javascript 1319382