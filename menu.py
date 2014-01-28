'''
Created on 04/11/2013

@author: asketsus
'''
import os
from file import *
from odds import *
from partido import *
from probability import *

code = 0

boleto = []

for key in range(14):
    partido = Partido()
    boleto.append(partido)

while True:
    
    os.system("clear")
    
    print """###################################################################
################     QUINIWIN (by asketsus)     ###################
###################################################################
             
             1) Load file from URL
             2) Load file from URL (with code)
             3) Load file from HD
             4) Show current file
             5) Load odds for current file
             6) Calculate probability
             7) Execute all
              """
    if code != 0:
        print "Current code => " + str(code) + "\n"         
    option = raw_input("Enter option (exit to close): ")
    
    if option == "1":
        code = load_code(boleto)
    elif option == "2":
        code = load_quini(boleto)
    elif option == "3":
        code = load_boleto()
    elif option == "4":
        if code == 0:
            print "\n\nDo not exists file currently selected."
        else:
            show_boleto(boleto)
    elif option == "5":
        get_odds(boleto)
    elif option == "6":
        getProbability(boleto)
    elif option == "7":
        code = load_code(boleto)
        get_odds(boleto)
        getProbability(boleto)
    elif option == "exit":
        break
    
    raw_input("\n\nPress any key to continue...")
    