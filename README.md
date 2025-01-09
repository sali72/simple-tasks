

# Simple Tasks API

A simple FastAPI application that allows you to manage tasks. You can create, update, retrieve, and delete tasks from a PostgreSQL database.

---

## Prerequisites

1. **Python** (3.9+)  
2. **PostgreSQL** (Database server)

---

## Installing and Configuring PostgreSQL Locally

Below is a quick guide to installing PostgreSQL on an Ubuntu-like distribution.  [Adapt the steps if you are using a different OS.](https://www.postgresql.org/download/)

1. Update your package list:  
   ```bash
   sudo apt update
   ```
2. Install PostgreSQL and its additional modules:  
   ```bash
   sudo apt install postgresql postgresql-contrib
   ```
3. Switch to the `postgres` user:  
   ```bash
   sudo -i -u postgres
   ```
4. Enter the PostgreSQL shell:  
   ```bash
   psql
   ```
5. Create a new database (for example, `simpletasks`):  
   ```sql
   CREATE DATABASE tasksdb;
   ```
6. Create a user (for example, `myuser`) and set a password:
   ```sql
   CREATE USER myuser WITH PASSWORD '123';
   ```
7. Grant privileges for the user on the new database:
   ```sql
   GRANT ALL PRIVILEGES ON DATABASE simpletasks TO myuser;
   ```
8. Exit the PostgreSQL shell:
   ```sql
   \q
   ```
9. Exit the `myuser` user session:
   ```bash
   exit
   ```

---

## Setting Up the .env File

In the project root directory, create a file named `.env`. Add your database connection string:
```bash
POSTGRES_URL="postgresql://myuser:123@localhost:5432/tasksdb"
```

Adjust the user, password, host, and port according to your local PostgreSQL configuration.

---

## Local Development Setup

1. Clone the repository (or download the source code) and navigate to the project directory.
2. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application (using any ASGI server, such as uvicorn):
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```
   Alternatively, you can use the built-in uvicorn runner in your code or another process manager of your choice.

Once the server is running, open your browser or HTTP client at:
http://127.0.0.1:8000/docs

---

## Deploying on a Linux Server with systemd

Below is an example of how to set up your systemd service to run the application using gunicorn with the Uvicorn worker.

Before proceeding, make sure:
1. Your PostgreSQL service is installed and running. You can verify by:
   ```bash
   sudo systemctl status postgresql
   # or for version-specific:
   sudo systemctl status postgresql-17
   ```
   If it’s not running, start it:
   ```bash
   sudo systemctl start postgresql
   ```
2. The required Python packages (`gunicorn`, `uvicorn`, etc.) are installed in an env on the server:
   ```bash
   pip install -r requirements.txt
   ```
3. Your .env file is in place with the correct database connection string.
4. PostgreSQL is properly configured with your database and user.

5. Create a systemd Service File (for example, `/etc/systemd/system/simple-tasks.service`) with the following content:

   ```ini
   [Unit]
   Description=Simple Tasks API
   After=network.target

   [Service]
   Type=simple
   User=youruser
   Group=yourgroup
   WorkingDirectory=/path/to/your/project
   Environment="PATH=/path/to/your/env/bin"
   ExecStart=/path/to/your/env/bin/gunicorn --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:7000 app.main:app
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

   Notes:
   - Adjust `User` and `Group` to match your setup.  
   - Update `WorkingDirectory` to the path to your project.  
   - Change the `Environment` line to the path to your Python environment.  
   - The `ExecStart` line reference should match the path where gunicorn is installed.

3. Reload systemd and enable/start the service:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable simple-tasks.service
   sudo systemctl start simple-tasks.service
   ```
4. Check the service status:
   ```bash
   systemctl status simple-tasks.service
   ```

Your FastAPI application will now run as a background service managed by systemd on port 7000.

---



## API Endpoints

Below is a summary of each endpoint provided by the tasks router:

---

### 1. Create a Task

- **Method:** `POST /tasks`  
- **Request Body (JSON):**  
  ```json
  {
    "title": "<string>",
    "is_completed": "<boolean>",
    "description": "<string or null>"
  }
  ```
- **Description:** Creates a new task in the database.  
- **Returns:**  
  ```json
  {
    "message": "Task created successfully",
    "data": {"id": "<created task id>"},
    "timestamp": "<creation time>"
  }
  ```

---

### 2. Retrieve a Single Task

- **Method:** `GET /tasks/{task_id}`  
- **URL Parameter:**  
  - `task_id` (int): The ID of the task to retrieve.  
- **Description:** Retrieves the details of a specific task by its ID.  
- **Returns:**  
  ```json
  {
    "message": "Task retrieved successfully",
    "data": {
      "id": "<task id>",
      "title": "<string>",
      "is_completed": "<boolean>",
      "description": "<string or null>",
      "created_at": "<datetime>"
    },
    "timestamp": "<time of retrieval>"
  }
  ```

---

### 3. Retrieve All Tasks

- **Method:** `GET /tasks`  
- **Description:** Retrieves all tasks in the system.  
- **Returns:**  
  ```json
  {
    "message": "Tasks retrieved successfully",
    "data": {
      "tasks": [
        {
          "id": "<task id>",
          "title": "<string>",
          "is_completed": "<boolean>",
          "description": "<string or null>",
          "created_at": "<datetime>"
        },
        ...
      ]
    },
    "timestamp": "<time of retrieval>"
  }
  ```

---

### 4. Update a Task

- **Method:** `PUT /tasks/{task_id}`  
- **URL Parameter:**  
  - `task_id` (int): The ID of the task to update.  
- **Request Body (JSON):**  
  ```json
  {
    "title": "<string or null>",
    "is_completed": "<boolean or null>",
    "description": "<string or null>"
  }
  ```
- **Description:** Updates the specified fields of a task.  
- **Returns:**  
  ```json
  {
    "message": "Task updated successfully",
    "data": {
      "id": "<task id>",
      "title": "<string>",
      "is_completed": "<boolean>",
      "description": "<string or null>",
      "created_at": "<datetime>"
    },
    "timestamp": "<time of update>"
  }
  ```

---

### 5. Delete a Task

- **Method:** `DELETE /tasks/{task_id}`  
- **URL Parameter:**  
  - `task_id` (int): The ID of the task to delete.  
- **Description:** Deletes the specified task from the system.  
- **Returns:**  
  ```json
  {
    "message": "Task deleted successfully",
    "data": null,
    "timestamp": "<time of deletion>"
  }
  ```

---

## Contact

If you have any questions or issues, feel free to contact:
- Email: sahashemi072@gmail.com

