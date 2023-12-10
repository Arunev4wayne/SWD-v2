from flask import Flask, jsonify, render_template
from sqlalchemy import text

from database import engine

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Python Developer',
    'location': 'New York',
    'salary': '$100,000'
  },
  {
    'id': 2,
    'title': 'Data analyst',
    'location': 'Amsterdam',
    'salary': '$200,000'
  },
  {
    'id': 3,
    'title': 'Software Engineer',
    'location': 'London',

  }
]

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row))
    return jobs  

@app.route("/")
def hello_world():
 #jobs = load_jobs_from_db()
  load_jobs_from_db()
  return render_template('Home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0', debug=True)  