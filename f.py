n=int(input())
t=[]
x=input()
t=x.split()
t.sort()
flag=0
a=int(t[0])
count=-1
for i in range(len(t)):
	count+=1
	if not (int(t[i])==a):
		b=int(t[i])
		flag+=1
		break

temp=count
if(flag==1):
	for i in range(temp,len(t)):
		count+=1
		if not (int(t[i])==b):
			c=int(t[i])
			flag+=1
			break
temp=count
if(flag==2):
	for i in range(temp,len(t)):
		count+=1
		if not (int(t[i])==c):
			flag+=1
			break

if(flag==2):
	if((b-a)==(c-b)):
		print ("YES")
	else:
		print ("NO")
elif(flag==3):
	print ("NO")

elif(flag==1 or flag==0):
	print("YES")









