from flask import Flask
from flask import render_template
from flask import request
from wordProcess import WordProcessor


app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('test.html')


@app.route('/data', methods=['POST'])
def data():
    word_array = []
    for counter, data in enumerate(request.form.getlist('text')):
        word_array.append(data)
    for counter, data in enumerate(request.form.getlist('date')):
        word_array.append(data)

    return WordProcessor(word_array).process(word_array)


if __name__ == '__main__':
    app.run()
