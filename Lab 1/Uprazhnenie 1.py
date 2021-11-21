import numpy as np
x=[1,10,1000]
for i in range(3):
   a=1/(np.sin(x[i])+1)
   b=(np.e)**a
   c=1.25+1/(x[i]**15)
   y=np.log(b/c)/np.log(1+x[i]**2)
   print ("for x=", x[i], "   y=", y)
