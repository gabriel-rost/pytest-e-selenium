from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Localizadores (elementos da página)
    _username_input = (By.ID, "username")
    _password_input = (By.ID, "password")
    _login_button = (By.CSS_SELECTOR, ".fa")

    # Método para preencher o nome de usuário
    def enter_username(self, username):
        username_input = self.wait.until(EC.visibility_of_element_located(self._username_input))
        username_input.click()
        username_input.send_keys(username)

    # Método para preencher a senha
    def enter_password(self, password):
        password_input = self.wait.until(EC.visibility_of_element_located(self._password_input))
        password_input.click()
        password_input.send_keys(password)

    # Método para clicar no botão de login
    def click_login_button(self):
        login_button = self.wait.until(EC.element_to_be_clickable(self._login_button))
        login_button.click()

    # Método para fazer o login completo
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
