from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock data for demonstration purposes
schedules = {
    'Monday': {'8:00 AM': 'Math', '10:00 AM': 'Physics'},
    'Tuesday': {'9:00 AM': 'English', '2:00 PM': 'History'}
}

# User roles (in a real system, these would be retrieved from a database)
user_roles = {
    'admin': {'schedule_access': True, 'announcement_access': True},
    'faculty': {'schedule_access': True, 'announcement_access': True},
    'student': {'schedule_access': True, 'announcement_access': False}
}

def is_user_authenticated(user_role):
    # Mock authentication logic; in a real system, use secure authentication mechanisms
    return user_role in user_roles

@app.route('/')
def index():
    return render_template('index.html', schedules=schedules)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user_role = request.form.get('user_role')

        if is_user_authenticated(user_role):
            return redirect(url_for('dashboard', user_role=user_role))
        else:
            return render_template('login.html', error='Invalid user role')

    return render_template('login.html', error='')

@app.route('/dashboard/<user_role>')
def dashboard(user_role):
    if not is_user_authenticated(user_role):
        return redirect(url_for('index'))

    return render_template('dashboard.html', user_role=user_role, schedules=schedules)

if __name__ == '__main__':
    app.run(debug=True)
