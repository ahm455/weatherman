A = [
    [2, 1, 3],
    [0, 4, 5],
    [1, 2, 6]
]

B = [
    [1, 0, 2],
    [3, 1, 1],
    [0, 4, 2]
]
print('---------------a+b--------------')
result=[]
for x in range(len(A)):
    rows=[]
    for y in range(len(A[0])):
        rows.append(A[x][y]+B[x][y])
    result.append(rows)
print(result) 
print('---------------a-b--------------')
result=[]
for x in range(len(A)):A = [
    [2, 1, 3],
    [0, 4, 5],
    [1, 2, 6]
]

B = [
    [1, 0, 2],
    [3, 1, 1],
    [0, 4, 2]
]
print('---------------a+b--------------')
result=[]
for x in range(len(A)):
    rows=[]
    for y in range(len(A[0])):
        rows.append(A[x][y]+B[x][y])
    result.append(rows)
print(result) 
print('---------------a-b--------------')
result=[]
for x in range(len(A)):
    rows=[]
    for y in range(len(A[0])):
        rows.append(A[x][y]-B[x][y])
    result.append(rows)
print(result) 

print('---------------a*b--------------')
rowa=len(A)
cola=len(A[0])
rowb=len(B)
colb=len(B[0])

result=[]
for x in range(rowa):
    rows=[]
    for y in range(colb):
        total=0
        for k in range(cola):
            total += A[x][k]*B[k][y]
        rows.append(total)
    result.append(rows)    
print(result) 

print('---------------transpose of A--------------')
result=[]
for x in range(len(A)):
    rows=[]
    for y in range(len(A[0])):
        rows.append(A[y][x])
    result.append(rows)    
print (result)    

print('---------------Determent of A--------------')
A = [
    [2, 1, 3],
    [0, 4, 5],
    [1, 2, 6]
]
a = A[0][0]
b = A[0][1]
c = A[0][2]
d = A[1][0]
e = A[1][1]
f = A[1][2]
g = A[2][0]
h = A[2][1]
i = A[2][2]
k = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
print(k)

print('---------------identity check of A--------------')
A = [
    [1, 0, 0,0],
    [0, 1, 0,0],
    [0, 0, 1,0],
    [0, 0, 0,0]
]
def func(A):
    row=len(A)
    col=len(A[0])
    if row != col:
        return False
    for x in range(row):
        for y in range(col):
            if x==y and A[x][y] != 1:
                return False
            elif x!=y and A[x][y] != 0:
                return False
    return True
print(f'given matrix is identity matrix : {func(A)}')           


print('------inverse of a matrix-------')
A=[
    [1,2],
    [5,7]
]
deter= A[0][0]*A[1][1]-A[0][1]*A[1][0]
Ainv= [[A[1][1]/deter,-A[0][1]/deter],
       [-A[1][0]/deter,A[0][0]/deter]]
print(Ainv)


    rows=[]
    for y in range(len(A[0])):
        rows.append(A[x][y]-B[x][y])
    result.append(rows)
print(result) 

print('---------------a*b--------------')
rowa=len(A)
cola=len(A[0])
rowb=len(B)
colb=len(B[0])

result=[]
for x in range(rowa):
    rows=[]
    for y in range(colb):
        total=0
        for k in range(cola):
            total += A[x][k]*B[k][y]
        rows.append(total)
    result.append(rows)    
print(result) 

print('---------------transpose of A--------------')
result=[]
for x in range(len(A)):
    rows=[]
    for y in range(len(A[0])):
        rows.append(A[y][x])
    result.append(rows)    
print (result)    

print('---------------Determent of A--------------')
A = [
    [2, 1, 3],
    [0, 4, 5],
    [1, 2, 6]
]
a = A[0][0]
b = A[0][1]
c = A[0][2]
d = A[1][0]
e = A[1][1]
f = A[1][2]
g = A[2][0]
h = A[2][1]
i = A[2][2]
k = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
print(k)

print('---------------identity check of A--------------')
A = [
    [1, 0, 0,0],
    [0, 1, 0,0],
    [0, 0, 1,0],
    [0, 0, 0,1]
]
def func(A):
    row=len(A)
    col=len(A[0])
    if row != col:
        return False
    for x in range(row):
        for y in range(col):
            if x==y and A[x][y] != 1:
                return False
            elif x!=y and A[x][y] != 0:
                return False
            else:    
                return True
print(f'given matrix is identity matrix : {func(A)}')           


print('------inverse of a matrix-------')
A=[
    [1,2],
    [5,7]
]
deter= A[0][0]*A[1][1]-A[0][1]*A[1][0]
Ainv= [[A[0][0]/deter,A[1][1]/deter],
       [A[0][1]/deter,A[1][0]/deter]]
print(Ainv)


