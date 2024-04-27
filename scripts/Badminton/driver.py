from selenium import webdriver
from constants import driver_path
from webdriver_manager.chrome import ChromeDriverManager

# Create ChromeOptions instance
options = webdriver.ChromeOptions()

# Create Chrome driver with ChromeOptions
driver = webdriver.Chrome(executable_path=driver_path, options=options)
