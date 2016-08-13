#The program generates a several box plots for bechmarks see(SPECjvm2008) combining results from every clusters available
import glob
import csv
import numpy as np
import matplotlib.pyplot as plt
import re
# array to hold clusters name without numbers or dashes, each value in this array will be key to find correct values from array
clusters = []
# dictionary to hold all benchmark result from every files
benchmarkDictionary = dict()
# benchmark names
benchmarkNames = []
def main():
	global benchmarkDictionary, clusters, full_clusters, benchmarkNames
	full_path = raw_input("Please provide full path where files should be retrieved from: ")
	# traverse all files and retrieve only line which starts with ##-nursultan-##
	lastLines = getLastLines(full_path)
	# benchmark names retrieved from array
	benchmarkNames = getBenchmarkNames(lastLines[0])
	# cluster names without numbers or dashes
	clusters = getClusterNames(lastLines)
	# get all becnhmark results
	benchmarkDictionary = getBenchmarkDictionary(lastLines)
	# print out possible options to choose
	for i in range(len(benchmarkNames)):
		print "%d %s"%(i, benchmarkNames[i])
	option = input("Please choose benchmark name: ")
	plot_clusters(option)
def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)
# get last lines of every file provided
def getLastLines(full_path):
	files = glob.glob(full_path+"/run*.csv")
	array = []
	for file in files:
		f = open(file)
		csv_f = csv.reader(f)
		for row in csv_f:
			if(row[0] == "##-nursultan-##"):
				# if length of row is not equal dismiss this file, because with all counted values the size should be exactly 284
				if(len(row) == 284):
					array.append(row)
	return array
def getBenchmarkNames(arr):
	benchmarks = []
	for row in range(len(arr)):
		if(hasNumbers(arr[row]) == False and arr[row] != "##-nursultan-##" and arr[row] != "n/a"):
			benchmarks.append(arr[row])
	return benchmarks
def getClusterNames(arr):
	for row in arr:
		removedDashesAndNumbers = remove_number_dashes(row[1])
		clusters.append(removedDashesAndNumbers)
	return clusters
def plot_clusters(option):
	global benchmarkDictionary, clusters, benchmarkNames
	# append results to appropriate cluster
	clusterDictionary = dict()
	# get selected benchmark from dictionary
	benchmark = benchmarkDictionary.get(option)
	# the number of clusters
	count  = len(clusters)
	for i in range(count):
		name = clusters[i]
		# if cluster name exist in the dictionary
		if name in clusterDictionary:
			arr = []
			arr = clusterDictionary.get(name)
			arr.append(benchmark[i])
			clusterDictionary[name] = arr
		# if not
		else:
			arr = []
			arr.append(benchmark[i])
			clusterDictionary[name] = arr
	# array to combine all results to box plot
	arr = []
	# iterate key and value of the cluster dictionary
	for key,value in clusterDictionary.iteritems():
		arr.append(np.asarray(value))
		bp = plt.boxplot(arr)
	index = np.arange(len(clusterDictionary.keys()))
	bar_width = 1
	plt.xlabel('Cluster Name')
	plt.ylabel('Operation per Minute')
	plt.title(benchmarkNames[option])
	plt.xticks(index+bar_width, clusterDictionary.keys(),rotation='vertical')
	plt.legend()
	plt.tight_layout()
	plt.show()
def remove_number_dashes(str):
	removedNumber = re.sub('\d', '', str)
	removedDashes = re.sub('-', '', removedNumber)
	return removedDashes
# returns dictionary of all benchmark results e.g. key 1 will return array of all results in startup.helloworld bechmark
def getBenchmarkDictionary(lastLine):
	check = np.array([i[9] for i in lastLine]).astype(np.float)
	startupHelloWorld = np.array([i[14] for i in lastLine]).astype(np.float)
	startupCompilerCompiler = np.array([i[19] for i in lastLine]).astype(np.float)
	startupCompilerSunflow = np.array([i[24] for i in lastLine]).astype(np.float)
	startupCompress = np.array([i[29] for i in lastLine]).astype(np.float)
	startupCryptoAes = np.array([i[34] for i in lastLine]).astype(np.float)
	startupCryptoRsa = np.array([i[39] for i in lastLine]).astype(np.float)
	startupCryptoSignverify = np.array([i[44] for i in lastLine]).astype(np.float)
	startupMpegaudio = np.array([i[49] for i in lastLine]).astype(np.float)
	startupScimarkFFT = np.array([i[54] for i in lastLine]).astype(np.float)
	startupScimarkLu = np.array([i[59] for i in lastLine]).astype(np.float)
	startupScimarkMonteCarlo = np.array([i[64] for i in lastLine]).astype(np.float)
	startupScimarkSor = np.array([i[69] for i in lastLine]).astype(np.float)
	startupScimarkSparse = np.array([i[74] for i in lastLine]).astype(np.float)
	startupSerial = np.array([i[79] for i in lastLine]).astype(np.float)
	startupSunflow = np.array([i[84] for i in lastLine]).astype(np.float)
	startupXmlTransform = np.array([i[89] for i in lastLine]).astype(np.float)
	startupXmlValidation = np.array([i[94] for i in lastLine]).astype(np.float)
	compilerCompiler = np.array([i[103] for i in lastLine]).astype(np.float)
	compilerSunflow = np.array([i[112] for i in lastLine]).astype(np.float)
	compress = np.array([i[121] for i in lastLine]).astype(np.float)
	cryptoAes = np.array([i[130] for i in lastLine]).astype(np.float)
	cryptoRsa = np.array([i[139] for i in lastLine]).astype(np.float)
	cryptoSignverify= np.array([i[148] for i in lastLine]).astype(np.float)
	derby = np.array([i[157] for i in lastLine]).astype(np.float)
	mpegaudio = np.array([i[166] for i in lastLine]).astype(np.float)
	scimarkFFT = np.array([i[175] for i in lastLine]).astype(np.float)
	scimarkLuLarge = np.array([i[184] for i in lastLine]).astype(np.float)
	scimarkSorLarge = np.array([i[193] for i in lastLine]).astype(np.float)
	scimarkSparseLarge = np.array([i[202] for i in lastLine]).astype(np.float)
	scimarkFFtSmall = np.array([i[211] for i in lastLine]).astype(np.float)
	scimarkLuSmall = np.array([i[220] for i in lastLine]).astype(np.float)
	scimarkSorSmall = np.array([i[229] for i in lastLine]).astype(np.float)
	scimarkSparseSmall = np.array([i[238] for i in lastLine]).astype(np.float)
	scimarkMonteCarlo = np.array([i[247] for i in lastLine]).astype(np.float)
	serial = np.array([i[256] for i in lastLine]).astype(np.float)
	sunflow = np.array([i[265] for i in lastLine]).astype(np.float)
	xmlTransform = np.array([i[274] for i in lastLine]).astype(np.float)
	xmlValidation = np.array([i[283] for i in lastLine]).astype(np.float)
	dictionary = {0 : check, 1 : startupHelloWorld, 2 : startupCompilerCompiler, 3 : startupCompilerSunflow, 4 : startupCompress, 5 : startupCryptoAes, 6 : startupCryptoRsa, 7 : startupCryptoSignverify, 8 : startupMpegaudio, 9 : startupScimarkFFT, 10 : startupScimarkLu, 11 : startupScimarkMonteCarlo, 12 : startupScimarkSor, 13 : startupScimarkSparse, 14 : startupSerial, 15 : startupSunflow, 16 : startupXmlTransform, 17 : startupXmlValidation, 18 : compilerCompiler, 19 : compilerSunflow, 20 : compress, 21 : cryptoAes, 22 : cryptoRsa, 23 : cryptoSignverify, 24 : derby, 25 : mpegaudio, 26 : scimarkFFT, 27 : scimarkLuLarge, 28 : scimarkSorLarge, 29 : scimarkSparseLarge, 30 : scimarkFFtSmall, 31 : scimarkLuSmall, 32 : scimarkSorSmall, 33 : scimarkSparseSmall, 34 : scimarkMonteCarlo, 35 : serial, 36 : sunflow, 37 : xmlTransform, 38 : xmlValidation}
	return dictionary
# start the program execution
main()
