from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class UploadPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Localizadores (elementos da página)
    _file_input = (By.ID, "file-upload")
    _submit_button = (By.ID, "file-submit")

    # Método para fazer o upload de um arquivo
    def upload_file(self, file_name):
        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), file_name)
        file_input = self.wait.until(EC.visibility_of_element_located(self._file_input))
        file_input.send_keys(file_path)

    # Método para clicar no botão de envio
    def submit(self):
        submit_button = self.wait.until(EC.element_to_be_clickable(self._submit_button))
        submit_button.click()

    # Método para realizar o upload completo
    def complete_upload(self, file_name):
        self.upload_file(file_name)
        self.submit()
