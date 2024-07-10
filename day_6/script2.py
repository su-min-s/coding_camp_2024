def read_xyz_files(filepath):
    """
    A function that reada a filepath and
    returns a suitable representation of
    a molecule

    Parameters
    ----------
    filepath : str
        A valid filepath in the system
    """

    with open('example.xyz', 'r') as f:
        lines = []
        for line in f:
            lines.append(line)

    n_atoms = int(lines[0].strip())
    molecule = lines[2:2+n_atoms]
    
    return molecule


def substraction(point0, point1):
    """
    It takes in two points and returns
    the element wise substraction of its
    coordinates.
    
    Parameters
    ----------
    point0 : tuple
        a tuple of length 3 where the positions
        correspond respectively to x,y,z
    
    point1 : tuple
        a tuple of length 3 where the positions
        correspond respectively to x,y,z
    Returnes        
    ----------
    filepath : str
    A valid filepath in the system
    
    """
def element_wise_power(value, point):
    pass

def get_distance(point0, point1):

    vector = substraction(point0, point1)
    vector = element_wise_power(2, vector)
    distance  = element_wise_power(0.5, vector)

    return distance

if __name__ == '__main__':
    
    ifile = 'example.xyz'
    atom0_idx = 3
    atom1_idx = 4
    # atom1 = ('C', (0.0, 0.0, 0.0))
    # molecule = a list of atoms
    
    molecule = read_xyz_files(ifile)

    atom0 = molecule[atom0_idx - 1]
    atom1 = molecule[atom1_idx - 1]

    distance = get_distance(atom0[1], atom1[1])
    
    print(f'distance = {distance}')