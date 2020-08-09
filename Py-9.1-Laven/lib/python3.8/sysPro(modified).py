# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 01:38:14 2020
@author: KL
"""
import os
import csv

directory = input ( "Enter the directory name:" )
newpath = os.path.join ( "/Users/ladylaven/Desktop/sysPro(modified).py", directory )
""
print ( newpath )
if (os.path.exists ( newpath ) == True):
    print ( "The directory exists." )
    filename = input ( "Enter the file name:" )
    newpath = os.path.join ( newpath, filename )
    print ( newpath )
    name = input ( "Enter the user's name:" )
    address = input ( "Enter the user's address:" )
    phone = input ( "Enter the user's phone number:" )
    with open ( newpath, mode='w', newline='' ) as fn:
        fn_writer = csv.writer ( fn, delimiter=',' )
        fn_writer.writerow ( [name, address, phone] )

    fn.close ()
    with open ( newpath, mode='r' ) as fr:
        csv_reader = csv.reader ( fr )
        for row in csv_reader:
            for item in row:
                print ( item )

else:
    print ( "No such directory was in existence" )
    newpath = os.path.join ( "D:\\", directory )
    os.mkdir ( newpath )
    print ( "Now", directory, " has been created." )
    print ( newpath )
    filename = input ( "Enter the file name:" )
    newpath = os.path.join ( newpath, filename )
    print ( newpath )
    name = input ( "Enter the user's name:" )
    address = input ( "Enter the user's address:" )
    phone = input ( "Enter the user's phone number:" )
    with open ( newpath, mode='w', newline='' ) as fn:
        fn_writer = csv.writer ( fn, delimiter=',' )
        fn_writer.writerow ( [name, address, phone] )
    fn.close ()
    with open ( newpath, mode='r' ) as fr:
        csv_reader = csv.reader ( fr )
        for row in csv_reader:
            for item in row:
                print ( item )
print ( "Program ends here" )