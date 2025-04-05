FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y \
    firefox-esr \
    wget \
    curl \
    ca-certificates \
    xvfb \
    && apt-get clean

RUN GECKODRIVER_VERSION=0.36.0 && \
    wget https://github.com/mozilla/geckodriver/releases/download/v$GECKODRIVER_VERSION/geckodriver-v$GECKODRIVER_VERSION-linux64.tar.gz && \
    tar -xvzf geckodriver-v$GECKODRIVER_VERSION-linux64.tar.gz && \
    mv geckodriver /usr/local/bin/ && \
    chmod +x /usr/local/bin/geckodriver && \
    rm geckodriver-v$GECKODRIVER_VERSION-linux64.tar.gz

RUN pip install --no-cache-dir \
    selenium \
    pytest \
    pytest-xdist \
    pytest-html

WORKDIR /app

COPY . /app

RUN mkdir -p /app/log

CMD ["xvfb-run", "pytest", "--maxfail=1", "--disable-warnings", "-v", "--html=log/report.html", "--self-contained-html", "--tb=short"]
