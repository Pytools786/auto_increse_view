from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

text = '''

   _____  ____________  ____  __   ____
  / _ \ \/ /_  __/ __ \/ __ \/ /  / __/
 / ___/\  / / / / /_/ / /_/ / /___\ \  
/_/    /_/ /_/  \____/\____/____/___/  
                                       
                                         coded by shivraj patil
'''
print(text)
url = input("ENTER BLOG URL: ")
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path= GeckoDriverManager().install())
while True:
    driver.get(url)
    print ("sending requests ..........")
