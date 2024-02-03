from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs_lst = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Lahore, Pakistan',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Karanchi, Pakistan',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 3,
        'title': 'Front-end Developer',
        'location': 'Remote'
    },
    {
        'id': 3,
        'title': 'Backend Engineer',
        'location': 'Dubai,UAE',
        'salary': '$120,000'
    },
]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=jobs_lst)


@app.route('/api/jobs')
def list_jobs():
  return jsonify(jobs_lst)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=8080)
