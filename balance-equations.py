import math
import numpy
import re
from sympy import Matrix, lcm
print("EQUATION BALANCER:")
print("1- EQUATION")
print("2-HELP")
choice = int(input("choose one of the options:"))

elementList = []
elementMatrix = []



def split_reaction():
      reagents = equations.split("=")[0]
      reagents = reagents.replace(' ','').split('+')
      products = equations.split("=")[1]
      products = products.replace(' ','').split('+')
      
      return reagents,products


# def addToMatrix(element, index, count,side):
#      if(index == len(elementMatrix)):
#           elementMatrix.append([])
#           for x in elementList:
#                elementMatrix[index].append(0)
#      if(element not in elementList):
#           elementList.append(element)
#           for i in range(len(elementMatrix)):
#                elementMatrix[i].append(0)
#      column = elementList.index(element)
#      elementMatrix[index][column]+=count*side
def addToMatrix(element, index, count, side):
    if(index == len(elementMatrix)):
       elementMatrix.append([])
       for x in elementList:
            elementMatrix[index].append(0)
    if(element not in elementList):
        elementList.append(element)
        for i in range(len(elementMatrix)):
            elementMatrix[i].append(0)
    column=elementList.index(element)
    elementMatrix[index][column]+=count*side
    
def findElements(segment,index,multiplier,side):
     elementsAndNumber  = re.split('([A-Z][a-z]?)',segment)
     i=0
     while(i<len(elementsAndNumber)-1):
          i+=1
          if(len(elementsAndNumber[i])>0):
               if(elementsAndNumber[i+1].isdigit()):
                count = int(elementsAndNumber[i+1])*multiplier
                addToMatrix(elementsAndNumber[i], index, count, side)
                i+=1
               else:
                  addToMatrix(elementsAndNumber[i], index, multiplier, side)
                    


def compoundDecipher(compound, index, side):
     segments = re.split('(\([A-Za-z0-9]*\)[0-9]*)', compound)
     for segment in segments:
          if segment.startswith("("):
               segment = re.split('\)([0-9]*)',segment)
               multiplier=int(segment[1])
               segment=segment[0][1:]
               print(segment, multiplier)
          else:
               print(segment)
               multiplier = 1
          findElements(segment,index,multiplier,side)
equations = input("Write down the chemical equation:")
reagents,products = split_reaction()
print(f'reagents:{reagents}')
print(f'products:{products}')


for i in range(len(reagents)):
     compoundDecipher(reagents[i],i,1)
for i in range(len(products)):
     compoundDecipher(products[i],i+len(reagents),-1)
elementMatrix = Matrix(elementMatrix) 
elementMatrix = elementMatrix.transpose()
solution = elementMatrix.nullspace()[0]
multiple = lcm([val.q for val in solution])
solution=multiple*solution

print(f"element list:{elementList}")
print(f'element matrix: {elementMatrix}')
print(f'solution: {solution}')
coefficient = solution.tolist()
output=""
for i in range(len(reagents)):
     output += str(coefficient[i][0])+reagents[i]
     if i<len(reagents)-1:
          output+=" + "
output += " -> "
for i in range(len(reagents)):
     output += str(coefficient[i + len(reagents)][0])+products[i]
     if i<len(reagents)-1:
          output+=" + "
print(f'Final balanced equations: {output}')



