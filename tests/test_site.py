import time #ТАБУ ЖОСКОЕ
from pages.homepage import HomePage
from pages.product import ProductPage


def test_open_link_to_phone (browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.check_title_is("Samsung galaxy s6")

def test_open_monitor_link(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_monitor_page()
    # browser.get('https://www.demoblaze.com/')
    # monitor_link = browser.find_element(By.CSS_SELECTOR, value='''[onclick="byCat('monitor')"]''')
    # monitor_link.click()
    time.sleep(2)
    # monitors = browser.find_elements(By.CSS_SELECTOR, value= '.card')
    # assert len(monitors) == 2
    homepage.check_monitor_count(2)