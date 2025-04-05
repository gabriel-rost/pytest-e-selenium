# Usar a imagem oficial do Python como base
FROM python:3.9-slim

# Instalar dependências do sistema (como o Firefox e o geckodriver)
RUN apt-get update && \
    apt-get install -y \
    firefox-esr \
    wget \
    curl \
    ca-certificates \
    # Instalar Xvfb para rodar o navegador sem interface gráfica
    xvfb \
    && apt-get clean

# Instalar o geckodriver (driver do Firefox para o Selenium)
RUN curl -sSL https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz | tar xz -C /usr/local/bin

# Instalar dependências do Selenium e pytest
RUN pip install --no-cache-dir \
    selenium \
    pytest \
    pytest-xdist

# Configuração do diretório de trabalho
WORKDIR /app

# Copiar os arquivos do seu código para dentro do container
COPY . /app

# Comando para rodar os testes (agora com Xvfb)
CMD ["xvfb-run", "pytest", "--maxfail=1", "--disable-warnings", "-v"]
