FROM python:3.5-alpine

ADD . /app
WORKDIR /app

RUN apk --update add \
    ca-certificates \
    openssl \
    tini \
    g++ \
    --update-cache \
    --repository http://dl-3.alpinelinux.org/alpine/edge/community/ --allow-untrusted \
    --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted

RUN apk --update add --virtual build-dependencies \
        build-base \
        --update-cache \
        --repository http://dl-3.alpinelinux.org/alpine/edge/community/ --allow-untrusted \
        --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted \
    && ln -s /usr/include/locale.h /usr/include/xlocale.h \
    && pip install  -r requirements.txt

RUN apk --no-cache del \
    wget \
    build-dependencies \
&& rm -rf /var/cache/apk/* /tmp/*

EXPOSE 9010

ENTRYPOINT ["/usr/local/bin/flask"]

CMD ["run" , "-h", "0.0.0.0", "-p", "9010"]