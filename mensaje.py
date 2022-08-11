import os, sys, time
while True:
 try:
  import requests
  break
 except ModuleNotFoundError:
  os.system("pip install requests")
while True:
 try:
  from lolpython import lol_py
  break
 except ModuleNotFoundError:
  os.system("pip install lolpython")

class color:
    morado = '\033[95m'
    blanco = '\033[97m'
    cyan = '\033[96m'
    azul  = '\033[94m'
    verde = '\033[92m'
    amarillo = '\033[93m'
    rojo = '\033[91m'
    fin = '\033[0m'



def banner():
 os.system("clear")
 print(f"""{color.cyan}
███████╗███████╗███╗  ██╗██████╗ ██╗██████╗
██╔════ ██╔════╝████╗ ██║██╔══██╗██║██╔══██╗
█████╗  █████╗  ██╔██╗██║██████╔╝██║██████╔╝
██╔══   ██╔══╝  ██║╚████║██╔══██╗██║██╔══██╗
██║     ███████╗██║ ╚███║██║  ██║██║██║  ██║
╚═╝     ╚══════╝╚═╝  ╚══╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝""")
 print(f"{color.fin}")

def cabecera():
 os.system("clear")
 print(f"""{color.cyan}

 ██████╗███╗   ███╗ ██████╗████████╗███╗   ███╗██╗   ██╗██╗  ██╗
██╔════╝████╗ ████║██╔════╝╚══██╔══╝████╗ ████║██║   ██║╚██╗██╔╝
╚█████╗ ██╔████╔██║╚█████╗    ██║   ██╔████╔██║██║   ██║ ╚███╔╝
 ╚═══██╗██║╚██╔╝██║ ╚═══██╗   ██║   ██║╚██╔╝██║██║   ██║ ██╔██╗
██████╔╝██║ ╚═╝ ██║██████╔╝   ██║   ██║ ╚═╝ ██║╚██████╔╝██╔╝╚██╗
╚═════╝ ╚═╝     ╚═╝╚═════╝    ╚═╝   ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝""")
def version():
 texto ="""
 |=======================================================|
 | Script by              : #FENRIR-00                   |
 | Version                : Version  1.2                 |
 | Follow me on Github    : https://github.com/Fenrir-00 |
 | Contact me on Telegram : @Ritorito1990                |
 ========================================================= """
 lol_py(texto)
def carga():
    print(f"{color.verde}")
    print("""Loading…
    █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…10%
    ███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…30%
    █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…50%
    ██████████▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…70%
    █████████████▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…100%
    ███████████████████""")
    time.sleep(1)
    os.system("clear")
    banner()

def incorrecto():
    os.system("clear")
    print(f"""{color.rojo}
░█████╗░██████╗░░█████╗░██╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗░██║
██║░░██║██████╔╝██║░░╚═╝██║██║░░██║██╔██╗██║
██║░░██║██╔═══╝░██║░░██╗██║██║░░██║██║╚████║
╚█████╔╝██║░░░░░╚█████╔╝██║╚█████╔╝██║░╚███║
░╚════╝░╚═╝░░░░░░╚════╝░╚═╝░╚════╝░╚═╝░░╚══╝


██╗███╗░░██╗░█████╗░░█████╗░██████╗░██████╗░
██║████╗░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║██╔██╗██║██║░░╚═╝██║░░██║██████╔╝██████╔╝
██║██║╚████║██║░░██╗██║░░██║██╔══██╗██╔══██╗
██║██║░╚███║╚█████╔╝╚█████╔╝██║░░██║██║░░██║
╚═╝╚═╝░░╚══╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝

███████╗░█████╗░████████╗░█████╗░
██╔════╝██╔══██╗╚══██╔══╝██╔══██╗
█████╗░░██║░░╚═╝░░░██║░░░███████║
██╔══╝░░██║░░██╗░░░██║░░░██╔══██║
███████╗╚█████╔╝░░░██║░░░██║░░██║
╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝{color.fin}""")
    time.sleep(4)
    menu()

def salir():
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…
    █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…10%
    ███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…30%
    █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…50%
    ██████████▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…70%
    █████████████▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…100%
    ███████████████████""")
    time.sleep(1)
    os.system("clear")
    print(f"{color.fin}")
    sys.exit()
def menu():
    os.system("clear")
    banner()
    carga()
    cabecera()
    version()
    print()
    print(f"{color.morado}TE GUSTARIA MANDAR UN SMS ANONIMO")
    print("")
    print(f"{color.verde}[1]MANDAR MENSAJE")
    print(f"{color.rojo}[0]SALIR{color.fin}")
    print()
    eleccion =input(f"{color.cyan}ELIJE UN NUMERO >>{color.fin} ")
    if eleccion == "1" :
     mensaje()
    elif eleccion == "0" :
     banner
     salir() 
    else:
        incorrecto()

def mensaje():
 banner()
 print()
 print(f"{color.verde}INTRODUCE TU API EJEMPLO: 69a6acf160d28cc.....{color.fin}")
 print(f"{color.amarillo}PUEDES CONSEGUIRLA EN: https://textbelt.com{color.fin}")
 print()
 var =input(f"{color.cyan}INTROCUDE TU API >> {color.fin}")
 banner()
 print()
 print(f"{color.verde}INTRODUCE TELEFONO CON CODIGO DE PAIS ESPAÑA = +34 VENEZUEL = +58{color.fin}")
 print(f"{color.amarillo}EJEMPLO: +3466666...{color.fin}")
 print()
 var1 =input(f"{color.cyan}INTRODUCE NUMERO DE TELEFONO >> {color.fin}")
 banner()
 print(f"{color.verde}INTRODUCE TU MENSAJE {color.fin}")
 print(f"{color.amarillo}PULSA ENTER PARA ENVIARLO {color.fin}")
 print()
 var2 =input(f"{color.cyan}INTRODUCE TU MENSAJE >> {color.fin}")
 resp = requests.post('https://textbelt.com/text', {
   'phone': (var1),
   'message': (var2),
   'key': (var),
 })
 banner()
 print(f"{color.amarillo} COMPROBACION SI SE MANDO CORRECTAMENTE {color.fin}")
 print(resp.json())
 time.sleep(3)
 print(f"{color.morado}QUE QUIERES HACER AHORA{color.fin}")
 print()
 print(f"{color.azul}[1] VOLVER")
 print(f"{color.rojo}[0] SALIR{color.fin}")
 print()
 var=input(f"{color.cyan}ELIJE UN NUMERO >> {color.fin}")
 if var == "1":
  menu()
 elif var == "0":
  salir()
 else :
  incorrecto()
menu()
