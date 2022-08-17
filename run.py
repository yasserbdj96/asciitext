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
from asciitext import *
import sys

try:
    font=sys.argv[1]
    color=sys.argv[2]
    bg=sys.argv[3]
    text=sys.argv[4]

    if bg.upper()=="FALSE":
        print(asciii.asciitext(font,text,color))
    else:
        print(asciii.asciitext(font,text,color,bg))

except:
    print(f"USAGE : python3 {sys.argv[0]} '<FONT_PATH/FONT_URL>' '<COLOR>' '<BACKGROUND/FALSE>' '<TEXT>'")
#}END.