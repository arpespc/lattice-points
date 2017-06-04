"""
If A1 A2 A3 are the base vectors of unit cell
then R=a1*A1+a2*A2+a3*A3
where R is the any point of fcc bravais lattice,and
A1=x+y   A2=y+z    A3=x+z
So R=(a1+a3 , a1+a2 , a2+a3)
"""
import os
num_a1 = 5                     #Make a1 a2 a3 range from 0 to 5
num_a2 = 5                     #And you can change them
num_a3 = 5
def fixed_len(string, max_length = 10):
    if len(string) <= max_length:
        d_str = max_length - len(string)
        space_list = (d_str + 1) * " "
        string += space_list
        return string
    else:
        print("Too Many Lattice Points!!!")
        return 
a1 = [a for a in range(num_a1)]
a2 = [a for a in range(num_a2)]
a3 = [a for a in range(num_a3)]
ls = []
for i in a1:
    for j in a2:
        for k in a3:
            str1 = str(i+k)
            str2 = str(i+j)
            str3 = str(j+k)
            ls.append(fixed_len(str1) + fixed_len(str2) + fixed_len(str3))
filename = os.path.join('.', 'fcc-lattice.dat')
file_object = open(filename, 'w')
for l in ls:
    file_object.write(l + '\n')
file_object.close()
print("The Job Has Normally Finished!!!")
