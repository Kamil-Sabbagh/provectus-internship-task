# provectus-internship-task
Solving tasks for provectus internship

# Data Processing Task
1. Requirements.
2. Task description.
3. Task Installation and running

## Requirements
- asgiref 3.4.1 or higher
- Django==3.2.8 or higher
- numpy==1.21.2 or higher
- pandas==1.3.3 or higher
- python-dateutil==2.8.2 or higher
- pytz==2021.3 or higher
- six==1.16.0 or higher
- sqlparse==0.4.2 or higher

## Task description
In this project, we created a Django server that accepts post & requests.
when it receives a get request it will return the current data in "processed_data.cvs".
when it receives a post request it will update the data "processed_data.cvs".

## Task Installation and running
first open your shell command and install the requirements from requirements.txt:
pip install -r requirements.txt 
before you could run the server you must change the current path in 'Data processing.py'. opening the file and changing the 5th row
path = '/home/kamil/work/internship/dataeng'
to where ever you store the file on. 


then run the server by running manage.py
python3 manage.py runserver

then you can use post and get request queries to check and update the data
curl -X POST http://127.0.0.1:8000/data/
curl -X GET http://127.0.0.1:8000/data/
