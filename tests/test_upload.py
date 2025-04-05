import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from selenium import webdriver
from pages.upload_page import UploadPage

class TestUpload:
    def setup_method(self, method):
        # Inicializa o navegador (exemplo com Firefox)
        self.driver = webdriver.Firefox()
        self.driver.get("https://the-internet.herokuapp.com/upload")

        # Instancia a página de upload
        self.upload_page = UploadPage(self.driver)

    def teardown_method(self, method):
        # Fecha o navegador
        self.driver.quit()

    def test_upload_file(self):
        # Realiza o upload de um arquivo usando o Page Object
        self.upload_page.complete_upload("upload-file.txt")
        
        # Verifica o resultado após o upload (isso pode variar de acordo com a página)
        # Por exemplo, verificando se há uma mensagem de sucesso.
        assert "File Uploaded!" in self.driver.page_source
