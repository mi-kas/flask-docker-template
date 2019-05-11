# Quickstart

Clone this repository and follow these steps:

## Create the environment

Change to the project folder and create the [virtual environment](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1) with:

```
python3 -m venv venv
```

On Windows:

```
py -3 -m venv venv
```

## Activate the environment

Before you work on the project, activate the corresponding environment:

```
. venv/bin/activate
```

On Windows:

```
venv\Scripts\activate
```

Your shell prompt will change to show the name of the activated environment.

## Install requirements

Install all the predefinied requirements:

```
pip install -r requirements.txt
```

## Start docker containers

Build the app and run it with:

```
docker-compose up
```

This will spin up a flask server on `localhost:5000`, a mongo db on `localhost:27017` and a postgres db on `localhost:5432`. Ther `src` directory is mounted to the container and allowing thereby to modify the code on the fly, without having to rebuild the image. More details [here](https://docs.docker.com/compose/gettingstarted/).

## Adding new requirements

If you need to add more packages to the project, you can simply install them:

```
pip install <package>
```

and add them to the requirements definition with:

```
pip freeze > requirements.txt
```

and don't forget to re-build the docker image afterwards:

```
docker-compose up --build
```

(Note: Re-building the image is only needed when adding new packages. Changes in the project's code files are automatically loaded into the container.)
