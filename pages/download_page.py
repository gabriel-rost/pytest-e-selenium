import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DownloadPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)  # tempo de espera aumentado

        # Garante que o diretório de logs existe
        os.makedirs("/app/logs", exist_ok=True)

    # Localizador mais flexível
    _file_link = (By.XPATH, "//a[contains(@href, 'download/not_empty.txt')]")

    def click_file_link(self):
        try:
            file_link = self.wait.until(EC.element_to_be_clickable(self._file_link))
            file_link.click()
        except Exception as e:
            # Salva a tela e HTML para debug
            self.driver.save_screenshot("/app/logs/screenshot_before_click.png")
            with open("/app/logs/page_source.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)

            # Repassa o erro original após logar o que foi possível
            raise e
