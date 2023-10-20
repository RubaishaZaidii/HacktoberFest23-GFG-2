#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

# CREATE MATRIX WITH RANDOM VALUES

def createMatrix(rows,columns):
    matrix=[]
    for i in range (rows):
        a=[]
        for j in range (columns):
            a.append(random.randint(1,10))
        matrix.append(a)
    return matrix
    
# ADD ALL ELEMENTS OF MATRIX

def matrixSum(matrix,rows,columns):
    sum=0
    for i in range (rows):
        for j in range (columns):
            sum=sum+matrix[i][j]
    return sum
    
    # DIVIDE MATRIX ELEMENTS BY SUM
    
def divideMatrixBySum(matrixSum,matrix,rows,columns):
    newMatrix=[]
    for i in range (rows):
        b=[]
        for j in range (columns):
            m=matrix[i][j]/matrixSum
            m=round(m,1)
            b.append(m)
        newMatrix.append(b)   
    return newMatrix

# FIND MARGINALS OF X

def marginalsX(newMatrix,rows,columns):
    rowMarginals=[]
    for i in range (rows):
        sum=0
        for j in range (columns):
            sum=sum+newMatrix[i][j]
            sum=round(sum,1)
        rowMarginals.append(sum)
    return rowMarginals
    
    # FIND MARGINALS OF Y

def marginalsY(matrix,rows,columns):
    colMarginals=[]
    for i in range (columns):
        sum=0
        for j in range (rows):
            sum=sum+matrix[j][i]
            sum=round(sum,1)
        colMarginals.append(sum)
    return colMarginals
    
    # CHECK INDEPENDENT MARGINALS

def checkIndependentMarginals(matrix,MarginalsOfX,MarginalsOfY,rows,col):
    for i in range (len(MarginalsOfX)):
        for j in range (len(MarginalsOfY)):
            matrix[i][j]=round(matrix[i][j],1)
            p=MarginalsOfX[i]*MarginalsOfY[j]
            p=round(p,1)
            
            if(matrix[i][j]!=p):
                return False
        
    return True
            

# INPUT FOR ROWS AND COLUMNS
rows=int(input("enter no of rows"))
columns=int(input("enter no of columns"))
count=0
while(count==0):
    matrix=createMatrix(rows,columns)
    sumOfMatrix=matrixSum(matrix,rows,columns)
    newMatrix=divideMatrixBySum(sumOfMatrix,matrix,rows,columns)
    probability=matrixSum(newMatrix,rows,columns)
    probability=round(probability)

#  CHECK SUM MUST 1

    if(probability==1):
        MarginalsOfX=marginalsX(newMatrix,rows,columns)
        print(MarginalsOfX)
        MarginalsOfY=marginalsY(newMatrix,rows,columns)
        print(MarginalsOfY)
        
    
        # CHECK INDEPENDENT 
    
        independent=checkIndependentMarginals(newMatrix,MarginalsOfX,MarginalsOfX,rows,columns)
        if(independent):
            count=1
            print("ORIGINAL MATRIX:",matrix)
            print("NEW MATRIX:",newMatrix)
            print(" ROW MARGINALS:",MarginalsOfX)
            print("COLUMN MARGINALS",MarginalsOfY)
            
            

