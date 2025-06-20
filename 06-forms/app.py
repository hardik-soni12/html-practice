from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET'])
def form():
    return render_template_string(open("basic-form.html").read())

@app.route('/submit.py', methods=['POST'])
def handle_form():
    username = request.form.get("username")
    password = request.form.get("pass")
    gender = request.form.get("Gender")
    skills = request.form.getlist("skills[]")
    state = request.form.get("state")
    feedback = request.form.get("feedback")


    return f"""
    <h2>Form Submitted</h2>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Password:</strong> {password}</p>
    <p><strong>Gender:</strong> {gender}</p>
    <p><strong>Skills:</strong> {', '.join(skills)}</p>
    <p><strong>State:</strong> {state}</p>
    <p><strong>Feedback:</strong> {feedback}</p>

    """

if __name__ == '__main__':
    app.run(debug=True)
