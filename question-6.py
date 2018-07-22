input = open("input.txt","r")
output =open("output.txt","w")
lineno=0
data=input.readlines()
for line in data:
  line=line.rstrip()
  lineno+=1
  words=line.split()
  output.write("LINE "+str(lineno)+":"+" WORD COUNT:"+str(len(words))+" CHARACTERS COUNT:"+str(len(line))+"\n")
input.close()
output.close()