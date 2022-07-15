# immutabe:str, tuple, bytes # immutable means modifications cannot change 
# mutable:list,                # mutable means modifications change
# a=[]
# print(a,type(a))  #class list
# a=['goutham',77]
# print(a,type(a))
# print(a[0],type(a[0]))  #str
# a=7
# print(a,type(a))
# a=[7]
# print(a,type(a)) # class list
# b=['ameerpet',55]
# print(b,type(b))   # class list
# print(b[0],type(b[0]))   # class str
# print(b[1],type(b[1]))      # class int
# a='none'
# print(type(a))   #str
# a=None
# print(type(a))   # none type
# b=[2,7.9,'hi',None,True]
# print(b[0],type(b[0]))   #  class int
# print(b[1],type(b[1]))   # class  float
# print(b[2],type(b[2]))   # class  str 
# print(b[3],type(b[3]))   #  class none type
# print(b[4],type(b[4]))   #  class bool
# print(b[5],type(b[5]))     # IndexError: list index out of range
# a=['hi']
# print(a[0])   # h
# print(a[1])     # i
# print(a[2])    #Idexerror: sting index out of range
# print(a[2])      #Indexerror: list index out of range
'''Note:modifications cannot be made inside thw string data type'''
# c='hello'
# c[0]='H'   # str object does not support item assignment
'''Note: List will allow the modifications'''
# d=[4,3,1,'python']
# d[0]=89.23
# d[-1]='GT'
# print(d)
# e=[1,3.7,'hello',[10,11]]
# print(e,type(e))           # class list
# print(e[0],type(e[0]))       # class int
# print(e[1],type(e[1]))       # class float
# print(e[2],type(e[2]))       # class str
# print(e[3],type(e[3]))       # class list
# print(e[6],type(e[6]))         # Indexerror: list index out of range
# print(e[3][0],type(e[3][0]))    #class int 10       
# print(e[3][1],type(e[3][1]))    #class int 11
# e=[1,3.7,'hello',[10,11]]
# e[0]=24
# e[3][0]=50
# print(e,type(e))
'''append method of list will add the element at the end of the list'''
# e=[1,3.7,'hello',[10,11]]
# e.append('josh','ravi')
# print(e)        #append() takes exactly one argument (2 given)
# e=[1,3.7,'hello',[10,11]]
# e.clear()
# print(e)           #[]  list
# d=[5,10,'hello',10,'']
# print(d.count(''))
# print(d.count(6))
# print(d.count(10))
# print(d.count('hello'))
# a=[5,10,15]
# b=[1,3,5,7]
# # a.extend(b)
# # print(a)
# b.extend(a)
# print(b)
# n='hello'
# print(n.index(y))  y# y name is not defined
n=[2,4,6,8,'hello',4.5,[56]]
# print(n.index(14.5))                  #valueerror: 14.5 is not in list
# print(n.index(8))     # 3
# print(n.index(4.5))   #  5
# print(n.index([56]))    #   6
# print(n.index([2]))
# print(dir(list))