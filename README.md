<p align="center"><img align="center" src="https://raw.githubusercontent.com/yasserbdj96/asciitext/main/screenshot/screenshot_0.png"></p>


<h1>Text to ASCII.</h1>

<p>Text to ASCII Art Generator.</p>

[![Python package](https://github.com/yasserbdj96/asciitext/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/yasserbdj96/asciitext/actions/workflows/python-app.yml) [![CodeFactor](https://www.codefactor.io/repository/github/yasserbdj96/asciitext/badge)](https://www.codefactor.io/repository/github/yasserbdj96/asciitext) [![Join the chat at https://gitter.im/yasserbdj96/asciitext](https://badges.gitter.im/yasserbdj96/asciitext.svg)](https://gitter.im/yasserbdj96/asciitext?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

<h2>Languages:</h2>
* python3

<h2>Requirements</h2>
[✓] hexor<br>
[✓] requests

<h2>Supported Distributions:</h2>

| Distribution | Version Check     | Python Test Version | Supported | Status      | Everything works |
| :----------: | :---------------: | :-----------------: | :-------: | :---------: | :--------------: |
| Ubuntu       | 20.04.3           | 3.6, 3.7, 3.8, 3.9  | Yes       | Working     | Yes              |
| Windwos      | 11.6.4            | 3.6, 3.7, 3.8, 3.9  | Yes       | Not Working | No               |
| MacOS        | 10.0.20348        | 3.6, 3.7, 3.8, 3.9  | Yes       | Working     | Yes              |
| Android (termux)| 10 (0.118.0)| 3.6, 3.7, 3.8, 3.9, 3.10  | Yes    | Working     | Yes              |
| Android (nethunter)| 10 (2022.3)| 3.6, 3.7, 3.8, 3.9, 3.10| Yes    | Working     | Yes              |


<h2>Python Package Installation:</h2>

```
# install from pypi:
pip install asciitext

# local install:
git clone https://github.com/yasserbdj96/asciitext.git
cd asciitext
sudo python setup.py install
```

<h2>Run without installation:</h2>

```
git clone https://github.com/yasserbdj96/asciitext.git
cd asciitext
pip install -r requirements.txt
python3 run.py '<FONT_PATH/FONT_URL>' '<COLOR>' '<BACKGROUND/FALSE>' '<TEXT>'
```

<h2>Script Usage:</h2>

```python
from asciitext import *

print(asciii.asciitext(<FONT_PATH/URL>,<TEXT>,<TEXT_COLOR>,<BACKGROUND_COLOR>,<COLOR_TYPE[hex/rgb]>))
```

<h2>Script Examples:</h2>

```python
from asciitext import *

# Example:1
print(asciii.asciitext("./fonts/ANSI_Shadow.txt","#asciitext","#ff0000"))

# Example:2
font_url="https://raw.githubusercontent.com/yasserbdj96/asciitext/main/fonts/Calvin_S.txt"
print(asciii.asciitext(font_url,"#asciitext","#ff0000"))
```

<h2>Screenshot:</h2>

<div align="center">
    <a href="https://raw.githubusercontent.com/yasserbdj96/asciitext/main/screenshot/screenshot_1.png">
        <img alt="yasserbdj96" height="100" src="https://raw.githubusercontent.com/yasserbdj96/asciitext/main/screenshot/screenshot_1.png">
    </a>
</div>

<h2>Changelog History:</h2>

```
## 0.0.5 [17-08-2022]
 - Fix bugs.

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
Don't forget to star ⭐ this repository
<br>

all posts [`#yasserbdj96`](#yasserbdj96) ,all views my own.

<br>
<div align="center">
    <a href="http://yasserbdj96.github.io/">Go to this link to get more information.</a>
</div>