import os
fobj = open("E:\Font\MAC_and_PC_Font_List.txt")
data = fobj.readlines()
fobj.close()

file_list = []
output_file = []
for line in data:
    #if os.path.isfile(line):    
     file_name = os.path.basename(line)
     file_list.append(file_name)
    
for f_name in file_list:
    count = file_list.count(f_name) 
    if count > 1:
        output_file.append(f_name)
#print output_file

fobj2 = open("E:\Font\out2.txt","w+")
#print fobj2.read()
for name in output_file:
    fobj2.write(name+":"+"\n")
    fobj2.write("\t"+"\t"+os.path.abspath(name)+"\n") 
fobj2.close()  


output = []
extention = ['.otf','.ttf','.pfm','.pfb','.afm','.afb','.scr','.bmp','.woff','.eot','.fnt']
for line in data:
    filename,file_extention = os.path.splitext(line)
    if file_extention not in extention:
        output.append(line)

fobj3 = open("E:\Font\extent_out.txt","w+")
fobj3.write("\n".join(output))        


        
