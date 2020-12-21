def register(name, password, urls):
    i = 0
    for url in urls:
        i += 1
        driver = webdriver.Firefox(executable_path="selenium-firefox/drivers/geckodriver")
        url = url.replace(" ", "")
        driver.get(url)

        # Registrate
        driver.find_element_by_xpath('//*[@id="real_name"]').send_keys(name)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/form/button').click()

        time.sleep(1)
        driver.quit()
        print(i)

name = "David Anthony"
password = "pasjhfe1"
url = "https://sitespeedio.slack.com/join/invite/enQtMTU3NDExODM4MDY3Ny03NDNjNTM0ZDM1YmY3YWYwYjIyZTkyMWYxNjE2ZTY5NTg1N2YxM2JiMzE5NWRiZDI5ZjBhZTZmZTY3ODdiZmFm#/credentials"
urls = [url]
register(name, password, urls)