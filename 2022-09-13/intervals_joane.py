import yogi

a1=yogi.read(int)
b1=yogi.read(int)
a2=yogi.read(int)
b2=yogi.read(int)

if a2>b1 or a1>b2:
    print('[]')

elif a1<=a2:
	if b2>=b1:
		print('[',a2,',',b1,']',sep='')
	else:
		print('[',a2,',',b2,']',sep='')
   
elif a1>=a2:
	if b2<=b1:
		print('[',a1,',',b2,']',sep='')
	else:
		print('[',a1,',',b1,']',sep='')

    