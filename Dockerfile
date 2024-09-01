FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install curl python3 python3-dev python3-setuptools python3-pip python3-distutils build-essential  -y\
    && python3 -m pip install -U pip setuptools poetry\
    && apt-get clean && rm -rf /var/cache/apt/archives /var/lib/apt/lists

RUN echo "export PATH=/usr/local/cuda/bin:/root/.local/bin:$PATH" > ~/.bashrc
RUN echo "export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH" > ~/.bashrc
WORKDIR /app
COPY . .
RUN poetry config virtualenvs.in-project true && poetry install

CMD poetry run python manage.py makemigrations && poetry run python manage.py migrate && poetry run gunicorn statracking.asgi:application -k uvicorn.workers.UvicornWorker -w 4
