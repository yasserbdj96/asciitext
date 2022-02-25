#!/usr/bin/env python
# coding:utf-8
#version:0.0.1
#code by:YasserBDJ96
#email:yasser.bdj96@gmail.com

#START{
import sys
import os.path
from os import path
from hexor import hexor

#asciitext:
def asciitext(font_file,text):
    ass=[]
    # open the sample file used:
    file = open(font_file, encoding="utf8")
  
    # read the content of the file opened:
    content = file.readlines()
    
    # last line:
    ascii_text=content[len(content)-1]
    
    text_split=list(text)
    ascii_text_split=list(ascii_text)

    new_text_split=[]
    for g in range(len(text_split)):
        
        not_in_list = text_split[g] not in ascii_text_split
        
        if not_in_list==False:
            new_text_split.append(text_split[g])
            
    text_split=new_text_split
    
    # n:
    n=int(content[len(content)-2].replace("\n",""))
    
    for i in range(len(text_split)):
        pls=int(ascii_text.find(text_split[i]))
        
        xrs=[]
        lls=[]
        if pls>-1:
            for i in range(0,n):
                xrs.append(content[(pls*n)+i].replace("\n",""))
                #lls.append(f"l{i}")
                
            #print(lls)
        ass.append(xrs)
    r=[]
    for y in range(0,n):
        m=[]
        for x in range(len(ass)):
        
            m.append(ass[x][y])
        r.append(m)
        
    f=[]
    for w in range(len(r)):
        l=""
        for z in range(len(r[w])):
            l+=r[w][z]
        f.append(l)
        
    q=""
    for o in range(len(f)):
        q+=f[o]+"\n"
        
    return q[0:len(q)-1]

#
try:
    #check font:
    if path.exists(sys.argv[1]):font_path=sys.argv[1]
    else:print(f"{sys.argv[1]} Not exists!");exit()
    
    #check text:
    if sys.argv[2]!="":text=sys.argv[2]
    else:print("Empty input!");exit()
    
    #check text color:
    try:color=sys.argv[3]
    except:color="#ffffff"
    
    #check background color:
    try:bg=sys.argv[4]
    except:bg=""
    
    #print:
    p1=hexor(False,"hex")
    p1.c(asciitext(font_path,text),color,bg)

#
except:
    print(f"usage: python3 {sys.argv[0]} <FONT_PATH> <TEXT> <TEXT_COLOR> <BACKGROUND_COLOR>")
    exit()
#}END.