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
First, we need to activate the virtual environment:
```
source venv/bin/activate
```

then install the requirements from requirements.txt:
```
pip install -r server/requirements.txt
```

then run the server by running manage.py
python server/manage.py runserver

then you can use post and get request queries to check and update the data
curl -X POST http://127.0.0.1:8000/process/
curl -X GET http://127.0.0.1:8000/process/

#Coding Tasks for Data Engineers

#SQL
1)Rewrite this SQL without subquery:
```
SELECT id
FROM users
WHERE id NOT IN (
	SELECT user_id
	FROM departments
	WHERE department_id = 1
);
```
Answer: 
```
SELECT id
FROM users
WHERE users.department_id != 1
```
2)Write a SQL query to find all duplicate lastnames in a table named user:
```
+----+-----------+----------+
| id | firstname | lastname |
+----+-----------+----------+
| 1  | Ivan      | Sidorov  |
| 2  | Alexandr  | Ivanov   |
| 3  | Petr      | Petrov   |
| 4  | Stepan    | Ivanov   |
+----+-----------+----------+
```
Answer:
```
SELECT DISTINCT lastname
FROM user
HAVING COUNT(lastname) > 1
```
3) Write a SQL query to get a username from the user table with the second highest salary from salary tables. Show the username and it's salary in the result:
```
+---------+--------+
| user_id | salary |
+---------+--------+
| 1       | 1000   |
| 2       | 1100   |
| 3       | 900    |
| 4       | 1200   |
+---------+--------+
+----+-------------+
| id | username    |
+----+-------------+
| 1  | Alex        |
| 2  | Maria       |
| 3  | Bob         |
| 4  | Sean        |
+----+-------------+
```
Answer:
```
select username
from user
where id in (
select usr_id from (  
	select *,  
	dense_rank() over (partition by salary order by salary desc) sal_max 
	from emp_table) a 
where a.sal_max = 2 )
```

#Algorithms and Data Structures
1) Optimise execution time of this Python code snippet:
```
def count_connections(list1: list, list2: list) -> int:
  count = 0
  
  for i in list1:
    for j in list2:
      if i == j:
        count += 1
  
  return count
```
Answer:
```
def count_connections(list1: list, list2: list) -> int:
  count = 0
  #We can create a dictionary to keep track of the numbers of repations of this item in the list
  repeating = {}
  for i in list1:
    if i in repeating :
      repeating[i]+=1
    else :
      repeating[i] = 1
  #then we for each item in the second list that also exist in the first list we increase the count by the number of repetitions from list1
  for i in list2 :
    if i in repeating :
      count+= repeating[i]


  return count
```
2)Given a string s, find the length of the longest substring without repeating characters. Analyze your solution and please provide Space and Time complexities:
```
#Time Complexity: O(n + d)
#Auxiliary Space: O(d)
#we will use two pointer (sliding window) to find the answer
def longestUniqueSubsttr(string):

	# we need to keep track of the index of the last time we seen a letter in the string
	# we create a dictionary to store this value
	seen = {}
	maximum_length = 0

	# the first pointer starts from index=0 
	start = 0
	
	#the second pointer is end and just mover to the right with each iteration
	for end in range(len(string)):

		# We need to check if we need to change the index if starting point
		# So we check if we already had seen this letter.
		if string[end] in seen:
		
			# Then we move the start pointer to position after the last occurrence
			start = max(start, seen[string[end]] + 1)

		# Updating the last seen value of the character
		seen[string[end]] = end
		maximum_length = max(maximum_length, end-start + 1)
	return maximum_length
```
3) Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

```
def index ( nums : list , target : int  ) -> int:
  st = 0
  en = len(nums)-1

  while st < en :
    mid = (st+en)//2

    if nums[mid] == target :
      return mid
    elif nums[mid] > target:
      en = mid
    else :
      st = mid + 1


  return st
```
#Linux Shell
1)List processes listening on ports 80 and 443:
```
kamil@kamil-Predator-G3-571:~$ lsof -i :443 & lsof -i :80
[1] 180706
COMMAND     PID  USER   FD   TYPE  DEVICE SIZE/OFF NODE NAME
kamil@kamil-Predator-G3-571:~$ chrome     7446 kamil   34u  IPv4 1070021      0t0  TCP kamil-Predator-G3-571:41806->lb-140-82-113-25-iad.github.com:https (ESTABLISHED)
chrome     7446 kamil   36u  IPv4 1153923      0t0  TCP kamil-Predator-G3-571:34378->aeab55d76dd13c9bb.awsglobalaccelerator.com:https (ESTABLISHED)
chrome     7446 kamil   44u  IPv4 1135614      0t0  TCP kamil-Predator-G3-571:33764->229.26.211.130.bc.googleusercontent.com:https (ESTABLISHED)
chrome     7446 kamil   51u  IPv4 1154961      0t0  UDP kamil-Predator-G3-571:58743->lf-in-f198.1e100.net:443 
chrome     7446 kamil   52u  IPv4 1139433      0t0  TCP kamil-Predator-G3-571:35674->53.16.211.130.bc.googleusercontent.com:https (ESTABLISHED)
chrome     7446 kamil   69u  IPv4 1159354      0t0  TCP kamil-Predator-G3-571:44110->191.93.217.35.bc.googleusercontent.com:https (ESTABLISHED)
chrome     7446 kamil   74u  IPv4 1162244      0t0  TCP kamil-Predator-G3-571:44112->191.93.217.35.bc.googleusercontent.com:https (CLOSE_WAIT)
chrome     7446 kamil   79u  IPv4  879850      0t0  TCP kamil-Predator-G3-571:40138->stackoverflow.com:https (ESTABLISHED)
telegram- 48746 kamil   20u  IPv4  360374      0t0  TCP kamil-Predator-G3-571:49632->149.154.167.92:https (ESTABLISHED)
telegram- 48746 kamil   22u  IPv4  743368      0t0  TCP kamil-Predator-G3-571:51806->149.154.167.92:https (ESTABLISHED)
telegram- 48746 kamil   31u  IPv4 1112092      0t0  TCP kamil-Predator-G3-571:37970->149.154.167.50:https (ESTABLISHED)
```
2)List process environment variables by given PID:
```
sudo cat /proc/`pgrep 'the process name'`/environ
```
3)Launch a python program my_program.py through CLI in the background. How would you close it after some period of time?
Answer: 
- we can use command: `s ax | grep my_program.py` to find the PID first.
- then the command: `kill 'PID of process'` which will the process.
