# docker pull yasserbdj96/asciitext:latest
# docker build -t docker.io/yasserbdj96/asciitext:latest .
# docker run -i -t docker.io/yasserbdj96/asciitext:latest
# docker run -e USE=True -e FONT="fonts/ANSI_Shadow.txt" -e TEXT="your text" -e COLOR="#ff0000" -e COLOR_BG="#ffffff" -i -t docker.io/yasserbdj96/asciitext:latest

FROM python:3.9

WORKDIR /wrdir

COPY ./examples.py /wrdir
COPY ./asciitext /wrdir/asciitext
COPY ./fonts /wrdir/fonts
COPY ./requirements.txt /wrdir/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /wrdir/requirements.txt

CMD ["python", "examples.py"]