from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyperclip
import time
import sys
from config import *
import re


from string import *

try:
    if sys.argv[1]:
        with open(sys.argv[1], 'r', encoding='utf8') as f:
            groups = [group.strip() for group in f.readlines()]
except IndexError:
    print('Please provide the group name as the first argument.')

with open('msg.txt', 'r', encoding='utf8') as f:
    msg = f.read()

options = webdriver.ChromeOptions()
options.add_argument(CHROME_PROFILE_PATH)



browser = webdriver.Chrome(executable_path= win_chrome, options=options)



browser.maximize_window()

browser.get('https://web.whatsapp.com/')

for group in groups:
    search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'

    search_box = WebDriverWait(browser, 500).until(EC.presence_of_element_located((By.XPATH, search_xpath)))
    search_box.clear()
    time.sleep(1)
    pyperclip.copy(group)
    search_box.send_keys(Keys.COMMAND +"v" + Keys.RETURN)  # Keys.CONTROL + "v"  # INGRESA CONTACTO Y LO SELECCIONA
    time.sleep(2)


    group_xpath = f'//span[@title="{group}"]'
    group_title = browser.find_element_by_xpath(group_xpath)
    group_title.click()
    time.sleep(4)    
    
    while True:
        print("inicia while")
        
        text_box = browser.find_element(By.CLASS_NAME, "y8WcF") # IDENTIFICA CAJA DE TEXTO
        a= text_box.text # variable que captura todo el texto del chat  
       
        last_line = a.strip().split("\n")[-2] # captura solo la ultima linea digitada
        print( "esta es la ultima linea  "+ last_line)
        time.sleep(5) # esta linea es una pausa de espera para ver que se captura comando
        

        try:

         comando = re.search( r"777", str(last_line))
         #print(comando)
         print(comando.group(0)) #imprime solo la palabra
         cmd = comando.group(0)
        except:
         continue
        
        if comando:
          print( "comando existe")
         
          input_xpath = "_1LbR4" #//body/div[@id='app']/div[1]/div[1]/div[4]/div[1]/footer[1]/div[1]/div[1]/span[2]/div[1]/div[2]/div[1]/div[1]"
          print( "localiza caja de envio de texto")
          input_box = browser.find_element(By.CLASS_NAME, input_xpath) 
          pyperclip.copy(msg)
          print("copia mensaje")
          input_box.send_keys(Keys.CONTROL +"v")   # Keys.CONTROL + "v"
          print("pega mensaje")
          browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/footer[1]/div[1]/div[1]/span[2]/div[1]/div[2]/div[2]/button[1]" ).click()
          print( "hace clic para enviar mensaje")
          #input_box.send_keys(Keys.ENTER)
          print( "############# se envio mensaje ############# ")

      
   