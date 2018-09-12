E = float(input('Enter the value of E: '))

A1 = 0.3
A2 = 0.5
A3 = 0.7
A4 = 0.9
k=1
i=0
def fun(p,q,r,t):
	while(p):
		p = p - E*(q+r+t)
		if (p<0):
			p=0
		return p

while (k):
	if(A1>0):
		A1 = fun(A1,A2,A3,A4)
	if(A2>0):
		A2 = fun(A2,A1,A3,A4)
	if(A3>0):
		A3 = fun(A3,A2,A1,A4)
	if(A3>0):
		A4 = fun(A4,A2,A3,A1)
	i+=1
	if(A1+A2+A3==0 or A1+A2+A4==0 or A1+A4+A3==0 or A4+A2+A3==0):
		k=0
		print("A1 =", A1, ",A2 =", A2, ",A3 =", A3, ",A4 =", A4, "obtained at",i, "th iteration.")
		