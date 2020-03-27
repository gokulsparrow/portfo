from flask import Flask, render_template, url_for, request, redirect 
import csv
app = Flask(__name__)

@app.route('/b')
def hello_world():
    return 'Hello, gokul!'

@app.route('/')
def my_home():
    return render_template('index.html')


def write_data_csv(data):
    with open('datacsvs.csv', mode="a") as dataj2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(dataj2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_data_csv(data)
        return "thank you so much"
    else:
        return "something went wrong"           

