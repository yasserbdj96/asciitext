from asciitext import *
import os

if os.name == 'nt':
    #os.system("Setlocal EnableDelayedExpansion")
    #os.system("chcp 65001 > nul")
    w=True
else:
    w=False

asciitext_chars=""#.encode("utf-8")
br="\n"#.encode("utf-8")

try:
    import os
    #
    if "USE" in os.environ and os.environ['USE']=="True":
        font = os.environ['FONT'] if "FONT" in os.environ else "fonts/ANSI_Shadow.txt"
        text = os.environ['TEXT'] if "TEXT" in os.environ else "#asciitext"
        color = os.environ['COLOR'] if "COLOR" in os.environ else "#ff0000"
        color_bg = os.environ['COLOR_BG'] if "COLOR_BG" in os.environ else "#000000"
    
        if color_bg=="#000000":
            asciitext_chars+=asciii.asciitext(font,text,color)+br#.encode("utf-8")+br
        else:
            asciitext_chars+=asciii.asciitext(font,text,color,color_bg)+br#.encode("utf-8")+br
    else:
        #this is error for pass try.
        print(os.environ['X'])
except Exception as e:
    if w==False:
        # Example:1
        asciitext_chars+=asciii.asciitext("fonts/ANSI_Shadow.txt","#asciitext","#ff0000")+br#.encode("utf-8")+br

    # Example:2
    font_url="https://raw.githubusercontent.com/yasserbdj96/asciitext/main/fonts/Calvin_S.txt"
    asciitext_chars+=asciii.asciitext(font_url,"#asciitext","#ff0000")+br#.encode("utf-8")+br

finally:
    print(asciitext_chars)#.decode("utf-8")