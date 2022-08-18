x=input()
y=['a','b']
for i in x:
  if i not in y:
     print('string not valid')
     exit()
p=0
for i in x:
   if p==0:
     if i=='a':
       p=1
     else:
        p=2
   elif p==1:
       if i=='a':
          p=3
       else:
           p=2
   elif p==2:
          if i=='a':
            p=3
          else:
            p=4
   elif p==3:
         if i=='a':
             p=3
         else:
             p=2
   elif p==4:
         if i=='a':
            p=1
         else:
            p=4
if p==4 or p==3:
   print('string accepted')
else:
    print('string not accepted')
