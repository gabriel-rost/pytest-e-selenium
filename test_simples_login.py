import pytest
from selenium import webdriver
from pages.login_page import LoginPage  # Importando o Page Object

class TestSimplesLogin:
    def setup_method(self, method):
        # Inicializa o navegador (exemplo com Firefox)
        self.driver = webdriver.Firefox()
        self.driver.get("https://the-internet.herokuapp.com/login")

        # Instancia a página de login
        self.login_page = LoginPage(self.driver)

    def teardown_method(self, method):
        # Fecha o navegador
        self.driver.quit()

    def test_simpleslogin(self):
        # Realiza o login usando o Page Object
        self.login_page.login("tomsmith", "SuperSecretPassword!")
        
        # Após o login, você pode verificar a página resultante
        # Por exemplo, verificando se o nome de usuário foi exibido na página
        assert "Welcome to the Secure Area" in self.driver.page_source
