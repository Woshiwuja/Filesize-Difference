import sys
import os

def getSize(fileobject):
    size = os.fstat(fileobject.fileno()).st_size
    return size


with open(sys.argv[1], 'r') as a, open(sys.argv[2], 'r') as b:
    a_size = getSize(a)
    b_size = getSize(b)
    if (a_size > b_size or a_size == b_size):
        diff_size = a_size - b_size
        a_file_name = os.path.basename(a.name)
        b_file_name = os.path.basename(b.name)
        print(a_file_name,"size:", a_size)
        print(b_file_name,"size:", b_size)
        print("size difference:",diff_size)
    else:
        diff_size = b_size - a_size
        a_file_name = os.path.basename(a.name)
        b_file_name = os.path.basename(b.name)
        print(a_file_name,"size:", a_size)
        print(b_file_name,"size:", b_size)
        print("size difference:",diff_size)
