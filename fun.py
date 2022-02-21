
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
from fun import *
from demo import *

from string import *


def chat(browser):
    #### for para caprturar textos y actualizarlos cada 10 segundos 
   
