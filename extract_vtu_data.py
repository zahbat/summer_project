from numpy import *
from math  import *
import csv

import sys
sys.path.append("~/VMExt/python/")

import vtk
import vtktools
import fluidity_tools

#from optparse import OptionParser
import argparse


probes = []
def readfile(fileWT):
	with open(fileWT, 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		i = 0
		for row in reader:
			i = i + 1
			probes.append(row)


	return probes

def turb_stats(data, coordinates):
	
	traceravg = "tracer1"
	velavg = "Velocity"
	
	# print "coordinates = ", coordinates
	coordinates = [float(coordinates[0]), float(coordinates[1]), float(coordinates[2])]	
      	
	coord_temp = vtktools.arr([coordinates])
	
	vavg = data.ProbeData(coord_temp, velavg)[0]
	travg = data.ProbeData(coord_temp, traceravg)[0][0]
		
	print("Reading, coordinates = ", coordinates)
    
	return travg, vavg
    
def write_to_file(t, probes, travg, vavg, filename, fileWT):
	
	with open(filename+"_"+fileWT+".csv", 'w') as csvfile:
		writer = csv.writer(csvfile, delimiter = ',')
		
		writer.writerow(['X', 'Y', 'Z', 'Travg', 'Uavg', 'Vavg', 'Wavg'])
		for i in range(len(travg)):
			writer.writerow([probes[i][0], probes[i][1], probes[i][2], str(travg[i]), \
			str(vavg[i][0]), str(vavg[i][1]), str(vavg[i][2])])
		

def main():

	spin_time = 0.0
	nprobe = 20
	velavg = "Velocity_time_average"
	vtu_start = 0

	parser = argparse.ArgumentParser()
	parser.add_argument('-d', '--file', help="Base filename of vtu files", required=True)
	parser.add_argument('-dWT', '--WTfile', help="Filename of WT csv file", required=True)

	args = parser.parse_args()
	
	
	file = args.file
	fileWT = args.WTfile
	
	probes = readfile(fileWT)
	print("probes = ", probes)
	filename=file+".vtu"
		
	data = vtktools.vtu(filename)
	t = data.ProbeData(array([[0.0, 0.0, 0.0]]), 'Time')[0][0]
	"t = ", t
	
	travg = []
	vavg = []
	uuavg = []
	vvavg = []
	wwavg = []
	for coordinates in probes:
		travgi, vavgi  = turb_stats(data, coordinates)
		
		travg.append(travgi)
		vavg.append(vavgi)
			
	write_to_file(t, probes, travg, vavg, filename, fileWT)
	
if __name__ == "__main__":
	main()
