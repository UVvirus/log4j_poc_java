from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the user input from the form
        user_input = request.form['user_input']

        # Call the Java application using subprocess
        result = subprocess.run(['java', 'LoggerApp', user_input], capture_output=True, text=True)

        # Get the output from the Java application
        java_output = result.stdout

        return render_template('result.html', java_output=java_output)
    else:
        return render_template('index.html')
    
if __name__ =="__main__":
    app.run(debug=True)