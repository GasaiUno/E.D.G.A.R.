def Bubble(s):
   print("Исходный массив:")
   print(s)
   for i in range (0,n):
       for k in range (0,n-i-1):
           if s[k]>s[k+1]:
              b=s[k]
              s[k]=s[k+1]
              s[k+1]=b
   print("Отсортированный массив:")
   print(s)
   return s
n=int(input())
f=[]
for i in range(0,n):
      f.append(int(input()))
Bubble(f)
