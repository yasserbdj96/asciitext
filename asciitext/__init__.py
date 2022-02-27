#!/usr/bin/env python
# coding:utf-8
#code by:YasserBDJ96
#email:yasser.bdj96@gmail.com

#START{
import sys
import os.path
from os import path
from hexor import hexor
import requests

#start ascii class:
class ascii:
    #asciitext:
    def asciitext(font_file,text,f_color="#ffffff",bg_color="",color_type="hex"):
        ass=[]
        #if url:
        if "http://" in font_file or "https://" in font_file:
            content=[]
            response=requests.get(font_file)
            data=response.text
            for i, line in enumerate(data.split('\n')):
                content.append(f'{line}'.replace("\r","\n"))
        #if path:
        else:
            # open the sample file used:
            with open(font_file,'r', encoding="utf-8") as file:
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
    
        p1=hexor(True,color_type)
        return p1.c(q[0:len(q)-1],f_color,bg_color)
#}END.