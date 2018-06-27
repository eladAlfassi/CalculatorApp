# Installation Instructions

## Prerequisites
First of all you should make sure you have [docker](https://docs.docker.com/install/)  and [docker compose](https://docs.docker.com/compose/install/) installed on your machine.
For downloading the source code you should have [git](https://git-scm.com/downloads) installed on your machine.

## How to download?
Run this command to clone the repository:
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

## Using the calculator
Open the browser and navigate to:
```
http://localhost:8080/login
```
enter your details and the calculator will appear.

## Making changes
If you want to make changes in the app, make sure -as was menchend- to rebuild it after making the changes.
Neither the less, after making changes it is recommended to run the **test_calculate_executor.py** module (you can find it in the [tests](https://github.com/eladAlfassi/CalculatorApp/tree/master/tests) directory) to ensure that everything works as expected.

Enjoy!


