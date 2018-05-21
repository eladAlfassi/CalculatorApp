# Installation Instructions

## Prerequisites
First of all you should make sure you have [docker](https://docs.docker.com/install/)  and [docker compose](https://docs.docker.com/compose/install/) installed on your machine.
For downloading the source code you should have [git](https://git-scm.com/downloads) installed on your machine.

## How to download?
run this command to clone the repository:
```
git clone https://github.com/eladAlfassi/CalculatorApp.git
```

## Building the docker image
Build the docker image by putting the **dockerfile** in the same level with **executor** and **server** folders.
then run the command:
```
docker-compose build calculator
```
You should run this command after every change you make in the **Calculator** source code.

## Running the app
To run all services run the command:
```
docker-compose up
```

## Using the calcuator
open the browser and navigate to:
```
http://localhost:8080/login
```
enter your details and the calculator will appear.

## making changes
If you want to make changes in the app, make sure -as was menchend- to rebuild it after making the changes.
Neither the less you should run the **test_calculate_executor.py** module that is in the **TESTS** directory.

Enjoy!


