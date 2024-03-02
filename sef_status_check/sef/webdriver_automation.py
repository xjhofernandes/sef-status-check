"""Module responsible for selenium automation in SEF website"""

from selenium import webdriver
from sef_status_check.utils import element


def get_residence_permit_status(
        driver: webdriver, email: str, password: str) -> str:
    """
    Get the Residence Permit status in SEF homepage.
    From endpoint: https://www.sef.pt/pt/Pages/homepage.aspx.

    Args:
        driver (webdriver): Selected Browser Driver (Chrome or Firefox).
        email (str): Email login to SEF website.
        password (str): Password login to SEF website.

    Returns:
        str: A text with the residence permit status.
    """
    print("Opening the SEF website...")
    driver.get("https://www.sef.pt/pt/Pages/homepage.aspx")
    login_menu_xpath = "/html/body/form/header/div[1]/div[2]/div[3]/div/a"

    print("Cliking in login button on website.")
    element.find_and_click_element("xpath", login_menu_xpath, driver)

    print("Putting your personal information...")
    email_login_input = driver.find_element(by="id", value="txtUsername")
    email_login_input.send_keys(email)
    password_login_input = driver.find_element(by="id", value="txtPassword")
    password_login_input.send_keys(password)

    print("Loggin in SEF...")
    element.find_and_click_element("id", "btnLogin", driver)
    print("Loading scheduling menu...")
    element.find_and_click_element("id", "agendamentosLink", driver)
    print("Obtaing your scheduling information...")
    element.find_and_click_element("id", "btnNovoAgendamento", driver)

    dropdown_services_list = driver.find_element(
        by="id",
        value="Services_List"
    )

    ar_status_info = dropdown_services_list.text.replace(
        "--Selecione uma opção--\n",
        ""
    )

    print("All done! :)")

    return ar_status_info
