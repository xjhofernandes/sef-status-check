"""Main config file of the project"""

from selenium import webdriver

option = webdriver.FirefoxOptions()
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-shm-usage')
option.add_argument('--disable-gpu')
option.add_argument('--log-level=3') 


def obtain_webdriver_browser(browser_name: str) -> webdriver:
    """
    Obtain the webdriver from the selected browser. 
    In this case, we just support Chrome and Firefox.

    Args:
        browser_name (str): The name of the cell webbrowser the user will use.

    Returns:
        webdriver: The name of the cell webbrowser the user will use.
    """
    if browser_name == "chrome":
        return webdriver.Chrome(options=option)
    elif browser_name == "firefox":
        return webdriver.Firefox(options=option)
    else:
        error_output = "Sorry, but we don't support this web browser yet... Se in your next updates..."
        raise ValueError(error_output)

def quit_webdriver(driver: webdriver) -> None:
    """
    Close the webdriver session.

    Args:
        driver (webdriver): Selected Browser Driver (Chrome or Firefox).
    """
    driver.quit()

patrick_estrela  = """
⣴⣶⣶⠿⠟⠛⠻⠷⣶⣶⣶⣤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⠁⠰⠆⠀⠀⠀⠀⠀⠈⠉⠛⠛⠿⣿⣶⣶⣦⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢹⣿⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠿⢿⣿⣷⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢻⣿⣇⠀⠀⢠⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⢾⣿⣿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠹⣿⣦⡀⢸⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠿⣿⣿⣶⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⣿⣿⣦⠙⠻⠟⠛⠀⠀⠀⠀⠀⠀⣶⣿⢷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⢿⣿⣷⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠻⣿⣷⣀⡀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠿⣿⣿⢶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠛⠿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⢿⣶⣤⣙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⡇⣀⣾⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣿⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡍⠛⠻⠶⠤⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⢿⣿⣶⣤⣀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡿⠻⠛⣿⡿⠁⠀⠀⠀⠀⣀⣤⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠿⣿⣷⣦⣄⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⣷⣶⣶⡶⠀⠀⠀⠀⠀⣼⣿⡇⠀⢸⣿⠇⠀⣠⣴⣾⠟⠛⠉⠉⠉⠉⠛⠻⣶⣤⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣽
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣶⠃⠀⠀⠐⠿⠿⠀⣴⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⠿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣷⣀⣀⣀⡠⠀⠀⠀⠀⠀⠀⣼⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⢀⣿⡇⠀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠺⠿⠿⠿⣿⡿⠿⠟⠛⠛⠀⠀⣀⣀⡀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⢣⣾⣿⣥⣾⣿⣿⡉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡄⠀⣀⣤⣶⠿⠛⠛⠛⠻⣿⣧⠀⠀⠀⠀⠀⣠⣶⣿⣶⣤⣾⡟⠁⠈⢱⣿⠁⠈⢹⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣾⡿⠋⠀⠀⠀⠀⠀⠀⠈⢻⣧⠀⠀⠀⠀⣿⣿⣿⣿⠟⠁⠀⠀⣠⣿⡟⠀⢀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡷⠶⠿⠿⠛⢋⡉⠁⠀⠀⣠⣾⡿⠋⠀⠀⣸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡷⣦⣤⣶⣿⣛⣋⣠⣴⡾⠟⠋⠀⠀⠀⣰⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡄⠀⠀⢀⣤⣶⣶⣄⢀⣴⡿⠋⠀⠀⣸⡟⠛⠛⠋⠉⠁⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠈⣿⣿⣿⣿⠿⠋⠀⠀⠀⣠⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡟⠛⠛⠛⢛⡉⠁⠀⠀⠀⠀⣠⣾⡿⠁⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠻⣿⣧⣤⣤⣤⣶⡾⠟⠉⠀⠀⠀⠀⠀⢀⣀⣴⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⡏⢩⡥⠄⠀⠀⠀⠀⣀⣠⣤⣶⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⠿⢻⣿⣾⣷⣤⣴⣶⣾⣿⣿⣿⣿⣟⣟⣻⣿⣿⠿⠛⠉⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⠛⠁⠀⠰⣿⡟⠉⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠋⠉⣀⣀⣀⣀⣴⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⠏⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⠏⠀⠀⠀⠀⠀⠀⠀⢿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

"""

cristiano_ronaldo = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢀⠀⣀⣀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⢴⣰⢦⣄⣿⣶⣿⣿⣷⣔⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣐⣾⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⣴⣾⡭⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⡉⠶⡈⡉⢿⠷⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣺⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⡀⢂⠰⡀⢀⡙⢮⣝⣪⣂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣻⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣹⣿⣿⡄⠗⢂⠉⣠⣍⣩⡐⡌⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣾⣷⡟⢋⠄⠠⢀⡾⢛⣽⣿⣿⣿⣷⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣟⣷⣿⠡⠈⠀⢤⠏⣼⣿⣿⣿⠟⠉⠛⠥⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⣿⣌⡆⠁⠉⠀⠈⠉⠉⠛⢛⡤⠀⠀⠈⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣻⣿⣿⣿⣿⣿⣿⢿⣧⡄⡉⠻⣿⣇⢀⠀⡀⢀⠀⠀⡀⢤⢋⡱⢳⠠⢂⣤⣼⡣⠀⣀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠾⣿⣿⣿⣿⣿⡩⡤⣷⢋⣇⠀⠠⢿⡮⠇⡘⠤⢊⠔⣩⢖⠣⡜⠹⠘⠛⣛⡿⡀⠘⡄⠠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡽⣿⣿⣿⣿⣿⢮⣢⠌⢤⡾⢑⢊⠱⠀⠂⠠⢈⠎⡵⣉⠎⣐⠃⣌⣞⣵⣶⡖⠀⡏⠐⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠽⣿⣿⣿⣿⣎⠻⣿⢿⡶⡉⢆⢂⠡⣈⠄⡡⠚⠤⡁⠎⠀⣢⢟⣯⣯⣻⡅⣦⣢⠄⣼⠀⠀⢀⠤⢄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢝⣿⣿⣿⠧⢃⡐⠂⡄⢳⡜⣢⠑⣆⠸⢤⣉⠦⡑⡌⠲⣅⠻⣙⢛⣯⠀⣿⠀⠀⠨⣀⢔⠕⠁⣠⣕⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⣿⠉⡆⣀⠁⢰⢉⣱⣉⡾⣈⡿⣶⣏⣶⢱⡀⢇⡈⠷⣈⣶⣹⡆⢿⠁⠀⠀⡉⠀⠀⣾⣿⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⢟⣋⠒⠤⢂⠡⠂⠼⡐⣼⣻⢿⣿⣿⣿⣾⣿⣿⣷⣯⣿⣿⣿⡿⠁⣿⠀⠀⢾⠁⠐⠀⢛⢉⣉⣩⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⠈⠲⣉⠔⡠⠁⠜⠰⣹⣿⣟⣮⡿⣝⡿⣋⣿⣿⣿⠿⠻⠛⠉⠀⠀⢛⡄⢀⢻⠀⠀⠀⡀⠀⠉⠛⡃⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠤⠀⠀⠀⠐⠂⠀⠒⠰⠀⠀⠀⠀⠘⢆⠡⠌⣀⢣⠹⣿⣞⡷⡙⢡⢒⣽⣿⣟⠁⠀⠀⠀⠀⠀⢸⣹⠁⠀⠄⠀⠀⠀⠀⠀⢀⠣⣿⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⠀⠀⠀⠀⠑⢄⣐⢪⠱⣋⢿⡅⢡⢃⢎⠹⣿⡆⠀⠀⠀⠀⠀⠀⠈⡜⡄⠀⠀⠀⠀⠀⠀⠀⠀⣸⠏⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠌⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠱⣌⢣⡝⣲⡜⢢⠭⣆⢳⡟⠄⠀⠀⠀⠀⠀⠀⠀⡇⠐⠀⠀⠀⠀⠀⠀⢀⣰⡓⠀⠀
⠀⠀⠀⠀⠀⠀⢀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠂⠄⣀⠀⠀⠀⠈⠢⠀⠀⠀⠀⠈⠳⣞⡵⣫⢧⣻⣾⣿⢣⠃⠀⠀⠀⠀⠀⠀⢠⠰⢀⠀⠀⠀⠀⠀⣤⣿⡗⠁⠀⠀
⠀⠀⠀⠀⠀⡠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠂⠄⠀⠐⢄⠀⠀⠀⠀⠈⠻⣧⣿⣿⣿⡟⡧⠑⠀⡀⠀⠀⠀⢀⠂⡁⠀⠀⠀⠀⢀⣼⣟⠃⠀⠀⠀⠀
⠀⠀⠀⠀⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠑⢄⠀⠀⠀⠀⠈⢻⣿⢏⡵⠁⠀⠲⡈⠂⢀⠀⡌⠠⠀⠀⠀⠀⠀⣼⡿⠌⠀⠀⠀⠀⠀
⠀⠀⠀⢠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠠⠀⠀⠀⠑⡙⣄⠀⠀⠀⢠⣠⣾⡇⠀⠠⠀⠈⠂⠀⢸⢀⠂⠄⠂⠀⠀⣰⡟⣷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣰⠶⣶⢤⡄⠀⠐⠙⢷⣄⢴⠛⢻⡽⠃⠀⠀⠁⠀⠰⡀⣞⠠⠐⠠⠀⠀⢠⣿⢩⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⢉⣿⣾⣏⣸⣶⡀⣎⠈⠎⢸⣇⠸⣾⠁⣰⢆⠀⠀⠀⢸⡏⠰⡈⠰⠀⢀⠸⣏⣾⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠼⢫⡲⢹⡿⣻⢦⢻⣄⠀⡦⠈⢿⡄⡷⣻⡝⣿⣮⠀⢀⡞⠤⡑⠤⠀⠀⣂⢽⡇⣞⠀⠀⠀⠀⠀⠀⠀
⠀⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢵⢈⠆⢕⣣⢎⣥⣿⠆⠀⠑⠀⢿⣸⠌⡙⠶⣹⠗⠉⠬⡑⣈⠐⠀⡁⢴⣺⢘⡏⠀⠀⠀⠀⠀⠀⠀
⠀⠇⠀⠀⠠⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠛⠓⠈⠛⠉⠁⠀⠀⠀⠀⠘⢾⡳⢌⡴⢃⠀⠌⠐⡐⠀⠀⠐⣈⠦⡛⡼⠇⠀⠀⠀⠀⠀⠀⠀
⠠⠀⠀⠀⠀⠀⠀⠀⠐⠒⠨⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠮⠿⢦⣌⠀⠄⠀⠀⢀⠂⡔⣫⢵⢻⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠠⠤⢀⠀⠤⢀⣈⣒⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠈⠳⡀⠀⢀⠂⡜⣸⢱⣾⡄⠀⠀⠀⠀⠀⠀⠀⠀
"""