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
ENV PATH="/app/monero-x86_64-linux-gnu-v0.18.4.1:$PATH"

COPY src/ ./src/

CMD ["python", "src/main.py"]