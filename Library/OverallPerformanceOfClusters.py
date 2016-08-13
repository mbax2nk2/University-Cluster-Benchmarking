# This program generates overall boxplot for benchmarks 
import glob
import csv
import numpy as np
import matplotlib.pyplot as plt
def main():
	full_path = raw_input("Please provide full path where files should be retrieved from: ")
	# get last lines of all files
	lastLines = getLastLines(full_path)
	# dictionary contatining all results of benchmarks
	benchmarkDictionary = getBenchmarkDictionary(lastLines)
	# get benchmark names
	benchmarkNames = getBenchmarkNames(lastLines[0])
	# plot graph
	plot_graph(benchmarkDictionary, benchmarkNames)
def plot_graph(benchmarkDictionary, benchmarkNames):
	n_groups = len(benchmarkNames)
	index = np.arange(n_groups)
	bar_width = 1
	plt.xticks(index + bar_width, benchmarkNames,rotation='vertical')
	arr = []
	for key,value in benchmarkDictionary.iteritems():
		arr.append(np.asarray(value))
		bp = plt.boxplot(arr)
	plt.xlabel('Benchmark Name')
	plt.ylabel('Operation per Minute')
	plt.title('Benchmark results')
	plt.xticks(index + bar_width, benchmarkNames,rotation='vertical')
	plt.legend()
	plt.tight_layout()
	plt.show()
def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)
def getBenchmarkNames(arr):
	benchmarks = []
	for row in range(len(arr)):
		if(hasNumbers(arr[row]) == False and arr[row] != "##-nursultan-##" and arr[row] !="n/a"):
			benchmarks.append(arr[row])
	return benchmarks
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