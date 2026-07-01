# Flask + Supabase Directory API

## Overview
This project is a REST API built with python, flask, and supabase. The API connects to a supabase postgres SQL database & performs CRUD-style operations on a table named Directory.

Currently the API allows users to:
- Check that the server is running
- Retrieve all contacts stored in the Directory Table
- Add new contacts to the Directory Table

Each contact contains the following info:
- name-Student's Name
- major-Student's Major
- year-Student's academic year

### Installation
1. Clone the repo
https://github.com/Lubeth2026/lvl4-flaskSupabase-w4d3.git
2. Create and activate a virtual environment
python -m venv .venv
source .venv/Scripts/activate
3. Install the required packages
pip install -r requirements.txt

#### Running the backend
1. Start the Flask development server:
python app.py or
flask run
2. The API will run locally at:
http://127.0.0.1:5000

##### API Routes
1. GET/health check
Returns a simple message confirming the server is running
2. GET /api/contacts
Retrieves every record stored in the Directory table
3. POST /api/contacts
Adds a new contact to the Directory table
