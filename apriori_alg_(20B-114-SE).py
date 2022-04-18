
## import pandas
import pandas as pd

## create data frame 


data={"item_no":["T1","T2","T3","T4","T5","T6"],"items":[[11,12,13],[12,13,14],[14,15],[11,12,14],[11,12,13,15],[11,12,13,14]]}
df=pd.DataFrame(data)

## print given information
print("minimum thershold is 50% which is equal to 3")
print("confidence  is 50%")


print("-------Given data set--------")
print(df)


m_sup=3
mt="50%"
c="60%"



lst= [[11,12,13],[12,13,14],[14,15],[11,12,14],[11,12,13,15],[11,12,13,14]]
a=sum(x.count(11) for x in lst)
b=sum(x.count(12) for x in lst)
c=sum(x.count(13) for x in lst)
d=sum(x.count(14) for x in lst)
e=sum(x.count(15) for x in lst)
print("---------- step no 1 count each item ------------")

print('count of 11 :',a)
print('count of 12 :',b)
print('count of 13 :',c)
print('count of 14 :',d)
print('count of 15 :',e)

print("---------- step no 02 ------------")
lst2=[]
def check():
        if a >= 3:
                lst2.append(a)
        if b >= 3:
                lst2.append(b)
        if c >= 3:
                lst2.append(c)
        if d >= 3:
                lst2.append(d)
        if e >= 3:
                lst2.append(e)
        
        print(" after campring minimum support we have : ",lst2)
        
check()

print('count of 11 :',a)
print('count of 12 :',b)
print('count of 13 :',c)
print('count of 14 :',d)

print("---------step no 03---------")

s= "{11 ,12 } >>> 13"
print("consider first item set:",s)

t_itemsets = 6
together= 3
seperate= 4

support= together/t_itemsets
confidence= together/seperate
con= support*100
con2=confidence*100


## compute values with minimum thershold and confidence
if support >= 0.5:
        print("support value is :", con)
if confidence >= 0.6:
        print("confidence value is :", con2)

print("--------Final Result---------")
print("most repeat item set in given data set is :" , s)
















