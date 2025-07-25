from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/student/<name>')
def student(name):
    return render_template("student.html", student_name=name)

@app.route('/healthz')
def healthz():
    return {"status": "ok"}

if __name__ == '__main__':
    app.run(host='0.0.0.0')
