directoryContents=[{'date':'02/15/2016','time':'10:49 PM','size':962,'name':'switchfinal.py'},{'date':'02/15/2016','time':'10:49 PM','size':943,'name':'switchfinal.py.bak'},{'date':'01/27/2016','time':'11:46 AM','size':15,'name':'t.py'},{'date':'03/31/2016','time':'12:39 PM','size':840,'name':'t1.py'},{'date':'01/25/2016','time':'10:34 AM','size':2407,'name':'tc1.py'},{'date':'02/14/2017','time':'09:13 AM','size':0,'name':'teat.py'},{'date':'03/15/2016','time':'05:52 PM','size':5,'name':'tes.py'}]

for file in directoryContents:
    if (file['size']==0):
        print (file['name'])
     