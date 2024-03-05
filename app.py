from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']

    matches = re.findall(regex_pattern, test_string)

    if matches:
        return render_template('index.html', test_string=test_string, regex_pattern=regex_pattern, matches=matches)
    else:
        return render_template('index.html', test_string=test_string, regex_pattern=regex_pattern, no_matches=True)

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if re.match(email_regex, email):
        return render_template('index.html', email=email, is_valid=True)
    else:
        return render_template('index.html', email=email, is_valid=False)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
