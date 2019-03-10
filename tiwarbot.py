# -*- coding: utf-8 -*- 

print("TiWaR Bot v. 1.0.2")


#Importing
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver import ActionChains

print('Starting Bot')

loop = 1
while loop < 100000:

	#Chrome Options
	options = webdriver.ChromeOptions()
	options.add_argument('--lang=en')
	browser = webdriver.Chrome(chrome_options=options)
	browser.get('https://tiwar.ru/?sign_in=1')
	time.sleep(1) 

	#Login
	login_field = browser.find_element_by_name('login')
	login_field.send_keys('YOUR USERNAME')
	print('Login Success')

	#Password
	login_field = browser.find_element_by_name('pass')
	login_field.send_keys('YOUR PASSWORD')
	print('Password Success')

	#Log In
	submit1 = browser.find_element_by_css_selector('input.label').click()
	sleep(2)
	
	#Arena
	submit2 = browser.find_element_by_link_text("Арена")
	submit2.click()
	print('Go to Arena')
	sleep(2)
	
	#Fighting
	submit3 = browser.find_element_by_partial_link_text('Атакoвать')
	res = 1
	
	# while res = loop FIGHTING
	while res < 5:
		submit3 = browser.find_element_by_partial_link_text('Атакoвать')
		submit3.click()
		browser.find_element_by_partial_link_text('Атакoвать').click()
		res = res + 1
		print('Fighting Success')
	sleep(2)
	
	#Go to main menu
	submit4 = browser.find_element_by_partial_link_text('На главную')
	submit4.click()
	print('Go To Main Menu')
	sleep(1)
	
	#Karier
	submit5 = browser.find_element_by_partial_link_text('Карьера')
	submit5.click()
	print('Karier')
	sleep(2)
	
	#Karier Fihting
	
	try :
		elem1 = browser.find_element_by_css_selector('a.nbtn1.b_red.w130p')
		if elem1.is_displayed():
			elem1.click()
		sleep(3)
	except NoSuchElementException :
		elem1 = browser.find_element_by_partial_link_text('На главную')
		elem1.click()
		print('No Found. Go to Main Menu')
		sleep(1)
	
	#Go to main menu
	submit6 = browser.find_element_by_partial_link_text('На главную')
	submit6.click()
	print('Go To Main Menu')
	sleep(1)
	
	#Karier
	submit7 = browser.find_element_by_partial_link_text('Карьера')
	submit7.click()
	print('Karier')
	sleep(2)
	
	try :
		elem2 = browser.find_element_by_css_selector('a.nbtn1.b_red.w130p')
		if elem2.is_displayed():
			elem2.click()
		sleep(3)
	except NoSuchElementException :
		elem2 = browser.find_element_by_partial_link_text('На главную')
		elem2.click()
		print('No Found. Go to Main Menu')
		sleep(1)
	
	#Go to main menu
	submit8 = browser.find_element_by_partial_link_text('На главную')
	submit8.click()
	print('Go To Main Menu')
	sleep(1)
	
	#Karier
	submit9 = browser.find_element_by_partial_link_text('Карьера')
	submit9.click()
	print('Karier')
	sleep(2)
	
	try :
		elem3 = browser.find_element_by_css_selector('a.nbtn1.b_red.w130p')
		if elem3.is_displayed():
			elem3.click()
		sleep(3)
	except NoSuchElementException :
		elem3 = browser.find_element_by_partial_link_text('На главную')
		elem3.click()
		print('No Found. Go to Main Menu')
		sleep(1)
	
	#Go to main menu
	submit10 = browser.find_element_by_partial_link_text('На главную')
	submit10.click()
	print('Go To Main Menu')
	sleep(1)
	
	#Karier
	submit11 = browser.find_element_by_partial_link_text('Карьера')
	submit11.click()
	print('Karier')
	sleep(2)
	
	try :
		elem4 = browser.find_element_by_css_selector('a.nbtn1.b_red.w130p')
		if elem4.is_displayed():
			elem4.click()
		sleep(3)
	except NoSuchElementException :
		elem4 = browser.find_element_by_partial_link_text('На главную')
		elem4.click()
		print('No Found. Go to Main Menu')
		sleep(1)
	
	#Go to main menu
	submit11 = browser.find_element_by_partial_link_text('На главную')
	submit11.click()
	print('Go To Main Menu')
	sleep(1)
	
	#Karier
	submit12 = browser.find_element_by_partial_link_text('Карьера')
	submit12.click()
	print('Karier')
	sleep(2)
	
	try :
		elem5 = browser.find_element_by_css_selector('a.nbtn1.b_red.w130p')
		if elem5.is_displayed():
			elem5.click()
		sleep(3)
	except NoSuchElementException :
		elem5 = browser.find_element_by_partial_link_text('На главную')
		elem5.click()
		print('No Found. Go to Main Menu')
		sleep(1)
	
	#Go to main menu	
	submit13 = browser.find_element_by_partial_link_text('На главную')
	submit13.click()
	print('Go To Main Menu')
	sleep(1)
	
	#Karier
	submit14 = browser.find_element_by_partial_link_text('Карьера')
	submit14.click()
	print('Karier')
	sleep(2)
	
	try :
		elem6 = browser.find_element_by_css_selector('a.nbtn1.b_red.w130p')
		if elem6.is_displayed():
			elem6.click()
		sleep(3)
	except NoSuchElementException :
		elem6 = browser.find_element_by_partial_link_text('На главную')
		elem6.click()
		print('No Found. Go to Main Menu')
		sleep(1)
	 
	#Go to main menu
	submit15 = browser.find_element_by_partial_link_text('На главную')
	submit15.click()
	print('Go To Main Menu')
	sleep(1)
	
	#Karier
	submit16 = browser.find_element_by_partial_link_text('Карьера')
	submit16.click()
	print('Karier')
	sleep(2)
	
	try :
		elem7 = browser.find_element_by_partial_link_text('ЗАБРАТЬ НАГРАДУ')
		if elem7.is_displayed():
			elem7.click()
		sleep(3)
	except NoSuchElementException :
		elem7 = browser.find_element_by_partial_link_text('На главную')
		elem7.click()
		print('No Found. Go to Main Menu')
		sleep(1)
	
	#Go to main menu
	submit17 = browser.find_element_by_partial_link_text('На главную')
	submit17.click()
	print('Go To Main Menu')
	sleep(1)
	
	#Go to Wars
	submit23 = browser.find_element_by_partial_link_text('Сражения')
	submit23.click()
	print('Go To WARS')
	sleep(3)
	
	#Go to League 
	submit38 = browser.find_element_by_partial_link_text('Лига опытных')
	submit38.click()
	print('Go To League')
	sleep(1)
	
	#League Prise
	try :
		elem15 = browser.find_element_by_partial_link_text('Забрать награду')
		if elem15.is_displayed():
			elem15.click()
	except NoSuchElementException :
		elem15 = browser.find_element_by_partial_link_text('Атаковать')
		elem15.click()
		print('Fighting')
		sleep(1)
	
	#Go to Main Menu
	submit39 = browser.find_element_by_partial_link_text('На главную')
	submit39.click()
	print('Go To Main Menu')
	sleep(1)
	
	#Go to Wars
	submit43 = browser.find_element_by_partial_link_text('Сражения')
	submit43.click()
	print('Go To WARS')
	sleep(3)
	
	#Go to League 
	submit40 = browser.find_element_by_partial_link_text('Лига опытных')
	submit40.click()
	print('Go To League')
	sleep(1)
	
	try :
		elem16 = browser.find_element_by_partial_link_text('Забрать награду')
		if elem16.is_displayed():
			elem16.click()
		sleep(3)
	except NoSuchElementException :
		elem16 = browser.find_element_by_partial_link_text('Атаковать')
		elem16.click()
		print('Fighting')
		sleep(3)
	
	#Go to Main Menu
	submit41 = browser.find_element_by_partial_link_text('На главную')
	submit41.click()
	print('Go To Main Menu')
	sleep(1)
	
	#Go to Wars
	submit44 = browser.find_element_by_partial_link_text('Сражения')
	submit44.click()
	print('Go To WARS')
	sleep(3)
	
	#Go to League 
	submit42 = browser.find_element_by_partial_link_text('Лига опытных')
	submit42.click()
	print('Go To League')
	sleep(3)
	
	try :
		elem17 = browser.find_element_by_partial_link_text('Забрать награду')
		if elem17.is_displayed():
			elem17.click()
		sleep(3)
	except NoSuchElementException :
		elem17 = browser.find_element_by_partial_link_text('Атаковать')
		elem17.click()
		print('Fighting')
		sleep(3)
	
	#Go to Main Menu
	submit9 = browser.find_element_by_partial_link_text('На главную')
	submit9.click()
	print('Go To Main Menu')
	sleep(1)
	
	#Cave
	submit18 = browser.find_element_by_partial_link_text('Пещера ')
	submit18.click()
	print('Go To Cave')
	sleep(1)
	
	#Find Cave
	try :
		elem8 = browser.find_element_by_partial_link_text('Новый поиск')
		if elem8.is_displayed():
			elem8.click()
		sleep(3)
	except NoSuchElementException :
		browser.back()
		browser.refresh()
		elem8 = browser.find_element_by_partial_link_text('На главную')
		elem8.click()
		print('No Found. Go to Main Menu')
		sleep(1)
	
	#Go to main menu
	submit19 = browser.find_element_by_partial_link_text('На главную')
	submit19.click()
	print('Go To Main Menu')
	sleep(1)
	
	#Sage
	submit20 = browser.find_element_by_partial_link_text('Хижина мудреца')
	submit20.click()
	print('Go To Sage')
	sleep(1)
	
	#Go to Tasks
	submit21 = browser.find_element_by_partial_link_text('Задания')
	submit21.click()
	print('Go to Tasks')
	sleep(3)
	
	#Prise if
	try :
		elem9 = browser.find_element_by_partial_link_text('Получить награду')
		if elem9.is_displayed():
			elem9.click()
		sleep(3)
	except NoSuchElementException :
		elem9 = browser.find_element_by_partial_link_text('На главную')
		elem9.click()
		print('No Found. Go to Main Menu')
		sleep(3)
	
	try :
		elem25 = browser.find_element_by_partial_link_text('Получить награду')
		if elem25.is_displayed():
			elem25.click()
		sleep(3)
	except NoSuchElementException :
		elem25 = browser.find_element_by_partial_link_text('На главную')
		elem25.click()
		print('No Found. Go to Main Menu')
		sleep(3)
	
	try :
		elem26 = browser.find_element_by_partial_link_text('Получить награду')
		if elem26.is_displayed():
			elem26.click()
		sleep(3)
	except NoSuchElementException :
		elem25 = browser.find_element_by_partial_link_text('На главную')
		elem25.click()
		print('No Found. Go to Main Menu')
		sleep(3)
	
	#go to main menu
	submit22 = browser.find_element_by_partial_link_text('На главную')
	submit22.click()
	print('Go To Main Menu')
	sleep(1)
	
	#Go to Wars
	submit23 = browser.find_element_by_partial_link_text('Сражения')
	submit23.click()
	print('Go To WARS')
	sleep(3)
	
	submit24 = browser.find_element_by_partial_link_text('Долина бессмертных')
	submit24.click()
	print('Go To WARS 1')
	sleep(3)
	#browser.back()
	#browser.refresh()
	try :
		elem10 = browser.find_element_by_partial_link_text('Подать заявку')
		if elem10.is_displayed():
			elem10.click()
		sleep(3)
	except NoSuchElementException :
	
		browser.back()
		browser.refresh()
		elem10 = browser.find_element_by_partial_link_text('На главную')
		elem10.click()
		print('No Found. Go to Main Menu')
		sleep(3)
	try :
		elem30 = browser.find_element_by_partial_link_text('Атаковать')
		if elem30.is_displayed():
			elem30.click()
		sleep(3)
	except NoSuchElementException :
	
		elem30 = browser.find_element_by_partial_link_text('На главную')
		elem30.click()
		print('No Found. Go to Main Menu')
		sleep(3)
	
	
	
	#go to main menu
	submit25 = browser.find_element_by_partial_link_text('На главную')
	submit25.click()
	print('Go To Main Menu')
	sleep(1)
	
	#Go to Wars
	submit26 = browser.find_element_by_partial_link_text('Сражения')
	submit26.click()
	print('Go To WARS 2')
	sleep(3)
	
	submit27 = browser.find_element_by_partial_link_text('Король бессмертных')
	submit27.click()
	print('Go To WARS 3')
	sleep(3)
	
	try :
		elem11 = browser.find_element_by_partial_link_text('Подать заявку')
		if elem11.is_displayed():
			elem11.click()
		sleep(3)
	except NoSuchElementException :
		browser.back()
		browser.refresh()	
		elem11 = browser.find_element_by_partial_link_text('На главную')
		elem11.click()
		print('No Found. Go to Main Menu')
		sleep(3)
	

	#go to main menu
	submit28 = browser.find_element_by_partial_link_text('На главную')
	submit28.click()
	print('Go To Main Menu')
	sleep(1)
	
	#Go to Wars
	submit29 = browser.find_element_by_partial_link_text('Сражения')
	submit29.click()
	print('Go To WARS 4')
	sleep(3)
	
	submit30 = browser.find_element_by_partial_link_text('Клановый турнир')
	submit30.click()
	print('Go To WARS 4')
	sleep(3)
	
	try :
		elem12 = browser.find_element_by_partial_link_text('Подать заявку')
		if elem12.is_displayed():
			elem12.click()
		sleep(3)
	except NoSuchElementException :
		browser.back()
		browser.refresh()	
		elem12 = browser.find_element_by_partial_link_text('На главную')
		elem12.click()
		print('No Found. Go to Main Menu')
		sleep(3)
	
	#go to main menu
	submit31 = browser.find_element_by_partial_link_text('На главную')
	submit31.click()
	print('Go To Main Menu')
	sleep(1)
	
	#Go to Wars
	submit32 = browser.find_element_by_partial_link_text('Сражения')
	submit32.click()
	print('Go To WARS 5')
	sleep(3)
	
	submit33 = browser.find_element_by_partial_link_text('Древние алтари')
	submit33.click()
	print('Go To WARS 5')
	sleep(3)	

	try :
		elem13 = browser.find_element_by_partial_link_text('Подать заявку')
		if elem13.is_displayed():
			elem13.click()
		sleep(3)
	except NoSuchElementException :
		browser.back()
		browser.refresh()
		elem13 = browser.find_element_by_partial_link_text('На главную')
		elem13.click()
		print('No Found. Go to Main Menu')
		sleep(3)
	
	#go to main menu
	submit34 = browser.find_element_by_partial_link_text('На главную')
	submit34.click()
	print('Go To Main Menu')
	sleep(1)
	
	#Gold
	submit35 = browser.find_element_by_partial_link_text('Получить золото')
	submit35.click()
	print('Gold Success')
	sleep(1)
	
	#Gold 2
	submit36 = browser.find_element_by_partial_link_text('Обменник золота')
	submit36.click()
	print('Gold Success 2')
	sleep(1)

	try :
		elem14 = browser.find_element_by_partial_link_text('Обменять')
		if elem14.is_displayed():
			elem14.click()
		sleep(3)
	except NoSuchElementException :
	
		elem14 = browser.find_element_by_partial_link_text('На главную')
		elem14.click()
		print('No Found. Go to Main Menu')
		sleep(3)


	#go to main menu
	submit37 = browser.find_element_by_partial_link_text('На главную')
	submit37.click()
	print('Go To Main Menu')
	sleep(1)

	browser.close()	
	sleep(3600)
loop = loop + 1
