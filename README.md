PREREQUISITES:
    install docker desktop on your laptops

Main Lab:
EX1:
In order to run our lab you have 2 options:
OPTION1:
Open docker desktop
docker run -p 8501:8501 - -name lab_container hiba25/lab6_image_1
open http://localhost:8501 in a browser

OPTION2:
Create a new folder
download the image file in that folder
Open docker desktop
docker load -i lab6_image_1.tar
docker run -p 8501:8501 - -name lab_container lab6_image_1
open http://localhost:8501 in a browser

To stop the container:
docker stop lab_container

To build new image after changing the code
docker build -f Dockerfile1 -t image_name .
docker run -p 8501:8501 - -name lab_container image_name

EX2:
In order to run our lab you have 2 options:
OPTION1:
Open docker desktop
docker run -p 8502:8501 - -name lab_container hiba25/lab6_image_1
open http://localhost:8502 in a browser

OPTION2:
Create a new folder
download the image file in that folder
Open docker desktop
docker load -i lab6_image_2.tar
docker run -p 8502:8501 - -name lab_container lab6_image_2
open http://localhost:8502 in a browser
