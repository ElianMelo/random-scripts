import os
import re

filepath = "G:/folderA/folderB/"
temp = '00';

p = re.compile('(?:i\s)(\d\d)(?:\s-)', re.IGNORECASE)

files = os.listdir(filepath);

for i in range(0, len(files)):
    m = p.findall(files[i])
    if(m):
        os.rename(filepath + files[i], filepath + 'TMP'+ temp + ' ' + 'EP' + m[0] + '.mkv')