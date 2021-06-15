

import csv
import vtu_class as vtu

csvf = open("out.csv", "w")
writer = csv.writer(csvf)

for i in range(0,323):
    file = vtu.vtufile("cube_disp_"+str(i))
    line = file.getField()
    writer.writerow(line)
    
csvf.close()
