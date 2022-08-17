#!/usr/bin/env python
# coding:utf-8
#   |                                                          |
# --+----------------------------------------------------------+--
#   |   Code by : yasserbdj96                                  |
#   |   Email   : yasser.bdj96@gmail.com                       |
#   |   Github  : https://github.com/yasserbdj96               |
#   |   BTC     : bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9   |
# --+----------------------------------------------------------+--  
#   |        all posts #yasserbdj96 ,all views my own.         |
# --+----------------------------------------------------------+--
#   |                                                          |

#START{
from hexor import hexor
import requests

#start asciii class:
class asciii:
    #asciitext:
    def asciitext(font_file,text,f_color="#ffffff",bg_color=False,color_type="hex"):
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
        for g,x5 in enumerate(text_split):
        #for g in range(len(text_split)):
        
            not_in_list = x5 not in ascii_text_split
        
            if not_in_list==False:
                new_text_split.append(x5)
            
        text_split=new_text_split
    
        # n:
        n=int(content[len(content)-2].replace("\n",""))
        
        for i,x4 in enumerate(text_split):
        #for i in range(len(text_split)):
            pls=int(ascii_text.find(x4))
        
            xrs=[]
            lls=[]
            if pls>-1:
                for i in range(0,n):
                    xrs.append(str(content[(pls*n)+i].replace("\n","")))
            ass.append(xrs)
        r=[]
        for y in range(0,n):
            m=[]
            for x,x3 in enumerate(ass):
            #for x in range(len(ass)):
                m.append(x3[y])
            r.append(m)
        
        f=[]
        for w,x1 in enumerate(r):
        #for w in range(len(r)):
            l=""
            for z,x2 in enumerate(x1):
            #for z in range(len(r[w])):
                l+=x2
            f.append(l)
        
        q=""
        for o,x0 in enumerate(f):
        #for o in range(len(f)):
            q+=x0+"\n"
    
        p1=hexor(True,color_type)

        if bg_color!=False:
            return p1.c(q[0:len(q)-1],f_color,bg_color)
        else:
            return p1.c(q[0:len(q)-1],f_color)
#}END.