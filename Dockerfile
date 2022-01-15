FROM python:3.10

WORKDIR /code

COPY . /code

RUN chmod +x /code/build.sh

RUN /code/build.sh

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5000", "--proxy-headers"]
