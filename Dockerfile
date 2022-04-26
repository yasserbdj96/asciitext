# docker build -t asciitext-docker .
# docker run -i -t asciitext-docker
# 
FROM python:3.9

WORKDIR /wrdir

COPY ./examples.py /wrdir
COPY ./asciitext /wrdir/asciitext
COPY ./fonts /wrdir/fonts
COPY ./requirements.txt /wrdir/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /wrdir/requirements.txt

CMD ["python", "examples.py"]