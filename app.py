from flask import Flask , render_template,render_template,request
from text_preprocessing import *
import joblib

app = Flask(__name__)

news_model = joblib.load('news_article_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/newsClassifier')
def newsClassifier():
    return render_template('classifier.html')

@app.route('/Classifier', methods = ['POST','GET'])
def submit():
    if request.method == 'POST':
        userInput = request.form['message']
        userInput = striphtml(userInput)
        userInput = remove_url(userInput)
        userInput = lower_case(userInput)
        userInput = word_tok(userInput)
        userInput = remove_stopwords(userInput)
        userInput = remove_punctuations(userInput)
        userInput = remove_number(userInput)
        userInput = stemming(userInput)
        userInput = lemmatization(userInput)
        userInput = remove_extraWords(userInput)
        userInput = [" ".join(map(str, userInput))]
        # print(userInput)
        result = news_model.predict(userInput)
        if result[0] == 1:
            # print("World News")
            return render_template('output.html', data=["World News", 'red'])
        elif result[0] == 2:
            # print('Sports News')
            return render_template('output.html', data=["Sports News", 'blue'])
        elif result[0] == 3:
            # print('Business News')
            return render_template('output.html', data=["Business News", 'green'])
        elif result[0] == 4:
            # print('Science-Technology News')
            return render_template('output.html', data=["Science-Technology News", 'red'])
    else:
        return render_template('classifier.html')


if __name__ == "__main__":
    app.run(debug=True)