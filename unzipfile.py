from zipfile import ZipFile	
f=ZipFile('fileszip.zip','r')
names=f.namelist()
for name in names:
	print('File Name:',name)
	print('The Content of this file is:')
	f1=open(name,'r')
	print(f1.read())
	print('*'*10)
