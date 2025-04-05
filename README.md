# 🧪 Testes Automatizados com Selenium e Pytest via Docker

---

## 🚀 Como Rodar os Testes com Docker

### 1. Clonar o repositório
```
git clone https://github.com/gabriel-rost/pytest-e-selenium.git
```
```
cd pytest-e-selenium
```
### 2. Construir e executar o container
```
docker-compose up --build
```
### 🧹 Limpando o ambiente
```
docker-compose down
```
### 📝 Logs dos Testes
Durante a execução dos testes via Docker, dois tipos de logs são gerados automaticamente no diretório logs/ do projeto:
* 📄 Log em Texto (.log)
* 🌐 Relatório em HTML (report.html)
