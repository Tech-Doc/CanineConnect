from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data (replace with a database in a real-world application)
dogs_for_sale = [
    {'id': 1, 'name': 'Buddy', 'price': 500, 'seller': 'John Doe'},
    # Add more dog listings as needed
]

@app.route('/')
def home():
    return render_template('index.html', dogs=dogs_for_sale)

@app.route('/buy/<int:dog_id>')
def buy(dog_id):
    # Implement buying logic (e.g., payment processing)
    return f'Thank you for buying dog with ID {dog_id}!'

if __name__ == '__main__':
    app.run(debug=True)

