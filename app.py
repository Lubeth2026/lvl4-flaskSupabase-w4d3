
import os
from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()
app = Flask(__name__)
CORS(app)

supabase: Client = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

@app.route("/")
def health():
    return {"status": "working Perfectly"}

# READ from supabase table created 
@app.route("/api/contacts")
def get_contacts():
    response = supabase.table("Directory").select("*").execute()
    return response.data

# WRITE to the supabase table created from Flask
@app.post("/api/contacts")
def create_contact():
    data = request.get_json()
    new_contact = {"name": data["name"], "major": data["major"], "year": data["year"]}

    response = supabase.table("Directory").insert(new_contact).execute()
    return {"message": "New Contact", "response": response.data}, 201

if __name__ == "__main__":
    app.run(debug=True)
