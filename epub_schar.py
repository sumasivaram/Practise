import shutil
import os
import zipfile
#copy the epub file in the same repository
os.chdir('E:\\Suma')
shutil.copy('9780545628396.epub','E:\\Suma\\9780545628396-Copy.epub')
#rename with zip extension
os.rename('9780545628396-Copy.epub','9780545628396.zip')
#extracting the zip file
with zipfile.ZipFile("9780545628396.zip","r") as zip_ref:
    zip_ref.extractall("E:\\Suma\\9780545628396")
result = ""
words = []
with open("E:\\Suma\\NamedEntity.txt") as fobj:
   file_data = fobj.read()
   words = file_data.split('|')
   #print words
   

#reading the all fles 
for word in words:
   #print type(word)
   for root, dirs, files in os.walk('E:\\Suma\\9780545628396\\OEBPS'):
      for filename in files:
         extention = ['.html','.xhtml','.css','.opf','.ncx','.xpgt']
         fname,file_extention = os.path.splitext(filename)
         if file_extention  in extention:
            with open(os.path.join(root, filename), "r") as fileobj:
            
               lines = fileobj.readlines()
               for line in lines:
                  #print type(line)
                  if word in line:
                     #print type(word)
                     result += filename+'\n'+word+'\n'
                     #print result
                      #print word  
                     
                  
print result
with open("E:\\Suma\\output.txt","w+") as fobj2:
   fobj2.write(result)




