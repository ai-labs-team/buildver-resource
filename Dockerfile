FROM python:3.6-alpine3.4

RUN mkdir -p /opt/resource

COPY src /opt/resource/
RUN chmod ug+x /opt/resource/*
RUN pip install -r /opt/resource/requirements.txt
RUN rm /opt/resource/requirements.txt

CMD ["/opt/resource/check"]