import sys
sys.path.append('fluidity-master')
import vtktools


class vtufile:
	def __init__(self, name):
		"""
		Creates the vtu object for the file name.vtu
		"""
		self.name = name
		self.file = vtktools.vtu(name+'.vtu')
		
		
		
	def getField(self):
		"""
		Returns a tuple containing the values of the tracer at the 			timestamp
		"""
		self.file.GetFieldNames()
		field = self.file.GetScalarField('tracer1')
		return field
		
		
		
	def setField(self, target):
		"""
		Modifies the values of the field in the object (not in 			the .vtu file)
		"""
		self.file.AddScalarField('tracer1', target)
		
	def save_as(self, target_name):
		"""
		Creates the file target_name.vtu containing the updated 			field
		"""
		self.file.Write(target_name+".vtu")
		
		
		
###### Example ######
cube7 = vtufile("cube_disp_PressureMesh")
f = cube7.getField()
print(f)
#cube7.setField(4*f)
#cube7.save_as("cube_disp_PressureMesh_100_checkpoint_bis")
#cube_bis = vtufile("cube_disp_PressureMesh_100_checkpoint_bis")
#print(cube_bis.getField())


		
		

		
	
		
