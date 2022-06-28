<p align="center">
 <img width="500px" src="https://www.issgovernance.com/file/images/iss_logo_header-1.png" align="center" alt="GitHub Readme Stats" />
 <h2 align="center">Service and UI to Showcase Named Entity Recognition.</h2>
</p>
<p align="center">
 <h2 align="center">By Farbod Ghiasi.</h2>
    <p align="center">
     <img width="500px" src="https://media-exp1.licdn.com/dms/image/C4D03AQGT3BF-pO2AOw/profile-displayphoto-shrink_400_400/0/1654327975308?e=1661990400&v=beta&t=6VcaEJQnHDloHzjmluKqD0GZPwwgPsl1HfAGY0PzXX8" align="center" alt="GitHub Readme Stats" />
    </p>
</p>
# Hello, folks! <img src="https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/wave.gif" width="30px" height="30px" />

My name is Farbod Ghiasi and recent graduate of the University of California with a Bachelor of Science in Computer Science, with an emphasis in Intelligent Systems. You can find me on [LinkedIn][3.2].

## 🔧 Technologies & Tools
![](https://img.shields.io/badge/OS-Ubuntu-informational?style=flat&logo=Ubuntu&logoColor=white&color=orange)
![](https://img.shields.io/badge/Editor-IntelliJ_IDEA-informational?style=flat&logo=PyCharm&logoColor=white&color=black)
![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/UI-H2oWave-informational?style=flat&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/Server-FastAPI-informational?style=flat&logo=FastAPI&logoColor=white&color=green)
![](https://img.shields.io/badge/Tools-spaCy-informational?style=flat&logo=spaCy&logoColor=white&color=blue)
![](https://img.shields.io/badge/Tools-Docker-informational?style=flat&logo=docker&logoColor=blue&color=blue)

[3.2]: https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/linkedin-3-16.png (LinkedIn icon without padding)


<!-- links to your social media accounts -->

[3]: https://www.linkedin.com/in/farbod-ghiasi-87401b96/

[//]: # ()
(## DEMO: https://youtu.be/7ajLhxPmnzY)

[//]: # (To use this repository as starter for your project you can run `configure_project.sh` script, which sets up all variables and file names. This way you can avoid configuring and renaming things yourself:)

[//]: # ()
[//]: # (```shell)

[//]: # (./configure_project.sh MODULE="coolproject" REGISTRY="docker.pkg.github.com/martinheinz/repo-name")

[//]: # (```)

[//]: # ()
[//]: # (## Running)

[//]: # ()
[//]: # (### Using Python Interpreter)

[//]: # (```shell)

[//]: # (~ $ make run)

[//]: # (```)

[//]: # ()
[//]: # (### Using Docker)

[//]: # ()
[//]: # (Development image:)

[//]: # (```console)

[//]: # (~ $ make build-dev)

[//]: # (~ $ docker images --filter "label=name=blueprint")

[//]: # (REPOSITORY                                                             TAG                 IMAGE ID            CREATED             SIZE)

[//]: # (docker.pkg.github.com/martinheinz/python-project-blueprint/blueprint   3492a40-dirty       acf8d09acce4        28 seconds ago      967MB)

[//]: # (~ $ docker run acf8d09acce4)

[//]: # (Hello World...)

[//]: # (```)

[//]: # ()
[//]: # (Production &#40;Distroless&#41; image:)

[//]: # (```console)

[//]: # (~ $ make build-prod VERSION=0.0.5)

[//]: # (~ $ docker images --filter "label=version=0.0.5")

[//]: # (REPOSITORY                                                             TAG                 IMAGE ID            CREATED             SIZE)

[//]: # (docker.pkg.github.com/martinheinz/python-project-blueprint/blueprint   0.0.5               65e6690d9edd        5 seconds ago       86.1MB)

[//]: # (~ $ docker run 65e6690d9edd)

[//]: # (Hello World...)

[//]: # (```)

[//]: # ()
[//]: # (## Testing)

[//]: # ()
[//]: # (Test are ran every time you build _dev_ or _prod_ image. You can also run tests using:)

[//]: # ()
[//]: # (```console)

[//]: # (~ $ make test)

[//]: # (```)

[//]: # ()
[//]: # (<div align="center">)

[//]: # ()
[//]: # (![logo]&#40;https://user-images.githubusercontent.com/30027932/134270064-baecfbec-b3e7-4cb7-a07e-c11a58526260.png&#41;)

[//]: # ()
[//]: # ()
[//]: # ([![Mentioned in Awesome <INSERT LIST NAME>]&#40;https://awesome.re/mentioned-badge-flat.svg&#41;]&#40;https://github.com/mjhea0/awesome-fastapi#boilerplate&#41;)

[//]: # ([![License]&#40;https://img.shields.io/cocoapods/l/AFNetworking?style=flat-square&#41;]&#40;https://github.com/rednafi/think-asyncio/blob/master/LICENSE&#41;)

[//]: # ([![Twitter]&#40;https://img.shields.io/twitter/follow/rednafi?style=flat-square&#41;]&#40;https://twitter.com/rednafi&#41;)

[//]: # ()
[//]: # (</div>)

[//]: # ()
[//]: # (## Description)

[//]: # ()
[//]: # (This is a minimalistic and extensible [FastAPI]&#40;https://fastapi.tiangolo.com/&#41; template that incorporates divisional pattern architecture with [divisional folder structure]&#40;https://exploreflask.com/en/latest/blueprints.html#divisional&#41;. It's suitable for developing small to medium sized API oriented micro-services. The architecture is similar to what you'd get with Flask's [Blueprint]&#40;https://exploreflask.com/en/latest/blueprints.html&#41;.)

[//]: # ()
[//]: # (## Features)

[//]: # ()
[//]: # (* It uses [FastAPI]&#40;https://fastapi.tiangolo.com/&#41; framework for API development. FastAPI is a modern, highly performant, web framework for building APIs with Python 3.6+.)

[//]: # ()
[//]: # (* The APIs are served with [Gunicorn]&#40;https://gunicorn.org/&#41; server with multiple [Uvicorn]&#40;https://www.uvicorn.org/&#41; workers. Uvicorn is a lightning-fast "ASGI" server. It runs asynchronous Python web code in a single process.)

[//]: # ()
[//]: # (* Simple reverse-proxying with [Caddy]&#40;https://caddyserver.com/docs/&#41;.)

[//]: # ()
[//]: # (* OAuth2 &#40;with hashed password and Bearer with JWT&#41; based authentication)

[//]: # ()
[//]: # (* [CORS &#40;Cross Origin Resource Sharing&#41;]&#40;https://fastapi.tiangolo.com/tutorial/cors/&#41; enabled.)

[//]: # ()
[//]: # (* Flask inspired divisional folder structure for better decoupling and encapsulation. This is suitable for small to medium backend development.)

[//]: # ()
[//]: # (* Dockerized using **python:3.10-slim-bullseye** and optimized for size and functionality. Dockerfile for Python 3.9 and 3.8 can also be found in the `dockerfiles` directory.)

[//]: # ()
[//]: # (## Quickstart)

[//]: # ()
[//]: # (### Run the app in containers)

[//]: # ()
[//]: # (* Clone the repo and navigate to the root folder.)

[//]: # ()
[//]: # (* To run the app using Docker, make sure you've got [Docker]&#40;https://www.docker.com/&#41; and [Docker Compose V2]&#40;https://docs.docker.com/compose/cli-command/&#41; installed on your system. From the project's root dirctory, run:)

[//]: # ()
[//]: # (    ```bash)

[//]: # (    docker compose up -d)

[//]: # (    ```)

[//]: # ()
[//]: # (### Or, run the app locally)

[//]: # ()
[//]: # (If you want to run the app locally, without using Docker, then:)

[//]: # ()
[//]: # (* Clone the repo and navigate to the root folder.)

[//]: # ()
[//]: # (* Create a virtual environment. Here I'm using Python's built-in venv in a Unix system. Run:)

[//]: # ()
[//]: # (    ```bash)

[//]: # (    python3.10 -m venv .venv)

[//]: # (    ```)

[//]: # ()
[//]: # (* Activate the environment. Run:)

[//]: # ()
[//]: # (    ```bash)

[//]: # (    source .venv/bin/activate)

[//]: # (    ```)

[//]: # ()
[//]: # (* Go to the folder created by cookie-cutter &#40;default is **fastapi-nano**&#41;.)

[//]: # ()
[//]: # (* Install the dependencies. Run:)

[//]: # ()
[//]: # (    ```bash)

[//]: # (    pip install -r requirements.txt && pip install -r requirements-dev.txt)

[//]: # (    ```)

[//]: # ()
[//]: # (* Start the app. Run:)

[//]: # ()
[//]: # (    ```bash)

[//]: # (    uvicorn app.main:app --port 5000 --reload)

[//]: # (    ```)

[//]: # ()
[//]: # (### Or, pull the Python 3.10 image from DockerHub)

[//]: # ()
[//]: # (If you just want to test out the app without cloning anything, then run:)

[//]: # ()
[//]: # (```)

[//]: # (docker run -p 5000:5000 --expose 5000 rednafi/fastapi-nano:0.1)

[//]: # (```)

[//]: # ()
[//]: # ()
[//]: # (### Check the APIs)

[//]: # ()
[//]: # (* To play around with the APIs, go to the following link on your browser:)

[//]: # ()
[//]: # (    ```)

[//]: # (    http://localhost:5000/docs)

[//]: # (    ```)

[//]: # ()
[//]: # (    This will take you to an UI like below:)

[//]: # ()
[//]: # (    ![Screenshot from 2020-06-21 22-15-18]&#40;https://user-images.githubusercontent.com/30027932/85229723-5b721880-b40d-11ea-8f03-de36c07a3ce5.png&#41;)

[//]: # ()
[//]: # ()
[//]: # (* Press the `authorize` button on the right and add *username* and *password*. The APIs use OAuth2 &#40;with hashed password and Bearer with JWT&#41; based authentication. In this case, the username and password is `ubuntu` and `debian` respectively.)

[//]: # ()
[//]: # (    ![Screenshot from 2020-06-21 22-18-25]&#40;https://user-images.githubusercontent.com/30027932/85229725-5e6d0900-b40d-11ea-9c37-bbee546f84a8.png&#41;)

[//]: # ()
[//]: # (    Clicking the `authorize` button will bring up a screen like this:)

[//]: # ()
[//]: # (    ![Screenshot from 2020-06-21 22-18-59]&#40;https://user-images.githubusercontent.com/30027932/85229729-6036cc80-b40d-11ea-877e-7421b927a849.png&#41;)

[//]: # ()
[//]: # ()
[//]: # ()
[//]: # (* Then select any of the `api_a` or `api_b` APIs and put an integer in the number box and click the `authorize` button.)

[//]: # ()
[//]: # (    ![Screenshot from 2020-06-21 22-31-19]&#40;https://user-images.githubusercontent.com/30027932/85229992-fcad9e80-b40e-11ea-850d-9ca86259d463.png&#41;)

[//]: # ()
[//]: # ()
[//]: # (* Hitting the API should give a json response with random integers.)

[//]: # ()
[//]: # (    ![Screenshot from 2020-06-21 22-32-28]&#40;https://user-images.githubusercontent.com/30027932/85230016-25359880-b40f-11ea-9196-c46fd72a760c.png&#41;)

[//]: # ()
[//]: # ()
[//]: # (* Also, notice the `curl` section in the above screen shot. You can directly use the highlighted curl command in your terminal. Make sure you've got `jq` installed in your system.)

[//]: # ()
[//]: # (    ```bash)
[//]: # (    curl -X GET "http://localhost:5000/api_a/22" \)

[//]: # (         -H "accept: application/json" \)

[//]: # (         -H "Authorization: Bearer $&#40;curl -X POST "http://localhost:5000/token" \)

[//]: # (                            -H "accept: application/x-www-form-urlencoded" \)

[//]: # (                            -d "username=ubuntu&password=debian" | jq -r ".access_token"&#41;")

[//]: # (    ```)

[//]: # ()
[//]: # (    This should show a response like this:)

[//]: # ()
[//]: # (    ```json)

[//]: # (    {)

[//]: # (    "seed": 22,)

[//]: # (    "random_first": 5,)

[//]: # (    "random_second": 13)

[//]: # (    })

[//]: # (    ```)

[//]: # ()
[//]: # (* To test the `GET` APIs with Python, you can use a http client library like [httpx]&#40;https://www.python-httpx.org/&#41;:)

[//]: # ()
[//]: # (    ```python)

[//]: # (    import httpx)

[//]: # ()
[//]: # (    with httpx.Client&#40;&#41; as client:)

[//]: # ()
[//]: # (        # Collect the API token.)

[//]: # (        r = client.post&#40;)

[//]: # (            "http://localhost:5000/token",)

[//]: # (            headers={"Content-Type": "application/x-www-form-urlencoded"},)

[//]: # (            data={"username": "ubuntu", "password": "debian"},)

[//]: # (        &#41;)

[//]: # (        token = r.json&#40;&#41;["access_token"])

[//]: # ()
[//]: # (        # Use the token value to hit the API.)

[//]: # (        r = client.get&#40;)

[//]: # (            "http://localhost:5000/api_a/22",)

[//]: # (            headers={"Accept": "application/json", "Authorization": f"Bearer {token}"},)

[//]: # (        &#41;)

[//]: # (        print&#40;r.json&#40;&#41;&#41;)

[//]: # (    ```)

[//]: # ()
[//]: # (## Folder structure)

[//]: # ()
[//]: # (This shows the folder structure of the default template.)

[//]: # ()
[//]: # (```)

[//]: # (fastapi-nano)

[//]: # (├── app                                 # primary app folder)

[//]: # (│   ├── apis                            # this houses all the API packages)

[//]: # (│   │   ├── api_a                       # api_a package)

[//]: # (│   │   │   ├── __init__.py             # empty init file to make the api_a folder a package)

[//]: # (│   │   │   ├── mainmod.py              # main module of api_a package)

[//]: # (│   │   │   └── submod.py               # submodule of api_a package)

[//]: # (│   │   └── api_b                       # api_b package)

[//]: # (│   │       ├── __init__.py             # empty init file to make the api_b folder a package)

[//]: # (│   │       ├── mainmod.py              # main module of api_b package)

[//]: # (│   │       └── submod.py               # submodule of api_b package)

[//]: # (│   ├── core                            # this is where the configs live)

[//]: # (│   │   ├── auth.py                     # authentication with OAuth2)

[//]: # (│   │   ├── config.py                   # sample config file)

[//]: # (│   │   └── __init__.py                 # empty init file to make the config folder a package)

[//]: # (│   ├── __init__.py                     # empty init file to make the app folder a package)

[//]: # (│   ├── main.py                         # main file where the fastAPI&#40;&#41; class is called)

[//]: # (│   ├── routes                          # this is where all the routes live)

[//]: # (│   │   └── views.py                    # file containing the endpoints of api_a and api_b)

[//]: # (│   └── tests                           # test package)

[//]: # (│       ├── __init__.py                 # empty init file to make the tests folder a package)

[//]: # (│       ├── test_api.py                 # integration testing the API responses)

[//]: # (│       └── test_functions.py           # unit testing the underlying functions)

[//]: # (├── dockerfiles                         # directory containing all the dockerfiles)

[//]: # (├── .env                                # env file containing app variables)

[//]: # (├── Caddyfile                           # simple reverse-proxy with caddy)

[//]: # (├── docker-compose.yml                  # docker-compose file)

[//]: # (├── pyproject.toml                      # pep-518 compliant config file)

[//]: # (├── requrements-dev.in                  # .in file to enlist the top-level dev requirements)

[//]: # (├── requirements-dev.txt                # pinned dev dependencies)

[//]: # (├── requirements.in                     # .in file to enlist the top-level app dependencies)

[//]: # (└── requirements.txt                    # pinned app dependencies)

[//]: # (```)

[//]: # ()
[//]: # (In the above structure, `api_a` and `api_b` are the main packages where the code of the APIs live and they are exposed by the endpoints defined in the `routes` folder. Here, `api_a` and `api_b` have identical logic. Basically these are dummy APIs that take an integer as input and return two random integers between zero and the input value. The purpose of including two identical APIs in the template is to demonstrate how you can decouple the logics of multiple APIs and then assemble their endpoints in the routes directory. The following snippets show the logic behind the dummy APIs.)

[//]: # ()
[//]: # (This is a dummy submodule that houses a function called `random_gen` which basically generates a dict of random integers.)

[//]: # ()
[//]: # (```python)

[//]: # (# This a dummy module)

[//]: # (# This gets called in the module_main.py file)

[//]: # (from __future__ import annotations)

[//]: # (import random)

[//]: # ()
[//]: # ()
[//]: # (def rand_gen&#40;num: int&#41; -> dict[str, int]:)

[//]: # (    num = int&#40;num&#41;)

[//]: # (    d = {)

[//]: # (        "seed": num,)

[//]: # (        "random_first": random.randint&#40;0, num&#41;,)

[//]: # (        "random_second": random.randint&#40;0, num&#41;,)

[//]: # (    })

[//]: # (    return d)

[//]: # (```)

[//]: # ()
[//]: # (The `main_func` in the primary module calls the `rand_gen` function from the submodule.)

[//]: # ()
[//]: # (```python)

[//]: # (from __future__ import annotations)

[//]: # (from app.api_a.submod import rand_gen)

[//]: # ()
[//]: # ()
[//]: # (def main_func&#40;num: int&#41; -> dict[str, int]:)

[//]: # (    d = rand_gen&#40;num&#41;)

[//]: # (    return d)

[//]: # (```)

[//]: # ()
[//]: # (The endpoint is exposed like this:)

[//]: # ()
[//]: # (```python)

[//]: # (# app/routes/views.py)

[//]: # (from __future__ import annotations)

[//]: # (#... codes regarding authentication ...)

[//]: # ()
[//]: # (# endpoint for api_a &#40;api_b looks identical&#41;)

[//]: # (@router.get&#40;"/api_a/{num}", tags=["api_a"]&#41;)

[//]: # (async def view_a&#40;num: int, auth: Depends =Depends&#40;get_current_user&#41;&#41; -> dict[str, int]:)

[//]: # (    return main_func_a&#40;num&#41;)

[//]: # (```)

[//]: # ()
[//]: # (So hitting the API with a random integer will give you a response like the following:)

[//]: # ()
[//]: # (```json)

[//]: # ({)

[//]: # (  "seed": 22,)

[//]: # (  "random_first": 27,)

[//]: # (  "random_second": 20)

[//]: # (})

[//]: # (```)

[//]: # ()
[//]: # (## Further modifications)

[//]: # ()
[//]: # (* You can put your own API logics in the shape of `api_a` and `api_b` packages. You'll have to add additional directories like `api_a` and `api_b` if you need more APIs.)

[//]: # ()
[//]: # (* Then expose the APIs in the `routes/views.py` file. You may choose to create multiple `views` files to organize your endpoints.)

[//]: # ()
[//]: # (* This template uses OAuth2 based authentication and it's easy to change that. FastAPI docs has a comprehensive list of the available [authentication options]&#40;https://fastapi.tiangolo.com/tutorial/security/&#41; and instructions on how to use them.)

[//]: # ()
[//]: # (* You can change the application port in the `.env` file.)

[//]: # ()
[//]: # (* During prod deployment, you might need to fiddle with the reverse-proxy rules in the Caddyfile.)

[//]: # ()
[//]: # (## Stack)

[//]: # ()
[//]: # (* [Caddy]&#40;https://caddyserver.com/docs/&#41;)

[//]: # (* [Docker]&#40;https://www.docker.com/&#41;)

[//]: # (* [FastAPI]&#40;https://fastapi.tiangolo.com/&#41;)

[//]: # (* [Gunicorn]&#40;https://gunicorn.org/&#41;)

[//]: # (* [Httpx]&#40;https://www.python-httpx.org/&#41;)

[//]: # (* [Pip-tools]&#40;https://github.com/jazzband/pip-tools&#41;)

[//]: # (* [Pydantic]&#40;https://pydantic-docs.helpmanual.io/&#41;)

[//]: # (* [Pytest]&#40;https://docs.pytest.org/en/latest/&#41;)

[//]: # (* [Starlette]&#40;https://www.starlette.io/&#41;)

[//]: # (* [Uvicorn]&#40;https://www.uvicorn.org/&#41;)

[//]: # ()
[//]: # (## Resources)

[//]: # ()
[//]: # (* [Flask divisional folder structure]&#40;https://exploreflask.com/en/latest/blueprints.html#divisional&#41;)

[//]: # (* [Deploying APIs built with FastAPI]&#40;https://fastapi.tiangolo.com/deployment/&#41;)

[//]: # (* [Reverse proxying with Caddy]&#40;https://caddyserver.com/docs/caddyfile/directives/reverse_proxy&#41;)

[//]: # ()
[//]: # ()
[//]: # (<div align="center">)

[//]: # (✨ 🍰 ✨)

[//]: # (</div>)
