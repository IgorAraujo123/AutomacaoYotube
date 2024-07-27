import pyautogui
import time
from tkinter.simpledialog import askstring 

pyautogui.PAUSE = 0.5

# Passo 1: Entrar no sistema

# Entrar no navegador
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# Entrar no site
link = 'https://www.youtube.com/'
pyautogui.write(link)
pyautogui.press('enter')

# Dar uma pausa um pouco maior 3 segundos
time.sleep(3)

#Procurar o canal
canal = askstring(title='canal', prompt= 'Coloque o nome do canal (Não coloque nenhuma acentuação)')
pyautogui.click(x=575,y=140)
pyautogui.write(canal)
pyautogui.press('enter')

# Dar uma pausa um pouco maior 3 segundos
time.sleep(3)

#Ver videos mais recentes
pyautogui.click(x=948,y=213)

# Dar uma pausa um pouco maior 3 segundos
time.sleep(3)

#clicar no video mais recente
pyautogui.click(x=576,y=409)
