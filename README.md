## Introduction

This is a personal project created to put into practice all the concepts I have learned about Django so far.

The idea was to create a Trello-like application where users can access rooms with tasks that can be moved between different states and even deleted.

EasyTask has been created in Python 3.11.1 and Djngo 4.2.1

https://github.com/marcodeArg/task-manager/assets/76412551/1284713f-3ac7-4d40-b3c5-182514e98bbd

## Main features
* **User Authentication**: Users can create accounts and log in to the application.
* **Room Management**: Users can create rooms, enter existing rooms, and leave rooms they are no longer interested in.
* **Task Management**: Users can create tasks within a room, modify the status of tasks, and delete tasks when necessary.


## Usage
1. Clone the repository  
```
$ git clone
```
2. Acces into the folder   
```
$ cd task-manager
```
3. Create a virtual environment  
```
$ python -m venv venv
```
4. Activate the environment using

- Windows : 
```
$ venv\Scripts\activate
```  
- Linux : 
```
$ source venv/bin/activate
```
5. Install the project requirements   
```
$ pip instal -r requirements.txt
```
6. Move into the "task_manager" folder and create a .env file 
```
$ cd task_manager && touch .env
```
7. Inside the env file, add the following environmental variables
```
DATABASE_URL=<your_database_url>
SECRET_KEY=<random-secret-key>
DEBUG=False
```
8. Make the migrations to the db
```
$ python manage.py migrate
```
9. Run the server
```
$ python manage.py runserver
```
10. Acces to *http://localhost:8000*. Enjoy

## TO DO
* Implement the functionality for the room creator to delete the entire room
* Implement the functionality for the room creator to remove users

