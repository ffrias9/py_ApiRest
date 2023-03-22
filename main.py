from execute_job import *
from getpass import getpass
from time import sleep
from colorama import Fore

def menu():
    print("")
    print(Fore.YELLOW + "1 - Ejecutar job")
    print("2 - Ejecutar workflow")
    print("3 - Salir")
    print("")
   
opcion=0
while opcion not in range(1,3):
    menu()
    opcion = int(input("Seleccione una opción: " + Fore.RESET))
    print("")
    if opcion == 3:
        quit()
    if opcion not in (1,2):
        print(Fore.RED + "Seleccione una opción correcta [1-3]." + Fore.RESET)
        sleep(2)

url = "http://192.168.10.50"
user = input("Introduzca el nombre de usuario: ")
password = getpass("Introduzca la contraseña: ")
id_job = input("Introduzca el job id: ")

if opcion == 1:
    id_credential = input("Introduzca el id de las credenciales: ")
    output = execute_job(url, user, password, id_job, id_credential)
elif opcion == 2:
    output = execute_workflow_job(url, user, password, id_job)

print(output)
