FROM python:3.9.1-alpine3.12

WORKDIR /app

COPY . ./

RUN \
    apk add --no-cache --virtual=build-dependencies  --update gcc musl-dev python3-dev linux-headers && \
    apk add --no-cache --virtual=runtime --update git

RUN sh build_model.sh

ENV PORT=5000

EXPOSE 3000

CMD ["python3", "./src/api.py"]