from selenium import webdriver
import quizcraper

driver = webdriver.Firefox(executable_path="./geckodriver")
quiz_url = "https://quizlet.com/170585467/44-a-48-flash-cards/"

quizcraper.get_terms(driver, quiz_url)
