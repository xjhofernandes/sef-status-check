"""Element utils module with some useless functions"""

from selenium import webdriver


def find_and_click_element(
        element_type: str, value: str, driver: webdriver) -> None:
    """
    Find and click in a element from HTML.
    You can use many types of elements and they are:
    * id
    * class
    * xpath

    Args:
        element_type (str): Element html type.
        value (str): Value of the element.
            Example: A ID with the name "my-button".
        driver (webdriver): Selected Browser Driver (Chrome or Firefox).
    """
    driver.find_element(by=element_type, value=value).click()
