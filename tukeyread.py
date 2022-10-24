import numpy as np
f=open('多重比較_shs_1-3.txt','r',encoding='UTF-8')
a=f.readlines()
b=np.zeros(len(a)).reshape(17,1)
for i in range(len(a)):
    a[i]=np.array(a[i].split(' ')).astype(str)
np.savetxt('tukey.txt',a)