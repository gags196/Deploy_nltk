from flask import Flask, render_template, request
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('input_page.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    paragraph = request.form['paragraph']

    # Tokenizing sentences and words
    sentences = sent_tokenize(paragraph)
    words = word_tokenize(paragraph)

    # Stop words filtering
    stop_words = set(stopwords.words('english'))
    filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

    # Word frequency
    word_freq = Counter(filtered_words)

    return render_template(
        'result.html',
        num_sentences=len(sentences),
        num_words=len(words),
        num_filtered_words=len(filtered_words),
        word_freq=word_freq
    )

if __name__ == '__main__':
    app.run(debug=True)

