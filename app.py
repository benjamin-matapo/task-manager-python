from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage — resets when server restarts
tasks = []
next_id = 1

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def create_task():
    global next_id
    data = request.get_json()
    task = {
        "id": next_id,
        "title": data["title"],
        "done": False
    }
    tasks.append(task)
    next_id += 1
    return jsonify(task), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = data.get("title", task["title"])
            task["done"] = data.get("done", task["done"])
            return jsonify(task)
    return jsonify({"error": "Not found"}), 404

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"message": "Deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)