P=48
G=9
print('value of P is:%d'%(P))
print('value of G is:%d'%(G))
a=4
print('the private key a forAlice is:%d'%(a))
x=int(pow(G,a,P))
b=3
print('the private key for DOB is:%d'%(b))
y=int(pow(G,b,P))
ka=int(pow(y,a,P))
kb=int(pow(x,b,P))
print('secret key for the alice is:%d'%(ka))
print('secret key for the DOB is:%d'%(kb))
