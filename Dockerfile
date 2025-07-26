FROM python:3.11-slim

WORKDIR /app

RUN apt-get update
# install bzip
RUN apt-get install -y wget tar bzip2
RUN rm -rf /var/lib/apt/lists/*

# install monero cli
RUN wget https://downloads.getmonero.org/cli/linux64 -O monero-linux-x64.tar.bz2 \
    && tar -xvf monero-linux-x64.tar.bz2 -C /app \
    && rm monero-linux-x64.tar.bz2

COPY src/ ./src/

CMD ["python", "src/main.py"]