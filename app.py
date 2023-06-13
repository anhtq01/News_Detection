from flask import Flask, escape, request, render_template
import pickle

# initialise a TfidVectorizer
vector = pickle.load(open("vectorizer.pkl", 'rb'))

model = pickle.load(open("finalized_model.pkl", 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":

        news = request.form['news']
        print(news)

        predict = model.predict(vector.transform([news]))[0]
        print(predict)
        if predict == 'FAKE':
            return render_template("fake.html", news = news)

        if predict == 'REAL':
            return render_template("real.html", news = news)

        #return render_template("prediction.html", prediction_text="News headline is -> {}".format(predict))

    else:
        return render_template("fake.html")


@app.route('/review')
def review():
    return render_template("review.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.debug = True
    app.run()