# provectus-internship-task
Solving tasks for provectus internship

# Data Processing Task
1. Requirements.
2. Task description.
3. Task Installation and running

## Requirements
- asgiref==3.4.1
- Django==3.2.8
- numpy==1.21.2
- pandas==1.3.3
- python-dateutil==2.8.2
- pytz==2021.3
- six==1.16.0
- sqlparse==0.4.2

## Task description
In this project, we created a Django server that accepts post & requests.
when it receives a get request it will return the current data in "processed_data.cvs".
when it receives a post request it will update the data "processed_data.cvs".

## Task Installation and running
First we need to activate the virtual enviroment:
'''
source venv/bin/activate
'''

then install the requirements from requirements.txt:
'''
pip install -r server/requirements.txt
'''

then run the server by running manage.py
python server/manage.py runserver

then you can use post and get request queries to check and update the data
curl -X POST http://127.0.0.1:8000/process/
curl -X GET http://127.0.0.1:8000/process/

#Coding Tasks for Data Engineers

#SQL
Rewrite this SQL without subquery:
'''
