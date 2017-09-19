from datasetGen import labelist,X,Y,testX,testY
from math import e,pow


#retruns a vector of length mentionede in parameter witha all attributes same as specified in the value 
def getVector(length,value) :
	i=0;
	l=[]
	while (i<length):
		l.append(value)
		i+=1
	return l 

#calculate dot product of two vectors thetea[n+1] and x[n+1] whew x[0] = 1 and remaing represnts attributes
def dotProduct(theta,x) :
	sum1 = 0.0
	n = len(x)
	i = 0
	while(i<n) :
		sum1+= theta[i]*x[i]
		i+=1
	return round(sum1,4)

#function to find output of list of two vectors (theta and list of x vectors)
def getAllDotProduct(theta, x) :
	y = []
	i = 0 
	for xi in x :
		y.append(dotProduct(theta,xi))
	return y


#sigmoid function = 1/(1+e^(-value))
def sigmoid(value) :
	return round(1.0/(1.0+pow(e,-1*value)),4)


#hypothesis output function
def hypothesis( theta_function_list ) :
	hypo = []
	for element in theta_function_list :
		hypo.append(sigmoid(element))
	return hypo

# gradient descent function
def gradDesent(x,y) :	
	learningRate = 0.04
        prevtheta = getVector(len(x[0]),-1.0)
        curtheta = getVector(len(x[0]),0.0)
	hy = [] #hypothesis output
	sumlist = []
	count = 0 ;
        while not set(prevtheta) == set(curtheta) and count <10000  :
		count+=1
		sumlist = getVector(len(x[0]),0.0) #length is number of attributes
		prevtheta = [] ; prevtheta.extend(curtheta)
		#print prevtheta
		#print curthet
		hy = hypothesis(getAllDotProduct(prevtheta,x))
		n = len(x)
		m= len(x[0])
		i= 0; j = 0; k = 0
		while j < m :
			sum1 = 0.0; i = 0 
			while i < n :
				sum1 = 0.0 
				sum1+= round((hy[i]-y[i])*x[i][j],4)
				sumlist[j]+=sum1
				i+=1
			j+=1
		k = 0
		for value in prevtheta :
			curtheta[k] = round(value - learningRate*sumlist[k],4)
			k+=1
	print count
	print "prev " , prevtheta
	print "cur" , curtheta
	return curtheta


def generateYvale(ylist, classtype ) :
	i = 0;
	y_modified = [] ;
	while i < len(ylist) :
		if(ylist[i] == classtype ) :
			y_modified.append(float(1))
		else :
			y_modified.append(float(0))
		i+=1

	return y_modified ;



#find the number of class labels 
modifiedYlist = []
for val in range(0,len(labelist)) :
	modifiedYlist.append(generateYvale(Y,val))


#for ecah lable find out a sigmoid function
thetalist = []
for modifiedY in modifiedYlist :
	thetalist.append(gradDesent(X,modifiedY))


#find output of each sigmoid function
testOP = []
for theta in thetalist :
	testOP.append(hypothesis( getAllDotProduct(theta, testX)))


#print the output of each sigmoid function
for m in testOP :
	print m

#ptint the result 
print "\n\n\n"
print "_____________________TEST DATA RESULT________________________\n"

p = 0 
i= 0  
j = 0
while j < len (testOP[0]) :
	i=0
	maxval = -1; indx = -1
	while i<len(testOP) :
		if testOP[i][j] > maxval :
			maxval = testOP[i][j]
			indx = i 
		i+=1
	print "hypothesis output label : ",labelist[indx], " actual label is ",labelist[testY[j]]
	j+=1


print "___________________________________________________________________"




