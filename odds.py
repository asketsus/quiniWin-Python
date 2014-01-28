'''
Created on 07/11/2013

@author: asketsus
'''
import os
from selenium import webdriver
import time

def load_teams():
    import csv
    teams = {}

    for key, oddsteam, category in csv.reader(open("teams.csv")):
        teams[key] = [oddsteam, category]

    return teams

def get_url(boleto):

	teams_first = 0
	for i in range(14):
		if boleto[i].getCategory() == "1":
			teams_first = teams_first + 1

	chromedriver = "/Users/asketsus/Dev/webdriver/chromedriver"
	os.environ["webdriver.chrome.driver"] = chromedriver
	driver = webdriver.Chrome(chromedriver)

	url = "http://www.oddsportal.com/soccer/spain/primera-division/"
	driver.get(url)
	time.sleep(5)

	for i in range(teams_first):
		links = driver.find_elements_by_partial_link_text(boleto[i].getMatchnameOddsportal())
		print links[0].get_attribute("href")
		boleto[i].putURLOddsPortal(links[0].get_attribute("href"))

	url = "http://www.oddsportal.com/soccer/spain/segunda-division/"
	driver.get(url)
	time.sleep(5)

	for i in range(teams_first, 14):
		links = driver.find_elements_by_partial_link_text(boleto[i].getMatchnameOddsportal())
		print links[0].get_attribute("href")
		boleto[i].putURLOddsPortal(links[0].get_attribute("href"))

	driver.close()

def get_odds_match(boleto):

	def load_url(driver, url, sleep=3):
		semaphore = 0

		while semaphore == 0:

			driver.get(url)
			time.sleep(sleep)

			try:
				captcha = driver.find_element_by_id("sf_wrap")
				raw_input("Fix the URL (" + url + ") and press enter to continue...")
			except:
				semaphore = 1

			try:
				captcha = driver.find_element_by_id("distil_ident_block")
				raw_input("Fix the URL (" + url + ") and press enter to continue...")
			except:
				semaphore = 1

		driver.execute_script("changeOddsFormat(1);")
		time.sleep(3)

	chromedriver = "/Users/asketsus/Dev/webdriver/chromedriver"
	os.environ["webdriver.chrome.driver"] = chromedriver
	driver = webdriver.Chrome(chromedriver)

	for i in range(14):

		url = boleto[i].getURLOddsPortal()
		load_url(driver, url)

		print "Getting odds for match: " + boleto[i].getMatchnameOddsportal()

		oddstext = driver.find_element_by_class_name("aver")
		oddsAvg = oddstext.text.split(' ')

		oddsAvg[4] = oddsAvg[4][:-1]
		for j in range(1,5):
			oddsAvg[j] = float(oddsAvg[j])
		print oddsAvg
		
		oddstext = driver.find_element_by_class_name("highest")
		oddsHi = oddstext.text.split(' ')

		for j in range(1,4):
			oddsHi[j] = float(oddsHi[j])
		print oddsHi

		boleto[i].putOdds1X2([oddsAvg[1], oddsAvg[2], oddsAvg[3], oddsAvg[4]],[oddsHi[1], oddsHi[2], oddsHi[3]])

		url = url + "#double;2"
		load_url(driver, url, 0)

		oddstext = driver.find_element_by_class_name("aver")
		oddsAvg = oddstext.text.split(' ')

		oddsAvg[4] = oddsAvg[4][:-1]
		for j in range(1,5):
			oddsAvg[j] = float(oddsAvg[j])
		print oddsAvg
		
		oddstext = driver.find_element_by_class_name("highest")
		oddsHi = oddstext.text.split(' ')

		for j in range(1,4):
			oddsHi[j] = float(oddsHi[j])
		print oddsHi

		boleto[i].putOddsDC([oddsAvg[1], oddsAvg[2], oddsAvg[3], oddsAvg[4]],[oddsHi[1], oddsHi[2], oddsHi[3]])
		boleto[i].showSelect()

	driver.close()

def get_odds(boleto):
	teams = load_teams()

	for i in range(14):
		boleto[i].putOddsportalData(teams[boleto[i].getTeamsQuini()[0]][0], teams[boleto[i].getTeamsQuini()[1]][0], teams[boleto[i].getTeamsQuini()[0]][1])

	get_url(boleto)
	get_odds_match(boleto)
