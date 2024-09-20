"""This program detects emotion from text"""
from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def analyzer():
    """defining response to user input on the server"""
    user_input_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(user_input_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is \
    'anger': {response['anger']}, \
    'disgust': {response['disgust']}, \
    'fear': {response['fear']}, \
    'joy': {response['joy']}, \
    'sadness': {response['sadness']}. \
    The dominant emotion is {response['dominant_emotion']}."

@app.route("/")
def render_index_page():
    """rendering html page on the server"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=5000,debug=True)
