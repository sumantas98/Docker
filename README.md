############### Calculation Project ##############

Project Description : 

In this project , I have implemented basic mathematics calculation using Python Restful API.
The main objective of this project is to explain the Docker ,RestfulAPI and MongoDb concept.
This project is a Restful Webservice.Please find the below 

Project Modules:

1. Number of hit count of a Website:
    In this case , I have used a MongoDb table "UserNum" where I'm storing the number of hit 
    in column "num_of_users_hit".
2. Addition Module :
    Here user will provide two numbers and based on the user input application may give error
	or success response. 
3. Multiplication Module :
    Here user will provide two numbers and based on the user input application may give error
	or success response.	
4. Subtraction Module :
    Here user will provide two numbers and based on the user input application may give error
	or success response.
5. Division Module :
    Here user will provide two numbers and based on the user input application may give error
	or success response. 



Error Code:

200 - Success Response

301 - Missing Input

302 - Zero Division error



Library Used :

1. os
2. flask
3. flask_restful
4. pymongo
5. Python version==3.8



Port Used:

Web Port No: 5000
DB  Port No: 27017

Docker Config:

FROM python:3.8-slim
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install --upgrade pip \
  && pip install -r requirement.txt 
CMD ["python", "Project1.py"]

#################### Thank you ########################