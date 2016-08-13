# this program plots cluster nodes performance for specific benchmark
import glob
import csv
import numpy as np
import matplotlib.pyplot as plt

import re
# array to hold clusters name without numbers or dashes, each value in this array will be key to find correct values from array
clusters = []
# array to hold clusters name with numbers and dashes
full_clusters =[]
# dictionary to hold all benchmark result from every files
benchmarkDictionary = dict()
# benchmark names
benchmarkNames = []
def main():
	global clusters, full_clusters, benchmarkDictionary, benchmarkNames
	# provide full path of the directory where files should be retrieved from
	full_path = raw_input("Please provide full path where files should be retrieved from: ")
	# get only last lines of all files
	lastLines = getLastLines(full_path)
	# get benchmark names
	benchmarkNames = getBenchmarkNames(lastLines[0])
	# get full clusternames
	full_clusters = getFullClusterNames(lastLines)
	# get cluster names without numbers or dashes
	clusters = getClusterNames(lastLines)
	# get bechmark dictionary
	benchmarkDictionary = getBenchmarkDictionary(lastLines)
	# print out which option corresponds to which benchmark
	for i in range(len(benchmarkNames)):
		print "%d %s"%(i, benchmarkNames[i])
	# provide selection
	should_run = True
	option = input("Please choose benchmark name: ")
	plot_cluster_computers(option)
def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)
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
		s = re.sub('\d', '', row[1])
		d = re.sub('-', '', s)
		clusters.append(d)
	return clusters
def getFullClusterNames(arr):
	for row in arr:
		full_clusters.append(row[1])
	return full_clusters
def remove_number(str1):
	removed_number = re.sub('\d', '', str1)
	removed_dashes = re.sub('-', '', removed_number)
	return removed_dashes
def plot_cluster_computers(option):
	global full_clusters, benchmarkDictionary, clusters, benchmarkNames
	# dictionary to hold results for every cluster nodes
	clusterDictionary = dict()
	# get selected benchmrak from dictionary
	benchmark = benchmarkDictionary.get(option)
	# get unique clusters to select
	cluster_names = list(set(clusters))
	for i in range(len(cluster_names)):
		print "%d %s"%(i, cluster_names[i])
	# select cluster name from unique cluster set
	clusterName = cluster_names[input('Please choose cluster ')]
	# the length of clusters
	count = len(full_clusters)
	for i in range(count):
		# get next cluster name without number and dashes
		name = remove_number(full_clusters[i])
		# if cluster node in selected cluster
		if name == clusterName:
			# get full name of the cluster node
			cluster = full_clusters[i]
			# if cluster node exist in dictionary
			if cluster in clusterDictionary:
				arr = []
				arr = clusterDictionary.get(cluster)
				arr.append(benchmark[i])
				clusterDictionary[cluster] = arr
			# otherwise
			else:
				arr = []
				arr.append(benchmark[i])
				clusterDictionary[cluster] = arr
	arr = []
	# append all results to one array
	for key,value in clusterDictionary.iteritems():
		arr.append(np.asarray(value))
		bp = plt.boxplot(arr)
	index = np.arange(len(clusterDictionary.keys()))
	plt.style.use('ggplot')
	# padding of the x axis labels
	if(len(clusterDictionary.keys()) == 111):
		bar_width = 1.25
	bar_width = 1
	plt.xlabel('Cluster Name')
	plt.ylabel('Operation per Minute')
	plt.title(benchmarkNames[option])
	plt.xticks(index+bar_width, clusterDictionary.keys(),rotation='vertical')
	plt.tick_params(direction='out', pad=5)
	plt.legend()
	plt.tight_layout()
	plt.show()
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
main()
