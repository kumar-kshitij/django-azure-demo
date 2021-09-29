# SIGA Backend Server

SIGA Backend Server is our main backend server based on [Django](https://github.com/django/django).

## Installation

Please ensure you have latest version of package manager [pip](https://pip.pypa.io/en/stable/) before proceeding with installation.

```bash
$ pip install -r requirements.txt
```

## Usage

Kickstart the backend server using the commands
``` bash
$ python manage.py migrate
$ python manage.py runserver 
```
Django Server runs on port 8000 by default

**REST API Endpoints**
>**POST**
>>{base_url}/api/v1/
>
> message: user message in plaintext
>
> language:  "en" for English Or "hi" for Hindi

``` bash
$ curl -d '{"message":"Hi","language":"en"}' -H 'Content-Type: application/json' -X POST {server_base_url}/api/v1/
```

## Deployment
The backend server is deployed with the help of [Azure App Service](https://azure.microsoft.com/en-in/services/app-service/web/) and can be accessed @ [https://simpledjango.azurewebsites.net](https://simpledjango.azurewebsites.net)



