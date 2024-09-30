from flask import Flask, render_template, redirect, request, url_for, flash
from models import db, User, Event, Registration, Feedback
from forms import RegistrationForm, EventForm
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

# Initialize Flask-Mail
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Save user logic
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Logic for login
    return render_template('login.html')

@app.route('/create_event', methods=['GET', 'POST'])
def create_event():
    form = EventForm()
    if form.validate_on_submit():
        # Save event logic
        flash('Event created successfully!', 'success')
        return redirect(url_for('event_list'))
    return render_template('create_event.html', form=form)

@app.route('/events')
def event_list():
    events = Event.query.all()
    return render_template('event_list.html', events=events)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
