'''
Created on 04/11/2013

@author: asketsus
'''
import os
from bs4 import BeautifulSoup
from urllib2 import urlopen
from partido import *

def eliminar_tildes(cadena):
    cadena = cadena.replace("\xc3\xa1","A").replace("\xc3\xa9","E").replace("\xc3\xad", "I").replace("\xc3\xb3", "O").replace("\xc3\xba", "U")
    cadena = cadena.replace("\xc3\x81","A").replace("\xc3\x89","E").replace("\xc3\x8d", "I").replace("\xc3\x93", "O").replace("\xc3\x9a", "U")
    cadena = cadena.upper()
    return cadena
        
def save_file(code, boleto):
    import csv
    w = csv.writer(open(str(code)+".csv", "w"))
    for key, val in boleto.items():
        w.writerow([key, val[0], val[1]])
        
def load_file(code):
    import csv
    dict = {}
    for key, valhome, valaway in csv.reader(open(str(code)+".csv")):
        dict[int(key)] = [valhome, valaway]
               
    return dict
 
def load_quini(boleto, code=0):
    boletoURL = {}
    
    os.system("clear")
    if code==0:
        code = raw_input("Please insert the current code: ")

    url = "http://www.loteriasyapuestas.es/es/la-quiniela/sorteos/2013/" + code

    soup = BeautifulSoup(urlopen(url))
    
    # Get column number
    for link in soup.find("ul", "derecha"):
        data = (str(link)).strip().replace("<li>","").replace("</li>","").strip()
        
        if data == "":
            continue
        
        boletoURL[int(data)] = ""
        
    # Get local team
    i = 1
    for element in soup.find("div", "cuerpoRegionLeft").find_all("ul")[1]:
        element = (str(element)).strip().replace("<li>","").replace("</li>","").strip()
        element = eliminar_tildes(element)
        
        if element == "":
            continue
        
        boletoURL[i] = [element,]
        i+=1
        
    # Get visitor team
    i = 1
    for element in soup.find("div", "cuerpoRegionLeft").find_all("ul")[2]:
        element = (str(element)).strip().replace("<li>","").replace("</li>","").strip()
        element = eliminar_tildes(element)
        
        if element == "":
            continue
        
        boletoURL[i].append(element)
        i+=1
        
    save_file(code, boletoURL)

    for i in range(0,14):
        boleto[i].putNombreQuini(boletoURL[i+1][0], boletoURL[i+1][1])

    show_boleto(boleto)

    return code
    
def load_boleto():
    os.system("clear")
    code = raw_input("Please insert the current code: ")
    
    boleto = load_file(code)
    show_boleto(boleto)
    
    return code

def load_boleto_code(code):
    os.system("clear")
    boleto = load_file(code)
    show_boleto_obsolete(boleto)
    
    return code

def show_boleto_file(boleto):
    for element in range(14):
        print str(element+1) + ")\t" + boleto[element+1][0] + " - " + boleto[element+1][1]

def show_boleto(boleto):
    for i in range(14):
        print boleto[i].getNombreQuini()

def load_code(boleto):
    url = "http://www.loteriasyapuestas.es/es/la-quiniela"
    soup = BeautifulSoup(urlopen(url))

    for link in soup.find("div", "botonJugarPeq").find_all('a', href=True):
        url = "http://www.loteriasyapuestas.es" + str(link['href'])

    soup = BeautifulSoup(urlopen(url))
    for link in soup.find("div", "enlace").find_all('a', href=True):
        fullcode = link['href']

    pos = 1
    newpos = 1

    while newpos > 0:
        pos = newpos
        newpos = fullcode.find("/", pos+1)

    code = load_quini(boleto, fullcode[pos+1:])
    return code



    