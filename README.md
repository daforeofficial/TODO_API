# Todo API

## Description
A Django-based API for managing tasks, including task creation, updating, deletion, and categorization. This project uses Docker for containerization and includes an API documentation setup with `drf-yasg`. 

### Prerequisites

- Python 3.11
- Docker
- Docker Compose

### Installation
   git clone https://github.com/daforeofficial/TODO_API
   python virtualenv env
   cd todo_api
   pip install requirements.txt
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runsever

#### API Endpoints
GET /tasks/ - List all tasks
POST /tasks/ - Create a new task
GET /tasks/{id}/ - Retrieve a task by ID
PUT /tasks/{id}/ - Update a task by ID
DELETE /tasks/{id}/ - Delete a task by ID

more you can visit api documentation after launching project at [https://lcoalhost/](http://localhost:8000/swagger/)

![image](https://github.com/user-attachments/assets/730ddd6f-9784-4f94-9075-88b15334b7c8)

# Example API Requests
List Tasks: curl -X GET http://localhost:8000/tasks/
Create Task: curl -X POST http://localhost:8000/tasks/ -H "Content-Type: application/json" -d '{"title": "New Task", "description": "Task description"}'
And many moree.....

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

Contact
For any questions or feedback, please contact offline4evr@gmail.com.

BestRegard: Muzammil Aslam
