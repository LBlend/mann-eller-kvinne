FROM python:3.13

COPY --from=ghcr.io/astral-sh/uv:0.13 /uv /uvx /bin/

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never

WORKDIR /code

COPY . /code

RUN chmod +x /code/build.sh

RUN /code/build.sh

ENV PATH="/code/.venv/bin:$PATH"

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5000", "--proxy-headers"]
