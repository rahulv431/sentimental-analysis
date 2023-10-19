from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

@app.route("/sentiment_analysis", methods=['GET', 'POST'])
def sentiment_analysis():
    if request.method == 'POST':
        # Get sentences from form data
        sentences = request.form['sentences'].split(',')

        # Create a SentimentIntensityAnalyzer object
        analyzer = SentimentIntensityAnalyzer()

        # Analyze the sentiment for each sentence and store thefa results
        results = []
        for sentence in sentences:
            sentiment_dict = analyzer.polarity_scores(sentence.strip())
            
            
            if sentiment_dict["compound"] >= 0.05:
                results.append("Positive")

            elif sentiment_dict["compound"] <= -0.05:
                results.append("Negative")

            else:
                results.append("Neutral")
            # results.append("{:-<65} {}".format(sentence, str(sentiment_dict)))

        # Generate the output
        output = '<br>'.join(results)

        # Return the results as a string
        return render_template('results.html', output=output)

    # Render form template if method is GET
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)

