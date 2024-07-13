from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Set up the database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the database model for the contact form
class ContactForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"ContactForm('{self.name}', '{self.email}', '{self.phone}', '{self.description}')"

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['mail']
    phone = request.form['phone']
    description = request.form['description']
    form_entry = ContactForm(name=name, email=email, phone=phone, description=description)
    db.session.add(form_entry)
    db.session.commit()
    return 'Form submitted successfully!'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
