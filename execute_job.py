import requests

def execute_job(url, user, password, id_job, id_credential):
    auth = (user, password)

    url = f"{url}/api/v2/job_templates/{id_job}/launch/"

    exvars = input("¿Desea agregar variables extra? (s/n): ")
    if exvars == "s":
        extra_vars = {}
        values = input("Introduzca las variables extras separadas por comas: ")
        elements = values.split(",")
        for element in elements:
            key, value = element.split("=")
            extra_vars[key] = value
        payload = {"extra_vars": extra_vars, "credentials": [id_credential]}
    else:
        payload = {"extra_vars": {}, "credentials": [id_credential]}

    response = requests.post(url, auth=auth, json=payload)

    if response.status_code == 201:
        job_id = response.json()["job"]
        return {"status": "success", "job_id": job_id}
    else:
        return {"status": "error", "message": response.text}
