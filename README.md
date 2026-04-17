# task-manager-python

A simple REST API for managing tasks, built with Python and Flask

## What it does

- Create, read, update, and delete tasks via HTTP requests
- Tasks are stored in memory (reset when the server stops)
- JSON in, JSON out

## Tech Stack

- Python 3.12.4
- Flask

## How it was made

Project was scaffolded manually - no framework generator.

A Virtual Environment was created with `python3 -m venv venv` to isolate dependencies.

Flask was installed with pip and pinned to `requirements.txt`.

All logic lives in a single `app.py` file. Tasks stored in plain Python list with an incrementing ID. Each CRUD operation is a separate Flask route using the appropriate HTTP method (GET, POST, PUT, DELETE).

## Project Setup

```bash
git clone https://github.com/benjamin-matapo/task-manager-python.git
cd task-manager-python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the server

```bash
source venv/bin/activate
python app.py
```

Server runs at `http://127.0.0.1:500`

## API Reference

| Method | Endpoint   | Description    |
|--------|------------|----------------|
| GET    | `/tasks`     | List all tasks |
| POST   | `/tasks`     | Create a task  |
| PUT    | `/tasks/:id` | Update a task  |
| DELETE | `/tasks/:id` | Delete a task  |

## Usage Examples

```bash
# Create a task
curl -X POST http://127.0.0.1:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy milk"}'
  
# Read all tasks
curl http://127.0.0.1:5000/tasks

# Mark task 1 as complete
curl -X PUT http://127.0.0.1:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"done": true}'
  
# Delete task 1
curl -X DELETE http://127:0.0.1:5000/tasks/1
```

## Folder Structure

```markdown
task-manager-python/
├── app.py              # all routes and logic
├── requirements.txt    # pinned dependencies
├── venv/               # local virtual environment (not committed)
└── README.md
```

## Branching Strategy

- `main` - stable, working code only
- `dev` - active development
