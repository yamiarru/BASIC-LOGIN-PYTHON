# -*- coding: utf-8 -*-
#!/usr/bin/env python
import time
import os
import sys
import sqlite3
import getpass

#declaracion de variables

registeredUser = ('KathyDally','KimCol','GuestUser')
registeredPW = ('code2016')

#declaracion de funciones
def login(usuario,passw):
    if usuario in registeredUser:
        if passw in registeredPW:
            return 1
        else:
            print("\n\tPassword does not match...\n")
    else:
        return 2

 #inicializacion de procesos
usuario=input('User: ')
passw = getpass.getpass('Password: ')

if login(usuario,passw)==1:
    print('Welcome ',usuario)
else:
    print('ERROR! User is not registered.')
