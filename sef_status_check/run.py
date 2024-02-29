"""Main module of the project"""

from sef_status_check import config
from sef_status_check.sef import webdriver_automation

def execute(email: str, password: str, browser: str) -> None:
    print("Loading browser driver....")
    driver = config.obtain_webdriver_browser(browser)

    ar_status_info = webdriver_automation.get_residence_permit_status(driver, email, password)

    print("============================================================================================================")
    print(f"Seu status atual: {ar_status_info} ")
    if ar_status_info == "Prorrogação Permanência":
        print("Infelizmente o seu título de residência ainda não está disponível. Tente verificar novamente mais tarde...")
    elif ar_status_info == "Renovação Título Residência":
        print("AEW Caralho, teu título tá pronto PORRA. PARABËNS")
        print(config.patrick_estrela)
        print(config.cristiano_ronaldo)
    else:
        print("Talvez o seu AR já esteja disponível. Por favor, cheque o site do SEF.")
    print("============================================================================================================")

    config.quit_webdriver(driver)
