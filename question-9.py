import os
path="binder"
dirs = os.listdir(path)
for file in dirs:
  stats=os.stat(path+"/"+file)
  if(stats.st_size==0):
   print (file)
        
     
