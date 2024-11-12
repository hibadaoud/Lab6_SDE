**PREREQUISITES:**
    Install Docker Desktop on your laptops.
      - **MAC:** [https://docs.docker.com/desktop/setup/install/mac-install/](https://docs.docker.com/desktop/setup/install/mac-install/)
      - **WINDOWS:** [https://docs.docker.com/desktop/setup/install/windows-install/](https://docs.docker.com/desktop/setup/install/windows-install/)
      - **Linux:** [https://docs.docker.com/desktop/setup/install/linux/](https://docs.docker.com/desktop/setup/install/linux/)


**Main Lab:**

**_EX1:_**
In order to run our lab you have 2 options:
- **OPTION1:**
  - Open Docker Desktop.
  - Run the following command:  
    ```
    docker run -p 8501:8501 --name lab_container hiba25/lab6_image_1
    ```
  - Open [http://localhost:8501](http://localhost:8501) in a browser.

- **OPTION2:**
  - Create a new folder.
  - Download the image file in that folder.
  - Open Docker Desktop.
  - Load the image using:  
    ```
    docker load -i lab6_image_1.tar
    ```
  - Run the container:  
    ```
    docker run -p 8501:8501 --name lab_container lab6_image_1
    ```
  - Open [http://localhost:8501](http://localhost:8501) in a browser.

- To stop the container:
    ```
    docker  stop lab_container

    ```
- To build new image after changing the code:
    ```
     docker build -f Dockerfile1 -t image_name . 
     docker run -p 8501:8501 --name lab_container image_name
    ```

- **_EX2:_**
In order to run our lab you have 2 options:
- **OPTION1:**
- Open Docker Desktop.
- Run the container on a different port:
  ```
  docker run -p 8502:8501 --name lab_container hiba25/lab6_image_1
  ```
- Open [http://localhost:8502](http://localhost:8502) in a browser.

- **OPTION2:**
- Create a new folder.
- Download the image file in that folder.
- Open Docker Desktop.
- Load the image:  
  ```
  docker load -i lab6_image_2.tar
  ```
- Run the container:  
  ```
  docker run -p 8502:8501 --name lab_container lab6_image_2
  ```
- Open [http://localhost:8502](http://localhost:8502) in a browser.


