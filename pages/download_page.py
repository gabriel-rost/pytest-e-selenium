from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DownloadPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Localizador (elemento da página)
    _file_link = (By.LINK_TEXT, "upload-me.txt")

    # Método para clicar no link do arquivo para download
    def click_file_link(self):
        file_link = self.wait.until(EC.element_to_be_clickable(self._file_link))
        file_link.click()
