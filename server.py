
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    return (
        f" 'anger': {response['anger']},"
        f" 'disgust': {response['disgust']},"
        f" 'fear': {response['fear']},"
        f" 'joy': {response['joy']},"
        f" 'sadness': {response['sadness']}, "
        f" 'dominant emotion': {response['dominant_emotion']}"
    )

@app.route("/")
def render_index_page():
    return render_template("index.html")


if __name__ == "__main__":
    # Run the application on localhost:5000
    app.run(host="0.0.0.0", port=5000)