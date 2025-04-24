from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.main.domain.contants import UnoparPageConsts
from src.main.infra.config.app_config import AppConfig
from src.main.infra.selenium.selenium_driver import SeleniumDriver
from src.main.business.colector.data_collector_i import DataCollectorI


class UnoparDataCollectorImpl(DataCollectorI):
    def __init__(self):
        self._web_driver = SeleniumDriver()
        self._driver = self._web_driver.get_driver()

    def collect(self) -> list[str]:
        driver = self._web_driver.get_driver()
        self._acessar_disciplinas(driver)

        atividades = self._coletar_atividades(driver)
        self._web_driver.close_driver()
        return atividades

    def _acessar_disciplinas(self, driver) -> None:
        # Acessa URL
        driver.get(AppConfig.scraping.url)

        # Faz login
        username = driver.find_element(By.ID, UnoparPageConsts.USERNAME)
        username.click()
        username.send_keys(AppConfig.scraping.username)

        password = driver.find_element(By.ID, UnoparPageConsts.PASSWORD)
        password.click()
        password.send_keys(AppConfig.scraping.password)

        password.send_keys(Keys.ENTER)

        # # Clica em 'entrar' para entrar no ambiente de estudo
        driver \
            .find_element(By.CSS_SELECTOR, UnoparPageConsts.BOTAO_ENTRAR) \
            .click()

    def _coletar_atividades(self, driver) -> list[dict]:
        all_atividades = []
        loop = 0
        while loop != 6:
            current_materia = self._find_materias(driver=driver)[loop]
            current_materia_nome = current_materia.text
            current_materia.click()

            atividades = self._find_atividades(driver=driver)
            atividades = list(map(lambda atividade: current_materia_nome + ' \n' + atividade.text, atividades))
            all_atividades.extend(atividades)

            self._click_botao_voltar(driver=driver) # Voltar para a tela inicial
            loop += 1
        return all_atividades

    def _find_materias(self, driver) -> list[str]:
        return driver.find_elements(By.CSS_SELECTOR, '.pull-left.atividadeNome')

    def _find_atividades(self, driver) -> list:
        return driver.find_elements(By.CSS_SELECTOR, '.atividades')

    def _click_botao_voltar(self, driver) -> None:
        botao_voltar = '//ol[@class="breadcrumb"]/li/a[contains(@href, "/aluno/dashboard/index/")]'
        driver \
            .find_element(By.XPATH, botao_voltar) \
            .click()
