import pytest
from selenium import webdriver
from pages.download_page import DownloadPage  # Importando o Page Object

class TestSimpleDownload:
    def setup_method(self, method):
        # Inicializa o navegador (exemplo com Firefox)
        self.driver = webdriver.Firefox()
        self.driver.get("https://the-internet.herokuapp.com/download")

        # Instancia a página de download
        self.download_page = DownloadPage(self.driver)

    def teardown_method(self, method):
        # Fecha o navegador
        self.driver.quit()

    def test_simple_download(self):
        # Realiza o download clicando no link usando o Page Object
        self.download_page.click_file_link()

        # Após o clique, normalmente você pode verificar se o arquivo foi baixado
        # O comportamento de verificação pode variar dependendo do sistema operacional e configuração do Selenium
        # Por exemplo, você pode verificar a presença do arquivo no diretório de downloads, mas isso depende do seu setup.
        
        # Um exemplo de asserção genérica que você pode usar:
        assert "https://the-internet.herokuapp.com/download" in self.driver.current_url
