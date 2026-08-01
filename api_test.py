import requests
from jsonschema import validate

BASE_URL = "http://127.0.0.1:5000"

employee_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "department": {"type": "string"},
        "salary": {"type": "integer"}
    },
    "required": ["id", "name", "department", "salary"]
}

# -----------------------
# GET
# -----------------------
response = requests.get(f"{BASE_URL}/employees")

assert response.status_code == 200
assert "application/json" in response.headers["Content-Type"]
assert response.elapsed.total_seconds() < 1

employees = response.json()

assert isinstance(employees, list)
assert len(employees) >= 2

validate(instance=employees[0], schema=employee_schema)

print("GET Test Passed")

# -----------------------
# POST
# -----------------------
new_employee = {
    "id": 5,
    "name": "David",
    "department": "IT",
    "salary": 90000
}

response = requests.post(
    f"{BASE_URL}/employees",
    json=new_employee
)

assert response.status_code == 201

print("POST Test Passed")

# -----------------------
# PUT
# -----------------------
updated_employee = {
    "id": 5,
    "name": "David",
    "department": "Cloud",
    "salary": 120000
}

response = requests.put(
    f"{BASE_URL}/employees/5",
    json=updated_employee
)

assert response.status_code == 200

print("PUT Test Passed")

# -----------------------
# PATCH
# -----------------------
response = requests.patch(
    f"{BASE_URL}/employees/5",
    json={
        "salary": 140000
    }
)

assert response.status_code == 200

print("PATCH Test Passed")

# -----------------------
# DELETE
# -----------------------
response = requests.delete(
    f"{BASE_URL}/employees/5"
)

assert response.status_code == 200

print("DELETE Test Passed")

# -----------------------
# NEGATIVE TEST
# -----------------------
response = requests.get(
    f"{BASE_URL}/employees/999"
)

assert response.status_code == 404

print("Negative Test Passed")

print("\n🎉 All API Tests Passed Successfully!")