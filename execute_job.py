import requests

def execute_job(url, user, password, id_job, id_credential):
    auth = (user, password)

    url = f"{url}/api/v2/job_templates/{id_job}/launch/"
    
    exvars="x"
    while exvars not in ("s","n","S","N"):
        exvars = input("¿Desea agregar variables extra? (s/n): ")
    if exvars in ("s","S"):
        extra_vars = {}
        values = input("Introduzca las variables extras separadas por comas: ")
        elements = values.split(",")
        for element in elements:
            key, value = element.split("=")
            extra_vars.update({key: value})
        payload = {"extra_vars": extra_vars, "credentials": [id_credential]}
    else:
        payload = {"extra_vars": {}, "credentials": [id_credential]}

    print(url, auth, payload)
    result = requests.post(url, auth=auth, json=payload)

    if result.status_code == 201:
        return {"status": "success", "job_id": result.json()["job"]}
    else:
        return {"status": "error", "message": result.text}

def execute_workflow_job(url, user, password, id_job):
    auth = (user, password)

    url = f"{url}/api/v2/workflow_job_templates/{id_job}/launch/"

    exvars="x"
    while exvars not in ("s","n","S","N"):
        exvars = input("¿Desea agregar variables extra? (s/n): ")
    if exvars in ("s","S"):
        extra_vars = {}
        values = input("Introduzca las variables extras separadas por comas: ")
        elements = values.split(",")
        for element in elements:
            key, value = element.split("=")
            extra_vars.update({key: value})
        payload = {"extra_vars": extra_vars}
    else:
        payload = {"extra_vars": {}}

    result = requests.post(url, auth=auth, json=payload)

    if result.status_code == 201:
        return {"status": "success", "job_id": result.json()["workflow_job"]}
    else:
        return {"status": "error", "message": result.text}
