import glob
import csv
import numpy as np
import matplotlib.pyplot as plt
import re
import scipy.stats as ss
import subprocess
import math
clusters = []
dictionary = dict()
benchmarkNames = []
option = ''
def main():
	global option, dictionary, clusters, benchmarkNames
	allBenchmarksDictionary = dict()
	full_path = raw_input("Please provide full path where files should be retrieved from: ")
	option = raw_input('Please choose mean, median, lowest or highest value: ')
	lastLines = getLastLines(full_path)
	dictionary = getBenchmarksDictionary(lastLines)
	clusters = getClusterNames(lastLines)
	if option == "mean":
		for cluster in clusters:
			allBenchmarksDictionary[cluster] = find_mean(cluster)
	elif option == "lowest":
		for cluster in clusters:
			allBenchmarksDictionary[cluster] = find_lowest_value(cluster)
	elif option == "highest":
		for cluster in clusters:
			allBenchmarksDictionary[cluster] = find_highest_value(cluster)
	elif option == "median":
		for cluster in clusters:
			allBenchmarksDictionary[cluster] = find_median_value(cluster)

	#keyList = allBenchmarksDictionary[allBenchmarksDictionary.keys()[0]].keys()
	#keyList.sort()
	#for key in keyList:
		#	benchmarkNames.append(key)
	plot_result(allBenchmarksDictionary)
	#writeCSV(allBenchmarksDictionary)
	#proc=subprocess.Popen(["Rscript", "/home/mbax2nk2/nursultan/Library/rank_generate_heatmap(Scimark).R","../Graphs/", option+"_scimark.csv", option+"_scimark.png", option])
	#proc.communicate()
def writeCSV(allBenchmarksDictionary):
	global benchmarkNames, option
	w = csv.writer(open("../Graphs/"+option+"_scimark.csv", "w"))
	w.writerow(["name"]+benchmarkNames)
	keyList = allBenchmarksDictionary.keys()
	keyList.sort()
	for key in keyList:
		arr = []
		keyList1 = allBenchmarksDictionary[key].keys()
		dict1 = allBenchmarksDictionary[key]
		keyList1.sort()
		for key1 in keyList1:
			arr.append(dict1[key1])
		w.writerow([key]+arr)
def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)
def plot_result(allBenchmarksDictionary):
	arr = []
	for key,value in allBenchmarksDictionary.iteritems():
		arr.append(np.asarray(value))
		bp = plt.boxplot(arr)
	index = np.arange(len(allBenchmarksDictionary.keys()))
	bar_width = 1
	plt.xlabel('Cluster Name')
	plt.ylabel('Operation per Minute')
	plt.title('Scimakr.Large')
	plt.xticks(index+bar_width, allBenchmarksDictionary.keys(),rotation='vertical')
	plt.legend()
	plt.tight_layout()
	plt.show()
def find_mean(cluster):
	global dictionary, clusters
	dict1 = dict()
	arr = []
	for i in range(len(clusters)):
		if(clusters[i] == cluster):
			arr.append(i)
	for key, value in dictionary.iteritems():
		arr1 = []
		for i in range(len(arr)):
			arr1.append(value[arr[i]])
		normalised = arr1 / np.linalg.norm(arr1)
		dict1[key] = np.mean(arr1)
	return dict1
def find_highest_value(cluster):
	global dictionary, clusters
	dict1 = dict()
	arr = []
	# get corresponding indexes of clusters
	for i in range(len(clusters)):
		if(clusters[i] == cluster):
			# array index of appropriate cluster
			arr.append(i)
	for key, value in dictionary.iteritems():
		arr1 = []
		for i in range(len(arr)):
			arr1.append(value[arr[i]])
		dict1[key] = np.amax(arr1)
	return dict1
def find_lowest_value(cluster):
	global dictionary, clusters
	dict1 = dict()
	arr = []
	for i in range(len(clusters)):
		if(clusters[i] == cluster):
			arr.append(i)
	for key, value in dictionary.iteritems():
		arr1 = []
		for i in range(len(arr)):
			arr1.append(value[arr[i]])
		dict1[key] = np.amin(arr1)
	return dict1
def getLastLines(full_path):
	files = glob.glob(full_path+"/run*.csv")
	array = []
	for file in files:
		f = open(file)
		csv_f = csv.reader(f)
		for row in csv_f:
			if(row[0] == "##-nursultan-##"):
				if(len(row) == 284):
					array.append(row)
	return array
def find_median_value(cluster):
	global dictionary, clusters
	dict1 = dict()
	arr = []
	res = []
	for i in range(len(clusters)):
		if(clusters[i] == cluster):
			arr.append(i)

	for i in range(len(arr)):
		arr1 = []
		for key, value in dictionary.iteritems():
			if "scimark" in key:
				if "small" not in key:
					arr1.append(value[arr[i]])
		mul = reduce(lambda x, y: x*y, arr1)
		res.append(math.pow(mul, 0.2))
	return res
def getBenchmarksDictionary(lastLine):
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
	dictionary = {'scimark.monte_carlo' : scimarkMonteCarlo,'scimark.fft.large' : scimarkFFT, 'scimark.lu.large' : scimarkLuLarge, 'scimark.sor.large' : scimarkSorLarge, 'scimark.sparse.large' : scimarkSparseLarge,'sunflow' : sunflow}
	return dictionary
def getBenchmarkNames(dict1):
	benchmarks = []
	for key, value in dict1.iteritems():
		benchmarks.append(key)
	return benchmarks

def getClusterNames(arr):
	for row in arr:
		s = re.sub('\d', '', row[1])
		d = re.sub('-', '', s)
		clusters.append(d)
	return clusters

main()
