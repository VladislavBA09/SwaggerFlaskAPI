import requests
from http import HTTPStatus

BASE_URL = "http://127.0.0.1:5000"

# ----------- Students Tests -----------

def test_create_student():
    payload = {
        "group_id": 1,
        "first_name": "John",
        "last_name": "Doe"
    }
    response = requests.post(f"{BASE_URL}/students/", data=payload)  # Use data instead of json
    assert response.status_code == HTTPStatus.CREATED, f"Error: {response.text}"


def test_get_students():
    response = requests.get(f"{BASE_URL}/students/")
    assert response.status_code == HTTPStatus.OK, f"Error: {response.text}"
    assert isinstance(response.json(), list)

def test_get_student():
    response = requests.get(f"{BASE_URL}/students/1")
    assert response.status_code == HTTPStatus.OK, f"Error: {response.text}"

def test_update_student():
    payload = {
        "data": "Updated Student Info"
    }
    response = requests.put(f"{BASE_URL}/students/1", data=payload)  # Use data instead of json
    assert response.status_code in [HTTPStatus.OK, HTTPStatus.NOT_FOUND], f"Error: {response.text}"


def test_delete_student():
    response = requests.delete(f"{BASE_URL}/students/1")
    assert response.status_code == HTTPStatus.NO_CONTENT, f"Error: {response.text}"



# ----------- Courses Tests -----------

def test_create_course():
    payload = {
        "data": "New Course"
    }
    response = requests.post(f"{BASE_URL}/course/", data=payload)  # Use data instead of json
    assert response.status_code == HTTPStatus.CREATED, f"Error: {response.text}"


def test_get_courses():
    response = requests.get(f"{BASE_URL}/course/")
    assert response.status_code == HTTPStatus.OK, f"Error: {response.text}"
    assert isinstance(response.json(), list)

def test_get_course():
    response = requests.get(f"{BASE_URL}/course/1")
    assert response.status_code == HTTPStatus.OK, f"Error: {response.text}"

def test_update_course():
    payload = {
        "data": "Updated Course Info"
    }
    response = requests.put(f"{BASE_URL}/course/1", json=payload)
    assert response.status_code == HTTPStatus.OK, f"Error: {response.text}"

def test_delete_course():
    response = requests.delete(f"{BASE_URL}/course/1")
    assert response.status_code == HTTPStatus.NO_CONTENT, f"Error: {response.text}"



# ----------- Groups Tests -----------

def test_create_group():
    payload = {
        "data": "New Group"
    }
    response = requests.post(f"{BASE_URL}/groups/", json=payload)
    print(f"Response status: {response.status_code}")
    print(f"Response text: {response.text}")
    assert response.status_code == HTTPStatus.CREATED, f"Error: {response.text}"
    assert "group_name" in response.json()

def test_get_groups():
    response = requests.get(f"{BASE_URL}/groups/")
    assert response.status_code == HTTPStatus.OK, f"Error: {response.text}"
    assert isinstance(response.json(), list)

def test_get_group():
    response = requests.get(f"{BASE_URL}/groups/1")
    assert response.status_code == HTTPStatus.OK, f"Error: {response.text}"

def test_update_group():
    payload = {
        "data": "Updated Group Info"
    }
    response = requests.put(f"{BASE_URL}/groups/1", json=payload)
    assert response.status_code == HTTPStatus.OK, f"Error: {response.text}"

def test_delete_group():
    response = requests.delete(f"{BASE_URL}/groups/1")
    assert response.status_code == HTTPStatus.NO_CONTENT, f"Error: {response.text}"



# ----------- Additional Operations -----------

def test_add_student_to_course():
    # Ensure course exists before adding student
    response = requests.post(f"{BASE_URL}/course/", data={"data": "Course 1"})
    assert response.status_code == HTTPStatus.CREATED

    response = requests.post(f"{BASE_URL}/courses/1/students/1")
    assert response.status_code == HTTPStatus.CREATED, f"Error: {response.text}"


def test_remove_student_from_course():
    response = requests.delete(f"{BASE_URL}/courses/1/students/1")
    assert response.status_code == HTTPStatus.NO_CONTENT, f"Error: {response.text}"
