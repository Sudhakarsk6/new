from flask import Flask, jsonify, request

app = Flask(__name__)

employees = [
    {"id": 1, "name": "Alice", "department": "HR", "salary": 55000},
    {"id": 2, "name": "Bob", "department": "IT", "salary": 70000}
]

@app.route("/")
def home():
    return jsonify({"message": "Employee API is running!"})

@app.route("/employees", methods=["GET"])
def get_employees():
    return jsonify(employees)

@app.route("/employees/<int:emp_id>", methods=["GET"])
def get_employee(emp_id):
    for employee in employees:
        if employee["id"] == emp_id:
            return jsonify(employee)
    return jsonify({"error": "Employee not found"}), 404

@app.route("/employees", methods=["POST"])
def add_employee():
    employee = request.get_json()
    employees.append(employee)
    return jsonify(employee), 201

@app.route("/employees/<int:emp_id>", methods=["PUT"])
def update_employee(emp_id):
    updated_employee = request.get_json()

    for index, employee in enumerate(employees):
        if employee["id"] == emp_id:
            employees[index] = updated_employee
            return jsonify(updated_employee)

    return jsonify({"error": "Employee not found"}), 404

@app.route("/employees/<int:emp_id>", methods=["PATCH"])
def patch_employee(emp_id):
    updates = request.get_json()

    for employee in employees:
        if employee["id"] == emp_id:
            employee.update(updates)
            return jsonify(employee)

    return jsonify({"error": "Employee not found"}), 404

@app.route("/employees/<int:emp_id>", methods=["DELETE"])
def delete_employee(emp_id):
    for employee in employees:
        if employee["id"] == emp_id:
            employees.remove(employee)
            return jsonify({"message": "Employee deleted successfully"})

    return jsonify({"error": "Employee not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)