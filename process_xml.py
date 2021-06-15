import xml.etree.ElementTree as ET

def get_vtu_ref(flml_file):
    """ 
    Returns the name of the pressure mesh vtu file to which the flml given file is referring
    
    WARNING : this includes the ".vtu" extension, and only works in a unique material phase.
    """
    
    tree = ET.parse(flml_file+'.flml')
    root = tree.getroot()

    res = root.find('material_phase').find('scalar_field').find('prognostic').find('initial_condition').find('from_file').get('file_name')

    return res

    

def get_next_name(flml_file, n=1):
    """
    Returns the name of the n-th next created vtu file by running fluidity on the flml_file
    
    WARNING : this includes the ".vtu" extension
    """
    
    
    tree = ET.parse(flml_file+'.flml')
    root = tree.getroot()
    
    base = root.find('simulation_name').find('string_value').text
    
    
    return base+"_"+str(n)+".vtu"




def get_simulation_name(flml_file):
    """
    Returns the root of the name of the vtu files that will be generated from
    this flml_file
    """
    
    tree = ET.parse(flml_file+'.flml')
    root = tree.getroot()
    
    base = root.find('simulation_name').find('string_value').text

    return base
    


def set_vtu_ref(flml_file, new_vtu):
    """
    Changes the name of the mesh vtu file to which the flml_file refers to run the simulation
    
    WARNING : the new_vtu string must include the ".vtu" extension
    """
    tree = ET.parse(flml_file+'.flml')
    root = tree.getroot()
    
    root.find('material_phase').find('scalar_field').find('prognostic').find('initial_condition').find('from_file').set('file_name', new_vtu)
    
    tree.write(flml_file+'.flml')
    
    return