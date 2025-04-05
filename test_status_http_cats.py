import pytest
from selenium import webdriver
from pages.http_cat_page import HttpCatPage  # Importando o Page Object

class TestStatusHttpCats:
    def setup_method(self, method):
        # Inicializa o navegador (exemplo com Firefox)
        self.driver = webdriver.Firefox()
        self.driver.get("https://http.cat/")

        # Instancia a página http.cat
        self.http_cat_page = HttpCatPage(self.driver)

    def teardown_method(self, method):
        # Fecha o navegador
        self.driver.quit()

    def test_status_http_cats(self):
        # Interage com a página usando o Page Object
        self.http_cat_page.click_category()
        self.http_cat_page.scroll_to_top()
        
        # Não há uma verificação explícita aqui, mas poderia ser feita uma verificação
        # por exemplo, de que a imagem ou status correto foi carregado.
        # Você pode fazer isso verificando a URL ou elementos específicos após a navegação.
        assert "https://http.cat/status/200" in self.driver.current_url  # Exemplo de verificação
