# Alerts Management Application

The Alerts Management Application is a Flask-based system designed to manage and store alerts securely. It offers functionalities to create alerts, to delete alerts, to get triggered alerts via a RESTful API.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Folder Structure](#folder-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Curl Commands](#curl-commands)
- [Importing the Postman Collection](#Importing-the-Postman-Collection)
- [Existing Users](#Existing-users)
- [Technologies Used](#technologies-used)
- [Deployed API Link](#Deployed-Link)

## Introduction

The Bookstore Management Application is a built using Python and Flask, designed to facilitate efficient books-taking functionalities. Leveraging MongoDB for data storage, it allows users to manage books through a RESTful API while ensuring data security.

## Features

- Add new books to the database.
- Retrieve all books or a specific book by ISBN.
- Update book details.
- Delete books from the database.
- Basic authentication to restrict access to certain endpoints.
- Unit tests for API endpoints.
- JWT token-based authentication (Bonus feature).

## Folder Structure

The application follows a well-organized folder structure:

```
Alerts_Management_API/
|-- app/
|   |-- __init__.py
|   |-- models.py
|   |-- routes.py
|   |-- auth.py
|   |-- alerts.py
|   |-- email_notifier.py
|-- config.py
|-- requirements.txt
|-- run.py
|-- Dockerfile
|-- docker-compose.yml

```

- **models**: Defines the schema for the User model, Alert model.
- **routes**: Handles API endpoints for authentication and alerts.
- **run.py**: Main entry point of the application.
- **config.py**: Stores configuration such as database credentials.

## Installation

To set up the application locally, follow these steps:

1. Clone the repository: `git clone https://github.com/saikrishnayadav764/Bookstore_Management_API.git`
2. Change Directory: `cd Bookstore_Management_API-main`
3. Install dependencies: `pip install -r requirements.txt`
4. Configure variables: MONGO_URI = "mongodb+srv://naruto:naruto@cluster0.be644zi.mongodb.net/db"
5. Start the server: `python run.py`

## Usage

The server starts at http://localhost:5000 by running `python run.py`. Once the server is running, you can access the defined API endpoints.

## API Endpoints

### Books

- **POST /api/books**: Add a new book.
- **GET /api/books**: Retrieve all books.
- **GET /api/books/<ISBN>**: Retrieve a specific book by ISBN.
- **PUT /api/books/<ISBN>**: Update book details.
- **DELETE /api/books/<ISBN>**: Delete a book.

### Authentication

- **POST /api/login**: Authenticate users and generate JWT tokens.

## Curl Commands

Execute these `curl` commands in your terminal to interact with the API endpoints:

### Obtain Token (Login)

```bash
curl -X POST -H "Content-Type: application/json" -d "{\"username\": \"admin\", \"password\": \"admin\"}" https://mushy-bathing-suit-foal.cyclic.app/api/login
```

Replace `username` and `password` with the credentials of the allowed users.

### Adding a new book

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer <access_token>" -d "{\"title\": \"Book Title\", \"author\": \"Author Name\", \"ISBN\": \"1234567890\", \"price\": 10.99, \"quantity\": 5}" https://mushy-bathing-suit-foal.cyclic.app/api/books
```

### Retrieving all books

```bash
curl -X GET -H "Authorization: Bearer <access_token>" https://mushy-bathing-suit-foal.cyclic.app/api/books
```

### Retrieving a specific book by ISBN

```bash
curl -X GET -H "Authorization: Bearer <access_token>" https://mushy-bathing-suit-foal.cyclic.app/api/books/:id
```

Replace `:id` with the actual ISBN of the book you want to retrieve.

### Updating book details

```bash
curl -X PUT -H "Content-Type: application/json" -H "Authorization: Bearer <access_token>" -d "{\"title\": \"Updated Title\", \"author\": \"Updated Author\", \"price\": 12.99, \"quantity\": 10}" https://mushy-bathing-suit-foal.cyclic.app/api/books/:id

```

Replace `:id` with the actual ISBN of the book you want to update.

### Deleting a book

```bash
curl -X DELETE -H "Authorization: Bearer <access_token>" https://mushy-bathing-suit-foal.cyclic.app/api/books/:id
```

Replace `:id` with the actual ISBN of the book you want to delete.

## Importing the Postman Collection

To import the Bookstore Management API collection into Postman, follow these steps:

1. Download the Postman collection file by clicking [here](https://github.com/saikrishnayadav764/Bookstore_Management_API/blob/main/Bookstore.postman_collection.json).
2. Open Postman.
3. Click on the "Import" button in the top left corner of the window.
4. In the dialog that appears, click on the "Upload Files" tab.
5. Select the downloaded collection file (`.json` format) from your computer.
6. Once the file is uploaded, click on the "Import" button to import the collection into Postman.

After importing the collection, you'll be able to see all the API endpoints along with example requests and responses. You can then use these requests to interact with the Bookstore Management API directly from Postman.

## Existing Users

The application has the following default users to authenticate:

- username: admin, password: admin

## Technologies Used

- Python 3.x
- flask==3.0.1
- flask_jwt_extended==4.6.0
- Flask-Caching==2.1.0
- redis==5.0.1
- flask_pymongo==2.3.0
- Werkzeug==3.0.1
- requests==2.31.0
- uuid==1.30


## Deployed Link

[https://mushy-bathing-suit-foal.cyclic.app/api/books]

