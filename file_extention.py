import os
fobj = open("E:\Font\MAC_and_PC_Font_List.txt")
data = fobj.readlines()
print data
fobj.close()
output = []
extention = ['.otf','.ttf','.pfm','.pfb','.afm','.afb','.scr','.bmp','.woff','.eot','.fnt']
for line in data:
    filename,file_extention = os.path.splitext(line)
    if file_extention not in extention:
        output.append(line)

fobj2 = open("E:\Font\extent_out.txt","w+")
fobj2.write("\n".join(output))
fobj2.close()
    
