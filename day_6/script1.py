with open('example.xyz', 'r') as f:
    lines = []
    for line in f:
        lines.append(line)

n_atoms = int(lines[0].strip())
atoms = lines[2:2+n_atoms]

atom3 = atoms[2].strip().split()
atom4 = atoms[3].strip().split()

x3 = float(atom3[1])
y3 = float(atom3[2])
z3 = float(atom3[3])
x4 = float(atom4[1])
y4 = float(atom4[2])
z4 = float(atom4[3])

distance  = ((x3 -x4)**2 + (y3 - y4)**2 + (z3 - z4)**2)**0.5

print(f'distance = {distance}')

