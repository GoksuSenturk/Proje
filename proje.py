import numpy as np
import random

t=[0,0,0] #fırınların başlangıç saati

tc= 1
vp= 2
a= 3

tcf=15
vpf=20
af=25

b1=[]
b2=[]
b3=[]
b4=[]
b5=[]
b6=[]
b7=[]
b8=[]
b9=[]


job_batch=[
[0,0,0,0,0,0,1,1,1],
[1,1,1,0,0,0,0,0,0],
[0,0,0,1,1,1,1,1,1],
[0,0,0,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1],
[1,1,1,0,0,0,0,0,0],
[0,0,0,0,0,0,1,1,1],
[1,1,1,0,0,0,0,0,0],
[1,1,1,0,0,0,1,1,1],
[0,0,0,1,1,1,1,1,1],
[0,0,0,1,1,1,0,0,0],
[0,0,0,1,1,1,0,0,0],
[1,1,1,0,0,0,0,0,0],
[1,1,1,1,1,1,0,0,0],
[0,0,0,1,1,1,0,0,0],
[1,1,1,1,1,1,1,1,1],
[0,0,0,1,1,1,0,0,0],
[1,1,1,1,1,1,1,1,1],
[1,1,1,0,0,0,1,1,1],
[1,1,1,0,0,0,1,1,1],
[1,1,1,0,0,0,0,0,0],
[0,0,0,1,1,1,0,0,0],
[0,0,0,1,1,1,1,1,1],
[1,1,1,0,0,0,0,0,0],
[0,0,0,0,0,0,1,1,1]]

for i in range(0,25):
    for j in range(0,9):
        if job_batch[i][j]==1:
            if j==0:
                b1.append(i)
            elif j==1:
                b2.append(i)
            elif j==2:
                b3.append(i)
            elif j==3:
                b4.append(i)
            elif j==4:
                b5.append(i)
            elif j==5:
                b6.append(i)
            elif j==6:
                b7.append(i)
            elif j==7:
                b8.append(i)
            elif j==8:
                b9.append(i)


#matrisin içinden random seçim yapıp işleri batchlere ata
rand1= random.randint(len(b1)-int(af/a),int(af/a))
batch1=np.zeros((rand1,1))
select1=len(b1)

while rand1>0:# her batch max 8 iş alabilir o yüzden 0-8 arası random sayı ürettik,batchin kaç iş alacağını belirledik
    rand2 = random.randint(0, select1-1)  # her batch için 13 ihtimal var,0-12 arası bir indis seçeriz,batch o indisteki işi alır
    batch1[rand1-1]=b1[rand2]
    del b1[rand2]   # kalan işleri burdan görebiliriz
    rand1-=1
    select1-=1

print("Batch1 = %s " % (batch1.transpose()))

for i in range(0,len(batch1)):
    if (batch1[i] in b2):
        b2.remove(batch1[i])
    if (batch1[i] in b3):
        b3.remove(batch1[i])
    if (batch1[i] in b4):
        b4.remove(batch1[i])
    if (batch1[i] in b5):
        b5.remove(batch1[i])
    if (batch1[i] in b6):
        b6.remove(batch1[i])
    if (batch1[i] in b7):
        b7.remove(batch1[i])
    if (batch1[i] in b8):
        b8.remove(batch1[i])
    if (batch1[i] in b9):
        b9.remove(batch1[i])


rand3=random.randint(0,len(b2)) #kalan işler arasından kaç tane iş seçeceğimize karar vermek için random bir sayı ürettik
select2=13-len(batch1)
batch2=np.zeros((rand3,1))

while rand3>0:
    rand4=random.randint(0,select2-1)
    batch2[rand3 - 1] = b2[rand4]
    del b2[rand4]  # kalan işleri burdan görebiliriz
    rand3 -= 1
    select2 -= 1

print("Batch2 = %s " % (batch2.transpose()))

for i in range(0,len(batch2)):
    if (batch2[i] in b3):
        b3.remove(batch2[i])
    if (batch2[i] in b4):
        b4.remove(batch2[i])
    if (batch2[i] in b5):
        b5.remove(batch2[i])
    if (batch2[i] in b6):
        b6.remove(batch2[i])
    if (batch2[i] in b7):
        b7.remove(batch2[i])
    if (batch2[i] in b8):
        b8.remove(batch2[i])
    if (batch2[i] in b9):
        b9.remove(batch2[i])


batch3=np.zeros((len(b3),1))
for i in range(0,len(b3)):
    batch3[i]=b3[i]


print("Batch3 = %s " % (batch3.transpose()))

for i in range(0,len(batch3)):
    if (batch3[i] in b4):
        b4.remove(batch3[i])
    if (batch3[i] in b5):
        b5.remove(batch3[i])
    if (batch3[i] in b6):
        b6.remove(batch3[i])
    if (batch3[i] in b7):
        b7.remove(batch3[i])
    if (batch3[i] in b8):
        b8.remove(batch3[i])
    if (batch3[i] in b9):
        b9.remove(batch3[i])

rand5=random.randint(0,len(b4)) #kalan işler arasından kaç tane iş seçeceğimize karar vermek için random bir sayı ürettik
select3=len(b4)
batch4=np.zeros((rand5,1))

while rand5>0:
    rand6=random.randint(0,select3-1)
    batch4[rand5 - 1] = b4[rand6]
    del b4[rand6]  # kalan işleri burdan görebiliriz
    rand5 -= 1
    select3 -= 1

print("Batch4 = %s " % (batch4.transpose()))

for i in range(0,len(batch4)):
    if (batch4[i] in b5):
        b5.remove(batch4[i])
    if (batch4[i] in b6):
        b6.remove(batch4[i])
    if (batch4[i] in b7):
        b7.remove(batch4[i])
    if (batch4[i] in b8):
        b8.remove(batch4[i])
    if (batch4[i] in b9):
        b9.remove(batch4[i])

rand7 = random.randint(0, len(b5))  # kalan işler arasından kaç tane iş seçeceğimize karar vermek için random bir sayı ürettik
select4 = len(b5)
batch5 = np.zeros((rand7, 1))

while rand7 > 0:
    rand8 = random.randint(0, select4 - 1)
    batch5[rand7 - 1] = b5[rand8]
    del b5[rand8]  # kalan işleri burdan görebiliriz
    rand7 -= 1
    select4 -= 1

print("Batch5 = %s " % (batch5.transpose()))

for i in range(0, len(batch5)):
    if (batch5[i] in b6):
        b6.remove(batch5[i])
    if (batch5[i] in b7):
        b7.remove(batch5[i])
    if (batch5[i] in b8):
        b8.remove(batch5[i])
    if (batch5[i] in b9):
        b9.remove(batch5[i])

rand9 = random.randint(0, len(b6))  # kalan işler arasından kaç tane iş seçeceğimize karar vermek için random bir sayı ürettik
select5 = len(b6)
batch6 = np.zeros((rand9, 1))

while rand9 > 0:
    rand10 = random.randint(0, select5 - 1)
    batch6[rand9 - 1] = b6[rand10]
    del b6[rand10]  # kalan işleri burdan görebiliriz
    rand9 -= 1
    select5 -= 1

print("Batch6 = %s " % (batch6.transpose()))

for i in range(0, len(batch6)):
    if (batch6[i] in b7):
        b7.remove(batch6[i])
    if (batch6[i] in b8):
        b8.remove(batch6[i])
    if (batch6[i] in b9):
        b9.remove(batch6[i])

rand11 = random.randint(0, len(b7))  # kalan işler arasından kaç tane iş seçeceğimize karar vermek için random bir sayı ürettik
select6 = len(b7)
batch7 = np.zeros((rand11, 1))

while rand11 > 0:
    rand12 = random.randint(0, select6 - 1)
    batch7[rand11 - 1] = b7[rand12]
    del b7[rand12]  # kalan işleri burdan görebiliriz
    rand11 -= 1
    select6 -= 1

print("Batch7 = %s " % (batch7.transpose()))

for i in range(0, len(batch7)):
    if (batch7[i] in b8):
        b8.remove(batch7[i])
    if (batch7[i] in b9):
        b9.remove(batch7[i])

rand13 = random.randint(0, len(b8))  # kalan işler arasından kaç tane iş seçeceğimize karar vermek için random bir sayı ürettik
select7 = len(b8)
batch8 = np.zeros((rand13, 1))

while rand13 > 0:
    rand14 = random.randint(0, select7 - 1)
    batch8[rand13 - 1] = b8[rand14]
    del b8[rand14]  # kalan işleri burdan görebiliriz
    rand13 -= 1
    select7 -= 1

print("Batch8 = %s " % (batch8.transpose()))

for i in range(0, len(batch8)):
    if (batch8[i] in b9):
        b9.remove(batch8[i])


batch9=np.zeros((len(b9),1))
for i in range(0,len(b9)):
    batch9[i]=b9[i]

print("Batch9 = %s " % (batch9.transpose()))

duedate=[12,13,12,11,12,13,12,13,13,11,13,13,13,13,13,12,13,12,11,12,13,13,12,13,12]

if len(batch1)==0:
    min1=100
else:
    min1 = duedate[int(batch1[0])]

if len(batch2)==0:
    min2=100
else:
    min2 = duedate[int(batch2[0])]

if len(batch3)==0:
    min3=100
else:
    min3 = duedate[int(batch3[0])]

if len(batch4)==0:
    min4=100
else:
    min4 = duedate[int(batch4[0])]

if len(batch5)==0:
    min5=100
else:
    min5 = duedate[int(batch5[0])]

if len(batch6)==0:
    min6=100
else:
    min6 = duedate[int(batch6[0])]

if len(batch7)==0:
    min7=100
else:
    min7 = duedate[int(batch7[0])]

if len(batch8)==0:
    min8=100
else:
    min8 = duedate[int(batch8[0])]

if len(batch9)==0:
    min9=100
else:
    min9 = duedate[int(batch9[0])]


for i in range(0,len(batch1)):
    if duedate[int(batch1[i])]<min1:
        min1=duedate[int(batch1[i])]

for i in range(0,len(batch2)):
    if duedate[int(batch2[i])]<min2:
        min2=duedate[int(batch2[i])]

for i in range(0,len(batch3)):
    if duedate[int(batch3[i])]<min3:
        min3=duedate[int(batch3[i])]

for i in range(0,len(batch4)):
    if duedate[int(batch4[i])]<min4:
        min4=duedate[int(batch4[i])]

for i in range(0,len(batch5)):
    if duedate[int(batch5[i])]<min5:
        min5=duedate[int(batch5[i])]

for i in range(0,len(batch6)):
    if duedate[int(batch6[i])]<min6:
        min6=duedate[int(batch6[i])]

for i in range(0,len(batch7)):
    if duedate[int(batch7[i])]<min7:
        min7=duedate[int(batch7[i])]

for i in range(0,len(batch8)):
    if duedate[int(batch8[i])]<min8:
        min8=duedate[int(batch8[i])]

for i in range(0,len(batch9)):
    if duedate[int(batch9[i])]<min9:
        min9=duedate[int(batch9[i])]


pbatch1=pbatch2=pbatch3=2   #batchlerin process zamanı
pbatch4=pbatch5=pbatch6=3   #değiştirilebilir
pbatch7=pbatch8=pbatch9=4


laststart=[min1-pbatch1,min2-pbatch2,min3-pbatch3,min4-pbatch4,min5-pbatch5,min6-pbatch6,min7-pbatch7,min8-pbatch8,min9-pbatch9]

#print(laststart)

#print(laststart.index(min(laststart))) #min last startın kaçıncı batchte olduğu (index sayısı+1 yapılması lazım)

minfirintime=t[0] #en erken başlaması gereken batchi ilk fırına at

pbatch=[2,2,2,3,3,3,4,4,4]  #batchlerin process zamanları

for k in range(0,len(laststart)):
    if min(laststart)<50:
        print("%s batchi %s . fırına atıldı" % (laststart.index(min(laststart))+1, t.index(min(t))+1))
        t[t.index(min(t))]+=pbatch[laststart.index(min(laststart))]

        laststart[laststart.index(min(laststart))] = 1000
        print(t)
