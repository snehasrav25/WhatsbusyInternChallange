# -*- coding: utf-8 -*-
"""Question3a.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tUWXAYe8g4TjWDs8nsO9zClp3vHnTvQk
"""

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import numpy as np
import statistics
from statistics import mean 
df={'days':[1,1,2,2,1,3,4],'values':[10,10,5,3,-2,4,20]}
days=df.get('days')
values=df.get('values')

modifiedarrays={}
days=np.array(days)
values=np.array(values)

for i in range (len(days)):
    if days[i] in modifiedarrays.keys():
        modifiedarrays[days[i]].append(values[i])
    else:
        modifiedarrays[days[i]]=[values[i]]

#print(modifiedarrays)
newdict={}
daysaslist=[]
avglist =[]
mediancomputed=[]
listmax=[]
listmin=[]
for k in modifiedarrays.keys():
  daysaslist.append(k)
  m=mean(modifiedarrays.get(k))
  avglist.append(m)
  mediancomputed.append(statistics.median(modifiedarrays.get(k)))
  listmax.append(max(modifiedarrays.get(k)))
  listmin.append(min(modifiedarrays.get(k)))

newdict['days']=daysaslist    
newdict['mean_values']=avglist
newdict['median_values']=mediancomputed
newdict['max_values']=listmax
newdict['min_values']=listmin

print(newdict)