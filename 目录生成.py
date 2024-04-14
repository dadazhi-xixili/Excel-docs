import os
import re
md_list = [x for x in os.listdir() if re.match(r'^(?!00_目录).*\.md$', x)]
title_list=[]
for f in md_list:
    md=open(f,'r',encoding='utf-8').readlines()
    title=[x for x in md if re.match(r'^#',x)]
    md.clear()
    title_list.extend(title)
with open('00_目录.md','w',encoding='utf-8') as f:
    f.write('\n'.join(title_list))