from execute_job import execute_job
from getpass import getpass

url = "http://192.168.10.50"
user = input("Introduzca el nombre de usuario: ")
password = getpass("Introduzca la contraseña: ")
id_job = input("Introduzca el job id: ")
id_credential = input("Introduzca el id de las credenciales: ")

output = execute_job(url, user, password, id_job, id_credential)

print(output)
