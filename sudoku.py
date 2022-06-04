test = []
for i in range(6):
    print("Enter the elements of row",i,"by space between two subsequent elements")
    row = [int(x) for x in input().strip().split()]
    test.append(row)
print(test)

def colomn(c):
    col=[]
    for w in range(6):
       col.append(test[w][c])
    return col

def matrix(q,j):
    if j in [3,4,5]:
        if q in [0,1]:
            mat = test[0][3:6]+test[1][3:6]
        if q in [2,3]:
            mat = test[2][3:6] + test[3][3:6]
        if q in [4,5]:
            mat = test[4][3:6] + test[5][3:6]
    if j in [0,1,2]:
        if q in [0, 1]:
            mat = test[0][0:3] + test[1][0:3]
        if q in [2, 3]:
            mat = test[2][0:3] + test[3][0:3]
        if q in [4, 5]:
            mat = test[4][0:3] + test[5][0:3]
    return mat

def zeros(suduco):
    khali = 0
    for i in range(6):
        khali = khali + suduco[i].count(0)
    return khali


totblanks = []
for i in range(6):
    blanks = test[i].count(0)
    totblanks.append([blanks,i])
totblanks.sort()


finalsort = []
for i in range(6):
    finalsort.append(totblanks[i][1])

ideal = [1,2,3,4,5,6]

while zeros(test)!=0:
    for i in finalsort:
      vadhela = [x for x in ideal if x not in test[i]]
      for x in range(6):
         a = 2
         if test[i][x]==0:
             for p in vadhela:
                 cond1 = p not in colomn(x)
                 cond2 = p not in test[i]
                 cond3 = p not in matrix(i,x)
                 if cond1 and cond2 and cond3 :
                     a = a - 1
                     test[i][x] = p
                     if a <= 0 :
                         test[i][x]=0


print(test)

