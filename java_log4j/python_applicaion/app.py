from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the user input from the form
        user_input = request.form['user_input']
        user_input2=request.form['user_input2']
        print(1)

        # Call the Java application using subprocess
        result = subprocess.run(['java', '-jar', "/home/ubuntu/log4j_poc_java/java_log4j/target/demo-1.0-SNAPSHOT-jar-with-dependencies.jar" , user_input, user_input2], capture_output=True, text=True)
        print(result)
        # Get the output from the Java application
        java_output = result.stdout
        print(java_output)
        return render_template('result.html', java_output=java_output)
    else:
        return render_template('index.html')
    
if __name__ =="__main__":
    app.run(debug=True)
