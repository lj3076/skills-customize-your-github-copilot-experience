# 📘 Assignment: Testing FastAPI with pytest

## 🎯 Objective

Practice writing automated tests for a FastAPI application using pytest and FastAPI's `TestClient`. Verify successful responses and error handling without starting a web server.

## 📝 Tasks

### 🛠️ Run the Example Test

#### Description
Install the required packages and run the provided test to see how pytest sends a request to the API and checks its response.

#### Requirements
Completed program should:

- Install the dependencies with `python -m pip install fastapi pytest httpx2`
- Run the tests from this assignment directory with `python -m pytest -v`
- Explain what the status-code and JSON assertions in `test_starter_code.py` verify


### 🛠️ Test the Items Endpoints

#### Description
Add tests for listing all items and retrieving an existing item by its ID. Use the sample data in `starter_code.py` to check the response contents.

#### Requirements
Completed program should:

- Check that `GET /items` returns a `200` status code and both sample items
- Check that `GET /items/1` returns a `200` status code and the expected item
- Use assertions to verify response JSON, not only the status code


### 🛠️ Test Missing Items

#### Description
Add a test for requesting an item ID that is not in the sample data. Confirm that the API reports the missing resource correctly.

#### Requirements
Completed program should:

- Check that `GET /items/999` returns a `404` status code
- Run all tests together and confirm they pass
- Keep each test focused on one API behavior