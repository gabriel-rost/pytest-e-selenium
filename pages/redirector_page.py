from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RedirectorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Localizadores (elementos da página)
    _redirect_button = (By.ID, "redirect")
    _link_404 = (By.LINK_TEXT, "404")

    # Método para clicar no botão de redirecionamento
    def click_redirect_button(self):
        redirect_button = self.wait.until(EC.element_to_be_clickable(self._redirect_button))
        redirect_button.click()

    # Método para clicar no link de 404
    def click_link_404(self):
        link_404 = self.wait.until(EC.element_to_be_clickable(self._link_404))
        link_404.click()
