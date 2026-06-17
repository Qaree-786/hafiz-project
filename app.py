from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    city = request.form.get('city')
    
    print(f"New Registration -> Name: {name}, City: {city}")
    
    return f"<h3>Registration Successful! Thank you, {name}.</h3>"

if __name__ == '__main__':
    app.run(debug=True)