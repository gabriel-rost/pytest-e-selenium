from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HttpCatPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Localizadores (elementos da página)
    _category_link = (By.CSS_SELECTOR, "li:nth-child(5) .contrast-\\[70\\%\\]")

    # Método para clicar em uma categoria
    def click_category(self):
        category_link = self.wait.until(EC.element_to_be_clickable(self._category_link))
        category_link.click()

    # Método para rolar até o topo da página
    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0,0)")

