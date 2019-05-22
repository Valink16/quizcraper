# -*- coding: utf-8 -*-

from selenium import webdriver
import logging
import quizcraper

logging.basicConfig(level=logging.INFO)

driver = webdriver.Firefox(executable_path="./geckodriver")
quiz_url = "https://quizlet.com/170585467/44-a-48-flash-cards/"

print(quizcraper.get_terms(driver, quiz_url, 0, 10))
