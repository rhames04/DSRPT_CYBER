from time import sleep
from selenium import webdriver


class Bot:
    def __init__(self, searchContent):
        self.driver = webdriver.Chrome()
        result = []
        sites = [
            "pastebin.com",
            "slexy.org",
            "github.com",
            "reddit.com",
            "facebook.com",
        ]

        print("")
        print("SUA BUSCA FOI ENCONTRADA EM: ")
        print("")

        for site in sites:
            self.driver.get("http://google.com/")
            sleep(3)
            self.driver.find_element_by_xpath(
                '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input'
            ).send_keys('"{}" site:{}'.format(searchContent, site))
            self.driver.find_element_by_xpath(
                '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]'
            ).click()
            sleep(3)
            if not (
                self.driver.find_elements_by_xpath('//*[@id="topstuff"]/div/div/div[1]')
            ):
                elements = self.driver.find_elements_by_xpath(
                    "//div[contains(@class, 'rc')]/div[1]/a"
                )
                for element in elements:
                    print(element.get_attribute("href"))
            sleep(4)


print("")
print("")
print("***************************************")
print("****                               ****")
print("****                               ****")
print("****        DSRPT21 - 4ECR         ****")
print("****                               ****")
print("****                               ****")
print("***************************************")
print("")
print("")

info = input("Digite que informação deseja buscar: ")
my_bot = Bot(info)
