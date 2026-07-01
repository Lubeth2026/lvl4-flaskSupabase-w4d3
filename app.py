
import os
from flask import Flask
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

