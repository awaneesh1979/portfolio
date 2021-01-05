from flask import Flask, render_template, request, url_for
import csv

app = Flask(__name__)


# with app.test_request_context():
#     url_for('static', filename='style.css')

@app.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')


@app.route('/action', methods=['GET', 'POST'])
def submit_action():
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')
    print(email)
    print(subject)
    print(message)

    # with open('./database.txt', mode='a') as database_file:
    #     database_file.writelines(f' {email} : {subject} : {message} \n' )

    with open('database.csv', 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter='|')
        csvwriter.writerow(request.form.to_dict().values())


    return render_template('contact.html', error_message ="Message Sent Successfully")


@app.route('/<page_name>', methods=['GET'])
def about_page(page_name=None):
    if page_name:
        if page_name == 'contact.html':
            return render_template('contact.html', error_message ="")

        return render_template(page_name)

    return render_template('index.html')


# @app.route('/contact.html', methods=['GET'])
# def contact_page():
#     return render_template('contact.html')
#
#
# @app.route('/components.html', methods=['GET'])
# def component_page():
#     return render_template('components.html')
#
#
# @app.route('/works.html', methods=['GET'])
# def works_page():
#     return render_template('works.html')


if __name__ == '__main__':
    app.run()
