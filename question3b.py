# Hello World program in Python
    
import numpy as np

df={'employee':[1001,1002,1004,1001,1001,1002,1004,1005,1005],'amount':[125,542,2345,892,100,1234,657,34,35],'pos':[2, 2, 2, 2, 2, 2, 2, 2, 2]}
employee=df.get('employee')
employee=np.array(employee)
amount=df.get('amount')
pos=df.get('pos')
#days=np.array(employee)
#values=np.array(amount)
employeeamount={}
employeepos={}

for i in range (len(employee)):
    if employee[i] in employeeamount.keys():
        employeeamount[employee[i]].append(amount[i])
    else:
        employeeamount[employee[i]]=[amount[i]]

#print(employeeamount)

for i in range (len(employee)):
    if employee[i] in employeepos.keys():
        continue
    else:
        employeepos[employee[i]]=pos[i]

#print(employeepos)

listemployee=[]
for k in employeeamount.keys():
    listemployee.append(k)   
#print(listemployee)
amountdiff=[]

for i in employeeamount.keys():
  #print(i)
  #print(max(employeeamount.get(i)))
  maximum=max(employeeamount.get(i))
  minimum=min(employeeamount.get(i))
  diff=maximum-minimum
  amountdiff.append(diff)


#print(amountdiff)

max1=0
employee=0
posfinal=[]
maxfinal=[]
employeefinal=[]
for i in range(len(amountdiff)):
  if amountdiff[i]>max1:
    max1=amountdiff[i]
    employee=listemployee[i]
    
maxfinal.append(max1)
employeefinal.append(employee)
posfinal.append(employeepos.get(employee))
amountdiff.remove(max1)
listemployee.remove(employee)
max1=0
employee=0
for i in range(len(amountdiff)):
  if amountdiff[i]>max1:
    max1=amountdiff[i]
    employee=listemployee[i]
maxfinal.append(max1)
employeefinal.append(employee)
posfinal.append(employeepos.get(employee))
newdict={}
newdict['employee']=employeefinal
newdict['pos']=posfinal
newdict['amount_diff']=maxfinal

print(newdict)