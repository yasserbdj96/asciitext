from asciitext import *

try:
    import os
    #
    if "USE" in os.environ and os.environ['USE']=="True":
        font = os.environ['FONT'] if "FONT" in os.environ else "fonts/ANSI_Shadow.txt"
        text = os.environ['TEXT'] if "TEXT" in os.environ else "#asciitext"
        color = os.environ['COLOR'] if "COLOR" in os.environ else "#ff0000"
        color_bg = os.environ['COLOR_BG'] if "COLOR_BG" in os.environ else "#000000"
    
        if color_bg=="#000000":
            print(asciii.asciitext(font,text,color))
        else:
            print(asciii.asciitext(font,text,color,color_bg))
    else:
        #this is error for pass try.
        print(os.environ['X'])
except:
    # Example:1
    print(asciii.asciitext("fonts/ANSI_Shadow.txt","#asciitext","#ff0000"))


    # Example:2
    font_url="https://raw.githubusercontent.com/yasserbdj96/asciitext/main/fonts/Calvin_S.txt"
    print(asciii.asciitext(font_url,"#asciitext","#ff0000"))
