<p align="center"><img align="center" src="https://raw.githubusercontent.com/yasserbdj96/asciitext/main/screenshot/screenshot_0.png"></p>


<h1>Text to ASCII.</h1>

<p>Text to ASCII Art Generator.</p>

[![Python package](https://github.com/yasserbdj96/asciitext/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/yasserbdj96/asciitext/actions/workflows/python-app.yml)

<h2>Languages:</h2>
* python3

<h2>Requirements</h2>
[✓] hexor
[✓] requests

<h2>Supported Distributions:</h2>

| Distribution | Version Check     | Python Test Version | Supported | Status      | Everything works |
| :----------: | :---------------: | :-----------------: | :-------: | :---------: | :--------------: |
| Ubuntu       | 20.04.3           | 3.6, 3.7, 3.8, 3.9  | Yes       | Working     | Yes              |
| Windwos      | 11.6.4            | 3.6, 3.7, 3.8, 3.9  | Yes       | Not Working | No               |
| MacOS        | 10.0.20348        | 3.6, 3.7, 3.8, 3.9  | Yes       | Working     | Yes              |

<h2>Installation:</h2>

```
pip install asciitext
```

<h2>Usage:</h2>

```python
from asciitext import *

print(ascii.asciitext(<FONT_PATH/URL>,<TEXT>,<TEXT_COLOR>,<BACKGROUND_COLOR>,<COLOR_TYPE>))
```

<h2>Examples:</h2>

```python
from asciitext import *

# Example:1
print(ascii.asciitext("fonts/ANSI_Shadow.txt","#asciitext","#ff0000"))

# Example:2
font_url="https://raw.githubusercontent.com/yasserbdj96/asciitext/main/fonts/Calvin_S.txt"
print(ascii.asciitext(font_url,"#asciitext","#ff0000"))
```

<h2>Screenshot:</h2>

<div align="center">
    <a href="https://raw.githubusercontent.com/yasserbdj96/asciitext/main/screenshot/screenshot_1.png">
        <img alt="yasserbdj96" height="100" src="https://raw.githubusercontent.com/yasserbdj96/asciitext/main/screenshot/screenshot_1.png">
    </a>
</div>

<h2>Changelog History:</h2>

```
## 0.0.4 [27-02-2022]
 - Fix bugs.
 - Enable type import from url.
 
## 0.0.3 [26-02-2022]
 - Fix bugs.

## 0.0.2 [26-02-2022]
 - Fix bugs.
 - Build a package instead of a script.
 
## 0.0.1
 - First public release.
```

<h1></h1> 

<div align="center">
    <a href="http://yasserbdj96.github.io/">Go to this link to get more information</a>
    <br>
    <a href="https://github.com/yasserbdj96/asciitext" align="center">
        <img align="center"  alt="" src="https://visitor-badge.laobi.icu/badge?page_id=yasserbdj96.asciitext">
    </a>
</div>