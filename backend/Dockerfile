FROM ubuntu:20.04

WORKDIR /app

COPY . ./

RUN apt-get update && apt-get install -y build-essential git python3 python3-pip

RUN sh build_backend.sh

ENV PORT=5000

EXPOSE 3000

CMD ["python3", "./src/api.py"]
