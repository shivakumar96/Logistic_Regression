import csv


#method to read from the csv file
def getData( reader, labels ) :
	x = []
	y = []
	for row in reader :
		strXj = row[1:len(row)-1]
		Xj = [float(1)]
		for element in strXj :
			Xj.append(float(element))
		x.append(Xj)
		#index of label in the list is itself used as label value
		y.append(labels.index(row[len(row)-1]))	

	return x,y ; #end of method retirurning attributes and class value as a list







#labels
label1 = "setosa" 
label2 = "virginica"
label3 = "versicolor"
#------ end of labels 

#labels list 
labelist = [label1,label2,label3]

#open csv file
trainfile  = open("iris.csv","r") 
testfile = open("test.csv")

#csv reader to read data
trainreader = csv.reader(trainfile,delimiter=',')
testreader = csv.reader(testfile,delimiter=',')

#store train data
X,Y = getData(trainreader,labelist)

#store the  test data 
testX,testY = getData(testreader,labelist)

testfile.close()
trainfile.close()

