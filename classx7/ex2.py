# -*- coding: utf-8 -*-
import os,shutil
cwd = os.getcwd()
print ("current path:",cwd)
filename = "test.txt"
with open(filename,"w") as f:
	f.write("hello world")


files = os.listdir(cwd)
print("include files:",files)

mywd = "mywd"
if os.path.exist(mywd):
	shutil.rmtree(mywd)
os.mkdir(mywd)
filename2 = "test2.txt"
with open(filename2,"w") as g:
	pass

shutil.copy(filename,filename2)

shutil.move(filename2,mywd)

os.chdir(mywd)
print(os.getcwd)


os.remove(filename2)

if os.path.exts(filename2):
	print("file exist")
else:
	print("file delete")
