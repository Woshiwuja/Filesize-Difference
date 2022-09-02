import sys
import os

def get_size(fileobject):
    size = os.fstat(fileobject.fileno()).st_size
    return size

def bytesize_diff(size_a,size_b):

    if(size_a/1073741824>=1 or size_b/1073741824>=1):
        a_converted = round((size_a/1073741824),2)
        b_converted = round((size_b/1073741824),2)
        size_diff = round((a_converted - b_converted),2)
        if (size_diff < 0):
            size_diff = size_diff*(-1)
        return size_diff,'GB',a_converted,b_converted

    elif(size_a/1048576>=1 or size_b/1048576>=1):
        a_converted = round((size_a/1048576),2)
        b_converted = round((size_b/1048576),2)
        size_diff = round((a_converted - b_converted),2)
        if (size_diff < 0):
            size_diff = size_diff*(-1)
        return size_diff,'MB',a_converted,b_converted

    elif(size_a/1024>=1 or size_b/1024>=1):
        a_converted = round((size_a/1024),2)
        b_converted = round((size_b/1024),2)
        size_diff = round((a_converted - b_converted),2)
        if (size_diff < 0):
            size_diff = size_diff*(-1)
        return size_diff,'kB',a_converted,b_converted

    else:
        size_diff = size_a - size_b
        a_converted = size_a
        b_converted = size_b
        if (size_diff < 0):
            size_diff = size_diff*(-1)
        return size_diff,'B',a_converted,b_converted
    
with open(sys.argv[1], 'r') as a, open(sys.argv[2], 'r') as b:
    a_size = get_size(a)
    b_size = get_size(b)
    unit = bytesize_diff(a_size,b_size)[1]
    a_converted = bytesize_diff(a_size,b_size)[2]
    b_converted = bytesize_diff(a_size,b_size)[3]
    diff_size = bytesize_diff(a_size,b_size)[0]
    a_file_name = os.path.basename(a.name)
    b_file_name = os.path.basename(b.name) 
    print(a_file_name,"size:",a_converted,unit)
    print(b_file_name,"size:",b_converted,unit)
    print("size difference:",diff_size,unit)
