from flask import Flask, request, jsonify, render_template, redirect

app = Flask(__name__)

tasks = []

# HOME PAGE UI
@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

# ADD TASK
@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")

    if task:
        tasks.append({
            "title": task,
            "status": "Pending"
        })

    return redirect("/")

# DELETE TASK
@app.route("/delete/<int:index>")
def delete_task(index):
    if index < len(tasks):
        tasks.pop(index)

    return redirect("/")

# COMPLETE TASK
@app.route("/complete/<int:index>")
def complete_task(index):
    if index < len(tasks):
        tasks[index]["status"] = "Completed"

    return redirect("/")

# API ENDPOINTS
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json
    tasks.append(data)
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)