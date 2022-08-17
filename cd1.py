x=input()
y=['a','b']
for i in x:
  if i not in y:
     print('string not accepted')
     exit()

p=0

for i in x:
     if p==0:
          if i=='a':
              p=1
          else:
               p=3
     elif p==1:
           if i=='a':
                p=0
           else:
                    p=2
     elif p==2:
           if i=='a':
                p=3
           else:
                  p=1
     elif p==3:
             if i=='a':
                   p=2
             else:
                    p=0
if p==0:
   print('string accepted')
else:
   print('string not accepted')
