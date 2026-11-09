# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API with FastAPI by defining routes, validating request data, and returning JSON responses for a small application.

## 📝 Tasks

### 🛠️ Create a Basic API

#### Description
Set up a FastAPI application with a few endpoints that return basic JSON data and demonstrate how a REST API is structured.

#### Requirements
Completed program should:

- Import and initialize a FastAPI app
- Create a home route that returns a welcome message
- Create an endpoint that returns a list of sample items
- Return data in JSON format
- Run the app locally with Uvicorn

### 🛠️ Add CRUD Functionality

#### Description
Expand the API so it can create, read, update, and delete records using HTTP methods and request JSON payloads.

#### Requirements
Completed program should:

- Define endpoints for creating and listing items
- Define an endpoint for retrieving a single item by ID
- Define endpoints for updating and deleting an item
- Use request models to validate incoming data
- Return appropriate status codes such as `200`, `201`, and `404`

