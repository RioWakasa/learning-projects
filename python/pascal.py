def c(n,k): 
  if(k<=0 or n==k):
  	return 1
  else:
  	return(c(n-1, k-1) + c(n-1, k))

N=int(input())

for i in range(N):
  print([c(i,j) for j in range(i+1)])