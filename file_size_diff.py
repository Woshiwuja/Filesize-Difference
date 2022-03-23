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
        if (a_size/1024<1 or b_size/1024<1):
            print(a_file_name,"size:",a_size,"bytes")
            print(b_file_name,"size:",b_size,"bytes")
            print("size difference:",diff_size,"bytes")

        elif ((a_size/1024)/1024>=1 or (b_size/1024)/1024>=1):
            print(a_file_name,"Size:",round((a_size/1024)/1024, 2),"Megabytes")
            print(b_file_name,"Size:",round((b_size/1024)/1024, 2),"Megabytes")
            print("Size difference:",round((diff_size/1024)/1024,2),"Megabytes")

        elif (a_size/1024>=1 or b_size/1024>=1):
            print(a_file_name,"Size:",round(a_size/1024, 2),"kilobytes")
            print(b_file_name,"Size:",round(b_size/1024, 2),"kilobytes")
            print("Size difference:",round(diff_size/1024,2),"kilobytes")
    else:
        diff_size = b_size - a_size
        a_file_name = os.path.basename(a.name)
        b_file_name = os.path.basename(b.name)
        if (a_size/1024<1 or b_size/1024<1):
            print(a_file_name,"size:",a_size,"bytes")
            print(b_file_name,"size:",b_size,"bytes")
            print("size difference:",diff_size,"bytes")
        elif ((a_size/1024)/1024>=1 or (b_size/1024)/1024>=1):
            print(a_file_name,"Size:",round((a_size/1024)/1024, 2),"Megabytes")
            print(b_file_name,"Size:",round((b_size/1024)/1024, 2),"Megabytes")
            print("Size difference:",round((diff_size/1024)/1024,2),"Megabytes")
        elif (a_size/1024>=1 or b_size/1024>=1):
            print(a_file_name,"Size:",round(a_size/1024, 2),"kilobytes")
            print(b_file_name,"Size:",round(b_size/1024, 2),"kilobytes")
            print("Size difference:",round(diff_size/1024,2),"kilobytes")

