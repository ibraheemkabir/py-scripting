FROM python:3

ADD liqScript.py /

RUN pip install pystrich

RUN pip install requests

ENTRYPOINT [ "python", "./liqScript.py" ]