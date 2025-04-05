import pytest
from selenium import webdriver
from pages.redirector_page import RedirectorPage  # Importando o Page Object

class TestRedirector:
    def setup_method(self, method):
        # Inicializa o navegador (exemplo com Firefox)
        self.driver = webdriver.Firefox()
        self.driver.get("https://the-internet.herokuapp.com/redirector")

        # Instancia a página de redirecionamento
        self.redirector_page = RedirectorPage(self.driver)

    def teardown_method(self, method):
        # Fecha o navegador
        self.driver.quit()

    def test_redirector(self):
        # Realiza a navegação utilizando o Page Object
        self.redirector_page.click_redirect_button()
        self.redirector_page.click_link_404()

        # Após o clique, a página de redirecionamento vai mudar.
        # Podemos verificar se a URL atual contém "/404" para garantir que fomos redirecionados para a página correta.
        assert "404" in self.driver.current_url
