import glob
import csv
import numpy as np
import matplotlib.pyplot as plt
import os
import re
import subprocess
clusters = []
full_clusters = []
option = ''
clusterName = ''
def main():
	global dictionary, clusters, full_clusters, clusterName, option
	allBenchmarksDictionary = dict()
	full_path = raw_input("Please provide full path where files should be retrieved from: ")
	option = raw_input("Choose mean, median, lowest, highest: ")
	lastLines = getLastLines(full_path)
	clusters = getClusterNames(lastLines)
	dictionary = getBenchmarksDictionary(lastLines)
	cluster_names = list(set(clusters))
	full_clusters = getFullClusterNames(lastLines)
	if(option == "mean"):
		for i in range(len(cluster_names)):
			clusterName = cluster_names[i]
			allBenchmarksDictionary = {}
			for cluster in full_clusters:
				if(clusterName == remove_number(cluster)):
					allBenchmarksDictionary[cluster] = find_mean(cluster)
			writeCSV(allBenchmarksDictionary)
			proc=subprocess.Popen(["Rscript", "/home/mbax2nk2/nursultan/Library/rank_generate_heatmap(Scimark).R","../Graphs/"+clusterName+"/", option+"_scimark.csv", option+"_scimark.png", option])
			proc.communicate()
	if(option == "lowest"):
		for i in range(len(cluster_names)):
			clusterName = cluster_names[i]
			allBenchmarksDictionary = {}
			for cluster in full_clusters:
				if(clusterName == remove_number(cluster)):
					allBenchmarksDictionary[cluster] = find_lowest_value(cluster)
			writeCSV(allBenchmarksDictionary)
			proc=subprocess.Popen(["Rscript", "/home/mbax2nk2/nursultan/Library/rank_generate_heatmap(Scimark).R","../Graphs/"+clusterName+"/", option+"_scimark.csv", option+"_scimark.png", option])
			proc.communicate()
	if(option == "highest"):
		for i in range(len(cluster_names)):
			clusterName = cluster_names[i]
			allBenchmarksDictionary = {}
			for cluster in full_clusters:
				if(clusterName == remove_number(cluster)):
					allBenchmarksDictionary[cluster] = find_highest_value(cluster)
			writeCSV(allBenchmarksDictionary)
			proc=subprocess.Popen(["Rscript", "/home/mbax2nk2/nursultan/Library/rank_generate_heatmap(Scimark).R","../Graphs/"+clusterName+"/", option+"_scimark.csv", option+"_scimark.png", option])
			proc.communicate()
	if(option == "median"):
		for i in range(len(cluster_names)):
			clusterName = cluster_names[i]
			allBenchmarksDictionary = {}
			for cluster in full_clusters:
				if(clusterName == remove_number(cluster)):
					allBenchmarksDictionary[cluster] = find_median_value(cluster)
			writeCSV(allBenchmarksDictionary)
			proc=subprocess.Popen(["Rscript", "/home/mbax2nk2/nursultan/Library/rank_generate_heatmap(Scimark).R","../Graphs/"+clusterName+"/", option+"_scimark.csv", option+"_scimark.png", option])
			proc.communicate()
def getClusterNames(arr):
	for row in arr:
		s = re.sub('\d', '', row[1])
		d = re.sub('-', '', s)
		clusters.append(d)
	return clusters
def remove_number(str1):
	s = re.sub('\d', '', str1)
	d = re.sub('-', '', s)
	return d
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
				if(len(row) == 284):
					array.append(row)
	return array
def writeCSV(allBenchmarksDictionary):
	global option, clusterName
	benchmarkNames = []
	directory ="../Graphs/"+clusterName
	keyList = allBenchmarksDictionary[allBenchmarksDictionary.keys()[0]].keys()
	keyList.sort()
	if not os.path.exists(directory):
    		os.makedirs(directory)
	for key in keyList:
		benchmarkNames.append(key)

   	file1 = directory+"/"+option+"_scimark.csv"
   	print file1
	w = csv.writer(open(file1, "w+"))
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
def getFullClusterNames(arr):
	full_clusters = []
	for row in arr:
		full_clusters.append(row[1])
	return full_clusters
def find_mean(cluster):
	global dictionary, full_clusters
	dict1 = dict()
	arr = []
	for i in range(len(full_clusters)):
		if(full_clusters[i] == cluster):
			arr.append(i)
	for key, value in dictionary.iteritems():
		arr1 = []
		for i in range(len(arr)):
			arr1.append(value[arr[i]])
		dict1[key] = np.mean(arr1)
	return dict1
def find_highest_value(cluster):
	global dictionary, full_clusters
	dict1 = dict()
	arr = []
	for i in range(len(full_clusters)):
		if(full_clusters[i] == cluster):
			arr.append(i)
	for key, value in dictionary.iteritems():
		arr1 = []
		for i in range(len(arr)):
			arr1.append(value[arr[i]])
		dict1[key] = np.amax(arr1)
	return dict1
def find_lowest_value(cluster):
	global dictionary, full_clusters
	dict1 = dict()
	arr = []
	for i in range(len(full_clusters)):
		if(full_clusters[i] == cluster):
			arr.append(i)
	for key, value in dictionary.iteritems():
		arr1 = []
		for i in range(len(arr)):
			arr1.append(value[arr[i]])
		dict1[key] = np.amin(arr1)
	return dict1
def find_median_value(cluster):
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
		dict1[key] = np.median(arr1)
	return dict1
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
main()
