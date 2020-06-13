from zipfile import ZipFile
f=ZipFile('fileszip.zip','w')
f.write('file1.txt')
f.write('file2.txt')
f.write('file3.txt')
f.close()
print('fileszip.zip created successfully')